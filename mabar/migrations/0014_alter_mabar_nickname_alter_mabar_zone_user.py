# Generated by Django 4.2.16 on 2024-09-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mabar', '0013_requesthero_type_lane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mabar',
            name='nickname',
            field=models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='Nickname'),
        ),
        migrations.AlterField(
            model_name='mabar',
            name='zone_user',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Zone'),
        ),
    ]
