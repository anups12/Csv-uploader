from django import forms
from . models import Csvdata, UploadCsv

class Csvdataadd(forms.ModelForm):
    class Meta:
        model = Csvdata
        fields = ('name','detected', 'dateadd')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),   
            'detected':forms.TextInput(attrs={'class':'form-control'}),   
            'dateadd':forms.DateInput(attrs={'class':'form-control'}),   
        }

class Uploaddatafromcsv(forms.ModelForm):
    class Meta:
        model = UploadCsv
        fields = ('Fileupload',)

        widgets={
            'Fileupload':forms.FileInput(attrs={'class':'form-control'}),   
        }