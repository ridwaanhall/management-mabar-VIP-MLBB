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

        # --- Mabar: All combinations of status, is_vvip, is_done ---
        statuses = [c[0] for c in Mabar.STATUS_CHOICES]
        vvip_options = [True, False]
        done_options = [True, False]
        mabar_objs = []
        idx = 1
        # Systematically create all combinations (7*2*2 = 28)
        for status in statuses:
            for is_vvip in vvip_options:
                for is_done in done_options:
                    mabar = Mabar.objects.create(
                        donate_name=f"User {idx}",
                        nickname=f"Nick{idx}",
                        id_user=10000 + idx,
                        zone_user=2000 + idx,
                        jumlah_game=(idx % 5) + 1,
                        telah_digunakan=(idx % 3),
                        catatan=f"Catatan status {status}, vvip {is_vvip}, done {is_done}",
                        status=status,
                        is_vvip=is_vvip,
                        is_done=is_done,
                    )
                    mabar_objs.append(mabar)
                    idx += 1
        # Add more random records to reach ~60
        for i in range(60 - len(mabar_objs)):
            mabar = Mabar.objects.create(
                donate_name=f"User {idx}",
                nickname=f"Nick{idx}",
                id_user=10000 + idx,
                zone_user=2000 + idx,
                jumlah_game=random.randint(1, 5),
                telah_digunakan=random.randint(0, 5),
                catatan="Random dummy catatan",
                status=random.choice(statuses),
                is_vvip=random.choice(vvip_options),
                is_done=random.choice(done_options),
            )
            mabar_objs.append(mabar)
            idx += 1

        # --- BonusSkin: All combinations of terkirim, plus variety of heroes/skins ---
        hero_names = [f"Hero{i+1}" for i in range(10)]
        skin_names = [f"Skin{i+1}" for i in range(10)]
        terkirim_options = [True, False]
        idx = 1
        for terkirim in terkirim_options:
            for hero in hero_names:
                for skin in skin_names[:3]:
                    BonusSkin.objects.create(
                        mabar=random.choice(mabar_objs),
                        hero_digunakan=hero,
                        skin_request=skin,
                        terkirim=terkirim,
                        date_terkirim=timezone.now() if terkirim else None
                    )
                    idx += 1
        # Add more random BonusSkin
        for i in range(20):
            BonusSkin.objects.create(
                mabar=random.choice(mabar_objs),
                hero_digunakan=random.choice(hero_names),
                skin_request=random.choice(skin_names),
                terkirim=random.choice(terkirim_options),
                date_terkirim=timezone.now() if random.choice(terkirim_options) else None
            )

        # --- RequestHero: All combinations of type_request, type_lane, is_done ---
        type_requests = [c[0] for c in RequestHero.TYPE_REQUEST_CHOICES]
        type_lanes = [c[0] for c in RequestHero.TYPE_LANE_CHOICES]
        idx = 1
        for type_request in type_requests:
            for type_lane in type_lanes:
                for is_done in done_options:
                    RequestHero.objects.create(
                        donate_name=f"UserReq{idx}",
                        type_request=type_request,
                        hero_name=f"HeroReq{idx}",
                        type_lane=type_lane,
                        count=(idx % 3) + 1,
                        catatan=f"Request {type_request} {type_lane} done {is_done}",
                        is_done=is_done,
                    )
                    idx += 1
        # Add more random RequestHero
        for i in range(30):
            RequestHero.objects.create(
                donate_name=f"UserReq{idx}",
                type_request=random.choice(type_requests),
                hero_name=f"HeroReq{idx}",
                type_lane=random.choice(type_lanes),
                count=random.randint(1, 3),
                catatan="Random request catatan",
                is_done=random.choice(done_options),
            )
            idx += 1

        # --- KomenAlbum: All combinations of is_done, plus variety ---
        idx = 1
        for is_done in done_options:
            for i in range(10):
                KomenAlbum.objects.create(
                    donate_name=f"KomenUser{idx}",
                    id_user_game=f"{11000 + idx}",
                    zone_user_game=f"{2100 + idx}",
                    keterangan=f"Komen {i} done {is_done}",
                    is_done=is_done,
                    done_at=timezone.now() if is_done else None
                )
                idx += 1
        # Add more random KomenAlbum
        for i in range(20):
            is_done = random.choice(done_options)
            KomenAlbum.objects.create(
                donate_name=f"KomenUser{idx}",
                id_user_game=f"{11000 + idx}",
                zone_user_game=f"{2100 + idx}",
                keterangan="Random komen catatan",
                is_done=is_done,
                done_at=timezone.now() if is_done else None
            )
            idx += 1

        self.stdout.write(self.style.SUCCESS('Comprehensive dummy data generated for all models.'))
