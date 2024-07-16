from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    desc=models.TextField()
    image=models.ImageField(upload_to="Blog/Images")
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title