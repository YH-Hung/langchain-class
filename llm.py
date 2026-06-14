from langchain_openai import ChatOpenAI


def create_llm(args):
    return ChatOpenAI(
        base_url=args.base_url,
        api_key=args.api_key,
        model=args.model,
    )
