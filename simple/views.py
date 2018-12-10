from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import *
from .form import CommentForm
from django.core.paginator import Paginator
#from markdown import markdown
#import pygments
# Create your views here.
def about(request):
	return render(request,"about.html")
class Index(ListView):
	template_name = "index.html"
	context_object_name = 'blog'
	model = Blog
	paginate_by = 5
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		quen1 = len(Blog.objects.select_related('category').filter(category__name="编程"))
		quen2 = len(Blog.objects.select_related('category').filter(category__name="随笔"))
		quen3 = len(Blog.objects.select_related('category').filter(category__name="笔记"))
		quen4 = len(Blog.objects.select_related('category').filter(category__name="感想"))
		context['title'] = "首页"
		context['count1']=quen1
		context['count2']=quen2
		context['count3']=quen3
		context['count4']=quen4
		return context


class Share(ListView):
	template_name='share.html'
	context_object_name = 'blog1'
	queryset = Blog.objects.select_related('category').filter(category__name="编程")
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "展示"
		context["blog2"] = Blog.objects.select_related('category').filter(category__name="随笔")
		context["blog3"] = Blog.objects.select_related('category').filter(category__name="笔记")
		context["blog4"] = Blog.objects.select_related('category').filter(category__name="感想")
		return context
'''class Info(DetailView):
	template_name = "info.html"
	context_object_name = "blog"
	pk_url_kwarg = 'blog_id'
	model = Blog
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['comment']=Comment.objects.select_related('blog').all()
		context['form']=CommentForm()
		context['title']="内容"
		return context'''
def get_search(request):
    keyword = request.POST.get('keyboard')
    #print(keyword)
    allArticle = Blog.objects.all()
    SearchResult = []
    for x in allArticle:
        if keyword in x.title:
            SearchResult.append(x)
        elif keyword in x.content:
            SearchResult.append(x)
    SearchStatus = "Error" if len(SearchResult) == 0 else "Success"
    ResultAmount = len(SearchResult)

    return render(request, 'search.html', {"title": "{}的查询结果".format(keyword),
                                           "SearchResult": SearchResult,
                                           "SearchStatus": SearchStatus,
                                           "ResultAmount": ResultAmount})
class biancheng(Index):
	#template_name='index.html'
	#context_object_name = 'blog'
	#queryset = Blog.objects.select_related('category').filter(category__name="编程")
	def get_queryset(self):
		return Blog.objects.select_related('category').filter(category__name="编程")
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "编程"
		return context
class suibi(Index):
	#template_name='index.html'
	#context_object_name = 'blog'
	#queryset = Blog.objects.select_related('category').filter(category__name="随笔")
	def get_queryset(self):
		return Blog.objects.select_related('category').filter(category__name="随笔")
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "随笔"
		return context
class biji(Index):
	#template_name='index.html'
	#context_object_name = 'blog'
	#queryset = Blog.objects.select_related('category').filter(category__name="笔记")
	def get_queryset(self):
		return Blog.objects.select_related('category').filter(category__name="笔记")
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "笔记"
		return context
class ganxiang(Index):
	#template_name='index.html'
	#context_object_name = 'blog'
	#queryset = Blog.objects.select_related('category').filter(category__name="感想")
	def get_queryset(self):
		return Blog.objects.select_related('category').filter(category__name="感想")
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "感想"
		return context

def info(request,blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.increase_views()
        context={}
        context['blog']=blog
        context['comment']=Comment.objects.select_related('blog').filter(blog=blog)
        context['form']=CommentForm()
        context['title']="内容"
        if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.blog=blog
                        comment.save()
        return render(request,"info.html",context)



