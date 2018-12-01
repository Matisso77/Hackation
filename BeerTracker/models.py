from django.db import models


class Beers(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, default="Piwko")
    Alcohol = models.FloatField()
    flavour = models.FloatField()


class Bar(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200, default="Bar")
    Link = models.CharField(max_length=600, default="Brak")
    Localization = models.CharField(max_length=50)


class Stock(models.Model):
    Beer = models.ForeignKey(Beers, on_delete=models.CASCADE, related_name="Piwo")
    Bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name="Bar")
    bigCost = models.FloatField(null=False)
    smallCost = models.FloatField(null=True)
