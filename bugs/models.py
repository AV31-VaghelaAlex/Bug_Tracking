
from django.db import models
from django.contrib.auth.models import User
class Bug(models.Model):
    PRIORITY=[('Low','Low'),('Medium','Medium'),('High','High'),('Critical','Critical')]
    STATUS=[('Open','Open'),('In Progress','In Progress'),('Testing','Testing'),('Closed','Closed')]
    title=models.CharField(max_length=200)
    description=models.TextField()
    priority=models.CharField(max_length=20,choices=PRIORITY)
    status=models.CharField(max_length=20,choices=STATUS,default='Open')
    assigned_to=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    attachment=models.FileField(upload_to='bugs/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Comment(models.Model):
    bug=models.ForeignKey(Bug,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
