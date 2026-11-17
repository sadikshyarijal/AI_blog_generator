
from services.ai_service import generate_response


def create_blog_plan(topic):

    prompt = f"""
    You are an expert blog content strategist.

    Your task is to Understand the user’s topic and create a basic article plan.

    Blog Topic: {topic}

    Create a structured plan containing:

    1. An engaging blog title.
    2. Target audience.
    3. Main objective of the blog.
    4. Introduction summary.
    5. Five main headings.
    6. Two subtopics under each heading.
    7. Important points to cover.
    8. Conclusion summary.

    Make the outline logical, informative,
    engaging and suitable for a blog article.

    Return the result in a clean, readable format.
    """

    print("Planning Agent is working...")

    plan = generate_response(prompt)

    return plan
