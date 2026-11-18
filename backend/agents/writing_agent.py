
from services.ai_service import generate_response


def write_blog(
    topic,
    blog_plan,
    research_data,
    length="Medium",
    style="Professional",
    language="English"
):

    print("Writing Agent is working...")

    # Convert research results into readable text.
    research_text = ""

    for index, item in enumerate(research_data, start=1):

        research_text += f"""
        Source {index}
        Title: {item['title']}
        URL: {item['url']}
        Information: {item['content']}
        """

    prompt = f"""
    You are a professional blog writer.

    Write a detailed, engaging and informative blog
    using the information provided below.

    BLOG TOPIC:
    {topic}

    BLOG OUTLINE:
    {blog_plan}

    RESEARCH INFORMATION:
    {research_text}

    ARTICLE REQUIREMENTS:

    1. ARTICLE LENGTH:
       Follow the selected article length:
       - Short: approximately 500–700 words.
       - Medium: approximately 1000–1300 words.
       - Long: approximately 1800–2200 words.

       Selected length: {length}

    2. WRITING STYLE:
       Write the entire article using this style:
       {style}

       Maintain a consistent tone throughout the article.

    3. LANGUAGE:
       Write the entire article in:
       {language}

       Use natural, fluent and grammatically correct language.
       Do not randomly switch between languages.

    GENERAL WRITING INSTRUCTIONS:

    4. Follow the provided blog outline.
    5. Write a compelling introduction.
    6. Explain each main heading clearly.
    7. Use research information to support your points.
    8. Include relevant examples where appropriate.
    9. Write a meaningful conclusion.
    10. Do not invent statistics or facts.

    CITATION INSTRUCTIONS:

    11. Add inline citations using numbers like [1], [2], and [3].
    12. Each citation number must correspond to the position
        of its source in the supplied research information.
    13. Only cite sources provided in the research information.
    14. Do not invent citation numbers or URLs.
    15. Include a References section with the supplied source URLs.

    Return only the completed blog article.
    """

    blog = generate_response(prompt)

    return blog
