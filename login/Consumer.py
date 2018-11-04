from channels.consumer import AsyncConsumer
class healthConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self,event):
        A=event['text'];
        ap=A.find("appointement")

        await self.send({
            "type":"websocket.send",
            "text":"Varun gandu or lichedh hai"
        })
    async def websocket_disconnect(self,event):
        print("disconnected",event)
