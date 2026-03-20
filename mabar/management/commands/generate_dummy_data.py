from django.core.management.base import BaseCommand
from mabar.models import Mabar, BonusSkin, RequestHero, KomenAlbum
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Generate dummy data for all models in mabar app.'

    def handle(self, *args, **options):
        # Clear existing data
        Mabar.objects.all().delete()
        BonusSkin.objects.all().delete()
        RequestHero.objects.all().delete()
        KomenAlbum.objects.all().delete()

        # Create Mabar records
        mabar_objs = []
        for i in range(10):
            mabar = Mabar.objects.create(
                donate_name=f"User {i+1}",
                nickname=f"Nick{i+1}",
                id_user=10000 + i,
                zone_user=2000 + i,
                jumlah_game=random.randint(1, 5),
                telah_digunakan=random.randint(0, 5),
                catatan="Dummy catatan",
                status=random.choice([c[0] for c in Mabar.STATUS_CHOICES]),
                is_vvip=random.choice([True, False]),
                is_done=random.choice([True, False]),
            )
            mabar_objs.append(mabar)

        # Create BonusSkin records
        for i in range(5):
            BonusSkin.objects.create(
                mabar=random.choice(mabar_objs),
                hero_digunakan=f"Hero{i+1}",
                skin_request=f"Skin{i+1}",
                terkirim=random.choice([True, False]),
                date_terkirim=timezone.now() if random.choice([True, False]) else None
            )

        # Create RequestHero records
        for i in range(7):
            RequestHero.objects.create(
                donate_name=f"User {i+1}",
                type_request=random.choice([c[0] for c in RequestHero.TYPE_REQUEST_CHOICES]),
                hero_name=f"HeroReq{i+1}",
                type_lane=random.choice([c[0] for c in RequestHero.TYPE_LANE_CHOICES]),
                count=random.randint(1, 3),
                catatan="Dummy request catatan",
                is_done=random.choice([True, False]),
            )

        # Create KomenAlbum records
        for i in range(5):
            KomenAlbum.objects.create(
                donate_name=f"User {i+1}",
                id_user_game=f"{10000 + i}",
                zone_user_game=f"{2000 + i}",
                keterangan="Dummy komen catatan"
            )

        self.stdout.write(self.style.SUCCESS('Dummy data generated for all models.'))
