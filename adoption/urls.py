from django.urls import path
from adoption import views


app_name = 'adoption'
urlpatterns = [
    path('', views.home, name='index'),# r means raw string
    path('detail/<int:id>', views.pet_detail, name='detail'),
]
