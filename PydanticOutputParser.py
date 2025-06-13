from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4")

class Person(BaseModel):
    name:str=Field(description="Name of the person")
    age:int=Field(lt=100,gt=18,description="Age of the person")
    city:str=Field(description="Name of the city the person belongs to")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate the name, age, and city of a person from {country}./n{format_instruction}",
    input_variables=["country"],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template|model|parser

result=chain.invoke({'country':'India'})

print(result)