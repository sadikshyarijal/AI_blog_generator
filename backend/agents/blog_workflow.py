
from agents.planning_agent import create_blog_plan
from agents.research_agent import conduct_research
from agents.writing_agent import write_blog
from agents.review_agent import review_blog


def generate_blog(
    topic,
    length="Medium",
    style="Professional",
    language="English"
):
    print("\n========== STARTING BLOG GENERATION ==========\n")

    
    print("STEP 1: Creating blog plan...")
    blog_plan = create_blog_plan(
        topic, length, style, language
    )

    
    print("\nSTEP 2: Researching the topic...")
    research_data = conduct_research(
        topic, blog_plan, language
    )

   
    print("\nSTEP 3: Writing the blog...")
    blog_draft = write_blog(
        topic,
        blog_plan,
        research_data,
        length,
        style,
        language
    )

  
    print("\nSTEP 4: Reviewing the blog...")
    final_blog = review_blog(
        topic,
        blog_draft,
        research_data,
        length,
        style,
        language
    )

    print("\n========== BLOG GENERATION COMPLETED ==========\n")

    return {
        "topic": topic,
        "plan": blog_plan,
        "research": research_data,
        "blog": final_blog
    }

