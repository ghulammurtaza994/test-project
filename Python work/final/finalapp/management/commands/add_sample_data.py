from django.core.management.base import BaseCommand
from finalapp.models import Instructor, Student, Course

class Command(BaseCommand):
    help = 'Add sample data to the database'

    def handle(self, *args, **options):
        # Create sample instructors
        if not Instructor.objects.exists():
            instructors = [
                Instructor(name='Dr. John Smith', email='john@example.com', department='Computer Science', qualification='PhD'),
                Instructor(name='Dr. Sarah Johnson', email='sarah@example.com', department='Mathematics', qualification='PhD'),
                Instructor(name='Prof. Michael Brown', email='michael@example.com', department='Physics', qualification='MSc'),
            ]
            Instructor.objects.bulk_create(instructors)
            self.stdout.write(self.style.SUCCESS('Sample instructors added'))

        # Create sample courses
        if not Course.objects.exists():
            instructors = list(Instructor.objects.all())
            if instructors:
                courses = [
                    Course(title='Introduction to Programming', description='Basic programming concepts', Instructor=instructors[0]),
                    Course(title='Advanced Mathematics', description='Calculus and Algebra', Instructor=instructors[1]),
                    Course(title='Physics Fundamentals', description='Basic physics principles', Instructor=instructors[2]),
                ]
                Course.objects.bulk_create(courses)
                self.stdout.write(self.style.SUCCESS('Sample courses added'))

        # Create sample students
        if not Student.objects.exists():
            courses = list(Course.objects.all())
            if courses:
                students = [
                    Student(name='Alice Wilson', email='alice@example.com', enrollment_number='2024001', course=courses[0]),
                    Student(name='Bob Davis', email='bob@example.com', enrollment_number='2024002', course=courses[1]),
                    Student(name='Charlie Miller', email='charlie@example.com', enrollment_number='2024003', course=courses[2]),
                    Student(name='Diana Garcia', email='diana@example.com', enrollment_number='2024004', course=courses[0]),
                ]
                Student.objects.bulk_create(students)
                self.stdout.write(self.style.SUCCESS('Sample students added'))

        self.stdout.write(self.style.SUCCESS('Sample data added successfully!'))