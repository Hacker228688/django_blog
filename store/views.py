from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from .models import Item, ItemTag
from .forms import ItemForm
from .paginator import paginator


def store(request):
    items = Item.objects.filter(is_available=True)
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],
    }

    return render(request, 'store/main_page.html', context)


class SearchResultsView(ListView):
    model = Item
    template_name = 'store/main_page.html'

class SearchResults(SearchResultsView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = super().get_queryset()
        filtered = qs.filter(title__iregex=query)
        print(filtered)
        return filtered




def item_details(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'store/item_details.html', context)


def tag_details(request, slug):
    tag = get_object_or_404(ItemTag, slug=slug)
    items = Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }
    return render(request, 'store/tag_details.html', context)


def tag_list(request):
    tags = ItemTag.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
    }
    return render(request, 'store/tag_list.html', context)


def create_article_view(request):
    if request.method == 'POST':
        form = ItemForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()

    else:
        form = ItemForm()

    context = {
        'form': form
    }
    return render(request, 'store/item_form.html', context)