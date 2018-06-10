from datetime import datetime

from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title + "--Views:"+str(self.view_count)
    class Meta:
        verbose_name_plural = "Posts"

class Comments(models.Model):
    user = models.IntegerField()
    comment_text = models.TextField()
    post_id = models.ForeignKey(Posts, on_delete=None)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.comment_text
    class Meta:
        verbose_name_plural = "Comments"
    

    
    