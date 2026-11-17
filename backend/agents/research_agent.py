
from services.search_service import search_web


def conduct_research(topic, blog_plan):

    print("Research Agent is working...")

    # Keep the search query short.
    query = f"Find reliable facts, statistics, studies, and recent developments about {topic}"

    results = search_web(query)

    research_data = []

    for item in results:

        research_data.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content")
        })

    return research_data
