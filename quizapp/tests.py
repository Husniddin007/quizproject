from django.test import TestCase

from .models import QuizType, Question
from quizapp.api.v1.serializers import QuestionSerializer

class QuizTypeTestCase(TestCase):
    def setUp(self):
        self.quiz_type = QuizType.objects.create(name='test_quiz_type', image='test_image')

    def test_data(self):
        serializer = QuestionSerializer(self.quiz_type).data
        print(serializer)


