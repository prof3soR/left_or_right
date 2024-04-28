from django.db import models


class votes(models.Model):
    Redg_no = models.CharField(max_length=10)
    votes = models.IntegerField()

    def __str__(self):
        return self.Redg_no, self.votes


class feedback(models.Model):
    name = models.CharField(max_length=20, blank=True)
    message = models.TextField()
