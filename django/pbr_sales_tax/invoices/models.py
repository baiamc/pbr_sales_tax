from django.db import models

# Create your models here.
class Invoice(models.Model):
    """Invoice model class"""

    def __unicode__(self):
        return self.number

    number = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax = models.DecimalField(max_digits=12, decimal_places=2)
    custno = models.IntegerField()
    report = models.ForeignKey('Report', null=True)


class Report(models.Model):
    """Report model class"""

    def __unicode__(self):
        return self.number

    number = models.IntegerField(primary_key=True)
    month = models.IntegerField()
    year = models.IntegerField()
