import asyncio
import json
import os
from django.conf import settings
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from login2.models import user
from loginDoctor.models import Doctor
from ChatBox.models import msg as msgdb
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
class msgConsumer(AsyncConsumer):
    @database_sync_to_async
    def function123(self,me,rec,msg):
        a=msgdb(suid=me,ruid=rec,msg=msg)
        a.save()
        return a
    async def websocket_connect(self,event):
        print("connected",event)
        sender=self.scope['session']['uid']
        reciver=self.scope['session']['rec']
        chatroom=await self.chatroom_id(sender,reciver)
        #chatroom=await self.chatroom_id("A","B")
        self.chatroom=chatroom
        print(chatroom)
        print(1)
        await self.channel_layer.group_add(
        chatroom,
        self.channel_name
        )
        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self,event):
        print("receive",event)
        b8=event.get('bytes',None)
        print('routing')
        if b8 is not None:
            print(len(b8))
            print('it try to run')
            await self.handle_chunk(b8)

        msg=event.get("text",None)
        if msg is not None:
            sender=self.scope['session']['uid']
            reciver=self.scope['session']['rec']
            loaded_dict_data=json.loads(msg)
            message=loaded_dict_data.get('message')

            msgres={
                'message':message,
                'sender':sender,
                'reciver':reciver
            }
            status=loaded_dict_data.get('status')
            stres={
                'status':status,
                'sender':sender,
                'reciver':reciver
            }
            fileData=loaded_dict_data.get('action')
            if fileData is not None:
                msgimgid=await self.function123(sender,reciver,message)
                self.msgimgid=msgimgid
                await self.handle_json(loaded_dict_data)
                await self.handle_chunk(loaded_dict_data)


            elif msgres['message'] is not None:
                await self.function123(sender,reciver,message)
                await self.channel_layer.group_send(self.chatroom,{
                    "type":"msgSend",
                    "text":json.dumps(msgres)
                    })
            elif stres['status'] is not None:
                await self.channel_layer.group_send(self.chatroom,{
                    "type":"msgSend",
                    "text":json.dumps(stres)
                    })



    async def msgSend(self,event):
        await self.send({
            "type": "websocket.send",
            "text":event['text']

        })

    async def websocket_disconnect(self,event):
        print("disconnected",event)


    @database_sync_to_async
    def chatroom_id(self,me,rec):
        print(3)
        if Doctor.objects.filter(uid=me).count()==1:
            return ("d"+me.replace('@','D')+"p"+rec.replace('@','D'))
        return ("d"+rec.replace('@','D')+"p"+me.replace('@','D'))



    async def handle_json(self, message):
        #sf=open('','wb')
        f=open('uploads','wb')
        self.session = {
            'upload_size':message['file_size'],
            'temp_destination':'./',
            'upload_file':f,
            'bcount':0
         #Set up file object and attributes
        }



    async def handle_chunk(self, message, **kwargs):
        upload_size = self.session.get('upload_size')
        temp_destination = self.session.get('upload_file')
        if not upload_size or not temp_destination:
            return self.error('Invalid request. Please try again.')

        if type(message)!=type({'a':'django'}):
            self.session['upload_file'].write(message)
            self.session['bcount']+=4096
        size = self.session['bcount']
        print(size)
        percent = round((size / upload_size) * 100)
        info={
            'action': 'progress',
            'percent': percent,
            'file_size':size,
        }
        if size <upload_size:
            await self.channel_layer.group_send(self.chatroom,{
                "type":"msgSend",
                "text":json.dumps(info)
            })

        if size >= upload_size:
            self.session['upload_file'].flush()
            file_name = await self.handle_complete(self.session['upload_file'])

    async def handle_complete(self,tempFile):
        save_path = os.path.join(settings.MEDIA_ROOT, 'static/uploads')
        save_path=save_path+'/'+str(self.msgimgid.id)+'.png'
        path='./uploads'
        os.rename(path,save_path)
        self.msgimgid.imgmsg=save_path
        self.msgimgid.save()

        msgres={
            'message':self.msgimgid.msg,
            'sender':self.msgimgid.suid,
            'reciver':self.msgimgid.ruid,
            'imgmsg':self.msgimgid.imgmsg[7::]
        }
        await self.channel_layer.group_send(self.chatroom,{
            "type":"msgSend",
            "text":json.dumps(msgres)
            })














#
