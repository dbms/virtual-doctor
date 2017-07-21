from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=120)
    pwd = forms.CharField(max_length=80)
    age = forms.IntegerField()
    sex = forms.CharField(max_length=7)
    address = forms.CharField(max_length=100)
    blood = forms.CharField(max_length=8)
    blood_type = forms.CharField(max_length=8)
    phone = forms.CharField(max_length=20)


class LoginForm(forms.Form):
    email=forms.CharField(max_length = 80)
    pwd= forms.CharField(max_length=80)

"""
class AddTopicForm(forms.Form):
    topic_text=forms.CharField(max_length = 250)
    topic_desc=forms.CharField(max_length = 700)
    tag_text=forms.CharField(max_length = 250)

class AddOpinionForm(forms.Form):
    opinion_text=forms.CharField(max_length = 500)
    topic = forms.CharField(max_length = 5)
"""

class SearchForm(forms.Form):
    topic_text=forms.CharField(max_length = 250)
    #symptom=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,required=False)