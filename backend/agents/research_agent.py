
from services.search_service import search_web


def conduct_research(topic, blog_plan, language="English"):

    print("Research Agent is working...")

    # Keep the search query short and focused.
    query = (
        f"Find reliable facts, statistics, studies, "
        f"and recent developments about {topic}. "
        f"Prefer credible sources in {language} where available."
    )

    results = search_web(query)

    research_data = []

    for item in results:
        research_data.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content")
        })

    return research_data
