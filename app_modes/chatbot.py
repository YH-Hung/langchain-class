from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from llm import create_llm


EXIT_COMMANDS = {"exit", "quit"}


class ChatHistoryStore:
    def __init__(self):
        self._store: dict[str, BaseChatMessageHistory] = {}

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self._store:
            self._store[session_id] = InMemoryChatMessageHistory()
        return self._store[session_id]

def run(args):
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="history"),
        ("human", "{content}")
    ])

    llm = create_llm(args)
    parser = StrOutputParser()
    
    chain = prompt | llm | parser

    # LangChain had switch memory mechanism to LangGraph. 
    # If you need memory, DONNOT use LangChain, USE LangGraph instead.
    history_store = ChatHistoryStore()
    bot = RunnableWithMessageHistory(
        chain,
        history_store.get_session_history,
        input_messages_key="content",
        history_messages_key="history"
    )

    print("Chatbot mode. Type 'exit' or 'quit' to stop.")

    while True:
        try:
            user_input = input(">> ").strip()
            if user_input.lower() in EXIT_COMMANDS:
                break

            result = bot.invoke({"content": user_input}, {"configurable": {"session_id": "curr_session"}})
            print(result)
        except EOFError:
            print()
            break

        