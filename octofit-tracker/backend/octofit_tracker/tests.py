from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.username, 'testuser')


class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team(name='Test Team')
        self.assertEqual(team.name, 'Test Team')


class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout(name='Push-ups', description='Upper body workout', duration=30)
        self.assertEqual(workout.name, 'Push-ups')
