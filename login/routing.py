# mysite/routing.py
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
#from ChatBox.consumer import  ChatConsumer
from channels.sessions import SessionMiddlewareStack
from ChatBox.consumer import msgConsumer
from login.Consumer import healthConsumer
from ChatBox.consumer2 import callConsumer
application = ProtocolTypeRouter({
    'websocket':SessionMiddlewareStack(
        URLRouter(
                    [
                        path('chat/chat/',msgConsumer),
                        path('chat/call/',callConsumer),
                        path('healthAssistant/',healthConsumer)

                    ]

        )
    )
    # (http->django views is added by default)
})
