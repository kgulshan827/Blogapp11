from django.shortcuts import  render,redirect
from django.http import HttpResponse
from.models import Articles
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

from .import forms


def home (request):
    return render(request,'home.html')
def article_list(request):
    articles=Articles.objects.all().order_by('date')

    return render(request,'article_list.html',{'articles':articles,
                                               })
@login_required(login_url="/accounts/login")
def article_detail(request,slug):

    articles=Articles.objects.get(slug=slug)


    comments = articles.comments.filter(active=True)
    new_comment = None

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
                                                 'comment_form': comment_form})
@login_required(login_url="/accounts/login")
def like_post(request):
     article = Articles.objects.get(id=request.POST.get('article_id'))
     article.likes.add(request.user)
     return redirect('list')
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

