# Generated by Django 3.1 on 2020-09-29 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_despesa_opcoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='opcoes',
            field=models.CharField(choices=[(1, 'Sim'), (2, 'Não')], default=2, max_length=10, verbose_name='Pago'),
        ),
    ]
