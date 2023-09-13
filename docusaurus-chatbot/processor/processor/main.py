from seaplane import app, start
from processing import process_docs


@app(id="docs-chatbot", path="/process-docs", method=["POST", "GET"])
def docs_processor(body):
    """
    Creates a HTTP enabled application with POST and GET enabled. Available on
    /process-docs. You can deploy this application by openeing a terminal and
    navigating to the root of the project and run seaplane deploy. Don't forget
    to update your API key for both Seaplane and OpenAI in the .env file.

    Args:
        data (dict): The HTTP post data.

    Returns:
        dict: Returns the output fo the chat_task task
    """
    # process notion
    return process_docs(body)


start()
