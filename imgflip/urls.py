from django.urls import path
from imgflip.views import home_view, populate_db, memes_view

urlpatterns = [
    path("", home_view, name="home"),
    path("update-db/", populate_db, name="update_db"),
    path("memes/<int:pk>/", memes_view, name="memes"),
]
