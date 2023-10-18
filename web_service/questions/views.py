from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .services import save_to_bd


class QuestionsView(APIView):
    """Метод для ввода количества вопросов и возврата пердпоследнего"""

    def post(self, request, *args, **kwargs):
        try:
            print(request.data)
            print(type(request.data))
            count_questions = request.data
        except:
            raise ValueError('Введите целое число')

        save_to_bd('https://jservice.io/api/random', count_questions)
        last_obj = None
        try:
            last_obj = Question.objects.order_by('-id')[1]
        except:
            pass

        return Response(last_obj.question) if last_obj else Response(None)
