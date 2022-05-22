from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerMessage,StickerSendMessage,
)
# from line_file_handler import line_file_system
class LineStickerHandler:
    def __init__(self,msg):
        self.msg = msg

    def handle_sticker_from_text_message(self):
        sticker_message = None
        if '貼圖' in self.msg:
            sticker_message = StickerSendMessage(
                package_id='446',
                sticker_id='2004'
            )
        elif '品妤' in self.msg:
            sticker_message = StickerSendMessage(
                package_id='789',
                sticker_id='10856'
            )
        elif '冠儒' in self.msg:
            sticker_message = StickerSendMessage(
                package_id='6632',
                sticker_id='11825377'
            )
        elif '麗君' in self.msg:
            sticker_message = StickerSendMessage(
                package_id='6632',
                sticker_id='11825376'
            ) 
        elif '書弘' in self.msg:
            sticker_message = StickerSendMessage(
                package_id='6632',
                sticker_id='11825384'
            )   
        return sticker_message

    def handle_str_form_text_message(self):
        reply_msg = None
        if self.msg == '1':
            reply_msg = '冠儒是笨蛋!!!'
        elif self.msg == '2':
            reply_msg = '書弘是大帥哥!!!'
        elif self.msg == '3':
            reply_msg = '品妤是大美女!!!'
        elif self.msg in ['幹','白痴','屁','媽的']:
            reply_msg = '有教養一點!不要罵髒話'
        elif self.msg in ['愛']：
            reply_msg = '我也愛你'
        else:
            reply_msg = '我看不懂你在打什麼，你是笨蛋嗎!!!'
        return reply_msg

