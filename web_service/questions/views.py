import requests
from rest_framework import generics
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer


class QuestionsView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        queryset_ids = [x.id_for_response for x in Question.objects.all()]
        response = requests.get('https://jservice.io/api/random?count=1 ')
        print(response.json)
        return Response(response.json())
