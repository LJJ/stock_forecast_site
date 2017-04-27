# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class History(models.Model):
    symbol = models.ForeignKey('StockInfo', models.DO_NOTHING, to_field="name", db_column='symbol', primary_key=True)
    time = models.DateField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    open = models.FloatField()

    class Meta:
        managed = False
        db_table = 'history'
        unique_together = (('symbol', 'time'),)


class Realtime(models.Model):
    symbol = models.ForeignKey('StockInfo', models.DO_NOTHING, to_field="name", db_column='symbol', primary_key=True)
    time = models.DateTimeField()
    price = models.FloatField()
    volume = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'realtime'
        unique_together = (('symbol', 'time'),)


class StockInfo(models.Model):
    stock_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'stock_info'