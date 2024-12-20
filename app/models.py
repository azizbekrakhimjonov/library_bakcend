from django.db import models


# models.py
class Yonalish(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Malumot(models.Model):
    yonalish = models.ForeignKey(Yonalish, related_name='malumotlar', on_delete=models.CASCADE)
    nomi = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    date = models.DateField()

    def __str__(self):
        return self.nomi
