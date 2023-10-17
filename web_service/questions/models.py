from django.db import models


class Question(models.Model):
    id_for_response = models.BigIntegerField(verbose_name='id с сайта')
    # id = models.PositiveIntegerField(primary_key=True, unique=True)
    answer = models.CharField(max_length=255, verbose_name='ответ')
    question = models.TextField(verbose_name='вопрос')
    created_at = models.DateTimeField(verbose_name='дата создания', null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
