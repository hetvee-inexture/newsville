from django.shortcuts import render,redirect
from news.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from news.forms import TagForm, NewsTagForm, HeadlinesForm, NewsHeadlinesForm

#home page for all users
@login_required
def home(request):
	if request.user.is_superuser:

		return render(request, 'news/home.html')
	else:

		context = {
			'headlines': Headlines.objects.all()
		}
		

		return render(request, 'news/home.html',context)

#ndtv news page
@login_required
def ndtv_news(request):
	latest_news_obj = NdtvNews.objects.all()

	if request.user.is_superuser:
		form = NewsTagForm()
		headline_form = NewsHeadlinesForm()

		if request.method == 'POST':
			form = NewsTagForm(request.POST)
			if form.is_valid():
				tag = form.save(commit=False)
				tag.news_id = request.POST.get('news_id')
				tag.save()

			headline_form = NewsHeadlinesForm(request.POST)
			if headline_form.is_valid():
				headline = headline_form.save(commit=False)
				headline.news_id = request.POST.get('news_id')
				headline.save()

			return redirect('/ndtv-news')
		
		
		context = {
			'latest_news' : latest_news_obj,
			'form' : form,
			'headline_form' : headline_form
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
		
#zee news page		
@login_required
def zee_news(request):
	news_obj = ZeeNews.objects.all()

	if request.user.is_superuser:
		form = NewsTagForm()
		headline_form = NewsHeadlinesForm()

		if request.method == 'POST':
			form = NewsTagForm(request.POST)
			if form.is_valid():
				tag = form.save(commit=False)
				tag.news_id = request.POST.get('news_id')
				tag.save()

			headline_form = NewsHeadlinesForm(request.POST)
			if headline_form.is_valid():
				headline = headline_form.save(commit=False)
				headline.news_id = request.POST.get('news_id')
				headline.save()

			return redirect('/zee-news')
		
		context = {
			'latest_news' : news_obj,
			'form' : form,
			'headline_form' : headline_form
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

#scroll news page
@login_required
def scroll_news(request):
	news_obj = ScrollNews.objects.all()

	if request.user.is_superuser:
		form = NewsTagForm()
		headline_form = NewsHeadlinesForm()

		if request.method == 'POST':
			form = NewsTagForm(request.POST)
			if form.is_valid():
				tag = form.save(commit=False)
				tag.news_id = request.POST.get('news_id')
				tag.save()

			headline_form = NewsHeadlinesForm(request.POST)
			if headline_form.is_valid():
				headline = headline_form.save(commit=False)
				headline.news_id = request.POST.get('news_id')
				headline.save()

			return redirect('/scroll-news')
		
		context = {
			'latest_news' : news_obj,
			'form' : form,
			'headline_form': headline_form
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
		
# function for adding tags
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

def add_headline(request):

	if request.method == 'POST':
		form = HeadlinesForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = HeadlinesForm()

	context = {
		'form': form
	}
	return render(request, 'news/add_headline.html', context)

def news_display(request):
	admin_headline = request.GET.get('admin_headline')
	headline = Headlines.objects.filter(headlines=admin_headline)
	news_headlines = NewsHeadlines.objects.filter(headlines_id=headline[0].id)
	news_tags = NewsTag.objects.all()
	context = {
		'news_tags': news_tags,
		'tags': Tags.objects.all(),
		'news_headlines':news_headlines,
		'ndtv_obj': NdtvNews.objects.all(),
		'zee_news': ZeeNews.objects.all(),
		'scroll_news': ScrollNews.objects.all()
	}
	return render(request, 'news/news_display.html',context)


