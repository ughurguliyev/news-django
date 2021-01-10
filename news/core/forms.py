from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField()


class CommentForm(forms.Form):
    comment = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.CharField()
