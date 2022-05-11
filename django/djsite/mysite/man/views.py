from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse('<h1> youre welcome </h1>')

def main(request):
    return HttpResponse('main page of this site')

def questions(request, question):
    print(request.GET)
    return HttpResponse(f'<h1>The Question:</h1><p>{question}</p>')

def archive(request, yearHere):
    if int(yearHere) > 2030:
        raise Http404()
    if int(yearHere) < 1960:
        return redirect('man', permanent=True)        
    return HttpResponse(f'<h1>The Archive:</h1><p>{yearHere}</p>')
    

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не неадена. <a href="http://127.0.0.1:8000/man">Перейти на главную страницу</a> </h1>')