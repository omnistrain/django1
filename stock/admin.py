from django.contrib import admin

from stock.models import Groupe, Formation

class GroupeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'creation')

class FormationAdmin(admin.ModelAdmin):
    list_display = ('name', 'groupe')

admin.site.register(Groupe, GroupeAdmin)
admin.site.register(Formation, FormationAdmin)
