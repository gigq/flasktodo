#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from application import app

CGIHandler().run(app)
