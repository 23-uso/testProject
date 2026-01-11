# app/models.py
from django.db import models
from django.contrib.auth.models import User #Django組み込みのUserモデルをインポート

class Post(models.Model):
    class Meta:
        app_label = 'testApp'

    title = models.CharField(max_length=200, null=True, blank=True)

    # 投稿内容 : 文字数制限のないテキストフィールド
    content = models.TextField()

    # 投稿日時 : データが作成された時に自動で日時を記録
    created_at = models.DateTimeField(auto_now_add=True)

    # 投稿者 : Userモデルと「一対多」の関係で紐付ける
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # 管理画面などで見やすいように、オブジェクトの文字列表現を定義
        return f'{self.author.username}: {self.content[:20]}'

class Product(models.Model):
    class Meta:
        app_label = 'testApp'
    
    # (ProductForm の fields に合わせて定義)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name