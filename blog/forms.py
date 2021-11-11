from django import forms

from .models import Post

class PostForm(forms.ModelForm):   #フォームの名前を作成

    class Meta:  # どのモデルを使うかをこちらで作成
        model = Post
        fields = ('title', 'text',)