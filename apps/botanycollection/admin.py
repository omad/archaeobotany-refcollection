from django.contrib import admin
from django.conf import settings
from apps.botanycollection.models import Accession, SeedFeatures, WoodFeatures
from apps.botanycollection.models import AccessionPhoto


class SeedFeaturesInline(admin.StackedInline):
    model = SeedFeatures


class WoodFeaturesInline(admin.StackedInline):
    model = WoodFeatures


class AccessionPhotoInline(admin.StackedInline):
    model = AccessionPhoto


class AccessionAdmin(admin.ModelAdmin):
    model = Accession
    inlines = [
        SeedFeaturesInline, WoodFeaturesInline,
        AccessionPhotoInline
    ]

    list_display = ('uq_accession', 'family', 'genus', 'species', 'common_name', 'material')
#    list_filter = ('family', 'genus')

    fieldsets = (
        (None, {
            'fields': ('uq_accession',
                        'material',
                        'source',
                        'state',
                        'family',
                        'subfam',
                        'tribe',
                        'genus',
                        'species',
                        'author',
        )}),
        ('Other', {
            'fields': (
                'sspna',
                'sspau',
                'varna',
                'varau',
                'cultivar',
                'common_name',
                'biological_synonym',
                'famno',
                'genno',
                'spno',
                'sspno',
                'varno',
                'detna',
                'detdate',
                'collector',
                'collector_serial_no',
                'collection_date',
                'source_number',
                'id_level_flag',
        )}),
        ('Location', {
            'fields': (
                'country',
                'site_name',
                'lat_long',
                'altitude',
                'notes',
                'related_accession',
                'grin__seed_atlas',
                )
        }),
    )

    class Media:
        css = {
            'all': [
                "%scss/django_admin_collapsed_inlines.css" % settings.STATIC_URL,
            ]
        }

        js = [
            "%sjs/jquery-1.8.2.min.js" % settings.STATIC_URL,
            "%sjs/django_admin_collapsed_inlines.js" % settings.STATIC_URL,
        ]


