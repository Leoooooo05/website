from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    price=models.FloatField()
    image=models.ImageField(upload_to="item_images",blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Conversation(models.Model):
    item=models.ForeignKey(Item,related_name="conversations",on_delete=models.CASCADE)
    members=models.ManyToManyField(User,related_name="conversations")
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="created_messages",on_delete=models.CASCADE)
    content=models.TextField()
    conversation=models.ForeignKey(Conversation,related_name="messages",on_delete=models.CASCADE)