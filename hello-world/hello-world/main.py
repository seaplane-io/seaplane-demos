from seaplane import task, app, config, start
import json

api_keys = {
    "SEAPLANE_API_KEY": "<YOUR-API-KEY>"
}

config.set_api_keys(api_keys)

@task(type='compute', id='world-task')
def world(data):
    s = "World " + data['name']
    return json.dumps({"string" : s})

@task(type='compute', id='hello-task')
def hello(data):
    data = json.loads(data)
    s = "hello " + data['string']
    return json.dumps({"string" : s})

@app(path='/hello', method=['POST', 'GET'], id='hello-world')
def hello_world(body):
    string = world(body)
    return hello(string)


start()