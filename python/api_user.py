from flask import request, session
from flask_restful import Resource
from Utils import ProtocolItem
import json
from Logic import logic
from DB import orm

from appfile import api
from appfile import auth

@auth.verify_password
def verify_password(username, password):
    """
    Authorize the session.
    
    If the session has been authorized before, return True.
    If it declare human in body, check username and password in database.
    If it declare gateway in body, use it's username as gateway_id.
    otherwise, return False.
    
    """
   
    print "verify_password called", username,password
    
    if session.has_key('login_body'):
        return True
    print request.data
    body = json.loads(request.data)
    if not body or not body.has_key(ProtocolItem.CLIENTTYPE):
        return False
    if body[ProtocolItem.CLIENTTYPE]==ProtocolItem.VALUE_GATEWAY:
        gateway = logic.GetGatewayById(username)
        if gateway is None:
            return False
        session[ProtocolItem.SESSION_GATEWAY] = gateway
        session[ProtocolItem.LOGIN_BODY] = body
        return True
    elif body[ProtocolItem.CLIENTTYPE]==ProtocolItem.VALUE_HUMAN:
        print "lsdjkfsldfjsdfl"
        user = orm.Account.query.filter_by(username = username).first()
        if not user or not user.verify_password(password):
            return False
        session[ProtocolItem.SESSION_ACCOUNT] = user
        session[ProtocolItem.LOGIN_BODY] = body
        return True

    return False


class Login(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        if session[ProtocolItem.LOGIN_BODY][ProtocolItem.CLIENTTYPE]==ProtocolItem.VALUE_HUMAN:
            return {ProtocolItem.ID: session[ProtocolItem.SESSION_ACCOUNT].id}
        else:
            return {}


class Logout(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        session.clear()
        return {}


class Keepalive(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        return {}


class Regist(Resource):
    def post(self):
        account = logic.Regist(json.loads(request.data))
        return {ProtocolItem.ID:account.id} if account else {}


api.add_resource(Keepalive, '/api/v1.0/keepalive')
api.add_resource(Logout, '/api/v1.0/logout')
api.add_resource(Login, '/api/v1.0/login')
api.add_resource(Regist, '/api/v1.0/regist')
