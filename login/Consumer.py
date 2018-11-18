from channels.consumer import AsyncConsumer
from login2.models import user
from chatbot.models import Symtoms
import json
from loginDoctor.models import Doctor
class fg(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connect",event)

        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_recive(self,event):
        print(event)
        await self.send({
            "type":"websocket.send",
            "text":"got something"
        })

class loginConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connect",event)

        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self,event):
        print(event)
        loaded_dict_data=json.loads(event['text'])
        uid=loaded_dict_data.get('uid')
        paswd=loaded_dict_data.get('pwd')
        if user.objects.filter(uid=uid).count()==1:
            a=user.objects.get(uid=uid)
            if a.password==paswd:
                myres={
                    'uid':uid,
                    'action':'DocaLogin',
                    'fname':a.fname+" "+a.lname,
                }
                await self.send({
                    "type":"websocket.send",
                    "text":json.dumps(myres)
                })
        elif Doctor.objects.filter(uid=uid).count()==1:
            a=Doctor.objects.get(uid=uid)
            if a.password==paswd:
                myres={
                    'uid':uid,
                    'action':'DocaLogin',
                    'fname':a.fname+" "+a.lname,
                }
                await self.send({
                    "type":"websocket.send",
                    "text":json.dumps(myres)
                })
        else:
            print("fail")

    async def websocket_disconnect(self,event):
        print("disconnected",event)


