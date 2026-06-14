from langchain_core.messages import HumanMessage

from llm import create_llm


EXIT_COMMANDS = {"exit", "quit"}


def run(args):
    llm = create_llm(args)
    messages = []

    print("Chatbot mode. Type 'exit' or 'quit' to stop.")

    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print()
            break

        if user_input.lower() in EXIT_COMMANDS:
            break
        if not user_input:
            continue

        messages.append(HumanMessage(content=user_input))
        response = llm.invoke(messages)
        messages.append(response)
        print(f"Assistant: {response.content}")
