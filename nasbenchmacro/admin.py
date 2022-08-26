from django.contrib import admin

import nasbenchmacro


@admin.register(nasbenchmacro.models.NASBenchMacroResult)
class NASBenchMacroAdmin(admin.ModelAdmin):
    list_display = ["id", "index", 'genotype']
    search_fields = ["index"]