# Generated by Django 3.1 on 2020-09-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_auto_20200904_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='offersad',
            name='contact_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]