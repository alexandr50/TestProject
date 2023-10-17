import requests
from rest_framework import generics
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer, CountQuestions
from .services import save_to_bd


class QuestionsView(generics.ListAPIView):
    """Метод для ввода количества вопросов и возврата пердпоследнего"""

    queryset = Question.objects.all()
    serializer_class = CountQuestions

    def post(self, request, *args, **kwargs):
        try:
            count_questions = int(request.POST.get('number'))
        except:
            raise ValueError('Введите целое число')

        save_to_bd('https://jservice.io/api/random', count_questions)
        last_obj = None
        try:
            last_obj = Question.objects.order_by('-id')[1]
        except:
            pass

        return Response(last_obj.question) if last_obj else Response(None)
