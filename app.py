from flask import Flask, request, abort

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

line_bot_api = LineBotApi('xlb7cZwZSJTUgwaM1ncwm2BUi5f6TfS+r6MovxSUaT4l5sTHgad+6iJikZ8785kr+dPDgoPeLigtFlNhoTNOMwP/sH+6ad2ga0Zy7q9h5oCCObtTambgIrwy2IEOq6uK4UzfzRmbTCzthsW73tXSWQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4c4db686792164206cbfb32bd5c19f53')


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
    msg = event.message.text
    s = '你吃飯了嗎'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()