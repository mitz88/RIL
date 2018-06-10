#from django.http import HttpResponse
# Create your views here.
'''
def index (request):
    return HttpResponse("Welcome to my blog !")
'''

from django.shortcuts import render

from .models import Posts, Comments
from django.db.models import F


def index(request):
    #return HttpResponse('HELLO FROM POSTS')
    posts = Posts.objects.all()[:10]    #asks for the data from the table in this way whose format is given in the Model.py, Posts class definition.
    #print(str(posts)); exit;
    context = {
      'title': 'Latest Posts',
      'posts': posts
    }
    
    return render(request, 'posts/index.html', context)

    
def details(request, id):
    
    post = Posts.objects.get(id=id)
    
    '''increment the view count of the blog'''
    inc_count = Posts.objects.filter(id=id).update(view_count=F("view_count")+1)
    comment = Comments.objects.filter(post_id=id)

    context = {
        'post': post,
        'comments':comment
    }
    
    return render(request, 'posts/details.html', context)