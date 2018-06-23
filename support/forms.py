from django import forms
from support.models import Ticket, TicketComment


class ListFilterForm(forms.Form):
    showClosed = forms.BooleanField(required=False, label='Show closed')
    searchQuery = forms.CharField(required=False, label='Search')


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ( 'category', 'text', )


class TicketCommentCreateForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ('comment',)


class TicketStatusChangeForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['status']
