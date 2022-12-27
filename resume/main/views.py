from django.shortcuts import render
from django.http import HttpResponse

from contact_form.form import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.email()
    else:
        form = ContactForm()
    return render(request, "index.html", {'form': form})
