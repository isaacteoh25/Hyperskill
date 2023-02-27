from django.contrib.auth.models import User
from django.db import models
# from django.contrib.auth.models.User
# Create your models here.
class Resume(models.Model):
    # title = models.CharField(max_length = 200)
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, related_name="author_resume", on_delete=models.CASCADE)
    class Meta:
        db_table = 'resume_resume'