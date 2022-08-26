from django.contrib import admin

import nasbenchgraph


@admin.register(nasbenchgraph.models.NASBenchGraphResult)
class NASBenchGraphAdmin(admin.ModelAdmin):
    list_display = ["id", "index", 'genotype']
    search_fields = ["index"]