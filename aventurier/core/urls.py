from django.urls import path
from core import views

urlpatterns = [
    path("", views.health, name="health"),
    path("vocab-item", views.VocabItemList.as_view(), name="vocab-item"),
]
