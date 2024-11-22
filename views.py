from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Post, File, Comment, PostFile
from .forms import RegistrationForm, LoginForm, PostForm, CommentForm, FileForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Вход выполнен!")
                return redirect('home')
            else:
                messages.error(request, "Неверный логин или пароль.")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Выход выполнен!")
    return redirect('home')

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Обработка файлов
            files = request.FILES.getlist('files')
            for file in files:
                file_obj = File.objects.create(
                    author=request.user,
                    file=file,
                    name=file.name
                )
                PostFile.objects.create(
                    post=post,
                    file=file_obj
                )
            messages.success(request, "Пост опубликован!")
            return redirect('home')
    else:
