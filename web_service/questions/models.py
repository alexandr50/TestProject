from django.db import models

class Question(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    answer = models.CharField(max_length=255, verbose_name='ответ')
    question = models.TextField(verbose_name='вопрос')
    created_at = models.DateTimeField(verbose_name='дата создания', null=True)
