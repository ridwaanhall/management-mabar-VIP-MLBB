from django import forms
from .models import Mabar

class MabarForm(forms.ModelForm):
    class Meta:
        model = Mabar
        fields = [
            'donate_name', 'nickname', 'id_user', 'zone_user', 'sisa_mabar', 'catatan', 'status', 'is_vvip', 'is_done'
        ]
