from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL


class Adres(models.Model):
    class Meta:
        verbose_name = 'Adress'
        verbose_name_plural = 'Adress'

    miejscowosc = models.CharField("City", max_length=200)
    ulica = models.CharField("Street", max_length=200)
    numer_domu = models.CharField("House number", max_length=200)
    kod_pocztowy = models.CharField("Postal code", max_length=200)

    def __str__(self):
        return f"Adress: {self.id} (city: {self.miejscowosc}, street: {self.ulica}, number: {self.numer_domu})"


class Stanowisko(models.Model):
    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Position'

    nazwa = models.CharField("Name", max_length=200)
    opis = models.CharField("Description", max_length=200)
    wymagania = models.CharField("Requirements", max_length=200)
    kod_dzialu = models.IntegerField("Departament code", default=0)

    def __str__(self):
        return f"Position: {self.id} (name: {self.nazwa}, desc: {self.opis})"


class Wyksztalcenie(models.Model):
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    typ = models.CharField("Type", max_length=200)
    opis = models.CharField("Description", max_length=200)
    data_uzyskania = models.DateTimeField("Obtaining date")

    def __str__(self):
        return f"Education: {self.id} (type: {self.typ}, desc: {self.opis})"


class Ubezpieczenie(models.Model):
    class Meta:
        verbose_name = 'Insurances'
        verbose_name_plural = 'Insurances'

    numer = models.CharField("Number", max_length=200)
    rodzaj_ubezpieczenia = models.CharField("Type of issurance", max_length=200)
    data_od = models.DateTimeField("From date")
    data_do = models.DateTimeField("To date")

    def __str__(self):
        return f"Insurance: {self.id} (issurance_number: {self.numer}, valid_from: {self.data_od}, valid_to: {self.data_do})"


class OcenaPracownika(models.Model):
    class Meta:
        verbose_name = 'Ratrings'
        verbose_name_plural = 'Ratrings'

    ocena = models.IntegerField("Rating", default=0)
    kryteria = models.TextField("Criteria")
    opis = models.CharField("Description", max_length=200)
    data_wydania = models.DateTimeField("Release date")
    data_oceny = models.DateTimeField("Rating date")

    def __str__(self):
        return f"Insurance: {self.id} (issurance_number: {self.numer}, valid_from: {self.data_od}, valid_to: {self.data_do})"


class KartaPracownika(models.Model):
    class Meta:
        verbose_name = 'Employee Cards'
        verbose_name_plural = 'Employee Cards'

    identyfikator = models.CharField("Identificatior", max_length=200)
    opis = models.CharField("Description", max_length=200)
    uwagi = models.CharField("Addontation", max_length=200)
    data = models.DateTimeField("Date")

    def __str__(self):
        return f"Employee Card: {self.id} (identificator: {self.identyfikator}, date: {self.data})"


class Pracownik(models.Model):
    class Meta:
        verbose_name = 'Employees'
        verbose_name_plural = 'Employees'

    imie = models.CharField("First name", max_length=200)
    drugie_imie = models.CharField("Secound name", max_length=200)
    nazwisko = models.CharField("Surname", max_length=200)
    nazwisko_panienskie = models.CharField("Maiden name", max_length=200)
    pesel = models.IntegerField("PESEL", default=0)
    numer_dowodu = models.CharField("Document ID", max_length=200)
    email = models.CharField("Email", max_length=200)
    numer_telefonu = models.IntegerField("Phone number")
    stan_cywilny = models.CharField("Marital status", max_length=200)
    ile_dzieci = models.IntegerField("How many kids?")
    niepelnosprawnosc = models.BooleanField("Is disabled?")
    numer_konta_bankowego = models.IntegerField("Bank account number")
    adres = models.ForeignKey(Adres, null=True, on_delete=SET_NULL, verbose_name="Employee Adress")
    stanowisko = models.ForeignKey(Stanowisko, null=True, on_delete=models.SET_NULL, verbose_name="Employee Position")
    wyksztalcenie = models.ForeignKey(
        Wyksztalcenie, null=True, on_delete=models.SET_NULL, verbose_name="Employee Education"
    )
    ubezpieczenie = models.ForeignKey(
        Ubezpieczenie, null=False, on_delete=models.CASCADE, verbose_name="Employee Issurance"
    )
    ocena_pracownik = models.ForeignKey(
        OcenaPracownika, null=True, on_delete=models.SET_NULL, verbose_name="Employee Rating"
    )
    karta_pracownik = models.ForeignKey(
        KartaPracownika, null=False, on_delete=models.CASCADE, verbose_name="Employee Card"
    )

    def __str__(self):
        return f"Employee: {self.id} (first_name: {self.imie}, surname: {self.nazwisko}, email: {self.email})"


class Szkolenie(models.Model):
    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

    nazwa = models.CharField("Name", max_length=200)
    opis = models.CharField("Description", max_length=200)
    data_rozpoczecia = models.DateTimeField("From date")
    data_zakonczenia = models.DateTimeField("To date")
    ilosc_miejsc = models.IntegerField("How many places?", default=0)
    koszt = models.IntegerField("Cost", default=0)
    zrodlo_finansowania = models.CharField("Source of financing", max_length=200)
    organizator = models.CharField("Organizer", max_length=200)
    miejsce = models.CharField("Place", max_length=200)
    delegacja = models.BooleanField("Is delegation?")
    typ = models.CharField("Type", max_length=200)

    def __str__(self):
        return f"Course: {self.id} (name: {self.nazwa}, date_from: {self.data_rozpoczecia}, date_to: {self.data_zakonczenia})"


