from django import forms


class PosForm(forms.Form):
    xPos = forms.FloatField(label='xPos')
    yPos = forms.FloatField(label='yPos')

    def getxPos(self):
        return xPos
    