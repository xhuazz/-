from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('0J5XDz26h0QZt21kC+88n15ifSc/Sfe+63Zf11z865+9hvQ+W71mTcPnNu5fhFiBilcLeAmuf1N5O5wqztAZgXkyrore5bCa6N6mfH3THIa8up/J+GzBHcayrOltZHZE/ECZUV5a2zywvy9jsSPMkwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('cb0c893e324fcc64fe72a5718c592c5e')


# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '下一節什麼課' in msg:
        import datetime
        
        # 建立課表資料庫，格式為 {星期幾: [課程1, 課程2, ...]}
        timetable = {
            0: ['公民', '英語', '數位科技進階','彈性學習時間','中國小說選讀','數學應用','商業溝通'],
            1: ['運算思維', '運算思維', '體育','會計實務','取為英文閱讀','經濟學進階','生涯規劃'],
            2: ['數位科技進階', '數位科技進階','商業經營管理', '趣味英文選讀','團體活動時間','團體活動時間','數學應用'],
            3: ['會計實務', '英語文', '體育','商業經營管理','經濟學進階','國語文','彈性學習時間'],
            4: ['資料庫應用', '資料庫應用', '會計實務','經濟學進階','國語文','數學應用','數位科技進階']}
            # 其他星期幾的課表資料

        # 定義函式 get_class_time，用來取得指定課程的上課時間
        def get_class_time(index, timetable):
            # 定義課程時間，格式為 'HH:MM-HH:MM'
            class_times = [
                '08:00-08:50',
                '09:00-09:50',
                '10:00-10:50',
                '11:00-11:50',
                '13:00-13:50',
                '14:00-14:50',
                '15:00-15:50',
                '16:00-16:50']
            return class_times[index]

        # 取得現在時間
        now = datetime.datetime.now()

        # 取得今天星期幾，0 為星期一，6 為星期日
        weekday = now.weekday()

        # 取得現在時間，格式為 'HH:MM'
        current_time = now.strftime('%H:%M')

        next_class = None

        # 查詢接下來的課程
        if weekday in timetable:
            # 取得今天的課表
            today_timetable = timetable[weekday]
            
            for i in range(len(today_timetable)):
                # 取得課程時間，格式為 'HH:MM-HH:MM'
                class_time = get_class_time(i, today_timetable)
                
                # 判斷現在時間是否在課程時間之前
                if current_time < class_time.split('-')[0]:
                    next_class = today_timetable[i]
                    break

        if next_class:
            message = next_class
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = '今天已經沒有課了'
            line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
