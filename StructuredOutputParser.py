from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name="fact1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact2",description="Fact 1 about the topic"),
    ResponseSchema(name="fact3",description="Fact 1 about the topic")
]

parser=StructuredOutputParser(schema)

template=PromptTemplate(
    template="Give me 3 facts about {topic}./n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template|model|parser

result=chain.invoke({"topic":"Black Hole"})

print(result) 