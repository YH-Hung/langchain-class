from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from llm import create_llm


def run(args):
    llm = create_llm(args)

    code_prompt = PromptTemplate.from_template(
        "Write a very short {language} function that will {task}"
    )
    parser = StrOutputParser()

    code_chain = code_prompt | llm | parser

    test_prompt = PromptTemplate.from_template(
        "Write a test for the following {language} code:\n{code}"
    )
    test_chain = test_prompt | llm | parser

    combined_chain = RunnablePassthrough.assign(code=code_chain).assign(test=test_chain)

    result = combined_chain.invoke({"language": args.language, "task": args.task})
    print(">>>>>> GENERATED CODE:")
    print(result["code"])
    print(">>>>>> GENERATED TEST:")
    print(result["test"])
