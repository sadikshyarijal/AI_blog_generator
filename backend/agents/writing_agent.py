
from services.ai_service import generate_response


def write_blog(topic, blog_plan, research_data):

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

    INSTRUCTIONS:
    1. Follow the provided blog outline.
    2. Write a compelling introduction.
    3. Explain each main heading clearly.
    4. Use the research information to support your points.
    5. Include relevant examples where appropriate.
    6. Write a meaningful conclusion.
    7. Do not invent statistics or facts.
    8. Add inline citations using numbers like [1], [2], and [3].
9. Each citation number must correspond to the position
    of its source in the supplied research information.
11. Only cite sources provided in the research information.
11. Do not invent citation numbers or URLs.
12. Include a References section with the supplied source URLs.

    Return only the completed blog article.
    """

    blog = generate_response(prompt)

    return blog
