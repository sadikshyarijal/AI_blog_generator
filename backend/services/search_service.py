
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY not found in .env file")

search_client = TavilyClient(api_key=api_key)


def search_web(query):

    response = search_client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    return response.get("results", [])
