
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import xlwings as xw


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def reply():
    text = request.form.get('Body')

   
    res = MessagingResponse()
    data=[]
    with open('data', 'rb') as fb:
        data = pickle.load(fb)
    message = ""

    print(f"{data[0]}")
    for item in data:
        if item[0] == text:
            message = f"{item[2]} \nStd - {str(int(item[1]))}\nCloths = {str(item[3])}\nBooks = {str(item[4])}\nTotal = {str(item[5])}"
            res.message(message)
            break
            # res.message("Not Fount")

    return str(res)


if __name__ == "__main__":
    app.run()
