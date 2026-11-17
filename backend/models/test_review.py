
from agents.review_agent import review_blog

topic = "Impact of Artificial Intelligence on Education"

sample_blog = """
# AI in Education

Artificial intelligence are changing education.
It help students learn faster and provide
personalized learning experiences.

Teachers can also use AI tools to reduce
repetitive tasks.
"""

sample_research = [
    {
        "title": "Example Education Research",
        "url": "https://example.com/research",
        "content": "AI tools can support personalized learning."
    }
]

reviewed_blog = review_blog(
    topic,
    sample_blog,
    sample_research
)

print("\n========== REVIEWED BLOG ==========\n")
print(reviewed_blog)
