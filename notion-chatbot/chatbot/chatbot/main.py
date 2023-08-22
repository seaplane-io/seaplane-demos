from seaplane import app, task, start
from langchain.chains import ConversationalRetrievalChain
from seaplane.integrations.langchain import SeaplaneLLM, langchain_vectorstore


# the chat task that performs the document search and feeds them to the LLM
@task(type="inference", id="chat-task")
def chat_task(data):
    # create vector store instance with langchain integration
    vectorstore = langchain_vectorstore(index_name="chat-documents")

    # Create the chain
    pdf_qa_hf = ConversationalRetrievalChain.from_llm(
        llm=SeaplaneLLM(),
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
    )

    # answer the question using MPT-30B
    result = pdf_qa_hf(
        {"question": data["query"], "chat_history": data["chat_history"]}
    )

    # return only the answer to the user
    return result["answer"].split("\n\n### Response\n")[1]


# HTTP enabled chat app
@app(id="chat-app", path="/chat", method=["POST", "GET"])
def chat_app(data):
    return chat_task(data)


start()
