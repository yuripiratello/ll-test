from django.urls import path, include
from rest_framework import routers
from employees import views

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet, base_name='employee')

urlpatterns = [
    path('', include(router.urls))
]
