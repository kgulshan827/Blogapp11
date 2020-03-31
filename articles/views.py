from django.shortcuts import  render,redirect
from django.http import HttpResponse
from.models import Articles
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

from .import forms

from django.db.models import Count    

def home (request):
    return render(request,'home.html')
def article_list(request):
    articles=Articles.objects.all().order_by('date')

    return render(request,'article_list.html',{'articles':articles,
                                               })
@login_required(login_url="/accounts/login")
def article_detail(request,slug):

    articles=get_object_or_404(Articles,slug=slug)


    comments = articles.comments.filter(active=True)
    new_comment = None
    is_liked=False
    if articles.likes.filter(id=request.user.id).exists():
        
        is_liked=True
    

    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            if not (request.user.is_authenticated):
                return redirect('login')

            new_comment = comment_form.save(commit=False)

            new_comment.post = articles
            new_comment.username = request.user
            new_comment.active = True

            new_comment.save()
    else:
        comment_form = forms.CommentForm()



    return render(request,'article_detail.html',{'article':articles,
                                                 'comments': comments,
                                                 'new_comment': new_comment,
                                                 'comment_form': comment_form,
                                                 'is_liked':is_liked,
                                                 'total_likes':articles.total_likes() })
@login_required(login_url="/accounts/login")
def like_post(request):
    article = Articles.objects.get(id=request.POST.get('article_id'))
     
    is_liked=False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        is_liked=False
    
    else:

        article.likes.add(request.user)
        is_liked=True

    return redirect('detail',article.slug)
def author(request):

    
    article=(Articles.objects.filter(author=request.user)).count()
    articles=Articles.objects.filter(author=request.user)
    
    
    return render(request,'author.html',{'article':article,
    'articles':articles})
def create(request):

    if request.method == 'POST':

        form=forms.Articleform(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user

            instance.save()
            return redirect('list')

    else:
      form=forms.Articleform()
    return render(request,'create.html',{'form':form})

