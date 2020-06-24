from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'
        # fields = ['judul', 'penulis', 'kelompok_id']
        # exclude = ['penerbit']
        widgets = {
            'judul': forms.TextInput({'class':'form-control', 'id':'input-judul'}),
            'penulis': forms.TextInput({'class':'form-control'}),
            'penerbit': forms.TextInput({'class':'form-control'}),
            'jumlah': forms.NumberInput({'class':'form-control'}),
            'kelompok_id': forms.Select({'class':'form-control'}),
        }