from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def render_html(request):
    return render(request, 'index.html')