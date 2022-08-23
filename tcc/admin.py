from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Orientador)
class OrientadorAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    ...

@admin.register(models.TCC)
class TCCAdmin(admin.ModelAdmin):
    ...