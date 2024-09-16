import datetime
import csv
from io import BytesIO
import openpyxl
from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
from .models import Mabar, BonusSkin, RequestHero
from django.utils.timezone import localtime

class DateRangeFilter(admin.SimpleListFilter):
    title = 'Date Created'
    parameter_name = 'date_created_range'

    def lookups(self, request, model_admin):
        return (
            ('last_7_days', 'Last 7 days'),
            ('last_30_days', 'Last 30 days'),
            ('this_month', 'This month'),
            ('last_month', 'Last month'),
        )

    def queryset(self, request, queryset):
        from datetime import timedelta
        from django.utils import timezone

        now = timezone.now()
        if self.value() == 'last_7_days':
            start_date = now - timedelta(days=7)
        elif self.value() == 'last_30_days':
            start_date = now - timedelta(days=30)
        elif self.value() == 'this_month':
            start_date = now.replace(day=1)
        elif self.value() == 'last_month':
            last_month = now.month - 1 if now.month > 1 else 12
            year = now.year if now.month > 1 else now.year - 1
            start_date = timezone.make_aware(datetime.date(year, last_month, 1))
            end_date = timezone.make_aware(datetime.date(year, last_month + 1, 1))
            return queryset.filter(date_created__range=(start_date, end_date))
        else:
            return queryset

        return queryset.filter(date_created__gte=start_date)

@admin.register(Mabar)
class MabarAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'donate_name', 'jumlah_game', 'telah_digunakan', 'nickname', 'id_user', 'zone_user', 'colored_status', 'catatan', 'is_vvip', 'is_done']
    list_filter = ['status', 'is_vvip', 'is_done', 'date_created', DateRangeFilter]
    search_fields = ['donate_name', 'id_user']
    readonly_fields = ['date_created']
    ordering = ['date_created']
    list_per_page = 25  # Pagination: Display 25 records per page
    actions = ['mark_as_salah_id', 'mark_as_kurang', 'mark_as_prepare', 'mark_as_in_mabar', 
               'mark_as_done', 'export_as_csv', 'export_as_excel']

    def colored_status(self, obj):
        color = {
            'antri': 'orange',
            'prepare': 'blue',
            'in_mabar': 'lightgreen',
            'salah_id': 'red',
            'kurang': 'red',
            'done': 'green',
        }.get(obj.status, 'black')
        return format_html(f'<span style="color: {color};">{obj.get_status_display()}</span>')
    
    colored_status.short_description = 'Status'

    fieldsets = (
        ('Data Donasi', {
            'fields': ('donate_name', 'jumlah_game', 'telah_digunakan')
        }),
        ('Data Player', {
            'fields': ('nickname', 'id_user', 'zone_user')
        }),
        ('Status dan Tanggal', {
            'fields': ('status', 'catatan', 'is_vvip', 'is_done', 'date_created'),
        }),
    )

    # Actions
    def mark_as_salah_id(self, request, queryset):
        updated = queryset.update(status='salah_id', catatan='Kirim ulang ID-mu!', is_done=False)
        self.message_user(request, f'{updated} mabar record(s) marked as Salah ID User.')
    mark_as_salah_id.short_description = 'Mark selected records as Salah ID User'

    def mark_as_kurang(self, request, queryset):
        updated = queryset.update(status='kurang', catatan='Whoopp! Danamu kurang!', is_done=False)
        self.message_user(request, f'{updated} mabar record(s) marked as Donasi Kurang.')
    mark_as_kurang.short_description = 'Mark selected records as Donasi Kurang'

    def mark_as_prepare(self, request, queryset):
        updated = queryset.update(status='prepare', catatan='Login dan bersiap!', is_done=False)
        self.message_user(request, f'{updated} mabar record(s) marked as Persiapan.')
    mark_as_prepare.short_description = 'Mark selected records as Persiapan'
    
    def mark_as_in_mabar(self, request, queryset):
        updated_count = 0
        for obj in queryset:
            # Increase the 'telah_digunakan' field value by 1
            obj.telah_digunakan = (obj.telah_digunakan or 0) + 1
            
            # Check if 'telah_digunakan' equals 'jumlah_game'
            if obj.telah_digunakan >= obj.jumlah_game:
                obj.status = 'done'
                obj.catatan='Mabar Selesai. Terima Kasih :)'
                obj.is_done = True  # Mark as done if 'telah_digunakan' equals or exceeds 'jumlah_game'
            else:
                obj.status = 'in_mabar'
                obj.catatan=f'Telah digunakan {obj.telah_digunakan} dari {obj.jumlah_game} game!'
                obj.is_done = False

            obj.save()  # Save the updated object
            updated_count += 1

        self.message_user(request, f'{updated_count} mabar record(s) marked as Sedang Mabar or Done as applicable.')
    mark_as_in_mabar.short_description = 'Mark selected records as Sedang Mabar or Done if "telah_digunakan" equals "jumlah_game"'

    def mark_as_done(self, request, queryset):
        updated = queryset.update(status='done', catatan='Mabar Selesai. Terima Kasih :)', is_done=True)
        self.message_user(request, f'{updated} mabar record(s) marked as done.')
    mark_as_done.short_description = 'Mark selected records as Done'
    
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected as CSV"

    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        # Create a workbook and a worksheet
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = meta.verbose_name_plural

        # Write the header row
        ws.append(field_names)

        for obj in queryset:
            row = []
            for field in field_names:
                value = getattr(obj, field)
                if isinstance(value, datetime.datetime):
                    # Convert timezone-aware datetime to naive datetime
                    if value.tzinfo is not None:
                        value = localtime(value).replace(tzinfo=None)
                row.append(value)
            ws.append(row)
        
        # Save the workbook to a BytesIO object
        output = BytesIO()
        wb.save(output)
        output.seek(0)
        
        # Create an HTTP response with the Excel file
        response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={meta.verbose_name_plural}.xlsx'
        
        return response

    export_as_excel.short_description = "Export Selected as Excel"

@admin.register(BonusSkin)
class BonusSkinAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'mabar', 'hero_digunakan', 'skin_request', 'terkirim', 'date_terkirim']
    list_filter = ['terkirim']
    search_fields = ['mabar__id_user', 'hero_digunakan', 'skin_request']
    
@admin.register(RequestHero)
class RequestHeroAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'donate_name', 'type_request', 'hero_name', 'type_lane', 'count', 'is_done', 'catatan')
    list_filter = ('type_request', 'is_done')
    search_fields = ('donate_name', 'hero_name')