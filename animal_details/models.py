from django.db import models
from django.core.urlresolvers import reverse

class Animal(models.Model):
    id=models.AutoField(primary_key=True)
    Animal_species=models.CharField(max_length=100)
    Animal_count=models.IntegerField(default=0)
    Animal_type=models.CharField(max_length=20)
    Scientific_name=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    Animal_feed=models.CharField(max_length=100)
    Feed_cost=models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('animal_details:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.id)+' - '+(self.Animal_species)

class Medicine(models.Model):
    Animal_id=models.ForeignKey(Animal,on_delete=models.CASCADE)
    Medicine_name=models.CharField(max_length=200)
    Medicine_cost=models.FloatField(default=0.0)
    Date=models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('animal_details:med-detail')

    def __str__(self):

        return str(self.Animal_id)+' on '+str(self.Date)
