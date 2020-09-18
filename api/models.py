from django.db import models


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    m_title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    awards = models.IntegerField()

    def __str__(self):
        return self.m_title