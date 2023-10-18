import requests

from questions.models import Question


def save_to_bd(url: str, count_questions: int):
    """Функция сохранения данных викторины в бд"""

    while count_questions > 0:
        response = requests.get(
            url,
            params={'count': count_questions}
        )
        if response.status_code == 200:
            id_for_response = response.json()[0]['id']
            if Question.objects.filter(id_for_response=id_for_response).exists():
                continue
            answer = response.json()[0]['answer']
            question = response.json()[0]['question']
            created_at = response.json()[0]['created_at']
            Question.objects.create(
                id_for_response=id_for_response,
                answer=answer,
                question=question,
                created_at=created_at
            )
            count_questions -= 1
