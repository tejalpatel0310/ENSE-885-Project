# Generated by Django 3.2.3 on 2021-06-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landownerlistingsmodel',
            name='contact_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
