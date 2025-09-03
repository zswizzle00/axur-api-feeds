# Axur API Feeds Connector for OpenCTI

This is an AXUR API feeds connector integration for OpenCTI that fetches threat intelligence data from Axur's API and ingests it into OpenCTI.

## Problem Solved

The original deployment was failing with the error:
```
ImportError: failed to find libmagic. Check your installation
```

This was caused by the `python-magic` package (a dependency of `pycti`) requiring the system library `libmagic` to be installed in the Docker container.

## Solution

The Dockerfile now properly installs the required system dependencies:
- `libmagic1` - Required by python-magic
- `gcc` - Required for building some Python packages

## Docker Hub

The fixed connector is now available on Docker Hub:
- **Image**: `zswizzle03/axur-api-feeds:latest`
- **Versioned**: `zswizzle03/axur-api-feeds:v1.0.0`

## Files

- `axur-feed.py` - Main connector script
- `Dockerfile` - Docker configuration with proper dependencies
- `requirements.txt` - Python package dependencies
- `axur_docker-compose.yml` - Docker Compose configuration
- `manifest.json` - OpenCTI connector manifest

## Deployment Options

### Option 1: Use Docker Hub Image (Recommended)
```yaml
connector-myfeed:
  image: zswizzle03/axur-api-feeds:latest
  # ... rest of configuration
```

### Option 2: Build Locally
```yaml
connector-myfeed:
  build: .
  # ... rest of configuration
```

## Quick Start

1. **Deploy with Docker Compose:**
   ```bash
   docker-compose -f axur_docker-compose.yml up -d
   ```

2. **Or pull and run manually:**
   ```bash
   docker pull zswizzle03/axur-api-feeds:latest
   docker run -d --name axur-connector zswizzle03/axur-api-feeds:latest
   ```

## Environment Variables

- `OPENCTI_URL` - OpenCTI instance URL
- `OPENCTI_TOKEN` - OpenCTI API token
- `CONNECTOR_ID` - Unique connector identifier
- `CONNECTOR_NAME` - Connector display name
- `CONNECTOR_SCOPE` - Data scope (indicator, etc.)
- `AXUR_FEED_URL` - Axur API feed endpoint
- `AXUR_BEARER_TOKEN` - Axur API authentication token
- `FEED_INTERVAL` - Feed polling interval in seconds

## Testing

To verify the connector works:
```bash
docker run --rm zswizzle03/axur-api-feeds:latest python -c "from pycti import OpenCTIConnectorHelper; print('Success!')"
```

## Building and Publishing

To build and push updates to Docker Hub:
```bash
docker build -t zswizzle03/axur-api-feeds:latest .
docker push zswizzle03/axur-api-feeds:latest
```

## Links

- [Docker Hub Repository](https://hub.docker.com/r/zswizzle03/axur-api-feeds)
- [Axur API Documentation](https://docs.axur.com/en/axur/api/)
- [OpenCTI Documentation](https://docs.opencti.io/)
