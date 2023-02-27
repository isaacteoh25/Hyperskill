from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Vacancy(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, related_name="author_vacancy", on_delete=models.CASCADE)
    # class Meta:
    #     db_table = 'vacancy_vacancy'