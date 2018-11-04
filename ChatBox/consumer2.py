from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from login2.models import user
from loginDoctor.models import Doctor
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
import json
class callConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        sender=self.scope['session']['uid']
        reciver=self.scope['session']['rec']
        chatroom=await self.chatroom_id(sender,reciver)
        await self.channel_layer.group_add(
            chatroom,
            self.channel_name,
        )
        self.chatroom=await self.chatroom_id(reciver,sender)

        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_receive(self,event):
        print(self.chatroom)
        print(len(event))
        b8=event.get('bytes',None)
        if b8 is not None:
            #print(b8)#
            try:
                await self.channel_layer.group_send(self.chatroom,{
                    "type":"chunkSend",
                    "bytes":b8
                    })

            except asyncio.TimeoutError:
                await self.send({
                    "type":"websocket.accept"
                })

        actn=event.get('text',None)
        if actn is not None:
            sender=self.scope['session']['uid']
            reciver=self.scope['session']['rec']
            loaded_dict_data=json.loads(actn)
            actn2=loaded_dict_data.get('action')
            if actn2=='call':
                myres={
                    'cali':sender,
                    'action':'incoming'
                }
                try:
                    await self.channel_layer.group_send(self.chatroom,{
                        "type":"respSend",
                        "text":json.dumps(myres)
                        })
                except asyncio.TimeoutError:
                    await self.send({
                        "type":"websocket.accept"
                    })
            elif actn2=='accept':
                myres={
                    'cali':sender,
                    'action':'outgoing'
                }
                try:
                    await self.channel_layer.group_send(self.chatroom,{
                        "type":"respSend",
                        "text":json.dumps(myres)
                        })
                except asyncio.TimeoutError:
                    await self.send({
                        "type":"websocket.accept"
                    })
            elif actn2=='dicline':
                myres={
                    'cali':sender,
                    'action':'dicline'

                }


    async def respSend(self,event):
        await self.send({
            "type":"websocket.send",
            "text":event["text"],
        })
    async def chunkSend(self,event):
        await self.send({
            "type": "websocket.send",
            "bytes":event['bytes'],

        })
    async def websocket_disconnect(self,event):
        print("disconnected",event)

    @database_sync_to_async
    def chatroom_id(self,me,rec):
        if Doctor.objects.filter(uid=me).count()==1:
            return ("p"+rec.replace('@','D'))
        return ("p"+rec.replace('@','D'))
