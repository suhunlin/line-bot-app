from flask import Flask, request, abort #因為我們用flask來架設伺服器，所以import flask

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('CQzA9nLYPmunXwSjzM1rPCPMySjN57YlKm1qnBzip4JuNE6ElAkPw4qJu0jmF70ItdGtXg9NUgUAWdbuKfexH4vRW5tKSGoXcpjcRF3FSWlNQqmcf8Suol1JDTIHxTUsQniNPKonwyBCHF1aG9YpMwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('875b2ea31d6851bba2ef6791d7675062')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '1':
        msg = '冠儒是笨蛋'
    elif event.message.text == '2':
        msg = '書弘是大帥哥'
    elif event.message.text == '3':
        msg = '品妤是大美女'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg))


if __name__ == "__main__":
    app.run()