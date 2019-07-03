from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model =Comment
		#fields = '_all_'
		#fields = ('post','author','message',)
		fields = ('message',)