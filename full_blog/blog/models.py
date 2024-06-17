from django.db import models


class Category(models.Model):
     title = models.CharField(max_length=255)
     slug = models.SlugField(unique=True)

     class Meta:
          ordering = ('title',)
          verbose_name_plural = 'Categories'

     def __str__(self):
          return self.title
class Post(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
     title = models.CharField(max_length=255)
     slug = models.SlugField(unique=True)
     intro = models.TextField()
     body = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          ordering = ('-created_at',)

     def __str__(self):
          return self.title

class Comment(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
     name = models.CharField(max_length=255)
     email = models.EmailField()
     body = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)