# Generated by Django 4.2.11 on 2024-06-10 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0005_rename_nome_local_cidade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='local',
            options={'ordering': ['pais', 'id']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='local',
            name='order',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='order',
        ),
    ]