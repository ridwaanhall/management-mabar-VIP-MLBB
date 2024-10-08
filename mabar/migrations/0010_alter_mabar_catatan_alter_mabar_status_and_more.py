# Generated by Django 4.2.16 on 2024-09-16 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mabar', '0009_alter_mabar_options_mabar_telah_digunakan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mabar',
            name='catatan',
            field=models.TextField(blank=True, default='Dalam antrian... Harap selalu pantau update status dan catatan, yaa!!', null=True, verbose_name='Catatan'),
        ),
        migrations.AlterField(
            model_name='mabar',
            name='status',
            field=models.CharField(choices=[('antri', 'Dalam Antrian'), ('salah_id', 'Salah ID User'), ('kurang', 'Donasi Kurang'), ('prepare', 'Persiapan'), ('in_mabar', 'Sedang Mabar'), ('done', 'Selesai')], default='antri', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='mabar',
            name='telah_digunakan',
            field=models.IntegerField(default=0, verbose_name='Digunakan'),
        ),
        migrations.CreateModel(
            name='BonusSkin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_digunakan', models.CharField(max_length=100, verbose_name='Hero Digunakan')),
                ('skin_request', models.CharField(max_length=100, verbose_name='Skin Request')),
                ('terkirim', models.BooleanField(default=False, verbose_name='Terkirim')),
                ('mabar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mabar.mabar', verbose_name='ID User')),
            ],
            options={
                'verbose_name': 'Bonus Skin',
                'verbose_name_plural': 'Bonus Skins',
            },
        ),
    ]
