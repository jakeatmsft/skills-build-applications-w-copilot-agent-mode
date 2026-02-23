"""
Management command to populate the octofit_db database with test data.
Populate the octofit_db database with test data for users, teams, activities, leaderboard, and workouts.
"""

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Cleared existing data.')

        # Create users
        users_data = [
            {'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'password123'},
            {'username': 'metalman', 'email': 'metalman@mhigh.edu', 'password': 'password123'},
            {'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'password123'},
            {'username': 'acidburn', 'email': 'acidburn@mhigh.edu', 'password': 'password123'},
            {'username': 'phantom', 'email': 'phantom@mhigh.edu', 'password': 'password123'},
        ]

        users = []
        for user_data in users_data:
            user = User(**user_data)
            user.save()
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')

        # Create teams
        team1 = Team(name='Octofit Warriors')
        team1.save()
        team1.members.add(users[0], users[1], users[2])
        self.stdout.write(f'Created team: {team1.name}')

        team2 = Team(name='Code Runners')
        team2.save()
        team2.members.add(users[3], users[4])
        self.stdout.write(f'Created team: {team2.name}')

        # Create activities
        activities_data = [
            {'user': users[0], 'activity_type': 'Running', 'duration': 30, 'date': date(2024, 1, 15)},
            {'user': users[1], 'activity_type': 'Cycling', 'duration': 45, 'date': date(2024, 1, 16)},
            {'user': users[2], 'activity_type': 'Swimming', 'duration': 60, 'date': date(2024, 1, 17)},
            {'user': users[3], 'activity_type': 'Yoga', 'duration': 40, 'date': date(2024, 1, 18)},
            {'user': users[4], 'activity_type': 'Weight Training', 'duration': 50, 'date': date(2024, 1, 19)},
        ]

        for activity_data in activities_data:
            activity = Activity(**activity_data)
            activity.save()
            self.stdout.write(f'Created activity: {activity.activity_type} for {activity.user.username}')

        # Create leaderboard entries
        leaderboard_data = [
            {'user': users[0], 'score': 150},
            {'user': users[1], 'score': 120},
            {'user': users[2], 'score': 180},
            {'user': users[3], 'score': 90},
            {'user': users[4], 'score': 200},
        ]

        for entry_data in leaderboard_data:
            entry = Leaderboard(**entry_data)
            entry.save()
            self.stdout.write(f'Created leaderboard entry for: {entry.user.username} with score {entry.score}')

        # Create workouts
        workouts_data = [
            {'name': 'Morning Run', 'description': 'A refreshing 5km morning run', 'duration': 30},
            {'name': 'HIIT Cardio', 'description': 'High intensity interval training', 'duration': 20},
            {'name': 'Upper Body Strength', 'description': 'Push-ups, pull-ups, and dips', 'duration': 45},
            {'name': 'Core Workout', 'description': 'Planks, crunches, and leg raises', 'duration': 25},
            {'name': 'Flexibility & Yoga', 'description': 'Full body stretching and yoga poses', 'duration': 40},
        ]

        for workout_data in workouts_data:
            workout = Workout(**workout_data)
            workout.save()
            self.stdout.write(f'Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data.'))
