# Generated by Django 3.1 on 2022-01-16 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employment_and_payments', '0007_auto_20220116_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='swiadectwopracy',
            name='pracownik',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employment_and_payments.pracownik'),
            preserve_default=False,
        ),
    ]