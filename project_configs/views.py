from django.shortcuts import render

def error_400(request, exception=None):
    return render(request, "400.html")

def error_404(request, exception=None):
    return render(request, "404.html")

def error_500(request, exception=None):
    return render(request, "500.html")