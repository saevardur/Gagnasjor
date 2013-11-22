#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

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


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
