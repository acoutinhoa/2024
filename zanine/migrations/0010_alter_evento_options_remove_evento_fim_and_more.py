# Generated by Django 4.2.11 on 2024-06-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zanine', '0009_evento_d0_evento_d1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['cidade', 'd0']},
        ),
        migrations.RemoveField(
            model_name='evento',
            name='fim',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='inicio',
        ),
        migrations.AlterField(
            model_name='evento',
            name='d0',
            field=models.CharField(help_text='definir como aaaa/mm/dd, aaaa/mm ou aaaa <br>>>> data do inicio de um periodo <br>>>> ou data de evento pontual', max_length=10),
        ),
        migrations.AlterField(
            model_name='evento',
            name='d1',
            field=models.CharField(blank=True, help_text='definir como aaaa/mm/dd, aaaa/mm ou aaaa <br>>>> data do fim de um periodo <br>>>> deixar em branco caso seja um evento pontual', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='pais',
            field=models.CharField(choices=[('BR', 'Brasil'), ('FR', 'França'), ('CH', 'Suíça')], default='BR', max_length=2),
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
