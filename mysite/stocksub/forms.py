from django.forms import ModelForm
from .models import Subscription

class SubscripForm(ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'ticker',
            'number'
        ]