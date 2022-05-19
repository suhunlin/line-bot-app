from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerMessage,StickerSendMessage,
)
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