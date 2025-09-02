import os
import time
import requests
from pycti import OpenCTIConnectorHelper, get_config_variable

class MyFeedConnector:
    def __init__(self):
        config = {
            "opencti_url": get_config_variable("OPENCTI_URL", ["opencti", "url"], required=True),
            "opencti_token": get_config_variable("OPENCTI_TOKEN", ["opencti", "token"], required=True),
            "connector_id": get_config_variable("CONNECTOR_ID", ["connector", "id"], required=True),
            "connector_name": get_config_variable("CONNECTOR_NAME", ["connector", "name"], required=True),
            "connector_scope": get_config_variable("CONNECTOR_SCOPE", ["connector", "scope"], required=True),
            "connector_confidence_level": get_config_variable("CONNECTOR_CONFIDENCE_LEVEL", ["connector", "confidence_level"], default=50),
            "feed_url": get_config_variable("AXUR_FEED_URL", ["feed", "url"], required=True),
            "bearer_token": get_config_variable("AXUR_BEARER_TOKEN", ["feed", "bearer_token"], required=True),
            "feed_interval": int(get_config_variable("FEED_INTERVAL", ["feed", "interval"], default=3600)),
        }
        self.helper = OpenCTIConnectorHelper(config)

    def fetch_feed(self):
        try:
            headers = {
                "Authorization": f"Bearer {self.helper.connect_conf['bearer_token']}",
                "Content-Type": "application/json"
            }
            r = requests.get(self.helper.connect_conf["feed_url"], headers=headers, timeout=10)
            r.raise_for_status()
            data = r.json()
            return data
        except Exception as e:
            self.helper.log_error(f"Failed to fetch feed: {e}")
            return None

    def process_feed(self, data):
        # Example: each entry is an IOC
        for item in data:
            value = item.get("indicator")
            description = item.get("description", "")
            if value:
                stix_indicator = {
                    "type": "indicator",
                    "spec_version": "2.1",
                    "pattern_type": "stix",
                    "pattern": f"[domain-name:value = '{value}']",
                    "name": description or value,
                    "x_opencti_score": 70,
                }
                self.helper.send_stix2_bundle([stix_indicator], update=True)

    def run(self):
        while True:
            self.helper.log_info("Fetching feed...")
            data = self.fetch_feed()
            if data:
                self.process_feed(data)
            time.sleep(self.helper.connect_conf["feed_interval"])

if __name__ == "__main__":
    MyFeedConnector().run()
