
from flask import request
from flask_restful import Resource
from Utils import ProtocolItem
import json
from DB import mongo


from appfile import api
from appfile import auth


class Gateway(Resource):
    method_decorators = [auth.login_required]
    def post(self):
        print "POST a Gateway:", request.data,"--"
        body = json.loads(request.data)
        _id = mongo.UpsertGateway(body[ProtocolItem.ADDGATEWAY][ProtocolItem.GATEWAY])
        resp = {'_id':str(_id)}
        return resp
    
    def delete(self, id):
        print "DELETE a Gateway<id:%d>:%s--" % (id,request.data)
        body = json.loads(request.data)
        return {'deleted_count':mongo.DeleteGateway(body[ProtocolItem.DELETEGATEWAY][ProtocolItem.GATEWAY])}

    def put(self, id):
        print "PUT a Gateway<id:%d>:%s--" % (id,request.data)
        body = json.loads(request.data)
        _id = mongo.UpsertGateway(body[ProtocolItem.UPDATEGATEWAY][ProtocolItem.GATEWAY])
        resp = {'_id':str(_id)}
        return resp

    def get(self, id):
        print "GET a Gateway<id:%s>:%s--" % (id,request.data)
        ret = mongo.GetGateway(id)
        print ret
        return ret

api.add_resource(Gateway, '/api/gateway','/api/gateway/<string:id>')

