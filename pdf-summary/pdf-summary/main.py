from seaplane import app, config, start

# import the tasks
from pre_processing import pre_processing
from inference import inferencing
from database import database

# set API keys
api_keys = {
    "SEAPLANE_API_KEY": "<YOUR-SEAPLANE-API-KEY>",
    "OPENAI_API_KEY": "<YOUR-OPENAI-API-KEY>",
}
config.set_api_keys(api_keys)


@app(id="pdf-summary", path="/demo-input", method="POST")
def my_smartpipe(body):
    # wire the tasks together in a DAG
    prompt = pre_processing(body)
    summary = inferencing(prompt)
    return database(summary)


start()
