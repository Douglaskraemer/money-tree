# Generated by Django 3.1 on 2020-09-08 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor total')),
                ('vencimento', models.DateField()),
                ('opcoes', models.BooleanField(default=False, verbose_name='Opções')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.categoria')),
            ],
        ),
    ]
