from flask import  request, Flask
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/bot', methods =['POST'])
def bot():
    user_msg = request.values.get('Body','').lower()
    bot_response = MessagingResponse()
    msg = bot_response.message()
    if 'hello' in user_msg:
        msg.body("at your service")
        #msg.media(link) to send images etc
    elif 'hi' in user_msg:
        msg.body("heyy")
    else:
        msg.body("at your service00")
    return str(bot_response)

if __name__=="__main__":
    app.run()
