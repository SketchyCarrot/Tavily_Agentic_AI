from langchain.chat_models import init_chat_model
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
import getpass
import os



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


research_template = """You are a professional researcher. Draft an answer with the given sections {format_instructions} based on the data given inside the triple backticks. Use at least 100 words for abstract, into, body and conclusion. Provide the references URL in harvard referencing style. Data: ```{text}```"""
prompt_template = ChatPromptTemplate.from_template(research_template)

def generate_research_draft(text: str):
        formatted_prompt = prompt_template.format_messages(
        text=text,
        format_instructions=format_instructions,
        )
        answer_draft = model(formatted_prompt)
        parsed_response = output_parser.parse(answer_draft.content)
        return parsed_response