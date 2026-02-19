from django.core.management.base import BaseCommand
from finalapp.models import Instructor


class Command(BaseCommand):
    help = 'Add sample instructors to the database'

    def handle(self, *args, **options):
        instructors = [
            {
                'name': 'Dr. Ali Ahmed',
                'email': 'ali.ahmed@university.com',
                'department': 'Computer Science',
                'qualification': 'PhD in Computer Science'
            },
            {
                'name': 'Prof. Fatima Khan',
                'email': 'fatima.khan@university.com',
                'department': 'Mathematics',
                'qualification': 'MS in Mathematics'
            }
        ]

        for instructor_data in instructors:
            instructor, created = Instructor.objects.get_or_create(
                email=instructor_data['email'],
                defaults={
                    'name': instructor_data['name'],
                    'department': instructor_data['department'],
                    'qualification': instructor_data['qualification']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added instructor: {instructor.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Instructor already exists: {instructor.name}"))
