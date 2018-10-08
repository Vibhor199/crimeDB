from django.shortcuts import render, HttpResponse

# Create your views here.
def front(request):
    return render(request, 'front/index.html')
