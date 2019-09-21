from django import forms

class DeckCodeForm(forms.Form):
	deck_code = forms.CharField(label='')
	def __init__(self, *args, **kwargs):
		super(DeckCodeForm, self).__init__(*args, **kwargs)
		self.fields['deck_code'].widget.attrs.update({'class': 'form-control'})