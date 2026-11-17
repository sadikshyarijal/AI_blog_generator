
from agents.planning_agent import create_blog_plan
from agents.research_agent import conduct_research
from agents.writing_agent import write_blog

topic = "Impact of Artificial Intelligence on Education"

# Step 1: Planning
print("\n========== PLANNING ==========\n")
blog_plan = create_blog_plan(topic)
print(blog_plan)

# Step 2: Research
print("\n========== RESEARCH ==========\n")
research = conduct_research(topic, blog_plan)

for item in research:
    print("Source:", item["title"])

# Step 3: Writing
print("\n========== WRITING ==========\n")
blog = write_blog(topic, blog_plan, research)

print(blog)

print("\nBlog generation completed!")

