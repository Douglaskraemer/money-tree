# Generated by Django 3.1 on 2020-09-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_despesa_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='opcoes',
            field=models.CharField(choices=[('1', 'Sim '), ('2', 'Não')], default=1, max_length=10, verbose_name='Pago'),
            preserve_default=False,
        ),
    ]
