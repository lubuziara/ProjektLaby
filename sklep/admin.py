from django.contrib import admin
from sklep.models import Produkt, Pracownicy, Zamowienia

@admin.register(Produkt)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']
    list_per_page = 25


@admin.register(Pracownicy)
class PracownicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','lastname','position']
    list_filter = ['name', 'id']
    search_fields = ['name', 'id']
    list_per_page = 25

@admin.register(Zamowienia)
class ZamowieniaAdmin(admin.ModelAdmin):
    list_display = ['id', 'userid','productid','amount']
    list_filter = ['userid', 'productid']
    search_fields = ['userid', 'productid']
    list_per_page = 25
