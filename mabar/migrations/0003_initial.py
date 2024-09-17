# Generated by Django 4.2.16 on 2024-09-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mabar', '0002_remove_mabarsession_player_delete_donation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mabar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donate_name', models.CharField(max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('id_user', models.CharField(max_length=50)),
                ('zone_user', models.CharField(max_length=50)),
                ('jumlah_game', models.IntegerField(default=1)),
                ('catatan', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('antri', 'Dalam Antrian'), ('salah_id', 'Salah ID User'), ('kurang', 'Donasi Kurang'), ('done', 'Done')], default='antri', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_vvip', models.BooleanField(default=False)),
            ],
        ),
    ]
