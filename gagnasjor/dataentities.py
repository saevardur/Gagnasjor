

from google.appengine.ext import ndb

class Company(ndb.M):
  """docstring for Company"""
  name = ndb.StringProperty()
  ssn = ndb.StringProperty()


class Ship(ndb.Model):
  """docstring for Ship"""
  name = ndb.StringProperty()
  registrationnumber = ndb.StringProperty()
  owner = ndb.StringProperty()

class Tour(ndb.Model):
  """docstring for Tour"""
  tourid = ndb.IntegerProperty()
  ship = ndb.IntegerProperty()
  datestarted = ndb.DateTimeProperty(auto_now_add=True)
  dateended = ndb.DateTimeProperty()

class Haul(ndb.Model):
  """docstring for Haul"""
   haulid = ndb.IntegerProperty()
   ship = ndb.IntegerProperty()
   date = ndb.DateTimeProperty(auto_now_add=True)
   timeStarted = ndb.DateTimeProperty()
   timeEnded = ndb.DateTimeProperty()
   gear = ndb.IntegerProperty()
   weight = ndb.FloatProperty()