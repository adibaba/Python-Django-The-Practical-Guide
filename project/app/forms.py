from django import forms


class BookmarkForm(forms.Form):
    url = forms.CharField(max_length=255, label="URL")
    title = forms.CharField(max_length=255)
