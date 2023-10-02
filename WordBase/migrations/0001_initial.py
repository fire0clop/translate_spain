# Generated by Django 4.2.5 on 2023-10-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russian_word', models.CharField(max_length=100, verbose_name='Russian Word')),
                ('spanish_word', models.CharField(max_length=100, verbose_name='Spanish Word')),
            ],
            options={
                'verbose_name': 'Translation',
                'verbose_name_plural': 'Translations',
            },
        ),
    ]
