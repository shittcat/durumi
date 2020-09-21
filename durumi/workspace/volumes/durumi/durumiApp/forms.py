#apitest/forms.py
from django import forms 
from django.http import HttpResponse , HttpResponseRedirect

class PosForm(forms.Form):
    xPos = forms.FloatField(label='xPos')
    yPos = forms.FloatField(label='yPos')

    def getxPos(self):
        return xPos