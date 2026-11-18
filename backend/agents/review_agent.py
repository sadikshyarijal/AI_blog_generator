
from services.ai_service import generate_response


def review_blog(
    topic,
    blog_draft,
    research_data,
    length="Medium",
    style="Professional",
    language="English"
):

    print("Review Agent is working...")

    # Collect the URLs of the research sources.
    source_urls = []

    for item in research_data:
        if item.get("url"):
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

    ARTICLE REQUIREMENTS:

    1. ARTICLE LENGTH:
       Check whether the article follows the requested length:
       - Short: approximately 500–700 words.
       - Medium: approximately 1000–1300 words.
       - Long: approximately 1800–2200 words.

       Selected length: {length}

    2. WRITING STYLE:
       Ensure the article consistently follows this style:
       {style}

    3. LANGUAGE:
       Ensure the entire article is written in:
       {language}

       Correct language inconsistencies and grammatical errors.

    YOUR REVIEW TASKS:

    4. Correct grammar and spelling mistakes.
    5. Improve sentence clarity and readability.
    6. Improve the flow between paragraphs.
    7. Check that headings are well organized.
    8. Remove unnecessary repetition.
    9. Check that factual claims are supported by
       the supplied research.
    10. Do not invent facts, statistics, or references.
    11. Preserve the original meaning and important details.

    CITATION PRESERVATION:

    12. Preserve all existing inline citation numbers exactly.
    13. Do not remove, renumber, or invent citations.
    14. Keep the References section and supplied source URLs.
    15. Do not introduce unsupported references.

    Return the complete improved blog article in Markdown.
    """

    reviewed_blog = generate_response(prompt)

    return reviewed_blog
