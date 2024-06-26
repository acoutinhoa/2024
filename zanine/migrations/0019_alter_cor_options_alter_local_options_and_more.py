# Generated by Django 4.2.11 on 2024-06-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0018_rename_variaveis_variavel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name_plural': 'cores'},
        ),
        migrations.AlterModelOptions(
            name='local',
            options={'ordering': ['id'], 'verbose_name_plural': 'locais'},
        ),
        migrations.AlterModelOptions(
            name='variavel',
            options={'verbose_name_plural': 'variaveis'},
        ),
        migrations.AddField(
            model_name='evento',
            name='visivel',
            field=models.BooleanField(default=True, help_text='define se este evento é visivel na timeline'),
        ),
    ]
