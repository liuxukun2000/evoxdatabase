from email.policy import default
from nasbenchbase.models import NASBenchResult
from django.db import models

class NASHPOBench2Result(NASBenchResult):
    index = models.IntegerField(db_index=True)
    phenotype = models.CharField(max_length=256)
    genotype = models.CharField(max_length=256, db_index=True)
    batch_size = models.IntegerField(default=0)
    lr = models.FloatField(default=0)
    acc = models.FloatField(default=0)
    cost = models.FloatField(default=0)


