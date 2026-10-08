# UrbanGIS AI

AI-assisted GIS and urban planning analysis platform.

UrbanGIS AI combines geospatial workflows with AI-assisted interpretation to help planners, architects, researchers and GIS professionals understand land use, accessibility, urban growth and transportation-related patterns.

## Current status

Early-stage prototype. This repository contains a small working AI prototype plus product documentation. Add real GIS analysis modules as they are developed.

## Planned capabilities

- Land Use / Land Cover analysis
- Urban expansion analysis
- Population density analysis
- Road accessibility analysis
- Spatial suitability analysis
- Traffic and congestion analysis
- AI-assisted interpretation of GIS results
- Automated planning-report generation

## Technology

- Python 3.10+
- FastAPI
- Anthropic Python SDK
- HTML/CSS/JavaScript
- Planned: GeoPandas, Rasterio, GDAL, QGIS and Google Earth Engine

## Run locally

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Anthropic API key, then:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

Never commit your API key.

## Vision

Make advanced GIS and evidence-based urban planning easier to use by combining spatial analysis with natural-language AI assistance.

## Disclaimer

This is a research/prototype project. AI-generated planning suggestions must be checked against GIS data, professional judgment and applicable planning regulations.
