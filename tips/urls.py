from django.urls import path
from .views import HomePageView, TipDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("<int:pk>/tips/", TipDetailView.as_view(), name="tips"),
]
