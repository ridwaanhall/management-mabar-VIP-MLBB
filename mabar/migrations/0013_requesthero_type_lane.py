# Generated by Django 4.2.16 on 2024-09-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mabar', '0012_requesthero'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesthero',
            name='type_lane',
            field=models.CharField(choices=[('roam', 'Roam'), ('gold', 'Gold Lane'), ('jungle', 'Jungle'), ('mid', 'Mid Lane'), ('exp', 'EXP Lane'), ('bebas', 'Bebas')], default='bebas', max_length=10, verbose_name='Tipe Lane'),
        ),
    ]
