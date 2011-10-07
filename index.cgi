#!/usr/bin/python 
from wsgiref.handlers import CGIHandler
from proxy import app

CGIHandler().run(app)