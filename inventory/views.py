from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from inventory.models import Item, Location


class IndexView(generic.ListView):
    template_name = 'inventory/index.html'
    context_object_name = 'latest_item_list'

    def get_queryset(self):
        """Return the last five published inventory."""
        return Item.objects.order_by('-added_date')[:5]


class DetailView(generic.DetailView):
    model = Item
    template_name = 'inventory/detail.html'


class EditView(generic.DetailView):
    model = Item
    template_name = 'inventory/edit.html'

class AddView(generic.DetailView):
    model = Item
    template_name = 'inventory/add.html'




