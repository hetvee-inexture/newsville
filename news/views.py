from django.shortcuts import render,redirect
from news.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from news.forms import TagForm, NewsTagForm

def home(request):

	return render(request, 'news/home.html')

def ndtv_news(request):
	latest_news_obj = NdtvNews.objects.all()

	if request.user.is_superuser:
		form = NewsTagForm()

		if request.method == 'POST':
			form = NewsTagForm(request.POST)
			if form.is_valid():
				tag = form.save(commit=False)
				tag.news_id = request.POST.get('news_id')
				tag.save()

				return redirect('/ndtv-news')
		
		context = {
			'latest_news' : latest_news_obj,
			'form' : form
		}
		return render(request, 'news/ndtv_news.html', context)
	else:

		latest_news_obj = NdtvNews.objects.all()
		tags = Tags.objects.all()
		news_tags = NewsTag.objects.all()
		context = {
			'latest_news' : latest_news_obj,
			'tags' : tags,
			'ids' :news_tags
		}
		return render(request, 'news/ndtv_news.html', context)

def zee_news(request):
	news_obj = ZeeNews.objects.all()

	if request.user.is_superuser:
		form = NewsTagForm()

		if request.method == 'POST':
			form = NewsTagForm(request.POST)
			if form.is_valid():
				tag = form.save(commit=False)
				tag.news_id = request.POST.get('news_id')
				tag.save()
				return redirect('/zee-news')
		
		context = {
			'latest_news' : news_obj,
			'form' : form
		}
		return render(request, 'news/zee_news.html', context)

	else:
		tags = Tags.objects.all()
		news_tags = NewsTag.objects.all()
		context = {
			'latest_news': news_obj,
			'tags': tags,
			'ids': news_tags
		}
		return render(request, 'news/zee_news.html', context)

def scroll_news(request):

	news_obj = ScrollNews.objects.all()

	if request.user.is_superuser:
		form = NewsTagForm()

		if request.method == 'POST':
			form = NewsTagForm(request.POST)
			if form.is_valid():
				tag = form.save(commit=False)
				tag.news_id = request.POST.get('news_id')
				tag.save()
				return redirect('/scroll-news')
		
		context = {
			'latest_news' : news_obj,
			'form' : form
		}
		return render(request, 'news/scroll_news.html', context)

	else:
		tags = Tags.objects.all()
		news_tags = NewsTag.objects.all()
		context = {
			'latest_news': news_obj,
			'tags': tags,
			'ids': news_tags
		}
		return render(request, 'news/scroll_news.html', context)

def add_tag(request):
	form = TagForm()
	if request.method == 'POST':
		form = TagForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form': form
	}
	return render(request, 'news/add_tag.html', context)
	  
