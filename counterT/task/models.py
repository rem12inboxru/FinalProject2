from tortoise.models import Model
from tortoise import fields


class Data(Model):
    id = fields.IntField(pk=True)
    ticker = fields.CharField(max_length=5)
    lastprice = fields.DecimalField(max_digits=2, decimal_places=5)
    timeframe = fields.IntField()
    timeevent = fields.DatetimeField(auto_now_add=True)



# Create your models here.
