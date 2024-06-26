# Generated by Django 4.2.11 on 2024-06-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0014_alter_evento_tag_alter_tag_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variaveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.IntegerField(default=1918, help_text='ano <br> início da timeline')),
                ('fim', models.IntegerField(default=2050, help_text='ano <br> fim da timeline')),
                ('coluna', models.IntegerField(default=30, help_text='somente números <br> largura (em px) da coluna de cada ano da timeline ')),
                ('linha', models.IntegerField(default=30, help_text='somente números <br> altura (em px) da linha de cada evento da timeline ')),
                ('text_size', models.IntegerField(default=12, help_text='somente números <br> tamanho (em px) do texto')),
                ('data_size', models.IntegerField(default=10, help_text='somente números <br> tamanho (em px) do texto da data da timeline')),
                ('padrao', models.BooleanField(default=True, help_text='define essas variaveis como padrão para o desenho')),
            ],
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['inicio']},
        ),
    ]
