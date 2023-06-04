from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.email

