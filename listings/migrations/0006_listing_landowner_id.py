# Generated by Django 3.2.3 on 2021-06-08 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landowners', '0005_auto_20210608_1809'),
        ('listings', '0005_alter_listing_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='landowner_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='landowners.landownerlistingsmodel'),
        ),
    ]
