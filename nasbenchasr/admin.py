from django.contrib import admin

import nasbenchasr


@admin.register(nasbenchasr.models.NASBenchASRResult)
class NASBenchASRAdmin(admin.ModelAdmin):
    list_display = ["id", "index", 'genotype']
    search_fields = ["index"]
# Register your models here.
