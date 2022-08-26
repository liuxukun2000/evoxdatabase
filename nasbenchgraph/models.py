from email.policy import default
from nasbenchbase.models import NASBenchResult
from django.db import models

class NASBenchGraphResult(NASBenchResult):
    index = models.IntegerField(db_index=True)
    genotype = models.CharField(max_length=32, db_index=True)
    valid_perf = models.JSONField(default=dict)
    perf = models.JSONField(default=dict)
    # mean_acc = models.FloatField(default=0)
    latency = models.JSONField(default=dict)
    para = models.JSONField(default=dict)
