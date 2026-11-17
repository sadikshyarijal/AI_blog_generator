
import { useState } from "react";
import {
  Sparkles,
  FileText,
  Search,
  PenTool,
  CheckCircle,
  ArrowRight,
  Menu
} from "lucide-react";

import "./App.css";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";


function renderBlogWithCitations(text) {
  const parts = text.split(/(\[\d+\])/g);

  return parts.map((part, index) => {
    const match = part.match(/^\[(\d+)\]$/);

    if (match) {
      const number = Number(match[1]);

      return (
        <a
          key={index}
          href={`#source-${number}`}
          className="inline-citation"
        >
          [{number}]
        </a>
      );
    }

    return part;
  });
}

function App() {
  const [topic, setTopic] = useState("");
  const [loading, setLoading] = useState(false);
  const [blog, setBlog] = useState("");
  const [error, setError] = useState("");
  const [research, setResearch] = useState([]);

  const handleGenerate = async () => {
    if (topic.trim().length < 3) return;

    setLoading(true);
    setError("");
    setBlog("");
    setResearch([]);

    try {
        const response = await fetch(`${import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"}/generate-blog`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            topic: topic.trim(),
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Blog generation failed.");
      }

      setBlog(data.blog);
      setResearch(data.research || []);

    } catch (err) {
      setError(err.message || "Unable to connect to the backend.");

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      <nav className="navbar">
        <div className="logo">
          <Sparkles size={24} />
          <span>Sourcer</span>
        </div>

        <div className="nav-links">
          <a href="#home">Home</a>
          <a href="#features">Features</a>
          <a href="#about">About</a>
        </div>

        <button className="menu-button">
          <Menu size={22} />
        </button>
      </nav>

      <main className="hero" id="home">

        <div className="hero-badge">
          <Sparkles size={15} />
          AI POWERED BLOG GENERATOR
        </div>

        <h1>
          Turn your ideas into
          <span> engaging blogs.</span>
        </h1>

        <p className="hero-description">
          Research, write and refine your content with
          intelligent AI agents. All in one place.
        </p>

        <div className="generator-box">

          <label htmlFor="topic">
            What would you like to write about?
          </label>

          <textarea
            id="topic"
            placeholder="Example: The future of artificial intelligence..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            maxLength={200}
          />

          <div className="generator-footer">

            <span>{topic.length}/200 characters</span>

            <button
              className="generate-button"
              onClick={handleGenerate}
              disabled={loading || topic.trim().length < 3}
            >
              {loading ? "Generating..." : "Generate Blog"}
              <ArrowRight size={18} />
            </button>

          </div>

          {loading && (
  <div className="generation-status">
    <div className="status-text">
      <Sparkles size={18} />
      <span>Your AI agents are working...</span>
    </div>

    <div className="progress-track">
      <div className="progress-bar"></div>
    </div>

    <p>
      Planning, researching, writing and reviewing your blog.
      This may take a few minutes.
    </p>
  </div>
)}
          {error && (
            <p className="error-message">
              {error}
            </p>
          )}

        </div>

        <div className="workflow" id="features">

          <div className="workflow-item">
            <FileText size={21} />
            <span>Plan</span>
          </div>

          <ArrowRight className="workflow-arrow" size={18} />

          <div className="workflow-item">
            <Search size={21} />
            <span>Research</span>
          </div>

          <ArrowRight className="workflow-arrow" size={18} />

          <div className="workflow-item">
            <PenTool size={21} />
            <span>Write</span>
          </div>

          <ArrowRight className="workflow-arrow" size={18} />

          <div className="workflow-item">
            <CheckCircle size={21} />
            <span>Review</span>
          </div>

        </div>

        
{blog && (
  <section className="blog-result">

    <div className="result-heading">
      <Sparkles size={20} />
      <h2>Your generated blog</h2>
    </div>

    <article className="blog-content">
  <ReactMarkdown
    remarkPlugins={[remarkGfm]}
  >
    {blog.replace(
      /\[(\d+)\]/g,
      "[$&](#source-$1)"
    )}
  </ReactMarkdown>
</article>
    {/* Research Sources */}
    <div className="sources-section">

      <h3>
        <Search size={19} />
        Research & References
      </h3>

      {research.length > 0 ? (
        <div className="sources-list">

          {research.map((item, index) => (
            <div
  className="source-item"
  id={`source-${index + 1}`}
  key={item.url || index}
> 

              <span className="source-number">
                {index + 1}
              </span>

              <div className="source-details">
                <a
                  href={item.url}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {item.title || "Research source"}
                  <ArrowRight size={14} />
                </a>

                <p>{item.url}</p>
              </div>

            </div>
          ))}

        </div>
      ) : (
        <p>No research sources were returned.</p>
      )}

    </div>

  </section>
)}


      </main>

      <footer id="about">
        <p>© 2026 Sourcer. Powered by intelligent AI agents.</p>
      </footer>

    </div>
  );
}

export default App;
