from django.shortcuts import render,HttpResponse,redirect
import blog.models as bm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allPosts = bm.post.objects.all()
    #print(allPosts)
    context ={'allPosts': allPosts}
    return render(request, 'blog/blogHome.html',context)

def blogPost(request, slug):
    post = bm.post.objects.filter(slug = slug).first()
    comments = bm.comment.objects.filter(post = post)
    #print(post.title)
    context = {'post':post,'comments':comments}
    return render(request, 'blog/blogPost.html',context)


def do_comment(request,slug):
    if request.method == 'POST':
        Comment = bm.comment()
        Comment.name = request.user
        Comment.body = request.POST['body']
        Comment.post = bm.post.objects.get(slug = slug)
        Comment.save()
        messages.success(request,"Comment successful")
        return redirect('/')