from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import os

# Create your views here.
def test_cmd(request):
    os.popen('/usr/bin/gnome-terminal')
    return render_to_response("test.html", {},
                              context_instance=RequestContext(request))

def add(request):
    return render_to_response("add.html", {},
                              context_instance=RequestContext(request))

def all(request):
    return render_to_response("all.html", {},
                              context_instance=RequestContext(request))


