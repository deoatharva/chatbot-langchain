import streamlit as st
from langchain_groq import ChatGroq
import os

# Fetch API key from environment variable
groq_api_key = os.getenv("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")

# Check if the API key is available
if not groq_api_key:
    st.error("API key having issues! Please check if it is expire or not.")
else:
    # Initialize the LLM with the Groq API key and model
    llm = ChatGroq(
        temperature=0,
        groq_api_key=groq_api_key,
        model_name="llama-3.1-70b-versatile",
    )

    # Streamlit application title and description
    st.title("Chat with LLM")
    st.markdown("Enter a question below, and get an answer from the model!")

    # Text input field for the user to type their question
    user_question = st.text_input("Ask a question:")

    # Function to get the model's response
    def get_response(question):
        if question:
            try:
                # Call the LLM to get the response
                response = llm.invoke(question)
                return response.content  # Adjust this according to the actual response format
            except Exception as e:
                return f"Error in getting response: {e}"
        return "Please enter a question to get an answer."

    # Display the response when the user enters a question
    if user_question:
        response_content = get_response(user_question)
        st.write("Model's response:")
        st.write(response_content)
