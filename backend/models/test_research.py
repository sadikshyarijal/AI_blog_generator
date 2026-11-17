
from agents.planning_agent import create_blog_plan
from agents.research_agent import conduct_research

topic = "Impact of Artificial Intelligence on Education"

# Step 1: Generate blog outline
print("\n========== PLANNING ==========\n")

blog_plan = create_blog_plan(topic)

print(blog_plan)


# Step 2: Research the topic
print("\n========== RESEARCH ==========\n")

research = conduct_research(topic, blog_plan)


# Step 3: Display research results
for index, item in enumerate(research, start=1):

    print(f"\nSource {index}")
    print("Title:", item["title"])
    print("URL:", item["url"])
    print("Information:", item["content"])

print("\nResearch completed!")
