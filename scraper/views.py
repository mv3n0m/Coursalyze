from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Search
from .src import indexer

# Create your views here.


def index(request):
    return render(request, 'scraper/index.html', {'title': "Something is fishy"})


def new_search(request):
    search = request.POST.get('search')
    # Search.objects.create(search_text=search)

    paginator = Paginator(indexer.index(search), 10)

    page = request.GET.get('page', 1)
    # final_list = paginator.get_page(page)

    try:
        final_list = paginator.page(page)
    except PageNotAnInteger:
        final_list = paginator.page(1)
    except EmptyPage:
        final_list = paginator.page(paginator.num_pages)

    context_items = {
        'search': search,
        'final_list': final_list,
    }
    return render(request, 'scraper/list.html', context_items)
