# Dual-Agent Research Drafter  
**Submission for Kairon Artificial Intelligence Internship**

This project is an implementation of **Tavily** for web search and **Groq (LLaMA3)** AI agents using **Langchain** to do research and draft answers. The app extracts the latest web data and generates a structured research document with a **title**, **abstract**, **introduction**, **body**, **conclusion**, **references**, and **images**.

## 1. #Installation
```bash
git clone [https://github.com/your-username/dual-agent-drafter](https://github.com/SketchyCarrot/Tavily_Agentic_AI.git)
cd dual-agent-drafter
pip install langchain groq tavily streamlit
```

## 2. API Keys
Set your API keys in ```main.py```
```markdown
os.environ["GROQ_API_KEY"] = "your-groq-key"
TAVILY_API_KEY = "your-tavily-key"
```

## 3. How to run
```streamlit run main.py```
