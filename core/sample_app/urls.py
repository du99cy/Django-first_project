from sample_app.views import StudentList, StudentDetail
from django.urls import path  
  
urlpatterns = [  
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
]  