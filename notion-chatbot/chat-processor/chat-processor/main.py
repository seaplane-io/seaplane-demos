from notion_processor import process_notion
from seaplane import app, start


# the HTTP enabled application
@app(id="processors", path="/process-chat-data", method=["POST", "GET"])
def chatbot_processor_application(data):
    # call the notion processor
    return process_notion(data)


start()
