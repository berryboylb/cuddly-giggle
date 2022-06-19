from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Grader. You're at the Blog index.")