from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def main():
    llm = ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",  # any non-empty string usually works
        model="qwen/qwen3.5-9b"
    )

    result = llm.invoke([HumanMessage("who are you?")])
    print(result.content)
    


if __name__ == "__main__":
    main()
