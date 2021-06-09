# Generated by Django 3.2.3 on 2021-06-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landowners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='landowners',
            name='sale_type',
            field=models.CharField(choices=[('for Rent', 'For Rent'), ('for Lease', 'For Lease')], default='for Rent', max_length=50),
        ),
    ]
