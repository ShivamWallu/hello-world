from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    
app.run(debug=True, host='0.0.0.0', port=80)

