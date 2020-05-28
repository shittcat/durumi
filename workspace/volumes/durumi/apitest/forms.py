#apitest/forms.py
from django import forms 
from django.http import HttpResponse , HttpResponseRedirect

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        cdata = super().clean()
        name = cdata
        return HttpResponse(name)