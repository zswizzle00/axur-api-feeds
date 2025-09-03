# Axur API Feeds Connector for OpenCTI

This is an AXUR API feeds connector integration for OpenCTI that fetches threat intelligence data from Axur's API and ingests it into OpenCTI.

## Files

- `axur-feed.py` - Main connector script
- `Dockerfile` - Docker configuration with proper dependencies
- `requirements.txt` - Python package dependencies
- `axur_docker-compose.yml` - Docker Compose configuration
- `manifest.json` - OpenCTI connector manifest

## Environment Variables

- `OPENCTI_URL` - OpenCTI instance URL
- `OPENCTI_TOKEN` - OpenCTI API token
- `CONNECTOR_ID` - Unique connector identifier
- `CONNECTOR_NAME` - Connector display name
- `CONNECTOR_SCOPE` - Data scope (indicator, etc.)
- `AXUR_FEED_URL` - Axur API feed endpoint
- `AXUR_BEARER_TOKEN` - Axur API authentication token
- `FEED_INTERVAL` - Feed polling interval in seconds

## Links

- [Docker Hub Repository](https://hub.docker.com/r/zswizzle03/axur-api-feeds)
- [Axur API Documentation](https://docs.axur.com/en/axur/api/)
- [OpenCTI Documentation](https://docs.opencti.io/)
