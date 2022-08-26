from email.policy import default
from nasbenchbase.models import NASBenchResult
from django.db import models

class NASBenchASRResult(NASBenchResult):
    index = models.CharField(max_length=64, db_index=True)
    genotype = models.CharField(max_length=32, db_index=True)
    test_per = models.JSONField(default=dict)
    # mean_acc = models.FloatField(default=0)

    latency = models.JSONField(default=dict)
    seed = models.IntegerField(default=0)
    params = models.IntegerField(default=0)
    flops = models.IntegerField(default=0)


