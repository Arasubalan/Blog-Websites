from django.db import models
from django.utils.text import slugify


class categary(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 

class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.URLField(null=True)
    cerated_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)
    categary=models.ForeignKey(categary,on_delete=models.CASCADE)
    
    def save(self,*args,**kwargs ):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    
   
