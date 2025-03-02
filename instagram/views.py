from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import login, authenticate, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

from .models import Post, Like, Comment, Story, Message, User


User = get_user_model()


@login_required
def home(request):
    """
    View for the home page of the application.
    """

    posts = Post.objects.all().order_by('-created_at')
    stories = Story.objects.all().order_by('-created_at')

    return render(request, 'home.html', {'posts': posts, 'stories': stories})


@login_required
def post_detail(request, post_id):
    """
    View for the post detail page of the application.
    """

    post = get_object_or_404(Post, id=post_id)

    return render(request, 'post_detail.html', {'post': post})


@login_required
def like_post(request, post_id):
    """
    View for liking a post.
    """

    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()

    return redirect('post_detail', post_id=post.id)


@login_required
def add_comment(request, post_id):
    """
    View for adding a comment to a post.
    """

    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        text = request.POST.get('text')

        Comment.objects.create(user=request.user, post=post, text=text)

    return redirect('post_detail', post_id=post.id)


@login_required
def user_profile(request, username):
    """
    View for the user profile page of the application.
    """

    user = get_object_or_404(User, username=username)
    posts = user.posts.all()

    return render(request, 'profile.html', {'profile_user': user, 'posts': posts})


@login_required
def follow_user(request, username):
    """
    View for following a user.
    """

    user_to_follow = get_object_or_404(User, username=username)

    if user_to_follow != request.user:
        if request.user in user_to_follow.followers.all():
            user_to_follow.followers.remove(request.user)
        else:
            user_to_follow.followers.add(request.user)

    return redirect('user_profile', username=username)


@login_required
def send_message(request, username):
    """
    View for sending a message to a user.
    """

    receiver = get_object_or_404(User, username=username)

    if request.method == 'POST':
        text = request.POST.get('text')

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            text=text,
        )

    return redirect('user_profile', username=receiver.username)


@login_required
def delete_post(request, post_id):
    """
    View for deleting a post.
    """

    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()

    return redirect('home')


@login_required
def delete_comment(request, comment_id):
    """
    View for deleting a comment.
    """

    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()

    return redirect('home')


@login_required
def delete_message(request, message_id):
    """
    View for deleting a message.
    """

    message = get_object_or_404(Message, id=message_id, sender=request.user)
    message.delete()

    return redirect('home')


def register_view(request):
    """
    View for registering a new user.
    """

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Parollar mos kelmadi!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ushbu username allaqachon mavjud!")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        login(request, user)

        messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz!")

        return redirect("home")

    return render(request, "register.html")


def login_view(request):
    """
    View for logging in a user.
    """

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect("home")
        else:
            messages.error(request, "Username yoki parol xato!")

    return render(request, "login.html")


@login_required
def logout_view(request):
    """
    View for logging out a user.
    """
    
    logout(request)
    messages.success(request, "Tizimdan muvaffaqiyatli chiqdingiz!")
    return redirect("login")
