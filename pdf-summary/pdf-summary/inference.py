from seaplane import task
import json


@task(type="inference", id="pdf-inferencer", model="gpt-3.5")
def inferencing(data, model):
    # get the URL and prompt from the input message
    prompt = data["prompt"]
    url = data["url"]

    # construct the model parameters including the prompt from the prev step
    params = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }

    # run the inference request
    result = model(params)

    # return the inferenced result plus input and parameters
    result["url"] = url
    result["prompt"] = prompt

    return json.dumps(result)
