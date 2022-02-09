from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index), #blogの中のindex
    path('<slug:pk>/', views.article), #PK=プライマリーキー
]