from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return render(request, "index.html")

def qr_redirect(request):
    exteenal_url = 'https://linko.page/spicethecat'
    return redirect(exteenal_url)