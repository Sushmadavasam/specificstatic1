from django.shortcuts import render

# Create your views here.
def specificstatic(request):
    return render(request,'specificstatic.html')