# Generated by Django 3.1 on 2022-01-18 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment_and_payments', '0010_auto_20220116_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='swiadectwopracy',
            name='imie',
            field=models.CharField(default=0, max_length=100, verbose_name='Employee name'),
        ),
        migrations.AddField(
            model_name='swiadectwopracy',
            name='nazwisko',
            field=models.CharField(default=0, max_length=100, verbose_name='Employee last name'),
        ),
        migrations.AlterField(
            model_name='harmonogram',
            name='data',
            field=models.DateTimeField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='kartapracownika',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='nagrody',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='ocenapracownika',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='premia',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='przypisaninaszkolenie',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='stanowisko',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='swiadectwopracy',
            name='data_zwolnienia',
            field=models.DateTimeField(verbose_name='Release date'),
        ),
        migrations.AlterField(
            model_name='swiadectwopracy',
            name='pracownik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employment_and_payments.pracownik'),
        ),
        migrations.AlterField(
            model_name='szkolenie',
            name='data_rozpoczecia',
            field=models.DateTimeField(verbose_name='From date'),
        ),
        migrations.AlterField(
            model_name='szkolenie',
            name='data_zakonczenia',
            field=models.DateTimeField(verbose_name='To date'),
        ),
        migrations.AlterField(
            model_name='szkolenie',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='ubezpieczenie',
            name='data_do',
            field=models.DateTimeField(verbose_name='To date'),
        ),
        migrations.AlterField(
            model_name='ubezpieczenie',
            name='data_od',
            field=models.DateTimeField(verbose_name='From date'),
        ),
        migrations.AlterField(
            model_name='umowa',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='urlop',
            name='data_rozpoczecia',
            field=models.DateTimeField(verbose_name='From date'),
        ),
        migrations.AlterField(
            model_name='urlop',
            name='data_wydania',
            field=models.DateTimeField(verbose_name='Release date'),
        ),
        migrations.AlterField(
            model_name='wyksztalcenie',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='zadania',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='zwolnienielekarskie',
            name='data_rozpoczecia',
            field=models.DateTimeField(verbose_name='From date'),
        ),
        migrations.AlterField(
            model_name='zwolnienielekarskie',
            name='opis',
            field=models.CharField(blank=True, max_length=200, verbose_name='Description'),
        ),
    ]
