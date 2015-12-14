import sys, os
#reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

from DB import orm
from Utils import ProtocolItem
from Utils import Util

def GetGatewayById(gateway_id):
    """
    Get the Gateway object from database
    
    If there isn't this gateway in database, create it in database automatically.    
    """

    gateway = orm.Gateway(gateway_id)
    orm.db.session.merge(gateway)
    orm.db.session.commit()
    return gateway


def BindGateway(account_id, gateway_id):
    """
    
    """
    pass


def Regist(request_body):
    """
    Add a new record into data table 'account'. 

    If the username has been exist, raise exception
    Otherwize, return the inserted account.
    """
    account = orm.Account(ProtocolItem.VALUE_LANGUAGE_DEFAULT, request_body[ProtocolItem.USERNAME], Util.hash_password(request_body[ProtocolItem.PASSWORD]), request_body[ProtocolItem.EMAIL], request_body[ProtocolItem.MOBILE])
    orm.db.session.add(account)
    orm.db.session.commit()
    return account
