from django.shortcuts import render
from django.utils import timezone
from .models import Post  # modelsの前にあるドットは カレントディレクトリ 、もしくは カレントアプリケーション 
from django.shortcuts import render, get_object_or_404    # views.pyと models.pyは、同じディレクトリに置いてあります。 だから、こんな風に.とファイル名だけを使って、簡単に記述することが出来る
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


"""render()の使い方
return render(request, template_name, context=None, content_type=None, status=None, using=None)
request template_name の2つは必須
request : requestにはgetまたはpostの情報や、セッション情報が格納されています。
template_name : templateには表示させるテンプレート（HTMLファイル）を指定(templateフォルダをスタートとする相対パスで指定)
context : contextには辞書型のデータを指定します。このcontextに入れた辞書データがテンプレートに渡されます。
          contextにはデータベース操作をして取得したデータなどを格納します。
"""


