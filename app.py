import os
from twilio.rest import Client

# NEVER hardcode secrets!
# Use .env file instead (add .env to .gitignore)
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

@app.route("/send-sos", methods=["GET"])
def send_sos():
    try:
        lat = request.args.get("lat")
        lng = request.args.get("lng")

        print("Received coordinates:", lat, lng)

        location_link = f"https://www.google.com/maps?q={lat},{lng}"

        message_body = (
            "🚨 SOS ALERT!\n"
            "User needs immediate help.\n\n"
            f"📍 Location:\n{location_link}"
        )

        message = client.messages.create(
            from_="whatsapp:+14155238886",
            to="whatsapp:"",
            body=message_body
        )

        return jsonify({
            "status": "success",
            "sid": message.sid
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
