
from cgitb import text
from operator import indexOf
from flask import Flask, request
from numpy import std
from twilio.twiml.messaging_response import MessagingResponse
import xlwings as xw


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def reply():
    text = request.form.get('Body')

    wb = xw.Book('Books.xlsx')
    ws = wb.sheets[f'Bot']
    res = MessagingResponse()

    data = ws.range('A2:F331').value
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
