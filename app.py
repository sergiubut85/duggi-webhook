from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        data = request.json
        return {"message": "Webhook received", "data": data}, 200
    return "Hello, this is the webhook app!"

if __name__ == "__main__":
    app.run()
