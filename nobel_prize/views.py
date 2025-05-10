from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import NobelPrize
from .forms import NobelPrizeForm
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class NobelListView(ListView):
    model = NobelPrize
    template_name = 'nobel_prize/nobel_list.html'
    context_object_name = 'prizes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return NobelPrize.objects.filter(name__icontains=query)
        return NobelPrize.objects.all()

class NobelCreateView(CreateView):
    model = NobelPrize
    form_class = NobelPrizeForm
    template_name = 'nobel_prize/nobel_form.html'
    success_url = reverse_lazy('nobel-list')

class NobelUpdateView(UpdateView):
    model = NobelPrize
    form_class = NobelPrizeForm
    template_name = 'nobel_prize/nobel_form.html'
    success_url = reverse_lazy('nobel-list')

class NobelDeleteView(DeleteView):
    model = NobelPrize
    template_name = 'nobel_prize/nobel_confirm_delete.html'
    success_url = reverse_lazy('nobel-list')

class NobelDetailView(DetailView):
    model = NobelPrize
    template_name = 'nobel_prize/nobel_detail.html'