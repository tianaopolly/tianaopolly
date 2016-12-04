# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def login(request):
    return render_to_response("login.html", context_instance=RequestContext(request))


def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))
