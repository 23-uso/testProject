from django import forms
from .models import Post, Product  # Product もインポート

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')  # ← Metaクラスの中に移動

class ProductForm(forms.ModelForm):  # ← おそらく 'ProductForm' への変更が必要
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')