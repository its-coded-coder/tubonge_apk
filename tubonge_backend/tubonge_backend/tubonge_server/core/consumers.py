
import json
from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        if action == 'offer' or action == 'answer':
            self.send(text_data=json.dumps({
                'action': action,
                'sdp': text_data_json['sdp']
            }))
        elif action == 'candidate':
            self.send(text_data=json.dumps({
                'action': action,
                'candidate': text_data_json['candidate']
            }))
        else:
            self.send(text_data=json.dumps({
                'message': 'Unknown action'
            }))
