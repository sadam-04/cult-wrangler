from django import forms
from .models import EventResponse

class EventResponseForm(forms.ModelForm):
    class Meta:
        model = EventResponse
        fields = '__all__'