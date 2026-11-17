
from services.ai_service import generate_response


def review_blog(topic, blog_draft, research_data):

    print("Review Agent is working...")

    # Collect the URLs of the research sources.
    source_urls = []

    for item in research_data:
        source_urls.append(item["url"])

    sources = "\n".join(source_urls)

    prompt = f"""
    You are an expert blog editor and content reviewer.

    Review and improve the following blog article.

    BLOG TOPIC:
    {topic}

    ORIGINAL BLOG:
    {blog_draft}

    AVAILABLE RESEARCH SOURCES:
    {sources}

    YOUR TASKS:
    1. Correct grammar and spelling mistakes.
    2. Improve sentence clarity and readability.
    3. Improve the flow between paragraphs.
    4. Check that headings are well organized.
    5. Remove unnecessary repetition.
    6. Check that factual claims are supported by
       the supplied research.
    7. Do not invent facts, statistics, or references.
    8. Preserve the original meaning and important details.

    Return the complete improved blog article in Markdown.
    """

    reviewed_blog = generate_response(prompt)

    return reviewed_blog
