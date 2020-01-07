from django.urls import path
from . import views
urlpatterns = [
path('',views.HomeListView.as_view(),name='index'),
path('detail/<int:pk>/',views.DetailDetailView.as_view(),name='detail'),
path('search/',views.search,name='search'),
path('contact/create/',views.ContactCreateView.as_view(),name='create'),
path('contact/update/<int:pk>/',views.ContactUpdateView.as_view(),name='update'),
path('contact/delete/<int:pk>/',views.ContactDeleteView.as_view(),name='delete'),
path('login/',views.login_user,name='login'),
path('logout/',views.logout_user,name='logout'),
path('register/',views.register_user,name='register'),
]
