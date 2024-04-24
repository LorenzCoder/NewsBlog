from django.db import models

# Create your models here.
class Meldung(models.Model):
    titel = models.CharField(max_length=100)
    zeitstempel = models.DateTimeField()
    text = models.TextField('Meldungstext')
    class Admin:
        pass
    def __unicode__(self):
        return self.titel

class Kommentar(models.Model):
    meldung = models.ForeignKey(Meldung, on_delete=models.CASCADE)
    autor = models.CharField(max_length=70)
    text = models.TextField('Kommentartext')
    def __unicode__(self):
        return self.titel

class Home(models.Model):
    pass