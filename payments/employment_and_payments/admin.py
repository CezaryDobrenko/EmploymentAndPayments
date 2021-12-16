from django.contrib import admin
from employment_and_payments.models import (
    Stanowisko, 
    OcenaPracownika, 
    Dokument, 
    Pracownik, 
    Premia, 
    PrzypisaniNaSzkolenie, 
    Wyksztalcenie,
    Umowa,
    ZwolnienieLekarskie,
    Harmonogram,
    Urlop,
    Zadania,
    Nagrody,
    Dzieci,
    Szkolenie,
    KartaPracownika,
    Ubezpieczenie,
    Adres,
)

class StanowiskoAdmin(admin.ModelAdmin):
    pass

class OcenaPracownikaAdmin(admin.ModelAdmin):
    pass

class DokumentAdmin(admin.ModelAdmin):
    pass

class AdresAdmin(admin.ModelAdmin):
    pass

class UbezpieczenieAdmin(admin.ModelAdmin):
    pass

class KartaPracownikaAdmin(admin.ModelAdmin):
    pass

class SzkolenieAdmin(admin.ModelAdmin):
    pass

class DzieciAdmin(admin.ModelAdmin):
    pass

class NagrodyAdmin(admin.ModelAdmin):
    pass

class ZadaniaAdmin(admin.ModelAdmin):
    pass

class UrlopAdmin(admin.ModelAdmin):
    pass

class HarmonogramAdmin(admin.ModelAdmin):
    pass

class ZwolnienieLekarskieAdmin(admin.ModelAdmin):
    pass

class UmowaAdmin(admin.ModelAdmin):
    pass

class WyksztalcenieAdmin(admin.ModelAdmin):
    pass

class PrzypisaniNaSzkolenieAdmin(admin.ModelAdmin):
    pass

class PracownikAdmin(admin.ModelAdmin):
    pass

class PremiaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Stanowisko, StanowiskoAdmin)
admin.site.register(OcenaPracownika, OcenaPracownikaAdmin)
admin.site.register(Dokument, DokumentAdmin)
admin.site.register(Adres, AdresAdmin)
admin.site.register(Ubezpieczenie, UbezpieczenieAdmin)
admin.site.register(KartaPracownika, KartaPracownikaAdmin)
admin.site.register(Szkolenie, SzkolenieAdmin)
admin.site.register(Dzieci, DzieciAdmin)
admin.site.register(Nagrody, NagrodyAdmin)
admin.site.register(Zadania, ZadaniaAdmin)
admin.site.register(Urlop, UrlopAdmin)
admin.site.register(Harmonogram, HarmonogramAdmin)
admin.site.register(ZwolnienieLekarskie, ZwolnienieLekarskieAdmin)
admin.site.register(Umowa, UmowaAdmin)
admin.site.register(Wyksztalcenie, WyksztalcenieAdmin)
admin.site.register(PrzypisaniNaSzkolenie, PrzypisaniNaSzkolenieAdmin)
admin.site.register(Pracownik, PracownikAdmin)
admin.site.register(Premia, PremiaAdmin)