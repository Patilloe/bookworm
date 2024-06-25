from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user
from .models import Book, Review
from django.contrib.auth.models import User

def createBook(title, author, summary, pub_year):
    return Book.objects.create(title=title, author=author, summary=summary, pub_year=pub_year)
    
def createReview(review_text, score, book):
    return Review.objects.create(review_text=review_text, score=score, book=book)

class BookIndexViewTests(TestCase):

    def test_redirected_if_not_logged_in(self):
        """
        If the client is not logged in, redirect to login page
        """
        response = self.client.get(reverse("app:index"))
        self.assertFalse(get_user(self.client).is_authenticated)
        self.assertRedirects(response, "/accounts/login/?next=/app/books/", status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_no_books(self):
        """
        If no books exist, an appropriate message is displayed.
        """
        
        user = User.objects.create_user("John Doe")
        self.client.force_login(user=user)
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No books are available")
        self.assertQuerySetEqual(response.context["book_list"], [])

    def test_order_books(self):
        """
        If multiple books exists, they are sorted by their average review score
        """
        book1 = createBook("First Book", "", "", 2024)
        book2 = createBook("Second Book", "", "", 2024)
        book3 = createBook("Last Book", "", "", 2024)

        user = User.objects.create_user("John Doe")
        self.client.force_login(user=user)
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["book_list"], [(book2, 5),(book3, 3),(book1, 2)])