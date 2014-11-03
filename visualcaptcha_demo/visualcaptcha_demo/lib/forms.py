from django import forms


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name", "required": "required"}))
