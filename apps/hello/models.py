from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    bio = models.TextField()
    skype = models.CharField(max_length=50)
    email = models.EmailField()
    jabber = models.EmailField()
    other = models.TextField()

    def __unicode__(self):
        return self.name + ' ' + self.surname
