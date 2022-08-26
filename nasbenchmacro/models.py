from nasbenchbase.models import NASBenchResult
from django.db import models

class NASBenchMacroResult(NASBenchResult):
    index = models.IntegerField(db_index=True)
    genotype = models.CharField(max_length=32, db_index=True)
    test_acc = models.JSONField(default=dict)
    mean_acc = models.FloatField(default=0)
    std = models.FloatField(default=0)
    params = models.IntegerField(default=0)
    flops = models.IntegerField(default=0)


