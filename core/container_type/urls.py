from django.urls import path  

from container_type import views
  
urlpatterns = [  
    path('', views.ContainerTypeList.as_view()),
    path('list/', views.ContainerTypeCreation.as_view()),
    path('<int:pk>/update/', views.ContainerTypeUpdate.as_view()),
    path('<int:pk>/', views.ContainerTypeDetailOrDelete.as_view()),
    path('<int:pk>/soft-delete', views.ContainerTypeSoftDelete.as_view()),
    path('bulk-soft-delete/', views.ContainerTypeBulkSoftDelete.as_view()),

]
