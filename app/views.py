from typing import Any
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm  
from numpy import mean


from .models import Book, Review
from .forms import ReviewForm, BookForm

@login_required  
def book_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_list = book.review_set.all()
    return render(request, "app/book_detail.html", {"book": book, "review_list": review_list})

@login_required
def index(request):
    book_list = Book.objects.all()
    average_list = []
    for book in book_list:
        if not book.review_set.values_list("score"):
            average_list.append(-1)
        else:
            average_list.append(round(mean(book.review_set.values_list("score")),2))

    complete_list = sorted(list(zip(list(book_list), average_list)), key=lambda l:l[1], reverse=True)
    template = loader.get_template("app/index.html")
    context = {
        "book_list": complete_list,
    }
    return HttpResponse(template.render(context, request))
        
@login_required
def get_review(request, book_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
                r = Review(review_text=form.cleaned_data.get("review"), score=form.cleaned_data.get("rating"), book=Book.objects.get(pk=book_id))
                r.save()
                return HttpResponseRedirect(reverse("app:book", args=(book_id,)))
    else:
        form = ReviewForm()

    return render(request, "app/review_form.html", {"form": form})

@login_required
def get_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        print(form)
        if form.is_valid():
                b = Book(
                    title=form.cleaned_data.get("title"), 
                    author=form.cleaned_data.get("author"), 
                    summary=form.cleaned_data.get("summary"),
                    pub_year=form.cleaned_data.get("pub_year"),
                    )
                b.save()
                return HttpResponseRedirect(reverse("app:index", args=()))
    else:
        form = ReviewForm()

    return render(request, "app/book_form.html", {"form": form})


def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("app:index", args=()))
    else:
        form = UserCreationForm()

    return render(request, "registration/create_account.html", {"form": form})