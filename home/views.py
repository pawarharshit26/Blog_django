from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout

from blog.models import post
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    messages.info(request,'Welcome to contact')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<3 or len(phone)<10 or len(email)<5 or len(content)<3:
            messages.error(request,"Fill form correctly")
        else:
            contact = Contact(name = name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"your query is submit")
       # print(name,email,phone,content)
        

    return render(request, 'home/contact.html')

def about(request):
    messages.error(request,'Welcome to About')
    messages.info(request,'Welcome to About')
    messages.success(request,'Welcome to About')
    messages.success(request,'Welcome to About')
    return render(request, 'home/about.html')

def search(request):
    #allPosts = post.objects.all()
    query = request.GET['query']
    if len(query) > 78:
        allPosts=post.objects.none()
        messages.warning(request,'query is too large try small query')
    else:
        allPostsTitle = post.objects.filter(title__icontains = query)
        allPostsContent = post.objects.filter(content__icontains = query)
        allPosts = allPostsTitle.union(allPostsContent)
        allPostsAuthor = post.objects.filter(author__icontains = query)
        allPosts = allPosts.union(allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request,'No search result found refine your query')
    params = {'allPosts': allPosts,'query':query}
    return render(request,"home/search.html", params)


def handleSingup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if len(username) > 10:
            messages.error(request, 'Username is very large')
            return redirect('home')
        if User.objects.filter(username=username).exists():
            messages.error(request,"this Username is not available")
            return redirect('home')
        if User.objects.filter(email=email).exists():
            messages.error(request,"this email is already registered")
            return redirect('home')
        if password != cpassword:
            messages.error(request, 'passwords are not match')
            return redirect('home')
        
        myuser = User.objects.create_user(username = username,email = email,password = password)
        myuser.save()
        messages.success(request, 'Your iCoder account is created')
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")


def handleLogin(request):
    if request.method == 'POST':
        lusername = request.POST['lusername']
        if  User.objects.filter(username = lusername).exists():
            lpassword = request.POST['lpassword']
            user = authenticate(username = lusername, password = lpassword)
            if user is not None:
                login(request, user)
                messages.success(request,'Login is Successful')
                return redirect('home')
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('home')
        else:
            messages.error(request,"User is not registered.please signup")
            return redirect('home')
    else:
        return HttpResponse('404 - Not found')

def handleLogout(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('home')
    