from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--task", default="return a list of numbers")
    arg_parser.add_argument("--language", default="python")
    args = arg_parser.parse_args()

    llm = ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",  # any non-empty string usually works
        model="qwen/qwen3.5-9b"
    )

    code_prompt = PromptTemplate.from_template("Write a very short {language} function that will {task}")
    parser = StrOutputParser()

    code_chain = code_prompt | llm | parser

    result = code_chain.invoke({"language": args.language, "task": args.task})
    print(result)
    


if __name__ == "__main__":
    main()
