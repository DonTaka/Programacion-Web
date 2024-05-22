from django.shortcuts import render


# Create your views here.
def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {
        "usuario": "Jose Riquelme",
    }
    return render(request, "pages/index.html", context)


def page2(request):
    context = {}
    return render(request, "pages/page2.html", context)
