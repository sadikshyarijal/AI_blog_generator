
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from agents.blog_workflow import generate_blog


# Create the FastAPI application
app = FastAPI(
    title="AI Blog Generator API",
    description="API for generating AI-powered blog articles",
    version="1.0.0"
)


# Allow our React frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
   allow_origins=[
    "http://localhost:5173",
    "https://sourcer-ai-blog-generetor.netlify.app"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the data we expect from the frontend
class BlogRequest(BaseModel):
    topic: str = Field(min_length=3, max_length=200)


# A simple endpoint to check whether the backend is running
@app.get("/")
def home():
    return {
        "message": "AI Blog Generator API is running!"
    }


# Endpoint to generate a blog
@app.post("/generate-blog")
def create_blog(request: BlogRequest):

    try:
        result = generate_blog(request.topic)

        return {
            "success": True,
            "topic": result["topic"],
            "plan": result["plan"],
            "research": result["research"],
            "blog": result["blog"]
        }

    except Exception as error:
        print("Blog generation error:", error)

        raise HTTPException(
            status_code=500,
            detail="Something went wrong while generating the blog."
        )
