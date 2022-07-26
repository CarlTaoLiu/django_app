from enum import IntEnum
from django.db import models
from apps.modules.companies.models import Companies
from apps.utils.base_model import BaseModel

class UserEnum(IntEnum):
    ADMIN = 0
    SENIOR_BUYER = 1
    JUNIOR_BUYER = 2
    SUPER_ADMIN = 3

    @classmethod
    def choices(cls):
        return tuple(((i.value, i.name) for i in cls))


class Users(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bc_id = models.IntegerField(null=True, blank=True)
    company_id = models.ForeignKey(Companies,related_name="company_user",on_delete=models.CASCADE)
    role = models.SmallIntegerField(choices=UserEnum.choices())

    class Meta:
        db_table = "users"
        verbose_name = 'users'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.first_name+" "+self.last_name