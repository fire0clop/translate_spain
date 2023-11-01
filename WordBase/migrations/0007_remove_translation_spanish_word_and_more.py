# Generated by Django 4.2.5 on 2023-10-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordBase', '0006_translation_progress_alter_translation_statys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='spanish_word',
        ),
        migrations.AddField(
            model_name='translation',
            name='english_word',
            field=models.CharField(default=1, max_length=100, verbose_name='English Word'),
            preserve_default=False,
        ),
    ]
