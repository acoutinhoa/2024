# Generated by Django 4.2.11 on 2024-06-11 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0010_alter_evento_options_remove_evento_fim_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['cidade', 'inicio']},
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='d1',
            new_name='fim',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='d0',
            new_name='inicio',
        ),
    ]