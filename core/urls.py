from django.urls import path, include

from core import views


urlpatterns = [
    path('appeal/', views.CreateAppealAPIView.as_view()),
    path('appeal/list/', views.ListAppealsAPIView.as_view()),
    path('appeal/<int:pk/>', views.RetrieveUpdateDeleteAppealAPIVew.as_view()),
]
