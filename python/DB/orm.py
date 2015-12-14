# coding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime, os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir))

import appfile
from Utils import Util

db = SQLAlchemy(appfile.app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.ForeignKey(u'language.id'))
    username = db.Column(db.String(255), unique=True)
    passwd = db.Column(db.String(255))
    email = db.Column(db.String(255))
    mobile = db.Column(db.String(30))

    language = db.relationship(u'Language')

    def verify_password(self, password):
        return self.passwd == password or Util.check_password(password, self.passwd)

    def __init__(self, language_id, username, passwd, email, mobile):
        self.language_id = language_id
        self.username = username
        self.passwd = passwd
        self.email = email
        self.mobile = mobile

    def __repr__(self):
        return '<Account %s>' % self.username


class AccountClient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.ForeignKey(u'account.id'))
    os = db.Column(db.String(50))
    code= db.Column(db.String(255))

    account = db.relationship(u'Account', backref= db.backref('accountclients', cascade="all, delete-orphan"))

    def __init__(self, account_id, os, code):
        self.account_id =account_id
        self.os = os
        self.code = code

    def __repr__(self):
        return '<AccountClient %d %s>' % (self.account_id, self.code)


class Gateway(db.Model):
    id = db.Column(db.String(255), primary_key=True)

    def __init__(self, id):
        self.id =id

    def __repr__(self):
        return '<Gateway %s>' % self.id


class AccountGateway(db.Model):
    account_id = db.Column(db.ForeignKey(u'account.id'), primary_key=True)
    gateway_id = db.Column(db.ForeignKey(u'gateway.id'), primary_key=True)

    account = db.relationship(u'Account', backref= db.backref('accountgateways', cascade="all, delete-orphan"))
    gateway = db.relationship(u'Gateway', backref= db.backref('accountgateways', cascade="all, delete-orphan"))

    def __init__(self, account_id, gateway_id):
        self.account_id =account_id
        self.gateway_id = gateway_id

    def __repr__(self):
        return '<AccountGateway %d %s>' % (self.account_id, self.gateway_id)


class Devicetype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Devicetype %s>' % self.name


class Devicemodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    devicetype_id = db.Column(db.ForeignKey(u'devicetype.id'))
    name =db.Column(db.String(50))

    devicetype = db.relationship(u'Devicetype', backref= db.backref('devicemodels', cascade="all, delete-orphan"))

    def __init__(self, devicetype_id, name):
        self.devicetype_id = devicetype_id
        self.name = name

    def __repr__(self):
        return '<Devicemodel %s>' % self.name


class Devicekey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    devicemodel_id = db.Column(db.ForeignKey(u'devicemodel.id'))
    name =db.Column(db.String(50))

    devicemodel = db.relationship(u'Devicemodel', backref= db.backref('devicekeys', cascade="all, delete-orphan"))

    def __init__(self, devicemodel_id, name):
        self.devicemodel_id = devicemodel_id
        self.name = name

    def __repr__(self):
        return '<Devicekey %s>' % self.name


class Devicestate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    devicekey_id = db.Column(db.ForeignKey(u'devicekey.id'))
    name =db.Column(db.String(50))

    devicekey = db.relationship(u'Devicekey', backref= db.backref('devicestates', cascade="all, delete-orphan"))

    def __init__(self, devicekey_id, name):
        self.devicekey_id = devicekey_id
        self.name = name

    def __repr__(self):
        return '<Devicestate %s>' % self.name


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, id, language):
        self.id = id
        self.language = language
        self.name = name
        self.telephone = telephone
        self.role = role

    def __repr__(self):
        return '<Account %s>' % self.username

