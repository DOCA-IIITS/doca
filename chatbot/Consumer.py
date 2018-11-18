from channels.consumer import AsyncConsumer
import json
from login2.models import  user
from login2.models import userF
from loginDoctor.models import Doctor
from login2.views import send_otp
from loginDoctor.models import DoctorF
from chatbot.models import Symtoms
import random
class login(AsyncConsumer):
    async def websocket_connect(self,event):
        await  self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self,e):
        print(e)
        #`now we will load data in dict
        rdict=json.loads(e['text'])
        uid=rdict.get("uid")
        pwd=rdict.get("pwd")
        if user.objects.filter(uid=uid).count()==1:
            us=user.objects.get(uid=uid)
            if pwd==us.password:
                res={
                    "resp":"verfied"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })
            else:
                res={
                    "resp":"not verified",
                    "reason":"password not match"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })
        elif Doctor.objects.filter(uid=uid).count() == 1:
            us = Doctor.objects.get(uid=uid)
            if pwd == us.password:
                res = {
                    "resp": "verfied"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })
            else:
                res = {
                    "resp": "not verified",
                    "reason": "password not match"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })
        else:
                res = {
                    "resp": "not verified",
                    "reason": "User is not found"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })


    async def websocket_close(self,e):
        print(e)

class forgot(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_receive(self,e):
        rdata=json.loads(e['text'])
        print(rdata)
        uid=rdata.get("uid")

        if user.objects.filter(uid=uid).count()==1:
            fprocess=rdata.get("pid")
            if fprocess==0:
                otp=random.randint(100000,999999)
                send_otp(uid,otp)
                a=userF(uid=uid,otp=otp)
                a.save()
                res={
                    "pid":1,
                    "message":'otp send to your email id '+uid
                }
                print(res)
                await self.send({
                    "type":"websocket.send",
                    "text":json.dumps(res)
                })
                print("done")
            elif fprocess==1:
                uotp=rdata.get("otp")
                if userF.objects.filter(uid=uid).count()==1:
                    udata=userF.objects.get(uid=uid)
                    print(udata.otp)
                    if str(udata.otp)==uotp:
                        res={
                            "pid":2,
                            "message":"otp matched"
                        }
                        await self.send({
                            "type":"websocket.send",
                            "text":json.dumps(res)
                        })
                    else:
                        res = {
                            "pid": 1,
                            "message": "otp not matched"
                        }
                        await self.send({
                            "type": "websocket.send",
                            "text": json.dumps(res)
                        })
            elif fprocess==2:
                upwd=rdata.get("pwd")
                us=user.objects.get(uid=uid)
                us.password=upwd
                us.save()
                res={
                    "pid":3,
                    "message":"password changed Succesfully"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })
        elif Doctor.objects.filter(uid=uid).count() == 1:
            fprocess = rdata.get("pid")
            if fprocess == 0:
                otp = random.randint(100000, 999999)
                send_otp(uid, otp)
                a = userF(uid=uid, otp=otp)

                a.save()
                res = {
                    "pid": 1,
                    "message": 'otp send to your email id' + uid[::7] + "********"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })
            elif fprocess == 1:
                uotp = rdata.get("otp")
                if DoctorF.objects.filter(uid=uid).count() == 1:
                    udata = DoctorF.objects.get(uid=uid)
                    if udata.otp == uotp:
                        res = {
                            "pid": 2,
                            "message": "otp matched"
                        }
                        await self.send({
                            "type": "websocket.send",
                            "text": json.dumps(res)
                        })
                    else:
                        res = {
                            "pid": 1,
                            "message": "otp not matched"
                        }
                        await self.send({
                            "type": "websocket.send",
                            "text": json.dumps(res)
                        })
            elif fprocess == 2:
                upwd = rdata.get("pwd")
                print(upwd)
                us = Doctor.objects.get(uid=uid)
                us.password = upwd
                us.save()
                print("done")
                res = {
                    "pid": 3,
                    "message": "password changed Succesfully"
                }
                await self.send({
                    "type": "websocket.send",
                    "text": json.dumps(res)
                })

        else:
            res={
                "pid":0,
                "message":"user not found"
            }
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(res)
            })

    async def websocket_disconnect(self,ev):
        print(ev)


