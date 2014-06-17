from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your models here.
class TestData(models.Model):
    name = models.CharField(max_length=50)
    datafile = models.FileField(upload_to='testdata/')

class History(models.Model):
    user = models.ForeignKey(User)
    dataset = models.ForeignKey(TestData)
    upfile = models.FileField(upload_to='mydata/')
    uptime = models.DateTimeField()
    algo = models.CharField(max_length=50)

class Performance(models.Model):
    history = models.ForeignKey(History)
    char_error = models.DecimalField(max_digits=6,decimal_places=3)
    word_error = models.DecimalField(max_digits=6,decimal_places=3)
    false_detect = models.IntegerField()
    missed_detect = models.IntegerField()
    under_seg = models.IntegerField()
    under_seg_comp = models.IntegerField()
    over_seg = models.IntegerField()
    over_seg_comp = models.IntegerField()
    correct_seg = models.IntegerField()
    total = models.DecimalField(max_digits=6,decimal_places=3)
