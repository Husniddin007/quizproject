# from django.test import TestCase
# from django.urls import reverse
#
# from .models import QuizType, Question
# from quizapp.api.v1.serializers import QuestionSerializer
# from quizapp.api.v1.views import hello_world
#
# class QuizTypeTestCase(TestCase):
#     def setUp(self):
#         self.quiz_type = QuizType.objects.create(name='test_quiz_type', image='test_image')
#
#     def test_data(self):
#         serializer = QuestionSerializer(self.quiz_type).data
#         assert serializer['id'] == self.quiz_type.id
#
# class Test_hello_world(TestCase):
#     def setUp(self) -> None:
#         self.url = reverse('hello_world')
#
#     def test_gets(self):
#         response = self.client.get(self.url)
#         assert response.status_code == 200
#         assert response.json()['message'] == 'hello_world'
# class Test_Create_Question(TestCase):
#
#     def setUp(self) -> None:
#         self.quiz_type1 = QuizType.objects.create(name='Tsat1')
#         self.quiz_type2 = QuizType.objects.create(name='Tsat1')
#
#     def test_get(self):
#         quiz_types = QuizType.objects.all()
#         serializer = QuestionSerializer(quiz_types, many=True).data
#
#         assert serializer.data == quiz_types.all()
#
#
#
#
