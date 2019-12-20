from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length = 200)
    time_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
       # verbose_name_plural选项是指定，模型的复数形式是什么
        verbose_name_plural = 'entries'
    def __str__(self):
        if(len(self.text) > 50):
            return self.text[:50] + "..."
        return self.text

class Pizza(models.Model):
    text = models.TextField(max_length=100)
    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    text = models.TextField()
    def __def__(self):
        return(self.text)

