from django.urls import include, path

from . import views


app_name = "app"
urlpatterns = [
    # path("books/", views.IndexView.as_view(), name="index"),
    path("books/", views.index, name="index"),
    path("books/", views.index, name="login"),
    path("books/<int:book_id>/", views.book_view, name="book"),
    path("books/<int:book_id>/review", views.get_review, name="review"),
    path("books/add_book", views.get_book, name="add_book"),

]
