from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about", views.AboutView.as_view(), name="about"),
    path("work", views.WorkView.as_view(), name="work"),
    path("research", views.ResearchView.as_view(), name="research"),
    path("projects", views.ProjectsView.as_view(), name="projects"),
]
