from django.core.mail import send_mail
from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Write here your message'
                }
            )
        }

    def email(self):
        name = self.data['name']
        email = self.data['email']
        sbj = self.data['subject']
        subject = f'Сообщение от {name} email: {email} subject: {sbj}'
        send_mail(subject,
                  self.data['message'],
                  'okiselev@okiselev.com',
                  ['zxpro8@gmail.com']
                  )

       

