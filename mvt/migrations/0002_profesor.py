# Generated by Django 4.1.2 on 2022-11-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
    ]