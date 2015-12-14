
from flask import request
from flask_restful import Resource
from Utils import ProtocolItem, Util
import json, threading


from appfile import api
from appfile import auth


class HelloWorld(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/a')


class Messages(Resource):
    def post(self):
        pass
        print "POST a Message:", request.data,"--"
        body = json.loads(request.data)
        if body[ProtocolItem.MESSAGES][ProtocolItem.DEST_TYPE] == ProtocolItem.VALUE_IOS:
            threading.Thread(target=Util.push_ios,args=([body[ProtocolItem.MESSAGES][ProtocolItem.DEST_ID]], "alarm", body[ProtocolItem.MESSAGES][ProtocolItem.CONTENT])).start()
#            Util.push_ios([body[ProtocolItem.MESSAGES][ProtocolItem.DEST_ID]], 'alarm', body[ProtocolItem.MESSAGES][ProtocolItem.CONTENT])
        return {'_id':'0'}

    def get(self):
        return {'get':'None'}


api.add_resource(Messages, '/api/messages')
