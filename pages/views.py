from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("<h1>The Home Page</h1>")
    return render(request, "pages/page.html")
