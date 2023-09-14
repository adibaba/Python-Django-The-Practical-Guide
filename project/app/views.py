from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponse('hello world')


def echo(request, string):
    if string == 'hello':
        return HttpResponseRedirect(reverse('echo', args=['world']))
    else:
        return HttpResponse(f'<b>{string}</b>')