class PrzypisaniNaSzkolenie(models.Model):
    class Meta:
        verbose_name = 'Assigned to course'
        verbose_name_plural = 'Assigned to course'

    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")
    szkolenie = models.ForeignKey(Szkolenie, null=False, on_delete=models.CASCADE, verbose_name="Course")
    opis = models.CharField("Description", max_length=200)
    czy_aktywny = models.BooleanField("Is active?")

    def __str__(self):
        return f"Assigned: {self.id} (employee: {self.pracownik}, course: {self.szkolenie})"

class Dzieci(models.Model):
    class Meta:
        verbose_name = 'Kids'
        verbose_name_plural = 'Kids'

    imie = models.CharField("Name", max_length=200)
    nazwisko = models.CharField("Surname", max_length=200)
    wiek = models.IntegerField("Age", default=0)
    pesel = models.IntegerField("PESEL", default=0)
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Kid: {self.id} (name: {self.imie}, surname: {self.nazwisko}, parent: {self.pracownik})"


class Nagrody(models.Model):
    class Meta:
        verbose_name = 'Prices'
        verbose_name_plural = 'Prices'

    opis = models.CharField("Description", max_length=200)
    kryteria = models.TextField("Criteria")
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Price: {self.id} (desc: {self.opis}, employee: {self.pracownik})"


class Zadania(models.Model):
    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Tasks'

    nazwa = models.CharField("Name", max_length=200)
    opis = models.CharField("Description", max_length=200)
    godzinowy_czas_trwania = models.IntegerField("Period count in hours", default=0)
    procentowy_udzial_w_zadaniu = models.IntegerField("Usage in percentage", default=0)
    ilu_pracownikow = models.IntegerField("How many employees", default=0)
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Task: {self.id} (name: {self.nazwa}, desc: {self.opis}, employee: {self.pracownik})"


class Urlop(models.Model):
    class Meta:
        verbose_name = 'Vacations'
        verbose_name_plural = 'Vacations'

    data_rozpoczecia = models.DateTimeField("From date")
    data_wydania = models.DateTimeField("Release date")
    kwota = models.IntegerField("Price", default=0)
    rodzaj = models.CharField("Kind", max_length=200)
    pozostalo = models.IntegerField("Remaining", default=0)
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Vacation: {self.id} (kind: {self.rodzaj}, employee: {self.pracownik}, date_from: {self.data_rozpoczecia})"


class Harmonogram(models.Model):
    class Meta:
        verbose_name = 'Harmonograms'
        verbose_name_plural = 'Harmonograms'

    data = models.DateTimeField("Date")
    godziny = models.IntegerField("Hours", default=0)
    wartosc = models.CharField("Value", max_length=200)
    czy_urlop = models.BooleanField("Is vacation?")
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Harmonogram: {self.id} (date: {self.data}, is_vacation: {self.czy_urlop}, employee: {self.pracownik})"


class ZwolnienieLekarskie(models.Model):
    class Meta:
        verbose_name = 'Sick Leaves'
        verbose_name_plural = 'Sick Leaves'

    opis = models.CharField("Description", max_length=200)
    data_rozpoczecia = models.DateTimeField("From date")
    data_wydania = models.DateTimeField("Release date")
    kod_choroby = models.IntegerField("Sickness code", default=0)
    wystawiajacy = models.CharField("Signed By", max_length=200)
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Sick Leave: {self.id} (desc: {self.opis}, date_from: {self.data_rozpoczecia}, employee: {self.pracownik})"


class Dokument(models.Model):
    class Meta:
        verbose_name = 'Documents'
        verbose_name_plural = 'Documents'

    typ = models.CharField("Type", max_length=200)
    wystawiajacy = models.CharField("Signed By", max_length=200)
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Document: {self.id}, type: {self.typ}, employee: {self.pracownik}, signed_by: {self.wystawiajacy}"


class Umowa(models.Model):
    class Meta:
        verbose_name = 'Contracts'
        verbose_name_plural = 'Contracts'

    data_zawarcia = models.DateTimeField("From date")
    data_rozwiazania = models.DateTimeField("To date")
    wynagrodzenie = models.IntegerField("Payment", default=0)
    opis = models.CharField("Description", max_length=200)
    pracownik = models.ForeignKey(Pracownik, null=False, on_delete=models.CASCADE, verbose_name="Employee")

    def __str__(self):
        return f"Contract: {self.id}, employee: {self.pracownik}, payment: {self.wynagrodzenie}, date_from: {self.data_zawarcia}"

class Premia(models.Model):
    class Meta:
        verbose_name = 'Bonuses'
        verbose_name_plural = 'Bonuses'
        
    typ = models.CharField("Type", max_length=200)
    opis = models.CharField("Description", max_length=200)
    wielkosc = models.IntegerField("Value", default=0)
    umowa = models.ForeignKey(Umowa, null=False, on_delete=models.CASCADE, verbose_name="Contract")

    def __str__(self):
        return f"Bonus: {self.id}, contract: {self.umowa}, value: {self.wielkosc}, desc: {self.opis}"
