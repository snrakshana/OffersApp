# Generated by Django 3.1 on 2020-09-02 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offersad',
            name='date_published',
            field=models.DateField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
