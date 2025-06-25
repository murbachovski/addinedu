# https://www.youtube.com/watch?v=bANQk--Maxs
# https://lmstudio.ai/
# pip install langchain-openai
# python > 3.10
# LM Studio 서버 구동 후

from langchain_openai import ChatOpenAI
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-7b-instruct-kowiki-qa",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

prompt = PromptTemplate.from_template(
    """
    You are a helpful.
    
#Question
{question}

#Answer"""
)

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"question": "서울의 면적은?"})

print(response)