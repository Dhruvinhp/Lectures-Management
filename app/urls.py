from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('students', views.StudentViewset, basename='students')
router.register('teachers', views.TeacherViewset, basename='teachers')
router.register('lectures', views.LectureViewset, basename='lecture')

urlpatterns=[
    path('', include(router.urls)),
    path('/<int:pk>/', include(router.urls)),
    
]

