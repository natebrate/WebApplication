from django.forms import ModelForm
from stale.models import *


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'name', 'phone',
                  'email', 'role']


class SpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = '__all__'


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
