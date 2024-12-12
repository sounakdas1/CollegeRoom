from django.db import models
from django.contrib.auth.models import User
# from accounts.models import UserProfile 
from django.utils.text import slugify

   
class Department(models.Model):
    name = models.CharField(max_length=30,unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
    

class CreateTopic(models.Model):
    name = models.CharField(max_length=300,unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='topics',null=True)
    description = models.CharField(max_length=750,null=True,blank=True)
    slug = models.SlugField(unique=True)
# Field to categorize topics
    def save(self, *args, **kwargs):
        if not self.slug:
            # Create the slug from the name
            self.slug = slugify(self.name)

            # Check for uniqueness
            original_slug = self.slug
            counter = 1
            while CreateTopic.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}-{self.description}"



class Chats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    chats = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(CreateTopic,on_delete=models.CASCADE,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    pdf = models.FileField(upload_to='pdfs/',null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='chats',null=True)
    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

        
class Replies(models.Model):

    chats = models.ForeignKey(Chats,on_delete=models.CASCADE,related_name='replies')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    topic = models.ForeignKey(CreateTopic,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='replies')
    reply = models.TextField(max_length=400)
    replied_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"


