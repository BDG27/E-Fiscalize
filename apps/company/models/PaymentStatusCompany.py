from django.db import models

class PaymentStatusCompany(models.IntegerChoices):
    PAGO = 1, "Pago"
    AGUARDANDO_PAGAMENTO = 2, "Aguardando Pagamento"