from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/<str:applicant_id>/", views.edit_user, name="edit"),
    path("del_user/<str:applicant_id>/", views.del_user, name="delete"),
]