from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DESG = (('Public', 'Public'),('Counsilor', 'Counsilor'),('Higher Official', 'Higher Official'))
    designation = models.CharField(max_length=100, choices=DESG)
    name = models.CharField(max_length=255)

class Petition(models.Model):
    petitioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='petitioner')
    petition_for = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='petitionfor')
    subject = models.CharField(max_length=255)
    petition = models.TextField()
    attachments = models.URLField()
    date = models.DateField(auto_now_add=True)
    due = models.DateField()

    def __str__(self):
        return self.subject
    