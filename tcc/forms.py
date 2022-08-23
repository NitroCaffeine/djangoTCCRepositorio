from django.forms import ModelForm
from .models import TCC, Autor, Curso, Orientador


class TccForm(ModelForm):
    class Meta:
        model = TCC
        fields = '__all__'  

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'  

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'  

class OrientadorForm(ModelForm):
    class Meta:
        model = Orientador
        fields = '__all__'  

