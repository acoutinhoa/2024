# Generated by Django 4.2.11 on 2024-06-11 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0011_alter_evento_options_rename_d1_evento_fim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('rgb', models.CharField(help_text='>>> separar cores com espaço <br>rgb = 0-255 0-255 0-255 <br>cinza = 0-255 <br>', max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='local',
            name='cor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zanine.cor'),
        ),
        migrations.AddField(
            model_name='tag',
            name='cor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zanine.cor'),
        ),
    ]
