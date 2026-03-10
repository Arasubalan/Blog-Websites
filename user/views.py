from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import contactform

#posts=[
#        {'id':1,'title':'post 1','content':'content of post 1'},
#        {'id':2,'title':'post 2','content':'content of post 2'},
#        {'id':3,'title':'post 3','content':'content of post 3'},
#        {'id':4,'title':'post 4','content':'content of post 4'},
#        {'id':5,'title':'post 5','content':'content of post 5'},
#        {'id':6,'title':'post 6','content':'content of post 6'},
#    ]
def home(request):
    post_name="Latest posts"
    # getting data from post model
    posts=post.objects.all()
    paginator= Paginator(posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    
    return render(request,'index.html',{"let_post":post_name,"page_obj":page_obj})

def detail(request, slug):
    #post=next((item for item in posts if item['id']==int(post_id)),None)
    #logger=logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    try:
        posts=post.objects.get(slug=slug)
        related_posts =post.objects.filter(categary=posts.categary).exclude(pk=posts.id)
    except post.DoesNotExist:
        raise Http404("post does not exit")   
    return render(request,'detail.html',{'post':posts,'related_posts':related_posts})

def old_urls_qwe(request):
    return redirect(reverse("user:new_url"))

def new_urls_qwe(request):
    return HttpResponse("I am ramnadu")  

def contact_view(request):
    if request.method == 'POST':
        form=contactform(request.POST)
        logger=logging.getLogger("TESTING")
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        if form.is_valid():
            logger.debug(f'post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message='your form successfully'
            return render(request,'contact.html',{'form':form,'success_message':success_message})

        else:
            logger.debug("from validation failure")
        return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})

    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


    
   

