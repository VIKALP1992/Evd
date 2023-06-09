from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.EmployeeViewset import EmployeeViewset

router = routers.DefaultRouter()
router.register(r'emps', EmployeeViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
