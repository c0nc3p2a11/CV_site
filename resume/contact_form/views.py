from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .form import ContactForm
from django.shortcuts import render


# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   return HttpResponse('Письмо отправлено!')

def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.email()
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form' : form})