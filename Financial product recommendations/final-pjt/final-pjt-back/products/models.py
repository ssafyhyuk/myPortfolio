from django.db import models
from django.conf import settings

# 정기예금 상품
class DepositProducts(models.Model):
    # 은행 (020000), 여신전문 (030200), 저축은행 (030300)
    # 보험 (050000), 금융투자 (060000)
    topFinGrp = models.TextField()
    # 공시제출월 (YYYY-MM)
    dcls_month = models.TextField()
    # 금융회사 코드
    fin_co_no = models.TextField()
    # 금융상품 코드
    fin_prdt_cd = models.TextField()
    # 금융회사 명
    kor_co_nm = models.TextField()
    # 금융 상품명
    fin_prdt_nm = models.TextField()
    # 가입 방법
    join_way = models.TextField()
    # 만기 후 이자율
    mtrt_int = models.TextField()
    # 우대조건
    spcl_cnd = models.TextField()
    # 가입제한 (1. 제한없음, 2. 서민전용, 3. 일부제한)
    join_deny = models.TextField()
    # 가입대상
    join_member = models.TextField()
    # 기타 유의사항
    etc_note = models.TextField()
    # 최고한도
    max_limit = models.TextField(blank=True, null=True)
    # 공시 시작일 (YYYY-MM-DD)
    dcls_strt_day = models.DateField()
    # 공시 종료일 (YYYY-MM-DD)
    dcls_end_day = models.DateField()
    # 금융회사 제출일 (YYYY-MM-DD HH-MM)
    fin_co_subm_day = models.DateTimeField()

    # 가입한 사용자
    deposit_join_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='deposit_join_products', blank=True)
    
# 정기예금 옵션
class DepositOptions(models.Model):
    # 외부키
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    # 금융상품 코드
    fin_prdt_cd = models.TextField()
    # 저축 금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 기간 (단위: 개월)
    save_trm = models.IntegerField()
    # 저축 금리 (소수점 2자리)
    intr_rate = models.FloatField()
    # 최고 우대금리 (소수점 2자리)
    intr_rate2 = models.FloatField()
    

# 적금 상품
class SavingProducts(models.Model):
    # 은행 (020000), 여신전문 (030200), 저축은행 (030300)
    # 보험 (050000), 금융투자 (060000)
    topFinGrp = models.TextField()
    # 공시제출월 (YYYY-MM)
    dcls_month = models.TextField()
    # 금융회사 코드
    fin_co_no = models.TextField()
    # 금융상품 코드
    fin_prdt_cd = models.TextField()
    # 금융회사 명
    kor_co_nm = models.TextField()
    # 금융 상품명
    fin_prdt_nm = models.TextField()
    # 가입 방법
    join_way = models.TextField()
    # 만기 후 이자율
    mtrt_int = models.TextField()
    # 우대조건
    spcl_cnd = models.TextField()
    # 가입제한 (1. 제한없음, 2. 서민전용, 3. 일부제한)
    join_deny = models.TextField()
    # 가입대상
    join_member = models.TextField()
    # 기타 유의사항
    etc_note = models.TextField()
    # 최고한도
    max_limit = models.TextField(blank=True, null=True)
    # 공시 시작일 (YYYY-MM-DD)
    dcls_strt_day = models.DateField()
    # 공시 종료일 (YYYY-MM-DD)
    dcls_end_day = models.DateField()
    # 금융회사 제출일 (YYYY-MM-DD HH-MM)
    fin_co_subm_day = models.DateTimeField()

    # 가입한 사용자
    saving_join_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='saving_join_products', blank=True)

# 적금 옵션
class SavingOptions(models.Model):
    # 외부키
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    # 금융상품 코드
    fin_prdt_cd = models.TextField()
    # 저축 금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 적립 유형명
    rsrv_type_nm = models.TextField()
    # 저축 기간 (단위: 개월)
    save_trm = models.IntegerField()
    # 저축 금리 (소수점 2자리)
    intr_rate = models.FloatField()
    # 최고 우대금리 (소수점 2자리)
    intr_rate2 = models.FloatField()


# 상품 추천 
## 답변
class Answer(models.Model):
    answer = models.TextField()




# # 정기예금 상품
# class DepositProducts(models.Model):
#     # 은행 (020000), 여신전문 (030200), 저축은행 (030300)
#     # 보험 (050000), 금융투자 (060000)
#     topFinGrp = models.TextField()
#     # 공시제출월 (YYYY-MM)
#     dcls_month = models.TextField()
#     # 금융회사 코드
#     fin_co_no = models.TextField()
#     # 금융상품 코드
#     fin_prdt_cd = models.TextField()
#     # 금융회사 명
#     kor_co_nm = models.TextField()
#     # 금융 상품명
#     fin_prdt_nm = models.TextField()
#     # 가입 방법
#     join_way = models.TextField()
#     # 만기 후 이자율
#     mtrt_int = models.TextField()
#     # 우대조건
#     spcl_cnd = models.TextField()
#     # 가입제한 (1. 제한없음, 2. 서민전용, 3. 일부제한)
#     join_deny = models.TextField()
#     # 가입대상
#     join_member = models.TextField()
#     # 기타 유의사항
#     etc_note = models.TextField()
#     # 최고한도
#     max_limit = models.TextField(blank=True, null=True)
#     # 공시 시작일 (YYYY-MM-DD)
#     dcls_strt_day = models.DateField()
#     # 공시 종료일 (YYYY-MM-DD)
#     dcls_end_day = models.DateField()
#     # 금융회사 제출일 (YYYY-MM-DD HH-MM)
#     fin_co_subm_day = models.DateTimeField()

#     # 가입한 사용자
#     deposit_join_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='deposit_join_products', blank=True)