from django.db import models

class StatusCompany(models.IntegerChoices):
    ATIVO = 1, "Ativo"
    INATIVO = 2, "Inativo"