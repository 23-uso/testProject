from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from rest_framework import generics 
from .models import Post
from .forms import PostForm
from .serializers import PostSerializer
from django.utils.decorators import method_decorator
import requests
from django.shortcuts import render

class PostListView(ListView):
    queryset = Post.objects.select_related('author').order_by('-created_at')
    template_name = 'timeline.html' 
    context_object_name = 'posts' 

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

def index(request):
    context = {
        'title': 'こんにちは、 Sota',
        'message':'これはテンプレートを使ったテストページです。',
        'food_list': ['カレー', 'ラーメン', '寿司', 'すき焼き', 'オムライス'],
    }
    return render(request, 'index.html', context)

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_new.html'
    success_url = reverse_lazy('timeline')
    # 元のFBVにあった post.author = request.user の処理を引き継ぐ

    def form_valid(self, form):
        # フォームから post オブジェクトを生成
        post = form.save(commit=False)
        # リクエストしているユーザーを author に設定
        post.author = self.request.user
        # データベースに保存
        post.save()
        # success_url へのリダイレクトを処理
        return redirect(self.success_url)
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('timeline')

class PostListAPIView(generics.ListAPIView): 
   # どのデータの一覧を返すか
   queryset = Post.objects.all()
   # どの翻訳者（シリアライザ）を使ってJSONに変換するか
   serializer_class = PostSerializer 

def weather(request):

    city_name = 'Kanazawa'
    if request.GET.get('city') and request.GET.get('city') in locations:
        city_name = request.GET.get('city')

    # APIのエンドポイント: https://api.open-meteo.com/v1/forecast
    api_url = f'https://api.openmeteo.com/v1/forecast?latitude=36.53&longitude=136.68¤t_weather=true'

   
    response = requests.get(api_url)
    data = response.json()

   
    context = {
        'city': city_name,
        'temperature': data['current_weather']['temperature'],
        'windspeed': data['current_weather']['windspeed'],
        # 天気コード(WMO code)。0=晴天, 1-3=曇り、61-65=雨など
        'weathercode': data['current_weather']['weathercode'],
    }

    return render(request, 'weather.html', context)

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'form.html' # 作成画面と同じフォームを再利用します
    success_url = reverse_lazy('timeline')

    def get_queryset(self):
        # 自分の投稿だけを編集できるように制限する安全策
        return Post.objects.filter(author=self.request.user)
        

