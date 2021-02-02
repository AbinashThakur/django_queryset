from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('api/', views.test_api, name = 'test_api'),
    path('api2/', views.test_api2, name = 'test_api2')
    #path('', views.QuestionsAPIView.as_view()),
   
]