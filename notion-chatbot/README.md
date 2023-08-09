# Notion Chatbot Application

This demo project consists of two applications.

- Processor application - This application extracts the content used for ICL,
embeds the text into vectors and stores them in the vector store. 
- Chatbot application - This application provides the API interface for Q&A it
uses the content stored in the vector store to answer user questions.

Specifically, the processor application is built to scrape notion pages and
store their vector representation in the Seaplane vector store. You can follow
along with [this tutorial](https://developers.seaplane.io/tutorials/chatbot), or
directly clone the project and deploy it yourself.

To deploy the applications open `.env` files and update your Seaplane API key
and Notion Secret.

Run `poetry install` followed by `seaplane deploy` in both the chat-processor
and chatbot to deploy the applications.