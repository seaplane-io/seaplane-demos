# Hello World Demo Application

This demo application deploys a simple hello world application on Seaplane. It
takes a name (string) and returns a string `Hello World <NAME>`.

To deploy follow these steps. We assume you have Seaplane installed on your
machine. You can do so by running `pip3 install seaplane`

- Open `main.py` and replace the Seaplane API key placeholders with your keys.
- In the main `hello-world` directory, run `poetry install`.
- Then run `seaplane deploy` to deploy the app.

You can create a request to the application you just deployed using either `cURL` or `plane`.

### cURL

- You will find the `<YOUR-DEPLOY-ENDPOINT>` in the output after running `seaplane deploy`.
- Configure your TOKEN: `TOKEN=$(curl -X POST https://flightdeck.cplane.cloud/identity/token --header "Authorization: Bearer <API-KEY>")`
- Create a `POST` request to your application by running the command below. This will return the batch ID. 
```
curl -X POST -H 'Content-Type: application/octet-stream' \
   -H "Authorization: Bearer $TOKEN" \
   -d '{"name": "<YOUR-NAME>"}' <YOUR-DEPLOY-ENDPOINT>
```
- To retrieve the response, create a `GET` request by running the command below. 
```
curl -X GET -H "Authorization: Bearer $TOKEN" https://carrier.cplane.cloud/v1/endpoints/hello-world/response/<YOUR-BATCH-ID>.1.1
```


### plane

To set up `plane`, follow the instructions [here](https://developers.seaplane.io/docs/plane/).

- Create a `POST` request to your application by running: `plane endpoints request hello-world -d '{"name": "<YOUR-NAME>"}'`. This will return the batch ID.
- To retrieve the response, create a `GET` request by running: `plane endpoints response <YOUR-BATCH-ID>.1.1`
