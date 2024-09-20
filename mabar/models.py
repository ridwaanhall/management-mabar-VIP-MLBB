from django.db import models
from django.utils import timezone

class Mabar(models.Model):
    STATUS_CHOICES = [
        ('antri', 'Antri Mabar'),
        ('antri_scrim', 'Antri Scrim'),
        ('salah_id', 'Salah ID User'),
        ('kurang', 'Donasi Kurang'),
        ('prepare', 'Persiapan'),
        ('in_mabar', 'Sedang Mabar'),
        ('done', 'Selesai'),
    ]

    donate_name = models.CharField(
        max_length=100, 
        verbose_name="Pendonasi"
    )
    nickname = models.CharField(
        default="-",
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Nickname"
    )
    id_user = models.IntegerField(
        verbose_name="ID"
    )
    zone_user = models.IntegerField(
        default=0,
        blank=True, 
        null=True, 
        verbose_name="Zone"
    )
    jumlah_game = models.IntegerField(
        default=1, 
        verbose_name="Jumlah"
    )
    telah_digunakan = models.IntegerField(
        default=0, 
        verbose_name="Digunakan"
    )
    catatan = models.TextField(
        default="Pantau Status mabarmu!",
        blank=True, 
        null=True, 
        verbose_name="Catatan"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='antri', 
        verbose_name="Status"
    )
    date_created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Tanggal Dibuat"
    )
    is_vvip = models.BooleanField(
        default=False, 
        verbose_name="Is VVIP"
    )
    is_done = models.BooleanField(
        default=False, 
        verbose_name="Is Done"
    )

    class Meta:
        verbose_name = 'Mabar Record'
        verbose_name_plural = 'Mabar Records'
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.donate_name} - {self.id_user} {self.nickname}"

class BonusSkin(models.Model):
    mabar = models.ForeignKey(Mabar, on_delete=models.CASCADE, verbose_name="ID User")  # ForeignKey relationship
    hero_digunakan = models.CharField(max_length=100, verbose_name="Hero Digunakan")
    skin_request = models.CharField(max_length=100, verbose_name="Skin Request")
    terkirim = models.BooleanField(default=False, verbose_name="Terkirim")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Dibuat")
    date_terkirim = models.DateTimeField(null=True, blank=True, verbose_name="Tanggal Terkirim")

    class Meta:
        verbose_name = 'Bonus Skin'
        verbose_name_plural = 'Bonus Skins'

    def save(self, *args, **kwargs):
        # Check if terkirim is set to True and date_terkirim is empty
        if self.terkirim and self.date_terkirim is None:
            self.date_terkirim = timezone.now()  # Set current time to date_terkirim
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bonus Skin for {self.mabar.id_user} - {self.hero_digunakan} ({'Terkirim' if self.terkirim else 'Belum Terkirim'})"
    
class RequestHero(models.Model):
    TYPE_REQUEST_CHOICES = [
        ('meta', 'Hero Meta'),
        ('non_meta', 'Hero Non-Meta'),
        ('troll', 'Hero Troll'),
        ('lain', 'Lain-lain')
    ]
    
    TYPE_LANE_CHOICES = [
        ('roam', 'Roam'),
        ('gold', 'Gold Lane'),
        ('jungle', 'Jungle'),
        ('mid', 'Mid Lane'),
        ('exp', 'EXP Lane'),
        ('bebas', 'Bebas'),
    ]

    donate_name = models.CharField(
        max_length=100,
        verbose_name="Pendonasi"
    )
    type_request = models.CharField(
        max_length=10,
        choices=TYPE_REQUEST_CHOICES,
        default='lain',
        verbose_name="Tipe Request"
    )
    hero_name = models.CharField(
        max_length=100,
        verbose_name="Nama Hero"
    )
    type_lane = models.CharField(
        max_length=10,
        choices=TYPE_LANE_CHOICES,
        default='bebas',
        verbose_name="Tipe Lane"
    )
    count = models.IntegerField(
        default=1,
        verbose_name="Jumlah Request"
    )
    catatan = models.TextField(
        default="-",
        blank=True,
        verbose_name="Catatan"
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Sudah Selesai"
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Tanggal Dibuat"
    )

    class Meta:
        verbose_name = 'Request Hero'
        verbose_name_plural = 'Request Heroes'
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.donate_name} - {self.hero_name} ({self.count} request)"
    
    
class KomenAlbum(models.Model):
    donate_name = models.CharField(
        max_length=100,
        verbose_name="Nama Pendonasi"
    )
    id_user_game = models.CharField(
        max_length=50,
        verbose_name="ID User Game"
    )
    zone_user_game = models.CharField(
        max_length=10,
        verbose_name="Zone User Game"
    )
    keterangan = models.TextField(
        blank=True,
        verbose_name="Keterangan"
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Sudah Selesai"
    )
    done_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Selesai Pada"
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Tanggal Dibuat"
    )

    class Meta:
        verbose_name = 'Komen Album'
        verbose_name_plural = 'Komen Albums'
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.donate_name} - {self.id_user_game}"