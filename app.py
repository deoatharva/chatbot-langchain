from flask import Flask, request, jsonify
from langchain_groq import ChatGroq
from pyngrok import ngrok
import os

# Check if the Groq API key is set
groq_api_key = os.getenv('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', None)  # Fetch API key from environment variable
if not groq_api_key:
    raise ValueError("API key has issue. Please check if it is expire or not.")

# Initialize the LLM with the Groq API key and model
llm = ChatGroq(
    temperature=0,
    groq_api_key=groq_api_key,  # Use the retrieved API key
    model_name="llama-3.1-70b-versatile",
)

# Flask application setup
app = Flask(__name__)

# Route to handle the prediction request
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("input")
    if data:
        try:
            # Invoke the LLM model to get the response
            response = llm.invoke(data)
            return jsonify({"response": response.content})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Please provide a valid input."}), 400

# Open a tunnel to the HTTP server using ngrok
public_url = ngrok.connect(5000)
print(f" * Running on {public_url}")

# Start the Flask app
if __name__ == "__main__":
    app.run(port=5000)
