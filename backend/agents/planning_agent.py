
from services.ai_service import generate_response


def create_blog_plan(
    topic,
    length="Medium",
    style="Professional",
    language="English"
):

    prompt = f"""
    You are an expert blog content strategist.

    Your task is to understand the user's topic
    and create a structured article plan.

    Blog Topic: {topic}

    Create a structured plan containing:

    1. ARTICLE LENGTH:
       Create an outline suitable for the selected article length:
       - Short: approximately 500–700 words.
       - Medium: approximately 1000–1300 words.
       - Long: approximately 1800–2200 words.

       Selected length: {length}

    2. WRITING STYLE:
       Design the outline to support the selected writing style:
       {style}

    3. LANGUAGE:
       Create the blog title, headings, subtopics,
       and outline in the selected language:
       {language}

    4. An engaging blog title.
    5. Target audience.
    6. Main objective of the blog.
    7. Introduction summary.
    8. Five main headings.
    9. Two subtopics under each heading.
    10. Important points to cover.
    11. Conclusion summary.

    Make the outline logical, informative,
    engaging and suitable for a blog article.

    Return the result in a clean, readable format.
    """

    print("Planning Agent is working...")

    plan = generate_response(prompt)

    return plan

