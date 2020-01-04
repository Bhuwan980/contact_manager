from django.urls import path
from . import views
urlpatterns = [
path('',views.HomeListView.as_view(),name='index'),
path('detail/<int:pk>/',views.DetailDetailView.as_view(),name='detail'),
]