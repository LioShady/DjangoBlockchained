from django.urls import path
from django.views.generic import TemplateView

from services.views import ServiceCreateView, ServiceDeleteView
from .views import (
    StudentProfileView,
    StudentProfileUpdateView,
    StudentInterestsView,
    TeacherProfileView,
    TeacherProfileUpdateView,
    TeacherInterestsView,
)

urlpatterns = (
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "student/interests/", StudentInterestsView.as_view(), name="student_interests"
    ),
    path(
        "teacher/interests/", TeacherInterestsView.as_view(), name="teacher_interests"
    ),
    path(
        "student/profile/<int:pk>/",
        StudentProfileView.as_view(),
        name="student_profile",
    ),
    path(
        "student/profile/<int:pk>/edit/",
        StudentProfileUpdateView.as_view(),
        name="student_profile_edit",
    ),
    path(
        "teacher/profile/<int:pk>/",
        TeacherProfileView.as_view(),
        name="teacher_profile",
    ),
    path(
        "teacher/profile/<int:pk>/edit",
        TeacherProfileUpdateView.as_view(),
        name="teacher_profile_edit",
    ),
    path("teacher/services/", ServiceCreateView.as_view(), name="teacher_services"),
    path(
        "teacher/services/<int:pk>/delete/",
        ServiceDeleteView.as_view(),
        name="delete_service",
    ),
)
