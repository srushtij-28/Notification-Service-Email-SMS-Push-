from flask import Flask, request, jsonify
from tasks import (
    send_email,
    send_sms,
    send_push
)

app = Flask(__name__)

@app.route("/notify", methods=["POST"])
def notify():

    data = request.get_json()

    channel = data["channel"]

    if channel == "email":

        task = send_email.delay(
            data["email"],
            data["subject"]
        )

    elif channel == "sms":

        task = send_sms.delay(
            data["number"]
        )

    elif channel == "push":

        task = send_push.delay(
            data["user"]
        )

    else:

        return jsonify({
            "message": "Invalid channel"
        }), 400

    return jsonify({
        "message": "Notification queued",
        "task_id": task.id
    })

@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(debug=True)
