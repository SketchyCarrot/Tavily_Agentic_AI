import streamlit as st
from tavily_agent import tavily_search_agent
from groq_agent_drafter import generate_research_draft
from tavily_agent import tavily_search_agent
from groq_agent_drafter import generate_research_draft, summarize

def main():
        st.set_page_config(page_title="Dual-agent Research Drafter", layout="wide")
        st.title("Dual-agent Research Drafter")

        st.markdown("Enter your query and adjust research paremeters.")

        query = st.text_input("1. Research Query", value="")
        search_depth = st.selectbox("2. Search Depth", ["basic", "advanced"], index=1)
        max_results = st.slider("3. Max Results", 1, 10, value=3)
        include_answer = st.selectbox("4. Include Answer", ["none", "basic", "advanced"], index=2)
        include_images = st.checkbox("5. Include Images", value=False)

        if st.button("Create Research Draft"):
                with st.spinner("Searching Tavily."):
                        total_content, references, image_links = tavily_search_agent(
                        query=query,
                        search_depth=search_depth,
                        max_results=max_results,
                        include_answer=include_answer,
                        include_images=include_images,
                        )


                with st.spinner("Drafting answer using Groq."):
                        summarized_content = summarize(text=total_content)
                        draft = generate_research_draft(text=summarized_content)

                st.markdown("### Title\n" + draft["title"])
                st.markdown("### Abstract\n" + draft["abstract"])
                st.markdown("### Introduction\n" + draft["intro"])
                st.markdown("### Body\n" + draft["body"])
                st.markdown("### Conclusion\n" + draft["conclusion"])
                st.markdown("### References")
                for reference in references:
                        st.markdown(f" {reference}")

                if image_links:
                        st.markdown("### Images")
                        for image in image_links:
                                st.image(image, use_container_width=True)


if __name__ == "__main__":
        main()