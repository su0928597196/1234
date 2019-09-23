from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('+8ppuqlOtUzevqJMjXxkJ4ryUh661cgK4Ro2avASD25XektkpRyhpADvVqT1q0JZcpjsitF0ajqydFDi4u1EkuJ7PdNQhF7LsT94f8IdMAkjZgV1Ddw0WdvGxe9KrUTnA2WWTEWridENtmYhmun0QAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('41ad6acca52aa078eaeb0135e7a8ec9f')


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
    r = '請按照順序輸入1~18'
    if msg == 1:
        r = '老實說,我真的煩惱了很久該不該留下來'
    elif msg == 2:
        r = '心情上是真的超想留下'
    elif msg == 3:
        r = '卻知道留下只是你的負擔'
    elif msg == 4:
        r = '可是我試著問自己'
    elif msg == 5:
        r = '如果你真的把我當成陌生人的話'
    elif msg == 6:
        r = '你會對我說這些嗎'
    elif msg == 7:
        r = '你應該會連回都不回,直接封鎖了吧,像另外兩個那樣'
    elif msg == 8:
        r = '你還願意留個朋友的位置等我,甚至回覆我'
    elif msg == 9:
        r = '或許不是你想斷開,而是不得不斷開,因為我真的太打擾你了'
    elif msg == 10:
        r = '你是在等待,等待我變成能給你自由,奮發向上的人'
    elif msg == 11:
        r = '所以當你判斷我改變的時候,希望你能解開我的所有封鎖,讓我們回到從前,在此之前我會努力'
    elif msg == 12:
        r = '等我'
    elif msg == 13:
        r = '如果我的猜測沒錯,你能告訴我是不是這樣嗎,因為我實在沒甚麼自信,我覺得這個解讀真的是我想多了'
    elif msg == 14:
        r = '如果沒錯的話'
    elif msg == 15:
        r = '我最後的決定,是想留下來,應該不會再變了'
    elif msg == 16:
        r = '最後我只想說,我果然還是放不下你,但我會試著喜歡你,卻把你當朋友看待,我會做到的'
    elif msg == 17:
        r = '因為我認為這輩子除了你,我不會再喜歡其他人了♥'

    
    if msg == 18:
        sticker_message = StickerSendMessage(package_id='11538',sticker_id='51626495')
    elif:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()