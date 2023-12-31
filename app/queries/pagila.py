from .base import BaseController
from marshmallow import fields, Schema
from sqlalchemy.sql import select
from sqlalchemy import Date

    
class RentalsList(BaseController):

    class ParamSchema(Schema):
        start_date = fields.Date(allow_none=True)
        end_date = fields.Date(allow_none=True)
    
    def get_df(self):
        return self.get_pagila_db_store().sqltodf(
            "SELECT * FROM rental ORDER BY rental_id ASC"
        )
    
class PaymentsList(BaseController):
    class ParamSchema(Schema):
        start_date = fields.Date(allow_none=True)
        end_date = fields.Date(allow_none=True)

    def get_df(self):
        payments = self.get_pagila_db_store().tables['payment']
        q = select(payments)
        if self.params:
            if self.params.get("start_date"):
                q = q.where(payments.c.payment_date >= self.params["start_date"])
            if self.params.get("end_date"):
                q = q.where(payments.c.payment_date <= self.params["end_date"])
        q = q.order_by(payments.c.payment_date.asc())
        return self.get_pagila_db_store().sqltodf(
            q.limit(100)
        )
