import os
import json
import random
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import StreamingResponse
from mcp.server import Server
from mcp.server.sse import SseServerTransport
import mcp.types as types

# Initialize FastAPI and MCP Server
app = FastAPI(title="SentinelStream MCP")
mcp = Server("sentinelstream-mcp")

# Simple in-memory cache for the UI to consume
cache = {
    "latest_feed": [],
    "sentiment_score": 5.0
}

@mcp.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """Defines the tools available to the AI Agent"""
    return [
        types.Tool(
            name="fetch_live_feed",
            description="Fetches recent brand mentions. Returns JSON array.",
            inputSchema={
                "type": "object",
                "properties": {"brand_name": {"type": "string"}},
                "required": ["brand_name"]
            }
        ),
        types.Tool(
            name="get_sentiment_pulse",
            description="Returns the aggregate sentiment score (0.0 to 10.0).",
            inputSchema={"type": "object", "properties": {}}
        ),
        types.Tool(
            name="generate_ai_draft",
            description="Drafts a PR response for a specific post.",
            inputSchema={
                "type": "object",
                "properties": {"post_id": {"type": "string"}},
                "required": ["post_id"]
            }
        )
    ]

@mcp.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    """Logic execution for the MCP tools"""
    if not arguments: arguments = {}

    if name == "fetch_live_feed":
        brand = arguments.get("brand_name", "Brand")
        
        # SIMULATED DATA ENGINE
        # This ensures your UI works perfectly today without Reddit API keys
        feed = [
            {"id": "p1", "source": "Reddit", "text": f"The new {brand} update is a game changer. Super smooth!"},
            {"id": "p2", "source": "X.com", "text": f"Is {brand} down for anyone else? My dashboard is lagging."},
            {"id": "p3", "source": "Reddit", "text": f"Thinking of switching to {brand}, are the docs good?"}
        ]
        random.shuffle(feed) # Makes it feel "Live"
        
        cache["latest_feed"] = feed
        cache["sentiment_score"] = round(random.uniform(4.0, 9.0), 1)
        
        return [types.TextContent(type="text", text=json.dumps(feed))]

    elif name == "get_sentiment_pulse":
        score = cache.get("sentiment_score", 5.0)
        return [types.TextContent(type="text", text=str(score))]

    elif name == "generate_ai_draft":
        post_id = arguments.get("post_id", "")
        post_text = next((p["text"] for p in cache["latest_feed"] if p["id"] == post_id), "your post")
        
        draft = f"SENTINEL DRAFT:\n\n'Hi! We appreciate the feedback on {post_text[:30]}... We're on it!'"
        return [types.TextContent(type="text", text=draft)]
        
    raise ValueError(f"Unknown tool: {name}")

# --- SSE TRANSPORT SETUP FOR CLOUD RUN ---
# This part is critical for the "SentinelStream" UI to talk to this server
transport = SseServerTransport("/messages")

@app.get("/sse")
async def sse(request: Request):
    async with transport.connect_sse(request.scope, request.receive, request._send) as sse_stream:
        await mcp.run(sse_stream[0], sse_stream[1], mcp.create_initialization_options())
        return StreamingResponse(sse_stream)

@app.post("/messages")
async def messages(request: Request):
    await transport.handle_post_message(request.scope, request.receive, request._send)
    return {"status": "ok"}