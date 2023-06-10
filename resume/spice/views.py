from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return render(request, "index.html")

def qr_redirect(request):
    external_url = 'https://linko.page/spicethecat'
    return redirect(external_url)
