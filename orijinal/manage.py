from django.db import models

class Category(models.Model):
    """
    「トヨタ」「ホンダ」「日産」
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        
        return self.name

class Product(models.Model):
    """
    「クラウン」「シビック」「フーガ」
    """
    # 商品名
    name = models.CharField(max_length=200)
    
    # 商品説明 
    description = models.TextField()
    
    # 価格 
    price = models.IntegerField()
    
    # カテゴリ
    category = models.ForeignKey(
        Category,                
        on_delete=models.CASCADE  
    )

    def __str__(self):
       
        return self.name