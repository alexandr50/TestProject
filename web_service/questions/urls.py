from django.urls import path

from .apps import QuestionConfig
from .views import QuestionsView

app_name = QuestionConfig.name

urlpatterns = [

    path('', QuestionsView.as_view(), name='questions')
]
