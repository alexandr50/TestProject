from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'answer', 'question', 'created_at')


class CountQuestions(serializers.Serializer):
    number = serializers.IntegerField(help_text='введите количество вопросов')
