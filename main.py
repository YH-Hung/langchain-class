from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--task", default="return a list of numbers")
    arg_parser.add_argument("--language", default="python")
    args = arg_parser.parse_args()

    llm = ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",  # any non-empty string usually works
        model="google/gemma-4-e4b"
    )

    code_prompt = PromptTemplate.from_template("Write a very short {language} function that will {task}")
    parser = StrOutputParser()

    # the output is NOT plain dictionary, so StrOutputParser is required.
    code_chain = code_prompt | llm | StrOutputParser()

    test_prompt = PromptTemplate.from_template("Write a test for the following {language} code:\n{code}")
    test_chain = test_prompt | llm | parser

    # () for line continuation
    combined_chain = (
        RunnablePassthrough.assign(code=code_chain)
        .assign(test=test_chain)
    )

    result = combined_chain.invoke({"language": args.language, "task": args.task})
    print(">>>>>> GENERATED CODE:")
    print(result["code"])
    print(">>>>>> GENERATED TEST:")
    print(result["test"])

if __name__ == "__main__":
    main()
