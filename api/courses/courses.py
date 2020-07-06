from rest_framework import generics
from api.courses.courses_serializers import CourseListSerializer
from course.models import Course, UserCourses
from user.models import User
from rest_framework.response import Response


class CourseList(generics.ListCreateAPIView):
    model = Course
    def get_serializer_class(self):
        return CourseListSerializer

    def get_queryset(self):
        q_set = Course.objects.all()
        return q_set

    def post(self, request, *args, **kwargs):
        subject_code = request.data['subjectCode']
        subject_number = request.data['subjectNumber']
        section_number = request.data['sectionNumber']
        phone_number = request.data['users']
        course = Course.objects.filter(subject_code=subject_code, subject_number=subject_number, section_number=section_number)
        user = User.objects.filter(phone_number=phone_number)

        if course and user:
            # if the course already exists in the database
                # Check if record already exists in the user table
            reservation = UserCourses(user=user[0], course=course[0])
            reservation.save()
            return Response({'status': 'Success'})

        elif not user and not course:
            user_data = User(phone_number=phone_number)
            user_data.save()
            course_data = Course(subject_code=subject_code, subject_number=subject_number, section_number=section_number)
            course_data.save()
            course_data.users.set([user_data])

            reservation = UserCourses(user=user_data, course=course_data)
            # reservation.save()
            return Response({'status': 'Success'})

        elif course and not user:
            # if the phone number does not exist in the database yet
            user_data = User(phone_number=phone_number)
            user_data.save()

            reservation = UserCourses(user=user_data, course=course[0])
            # reservation.save()
            return Response({'status': 'Success'})

        elif user and not course:
            # if the course does not exist in the database yet
            course_data = Course(subject_code=subject_code, subject_number=subject_number, section_number=section_number)
            course_data.save()
            course_data.users.set([user[0]])

            reservation = UserCourses(user=user[0], course=course_data)
            # reservation.save()
            return Response({'status': 'Success'})
