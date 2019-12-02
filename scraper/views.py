import random
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from login_app.models import User_Data
from django.contrib.auth.models import User
from .src import indexer


@login_required
def index(request):
    obj = []
    suggs = []
    pref = request.POST.get('pref')
    u = request.POST.get('u')

    if pref:
        User_Data.objects.create(user=request.user, preferences=pref)
        user_object = User_Data.objects.get(user=request.user)
    else:
        username = str(request.user)
        user_object = User_Data.objects.get(username=username)
        user_object.user = request.user
        user_object.save(update_fields=['user'])
        if u:
            user_object.preferences = u
            user_object.save(update_fields=['preferences'])

        b_User = User.objects.get(username=request.user)
        b_User.first_name = user_object.first_name
        b_User.last_name = user_object.last_name
        b_User.save(update_fields=['first_name', 'last_name'])

    obj.clear()
    suggs.clear()

    for preference in user_object.preferences.split(','):
        obj.extend(indexer.temp(search=preference))
    for i in range(5):
        suggs.append(obj[random.randint(0, len(obj)-1)])

    context_items = {
        'f_name': User.objects.get(username=request.user).first_name,
        'suggs': suggs,
    }

    return render(request, 'scraper/index.html', context_items)


@login_required
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


@login_required
def detail(request, slug):
    data = indexer.detail(slug)
    context_items = {
        'slug': slug,
        'data': data,
    }
    return render(request, 'scraper/details.html', context_items)


@login_required
def update(request):
    u = User_Data.objects.get(username=request.user).preferences
    return render(request, 'scraper/update.html', {'u': u})
