# Generated by Django 4.2.11 on 2024-06-11 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0012_cor_local_cor_tag_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zanine.cor'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='cor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zanine.cor'),
        ),
    ]