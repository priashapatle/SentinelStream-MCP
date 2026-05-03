#!/bin/bash
# start.sh - Launch both FastAPI and Streamlit

# Start FastAPI MCP Server in the background
# Internal port 8081
python -m uvicorn server:app --host 0.0.0.0 --port 8081 &

# Start Streamlit App in the foreground
# Public port 8080 (Cloud Run default)
python -m streamlit run app.py --server.port 8080 --server.address 0.0.0.0
