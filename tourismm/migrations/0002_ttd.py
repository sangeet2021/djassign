# Generated by Django 3.0.2 on 2021-04-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourismm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ttd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
