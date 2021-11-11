from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  #Djangoは整数の値を期待し、その値がpkという名前の変数でビューに渡される
]
# プロジェクトでは名前づけされたURLを後で使うことになるので、アプリのそれぞれのURLに名前をつけておくのは重要
# Ctrl + Fn + B で起動を終了