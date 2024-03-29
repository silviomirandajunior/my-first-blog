# Generated by Django 2.2.24 on 2021-08-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrabalheConosco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='professor',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='disciplina',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='sobrenome',
        ),
        migrations.AddField(
            model_name='professor',
            name='telefone',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
