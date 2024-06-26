# Generated by Django 4.2.11 on 2024-05-03 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import links.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.DateTimeField(auto_now_add=True)),
                ('tag', models.SlugField(help_text='only letters, numbers, underscores or hyphens', max_length=200, unique=True)),
                ('u0', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.CreateModel(
            name='Ps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d0', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(upload_to=links.models.print_filepath)),
                ('visivel', models.BooleanField(default=True)),
                ('titulo', models.CharField(blank=True, help_text='se em branco, um titulo vai ser gerado a partir do link', max_length=400)),
                ('link', models.URLField(max_length=400)),
                ('ativo', models.BooleanField(default=True)),
                ('link2', models.URLField(blank=True, help_text='link do internet archive, caso o link não exista mais', max_length=400)),
                ('obs', models.TextField(blank=True)),
                ('tags', models.ManyToManyField(to='links.tg')),
                ('u0', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
