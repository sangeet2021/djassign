# Generated by Django 3.0.2 on 2021-04-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismm', '0017_auto_20210419_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Package',
            field=models.CharField(choices=[('Family Package', 'Family Package'), ('Solo Package', 'Solo Package'), ('Complete Guided Package', 'Complete Guided Package')], default='Family Package', max_length=100),
        ),
        migrations.AlterField(
            model_name='hotelbook',
            name='Hotel',
            field=models.CharField(choices=[('HeavenView Hotel', 'HeavenView Hotel'), ('NepStay', 'NepStay')], default='NepStay', max_length=100),
        ),
    ]
