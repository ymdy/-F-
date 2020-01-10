import os

from http_client import HttpClient


class TocaroHandler:

    def __init__(self):
        self.message = {
            "text": "string",
            "color": "info",
            "attachments": [
                {
                    "title": "string",
                    "value": "string"
                },
                {
                    "image_url": "string"
                }
            ]
        }

    def set_text(self, text):
        self.message["text"] = text

    def set_color(self, color):
        self.message["color"] = color

    def set_attachments(self, contents):
        self.message["attachments"] = contents

    def set_imageurl(self, imageurlstr):
        self.message["attachments"] = imageurlstr

    def send2tocaro(self):
        tocaro_url = "https://hooks.tocaro.im/integrations/inbound_webhook/hsujhiraoxyyaihnhpszxfeua4jbux53"
        headers = {"Content-type": "application/json"}
        body = HttpClient.post(tocaro_url, self.message, headers)
        return body
