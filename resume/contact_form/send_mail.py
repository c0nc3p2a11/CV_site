from django.core.mail import send_mail
from django.conf import settings

send_mail('Тема сообщения',
   'Содержание',
   'okiselev@okiselev.com',
   ['zxpro8@gmail.com']
)

## it works!