import streamlit as st
import json
import os

# import api requests
from api_requests import get_request, post_request

# Get the seaplane API key
API_KEY = os.getenv("SEAPLANE_API_KEY")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.history = []

    # start with a welcome message and append it to the state
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": """
                <your welcome message here. Messages support markdown>
                """,
        }
    )

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # submit question to seaplane
    post_r = post_request(API_KEY, prompt, st.session_state.history)

    try:
        # get the request id from the response
        post_r_data = json.loads(post_r)
        request_id = post_r_data["id"]

        # counter to see how long we are waiting
        counter = 0

        while True:
            # GET request to get the result in loop to anticpate longer
            # processing times
            get_r = get_request(API_KEY, request_id)
            get_r_data = json.loads(get_r)

            # if more than 2 seconds tell the user we are busy processing
            if counter == 1:
                with st.chat_message("assistant"):
                    st.markdown("Searching through all the docs please bear with me...")
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "Searching through all the docs please bear with me...",
                        }
                    )

            # update counter
            counter += 1

            # update response once status is completed
            if get_r_data["status"] == "completed":
                # get the answer from the LLM
                response = get_r_data["output"][0]["result"]

                # get the relevant source documents from the request
                source_docs = get_r_data["output"][0]["source_documents"]

                # start of the resposne documents message
                source_response = (
                    "Take a look at the following documents to learn more: \n"
                )

                # create a list of relevant documents to display
                for idx, text in enumerate(source_docs):
                    source_response += f" - [{source_docs[idx]}]({source_docs[idx]})\n"

                # break out of repetitive GET loop when we get a response
                break

    # catch an error with the GET request and show it in the chat. You can turn
    # this off for production workloads where you don't want your users to see
    # the errors
    except Exception as error:
        print("Error")
        response = error

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # combine the LLM response and the source documents into a single
        # response message
        combined_response = response + "\n\n" + source_response
        st.markdown(combined_response)

        # store the history
        st.session_state.history.append((prompt, response))

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": combined_response}
    )
