# Generated by Django 4.2.11 on 2024-06-11 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0013_alter_local_cor_alter_tag_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zanine.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]