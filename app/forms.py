from django import forms


class ReviewForm(forms.Form):
    review = forms.CharField(label="review", max_length=500)
    rating = forms.IntegerField(label="rating")


class BookForm(forms.Form):
    title = forms.CharField(label="title", max_length=200)
    author = forms.CharField(label="author", max_length=200)
    summary = forms.CharField(label="summary", max_length=500)
    pub_year = forms.IntegerField(label="pub_year")
