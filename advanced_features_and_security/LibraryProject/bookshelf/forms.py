from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_year = forms.IntegerField(min_value=0, required=True)
    isbn = forms.CharField(max_length=13, required=True)
    pages = forms.IntegerField(min_value=1, required=True)
    cover = forms.ChoiceField(choices=[('hard', 'Hardcover'), ('soft', 'Softcover')], required=True)
    language = forms.CharField(max_length=50, required=True)
