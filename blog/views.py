from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login
from blog.models import Post, Comment

def index(request):
	posts = Post.objects.all().order_by('-date')[:4]
	return render(request, 'blog/index.html', {'posts':posts, 'user':request.user})

def allEntries(request):
	posts = Post.objects.all().order_by('-date')
	return render(request, 'blog/all-entries.html', {'posts':posts, 'user':request.user})

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	comments = post.comment_set.all()
	author = post.author.username
	date = str(post.date.date())
	context = {
		'post': post,
		'comments': comments,
		'author': author,
		'date': date,
		'user': request.user
	}
	return render(request, 'blog/post.html', context)

@login_required(login_url='/posts/login-required/')
def edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/edit.html', {'post':post, 'user':request.user})

def update(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	newTitle = request.POST['title']
	newContent = request.POST['content']
	post.title = newTitle
	post.content = newContent
	post.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))

def create(request):
	title = request.POST['title']
	content = request.POST['content']
	date = timezone.now()
	post = Post(title=title, author=request.user, content=content, date=date)
	post.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))

@login_required(login_url='/posts/login-required/')
def compose(request):
	return render(request, 'blog/compose.html', {'user':request.user})

def userLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect(reverse('blog:index'))
		else:
			#return render(request, 'blog/inactive.html', {'user':user})
			pass
	else:
		return render(request, 'blog/login-failed.html', {'username':username})

def userLogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:index'))

def register(request):
	return render(request, 'blog/register.html')

def createUser(request):
	username = request.POST['username']
	password = request.POST['password']
	user = User.objects.create_user(username, password=password)
	user.save()
	return HttpResponseRedirect(reverse('blog:index'))

def loginRequired(request):
	return render(request, 'blog/login-required.html')

@login_required(login_url='/posts/login-required')
def delete(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.comment_set.all().delete()
	post.delete()
	return HttpResponseRedirect(reverse('blog:index'))

def comment(request, post_id):
	author = request.POST['author']
	content = request.POST['comment']
	post = get_object_or_404(Post, pk=post_id)
	comment = Comment(author=author, comment=content, date=timezone.now(), post=post)
	comment.save()
	return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))
