# Generated by Django 4.2.2 on 2023-06-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='competitions')),
                ('name', models.CharField(max_length=150)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
