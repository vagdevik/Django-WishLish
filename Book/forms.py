from django import forms
class form(forms.Form):
    reader=forms.CharField(label="Reader Name",max_length=255,widget=forms.TextInput(attrs={'placeholder':'username'}))
    book=forms.CharField(label="Book",max_length=255,widget=forms.TextInput(attrs={'placeholder':'Name of the Book'}))
    author=forms.CharField(label="Author",max_length=255,widget=forms.TextInput(attrs={'placeholder':'Author'}))
    category=forms.CharField(label="Category",max_length=255,widget=forms.TextInput(attrs={'placeholder':'Category'}))
    rate=forms.IntegerField(label="How much do you rate?",widget=forms.NumberInput(attrs={'placeholder':'your rating'}))
