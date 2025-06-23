import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

load_dotenv()

groq_api = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api)

# Creating Prompt Template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Translate the following from English to {language}."),
        ("user", "{text}"),
    ]
)
parser = StrOutputParser()

# Creating Chain
chain = prompt_template | model | parser

# Definig APP
app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A simple API server using Langchain runnable interfaces")


# Chain Routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
