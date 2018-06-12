#from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render

from .models import Posts, Comments
from django.db.models import F
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
import json
import ast


def index(request):
    #return HttpResponse('HELLO FROM POSTS')
    posts = Posts.objects.all()[:10]    #asks for the data from the table in this way whose format is given in the Model.py, Posts class definition.
    #print(str(posts)); exit;
    context = {
      'title': 'Latest Posts',
      'posts': posts
    }
    
    return render(request, 'posts/index.html', context)

#@cache_page(CACHE_TTL)   
def details(request, id):
        
    if cache.__contains__(id):
            
        comment = Comments.objects.filter(post_id=id)
        #increment the view count of the blog
        inc_count = Posts.objects.filter(id=id).update(view_count=F("view_count")+1)
        data_str = cache.get(id)
        data_dict = ast.literal_eval(data_str)
        
        class Object(object):
            pass
        
        a = Object() 
        a.title =  data_dict['title']
        a.body = data_dict['body']
        a.created_at = data_dict['created_at']
        
        context = {
            'post': a,
            'comments': comment
        }
        return render(request, 'posts/details.html', context)
    
    else:
        
        post = Posts.objects.get(id=id)
        print(str(post.created_at))#(post.body)    (post.created_at)
        comment = Comments.objects.filter(post_id=id)
        
        detail_dict = {"title":(post.title), "body":post.body, "created_at":str(post.created_at)}
        
        setkey = cache.set(id, json.dumps(detail_dict), timeout=CACHE_TTL)
        
        print(id) 
        
        context = {
            'post': post,
            'comments': comment
        }
        
        return render(request, 'posts/details.html', context)
        
        
        