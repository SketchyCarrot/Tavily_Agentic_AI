from tavily import TavilyClient
import os


client = TavilyClient(api_key=TAVILY_API_KEY)

def tavily_search_agent(query, search_depth="basic", max_results=1, include_answer="none", include_images=False):
        response = client.search(
        query=query,
        search_depth=search_depth,
        max_results=max_results,
        include_answer=include_answer,
        include_images=include_images,
        )
        return response
