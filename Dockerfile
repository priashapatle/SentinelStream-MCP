FROM python:3.11-slim

WORKDIR /app

# Step 1: Pehle requirements copy karein
COPY requirements.txt .

# Step 2: Dependencies install karein (mcp ko explicitly add kiya hai safety ke liye)
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir mcp sse-starlette

# Step 3: Baaki saara code copy karein
COPY . .

# Step 4: Script ko permissions dein
RUN chmod +x start.sh

# Cloud Run default port
EXPOSE 8080

# Startup script run karein
CMD ["./start.sh"]