


from agents.blog_workflow import generate_blog

topic = "Impact of Artificial Intelligence on Education"

result = generate_blog(topic)

print("\n========== FINAL BLOG ==========\n")

print(result["blog"])

print("\n========== RESEARCH SOURCES ==========\n")

for item in result["research"]:
    print(item["title"])
    print(item["url"])
