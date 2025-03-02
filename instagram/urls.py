from django.urls import path

from .views import (
    home, post_detail, like_post, add_comment, user_profile, 
    follow_user, send_message, delete_post, delete_comment, delete_message,
    register_view, login_view, logout_view
)


urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('profile/<str:username>/follow/', follow_user, name='follow_user'),
    path('profile/<str:username>/message/', send_message, name='send_message'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('message/<int:message_id>/delete/', delete_message, name='delete_message'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
