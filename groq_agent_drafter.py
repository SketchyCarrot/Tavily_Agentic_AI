from langchain.chat_models import init_chat_model
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
import getpass
import os

os.environ["GROQ_API_KEY"] = "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"

model = init_chat_model("llama3-8b-8192", model_provider="groq")

title_schema = ResponseSchema(name="title", description="The Title of the research topic.")
abstract_schema = ResponseSchema(name="abstract", description="The abstract of the entire study.")
intro_schema = ResponseSchema(name="intro", description="The introduction for the draft.")
body_schema = ResponseSchema(name="body", description="The body content.")
conclusion_schema = ResponseSchema(name="conclusion", description="The conclusion to the entire study, including summarizing the results (if any).")
references_schema = ResponseSchema(name="references", description="The references in the data.")
image_links_schema = ResponseSchema(name="images", description="The links of the images in the data.")

response_schemas = [
        title_schema,
        abstract_schema,
        intro_schema,
        body_schema,
        conclusion_schema,
        references_schema,
        image_links_schema,
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()


research_template = research_template = """
You are an expert academic researcher and writer.
Your task is to generate a structured research draft in strict JSON format using the following schema:
{format_instructions}
Each section (abstract, intro, body, conclusion) should be thoughtful, coherent, and at least 100 words long.
Please write:
- A clear and academic 'title'.
- A concise and informative 'abstract'.
- A strong 'introduction' to set context.
- A well-developed 'body' section with evidence or analysis.
- A reflective 'conclusion' summarizing the study.

Also:
- Include references in 'Harvard referencing style' with 'research papers listed first'.
- If image links are provided in the data, list them under the `images` field.

Use only the information from the data below, enclosed in triple backticks.

```data
{text}
```"""
prompt_template = ChatPromptTemplate.from_template(research_template)

def generate_research_draft(text: str):
        formatted_prompt = prompt_template.format_messages(
        text=text,
        format_instructions=format_instructions,
        )
        answer_draft = model(formatted_prompt)
        parsed_response = output_parser.parse(answer_draft.content)
        return parsed_response