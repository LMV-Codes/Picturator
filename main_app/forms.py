from django import forms


class ImageFieldForm(forms.Form):
    image_field = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))