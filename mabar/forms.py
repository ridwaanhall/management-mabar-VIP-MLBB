from django import forms

from .models import Mabar, BonusSkin, RequestHero
class BonusSkinForm(forms.ModelForm):
    class Meta:
        model = BonusSkin
        fields = ['mabar', 'hero_digunakan', 'skin_request', 'terkirim', 'date_terkirim']

class RequestHeroForm(forms.ModelForm):
    class Meta:
        model = RequestHero
        fields = ['donate_name', 'type_request', 'hero_name', 'type_lane', 'count', 'catatan', 'is_done']

class MabarForm(forms.ModelForm):
    class Meta:
        model = Mabar
        fields = [
            'donate_name', 'nickname', 'id_user', 'zone_user', 'sisa_mabar', 'catatan', 'status', 'is_vvip', 'is_done'
        ]
