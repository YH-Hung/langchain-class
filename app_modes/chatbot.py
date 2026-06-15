from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import create_llm


EXIT_COMMANDS = {"exit", "quit"}


def run(args):
    prompt = ChatPromptTemplate.from_messages([
        ("human", "{content}")
    ])

    llm = create_llm(args)
    parser = StrOutputParser()
    
    chain = prompt | llm | parser

    print("Chatbot mode. Type 'exit' or 'quit' to stop.")

    while True:
        try:
            user_input = input(">> ").strip()
            if user_input.lower() in EXIT_COMMANDS:
                break

            result = chain.invoke({"content": user_input})
            print(result)
        except EOFError:
            print()
            break

        