from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# import os
# from dotenv import load_dotenv

# load_dotenv()


ACCOUNT_SID="AC62f70d4751a713e217c7c23f24ce58ee"
AUTH_TOKEN="bb7212d4e217a51d2ee42f7f3b69c753"
TO_NUMBER="5147704765" # my number to send to
FROM_NUMBER="+17129738496" # twilio number to send from

app = Flask(__name__)


account_sid =ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)


@app.route('/send_sms', methods=['POST'])
def send_sms():
    to_number = TO_NUMBER
    from_number = FROM_NUMBER
    print("sending message with picture")

    message_body = request.form['message_body']

    if 'image' not in request.files:
        return jsonify({'error': 'No image attached'})

    image_file = request.files['image']
    print(image_file)

    # Check if the file is a valid image file
    if image_file and allowed_file(image_file.filename):

        message = client.messages.create(
            to=to_number,
            from_=from_number,
            body=message_body,
            media_url=['https://sugargeekshow.com/wp-content/uploads/2023/10/easy_chocolate_cake_slice.jpg']
            
        )

        return jsonify({'message_sid': message.sid})
    else:
        return jsonify({'error': 'Invalid image file'})

    """files can only be images"""
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}



if __name__ == '__main__':
    app.run(debug=True)


