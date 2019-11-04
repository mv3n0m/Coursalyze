from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Search
from .src import indexer

# Create your views here.


def index(request):
    return render(request, 'scraper/index.html')


def new_search(request):
    search = request.POST.get('search')
    filters = request.POST
    paginator = Paginator(indexer.index(search, filters), 12)
    page = request.GET.get('page', 1)
    try:
        final_list = paginator.page(page)
    except PageNotAnInteger:
        final_list = paginator.page(1)
    except EmptyPage:
        final_list = paginator.page(paginator.num_pages)

    context_items = {
        'search': search,
        'final_list': final_list,
        'filters': filters,
    }
    return render(request, 'scraper/list.html', context_items)


def detail(request, slug):
    data = indexer.detail(slug)
    context_items = {
        'slug': slug,
        'data': data,
    }
    return render(request, 'scraper/details.html', context_items)
