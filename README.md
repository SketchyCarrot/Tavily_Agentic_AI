# Dual-Agent Reseach Drafter
Submission for Kairon Artificial Intelligence Internship

This projects is an implentation of Tavily for web search and Groq (LLaMA3) AI Agents using Langgraph, to do research and draft answers. The app extracts the latest web data and generates a structured research document with title, abstract, introduction, body, conclusion, references, and images.

# Installation
```git clone https://github.com/SketchyCarrot/Tavily_Agentic_AI.git
cd dual-agent-drafter
pip install streamlit langchain groq tavily-python```

# API Keys
Set your API keys in ```main.py```
```os.environ["GROQ_API_KEY"] = "your-groq-key"
TAVILY_API_KEY = "your-tavily-key"```

# How to run
```streamlit run main.py```
