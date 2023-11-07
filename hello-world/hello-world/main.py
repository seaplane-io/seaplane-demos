from seaplane import task, app, start
import json

# World task
@task(type="compute", id="world-task")
def world(context):
    json_body = json.loads(context.body)
    new_message = "World " + json_body['name']
    context.emit(new_message)

# Hello task
@task(type='compute', id='hello-task')
def hello(context):
    world_output = context.body.decode()
    final_message = "Hello " + world_output
    context.emit(final_message)

# Application
@app(path='/hello', method=['POST', 'GET'], id='hello-world')
def hello_world(body):
    string = world(body)
    return hello(string)

start()
