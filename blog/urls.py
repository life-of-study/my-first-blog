from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
# プロジェクトでは名前づけされたURLを後で使うことになるので、アプリのそれぞれのURLに名前をつけておくのは重要
# Ctrl + Fn + B で起動を終了