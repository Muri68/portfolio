from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [
    path('', views.HomeView, name="home"),
    path('<slug:slug>/', views.ProjectDetailedView, name="single-project"),
    path('category/<slug:slug>/', views.CategoryView, name="project-category"),
]