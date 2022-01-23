from ..test-project import TestProject
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestTestProject(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(TestProject, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")
