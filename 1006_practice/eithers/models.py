from django.db import models

# Create your models here.
class Either(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)


class Comment(models.Model):
    either = models.ForeignKey(Either, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    choice = (
        ('BLUE','BLUe'),
        ('RED','RED')
    )