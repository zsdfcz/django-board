from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=20) # 제목
    body = models.TextField() # 내용
    created_at = models.DateTimeField(auto_now_add=True) #생성시 적용
    updated_at = models.DateTimeField(auto_now=True) # 수정시 적용
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    comment = models.ForeignKey(Board, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message