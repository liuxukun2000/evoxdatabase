from django.contrib import admin

import nashpobench2


@admin.register(nashpobench2.models.NASHPOBench2Result)
class NASHPOBench2Admin(admin.ModelAdmin):
    list_display = ["id", "index", 'genotype']
    search_fields = ["index"]