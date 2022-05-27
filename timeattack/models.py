from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "user"

    def __init__(self, email, password):
        # 이메일
        self.email = models.CharField(max_length=20, null=False)
        # 비밀번호
        self.password = models.CharField(max_length=256, null=False)