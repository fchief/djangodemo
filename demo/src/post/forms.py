from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['post_id', 'title', 'content', 'post_type']