# it is consumer for the profile of a doctor
class proDoct(AsyncConsumer):
    async def websocket_open(self,ev):
        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_recieve(self,ev):
        print(ev["text"])
        jresd=json.load(ev["text"])
        uid=jresd["uid"]
        pwd=jresd["pwd"]
        did=jresd["did"]
        if user.objects.filter(uid=uid).count()==1:
            udata=user.objects.get(uid=uid)
            if udata.password==pwd:
                if Doctor.objects.filter(uid=did).count()==1:
                    ddata=user.objects.get(uid=did)
                    res={
                        "rid":0,
                        "fname":ddata.fname,
                        "lname":ddata.lname,
                        "spec":ddata.Specilazation,
                        "location":ddata.country+","+ddata.city+" "+ddata.state,
                        "rating":4.5,
                        "fees":249,
                    }
                else:
                    res={
                        "rid":1,
                        "message":"Something wrong went. try again :("
                    }
            else:
                res = {
                    "rid": 1,
                    "message": "Something wrong went. try again :("
                }
        else:
            res = {
                "rid": 1,
                "message": "Something wrong went. try again :("
            }
        await self.send({
            "type":"websocket.send",
            "text":json.dumps(res)
        })

    async def websocket_disconnect(self,ev):
        print(ev)

class Chatbot(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            "type":"websocket.accept"
        })
    asp=0
    async def websocket_receive(self,event):
        ldata = json.loads(event['text'])
        print(event['text'])
        uid=ldata['uid']
        if user.objects.filter(uid=uid).count()==1:
            uObject=user.objects.get(uid=uid)
            print(event['text'])
            A=ldata['input']
            b=Symtoms.objects.all().values_list()
            for c in b:
                tm=A.find(c[1].lower())
                if tm>=0:
                    print(c[1])
                    print("1")
                    break
                tm=A.find(c[2].lower())
                if tm>=0:
                    print(c[2])
                    print(tm)
                    break
            ap=A.find("appointement")
            bk=A.find("book")
            fn=A.find("next")
            hn=A.find("hello")
            dc=A.find("Dhoka")
            if(dc>=0&hn>=0):
                m='hello Mr.'+uObject.fname+" "+uObject.lname+" ,How may I help You ?"

                mres={
                    "gspeak":m,
                    "nopt":2,
                    "opt0":"book appointment",
                    "opt1":"next appointment",

                }
            elif(bk>=0&ap>=0):
                asp=1
                m='sorry curently we are facing some issues'
                mres={
                    "gspeak":m,
                    "nopt":2,
                    "opt0":"report",
                    "opt1":"ignore",

                }

            elif(fn>=0&ap>=0):
                m='you have next appointment tommorrow with Dr.Roshan at 4:00 PM '
                mres={
                    "gspeak":m,
                    "nopt":3,
                    "opt0":"cancel",
                    "opt1":"prepond",
                    "opt2":"postpond",

                }
            elif(tm>=0):
                m="So can i book appointment for you with Dr.Avinash"
                mres={
                "gspeak":m,
                "ds":'yes',
                }
            else:
                m='I don\'t know it'
                mres={
                    "gspeak":m,
                    "nopt":2,
                    "opt0":"book appointment",
                    "opt1":"next appointment",

                }


            print(mres)
            await self.send({
                "type":"websocket.send",
                "text":json.dumps(mres)
            })
    async def websocket_disconnect(self,event):
        print("disconnected",event)


    def nAppoint(self,uid):
        if user.objects.filter(uid=uid).count()==1:
            m={
                "gspeak":"you have next appointement with Dr. Avinash at 4:00 PM",
                "nopt":2,
                "opt1":"cancel",
                "opt2":"View Details"
            }
            return m
        elif Doctor.objects.filter(uid=uid).count()==1:
            m={
                "gspeak": "you have next appointement with Dr. Avinash at 4:00 PM",
                "nopt": 2,
                "opt1": "cancel",
                "opt2": "View Details"
            }
        else:
            return 0



