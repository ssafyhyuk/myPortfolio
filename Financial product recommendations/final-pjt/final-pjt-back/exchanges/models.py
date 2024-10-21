from django.db import models

# 환율
class Exchanges(models.Model):
    # 통화코드
    cur_unit = models.TextField()
    # 국가/통화명
    cur_nm = models.TextField()
    # 매매 기준율
    deal_bas_r = models.FloatField()
    