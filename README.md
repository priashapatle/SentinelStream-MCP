🛰️ SentinelStream MCP — Brand Intelligence EngineSentinelStream MCP is an enterprise-grade real-time brand intelligence dashboard. It leverages the cutting-edge Model Context Protocol (MCP) to bridge live social data feeds with AI-driven sentiment analysis, providing businesses with a "Sentinel Pulse" on their digital reputation.🔗 Live Demo: https://sentinel-stream-343827421929.us-central1.run.app/📂 Project StructurePlaintextsentinelstream-mcp/
├── app.py              # Streamlit Frontend (MCP Client)
├── server.py           # FastAPI Backend (MCP Server)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
├── start.sh            # Dual-process startup script
├── .gitignore          # Git exclusion rules
└── README.md           # Project documentation
✨ Features🛡️ Core Brand MonitoringReal-time Sentiment Gauge: A dynamic, glassmorphic UI featuring a needle-gauge that visualizes brand health on a scale of 0-10.Live Mention Scanning: Aggregates real-time "mentions" from digital feeds using standardized MCP tools.AI-Powered Pulse: Deep analysis of tone and context to determine if a brand keyword is trending positively or negatively.🧠 Advanced CapabilitiesMCP Architecture: Decoupled Server-Client communication using Server-Sent Events (SSE) for high interoperability.Strategic AI Drafts: Automatically generates PR-ready response drafts tailored to specific negative or positive social mentions.Premium UX/UX: Built with a modern dark-mode aesthetic featuring Glassmorphism, responsive containers, and smooth CSS animations.🏗️ System ArchitectureThe application is built using a modern decoupled stack and containerized for scalable deployment on Google Cloud Platform.Code snippetgraph TD
    A[User / Brand Manager] -->|Access Web App| B(Streamlit Frontend)
    B -->|MCP Tool Calls| C{MCP Client Session}
    C -->|SSE Requests| D[FastAPI MCP Server]
    D -->|Internal Logic| E[Sentiment Pulse Tool]
    D -->|Data Fetching| F[Live Feed Tool]
    D -->|AI Logic| G[Draft Generator Tool]
    E & F & G -->|JSON Response| D
    D -->|SSE Stream| C
    C -->|Update UI| B
🛠️ Tech StackLayerTechnologyFrontendStreamlit, HTML5, Vanilla CSS (Glassmorphism)BackendPython, FastAPI, UvicornProtocolModel Context Protocol (MCP) via SSEDeploymentGoogle Cloud Run, DockerContainerizationDocker (python:3.11-slim)🚀 Local DevelopmentTo run this project locally:1. Install DependenciesPowerShellpip install -r requirements.txt
2. Start the MCP BackendPowerShellpython -m uvicorn server:app --host 0.0.0.0 --port 8081
3. Start the DashboardPowerShellpython -m streamlit run app.py
☁️ GCP Deployment (Cloud Run)This project is configured to be deployed easily to Google Cloud Run using Docker.1. Build and DeployPowerShellgcloud run deploy sentinel-stream `
  --source . `
  --project numeric-vehicle-495215-v2 `
  --region us-central1 `
  --allow-unauthenticated
📖 Usage GuideSelect a Keyword: Enter a major brand name like Swiggy, Zomato, or Tesla.Initialize: Click the "INITIALIZE LIVE FEED" button to start the MCP handshake.Analyze: Watch the "Analyzing Pulse" phase as the MCP server fetches and scores data.Review: The needle will move to reflect the current sentiment score. Scroll down to see specific social mentions and AI-generated response drafts.🗺️ Roadmap[ ] Integration with real-world Reddit/X APIs.[ ] Multi-keyword comparison dashboard.[ ] Historic sentiment trend lines (PostgreSQL/BigQuery).[ ] Automated Slack/Discord alerts for sentiment drops.📄 LicenseThis project is for educational purposes. All product names, logos, and brands are property of their respective owners.👤 AuthorPriasha Patle📩 priashapatle@gmail.com
