# Generated by Django 3.1.7 on 2021-03-21 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Architect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Rc', models.CharField(blank=True, max_length=255, null=True)),
                ('ICE', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('ville', models.CharField(max_length=255)),
                ('pays', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
