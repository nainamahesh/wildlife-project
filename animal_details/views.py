from django.views import generic
from .models import Animal,Medicine
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'animal_details/index.html'

    def get_queryset(self):
        return Animal.objects.all()

class DetailView(generic.DetailView):
    model = Animal
    template_name = 'animal_details/detail.html'

class AnimalCreate(CreateView):
    model = Animal
    fields = ['id','Animal_species','Animal_count','Animal_type','Scientific_name','Country','Animal_feed','Feed_cost']


class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['id','Animal_species','Animal_count','Animal_type','Scientific_name','Country','Animal_feed','Feed_cost']


class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal_details:index')

class MedicineDetail(generic.ListView):

    model = Medicine
    template_name = 'animal_details/med.html'

class MedicineCreate(CreateView):
    model = Medicine
    fields = ['Animal_id','Medicine_name','Medicine_cost']

class MedicineUpdate(UpdateView):
    model = Medicine
    fields = ['Animal_id','Medicine_name','Medicine_cost']

