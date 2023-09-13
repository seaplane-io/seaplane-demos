# Docusaurus Chatbot Powered by Seaplane and OpenAI

This repository contains all the required code to build and deploy a chatbot
with in-context learning on Docusaurus pages. Not familiar with in-context
learning you can read more about it
[here](https://www.seaplane.io/blog/on-in-context-learning-and-vector-databases).
You can see a live example of a chatbot on the Seaplane docs
[here](https://developers.seaplane.io/docs/seaplane-gpt).

This chatbot requires:
-  A Seaplane account (sign up
[here](https://developers.seaplane.io/docs/seaplane-gpt))
- An OpenAI account (sign up
  [here](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBPaGtHUlZEajRhOWFmWkcwVmtlR3huX2ZfWUNnMGMtQ6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFp2M3N6QkxlLUN4eDI1WVFvaHhtZjh4aVpOYnpIcENWo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q))
- A Streamlit Cloud account (sign up [here](https://share.streamlit.io/signup))

## Application structure

The chatbot consist of two Seaplane applications deployed and one Streamlit
application.

- processor - To process your documentation pages and store them in a vector
  store
- chatbot - Powers the chat back end
- Streamlit - Powers the front end

While its easist to use Seaplane you are free to copy the code and make changes
to deploy it on your own infrastructure or use other platforms.

## Prepping your Docusaurus website

The processor app requires a `sitemap.xml` file to function. You can add one
using the [sitemap
plugin](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-sitemap). Be
aware that sitemaps only work on live deployments and not on local deployments.
Once installed confirm the location of your sitemap. Usually
`www.yourdomain.com/sitemap.xml`

## Documents processor

The processor application creates a scalable HTTP endpoint that takes your
`sitemap.xml` url as input and creates vector representations of all your
documentation pages. 

### Deploying

Before you deploy open `processor/processor/processing.py` and update the vector
store index name on line 26.

```python
index_name = "<YOUR-INDEX>"
```

Also update `processor/.env` and add your Seaplane API key and OpenAI API key.

```text
SEAPLANE_API_KEY=<YOUR-SEAPLANE-KEY>
OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>
```

Navigate to the root directory of the processor application i.e `/processor` and
run `poetry install` followed by `seaplane deploy`. Once completed your
processing applicaiton is available on the provided URL.

```text
[Seaplane] 🚀 docs-chatbot Endpoint: POST <YOUR-APPLICATION-URL>
```

### Indexing your pages

You can now start your first processing run. You should rerun the processing of
your documentation pages every time you add new information. Rerunning recreates the vector store so your chat app will be temporaritly unavailable while the processing runs. Usually a few seconds depending on the number of documentation pages you have.

To start an index run call your endpoint with the following cURL request. Note
the application URL might differ slightly if you made any changes to the app.
The deployment step provides the correct deployment URL after it finishes the
deployment.

```bash
curl -X POST -H 'Content-Type: application/json' \
--header "Authorization: Bearer $(curl https://flightdeck.cplane.cloud/identity/token --request POST  --header "Authorization: Bearer <YOUR-API-KEY>")" \
-d '{"input" : [{"url": "<YOUR-SITEMAP-URL>"}]}' https://carrier.cplane.cloud/apps/docs-chatbot/latest/process-docs
```

Replace `<YOUR-API-KEY>` with your Seaplane API key and `<YOUR-SITEMAP-URL>`
with the URL to your `sitemap.xml` file. The POST request output contains your
request `id`

```json
{"id":"<REQUEST_ID>","status":"processing"}
```

You can check the status of your processing request with the following cURL
command. Replace `<YOUR-API-KEY>` with your Seaplane API key and `<REQUEST-ID>`
with the `id` from the POST output JSON.

```bash
curl -X GET \
--header "Authorization: Bearer $(curl https://flightdeck.cplane.cloud/identity/token --request POST  --header "Authorization: Bearer <YOUR-API-KEY>")" \
https://carrier.cplane.cloud/apps/docs-chatbot/latest/process-docs/request/<REUEST-ID>
```

If completed the GET output will look like this:

```json
{"id":"<REQUEST_ID>","output":["done"],"status":"completed"}
```

## Deploy the chatbot application

With your pages indexed you can deploy the chat API endpoint. Navigate to
`/chatbot/chabot` and update the `index_name` on line 33 to the same
`index_name` as you used in your processor application.

```python
index_name = "<INDEX-NAME>"
```

Navigate to `/chatbot`. Update the Seaplane API key and OpenAI API key in the
`.env` file.

In the same directory run `poetry install` followed by `seaplane deploy` to
deploy your application. Once completed your application is live on the provided
URL.

## Deploy the streamlit front end

With your processor and chatbot endpoint deployed you can start the deployment
of the front-end. The front-end is deployed on Streamlit Cloud.

Fork this repository on Github. Head over to Streamlit cloud and create a new
application. Select the newly created repo as the source repository and set
`streamlit_chat.py` as the main file path. Optionally update the App URL.

Click on advanced settings and add your Seaplane API key as a secret by adding
the following line to the secretes field. Replace `<YOUR-SEAPLANE-API-KEY>` with
your Seaplane API key. Note the `"` around the API key.

```text
SEAPLANE_API_KEY="<YOUR-SEAPLANE-API-KEY>"
```

Finally, click deploy. Your new chat app is ready for use once the deployment
finishes 🎉

### Adding the chatbot to your documentation pages

As a final step you can embed your chat application as an iframe directly into
your applicaiton pages. You can learn more about embedding your Streamlit
application
[here](https://docs.streamlit.io/streamlit-community-cloud/share-your-app/embed-your-app#embedding-with-iframes).

```html
<iframe
  src="<YOUR-STREAMLIT->"
  height="750"
  width="1000"
></iframe>
```

If you have any questions or issues with any of the steps above feel free to
contact me at [fokke@seaplane.io](mailto:fokke@seaplane.io)
