from tavily import TavilyClient
import os


client = TavilyClient(api_key="TAVILY_API_KEY")

def tavily_search_agent(query, search_depth="basic", max_results=1, include_answer="none", include_images=False):
        response = client.search(
        query=query,
        search_depth=search_depth,
        max_results=max_results,
        include_answer=include_answer,
        include_images=include_images,
        )
        
        search_results = response.get("results", [])

        content = []
        references = []
        image_links = response.get("images", [])

        for result in search_results:
             content.append(result.get("content", ""))
             references.append(f"{result['title']} ({result['url']})")
        
        total_content = "\n".join(content)
        if len(total_content) > 15000:
                total_content = total_content[:15000]

        return total_content, references, image_links
