# Django

**安装django**

```
pip install django==2.1.12
pip install djangorestframework==3.10.0
```

**创建项目**

```
django-admin startproject django_app
```

**运行**

```
python manage.py runserver
```

**创建模块**

```
python manage.py startapp users apps/modules/users
python manage.py startapp companies apps/modules/companies
```

**配置数据库**

```
//配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':32768
    }
}
```

**安装数据库驱动**

```
pip install psycopg2==2.8.6
```

**迁移到数据库**

```
python manage.py migrate
```

**创建超级管理员**

```
python manage.py createsuperuser
```

**创建基本模型** 

```python
#django_app\apps\utils\base_model.py

from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

```

**创建公司模型**

```python
#django_app\apps\modules\companies\models.py
from django.db import models
from apps.utils.base_model import BaseModel

class Companies(BaseModel):
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True,blank=True)
    bc_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "companies"
        verbose_name = 'companies'
        verbose_name_plural = 'companies'
    def __str__(self):
        return self.name



```

**创建user模型**

```python
#django_app\apps\modules\users\models.py

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
```

**注册模型**

```python
#django_app\django_app\settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
    'apps.modules',
    'apps.modules.companies',
    'apps.modules.users'
]

```

**构建迁移文件**

```
python manage.py makemigrations
```

**迁移到数据库**

```
python manage.py migrate
```

**在admin.py中注册两个模块**

```
#Users 取消User，Group的显示
from django.contrib import admin
from .models import Users
from django.contrib.auth.models import User, Group

admin.site.register(Users)
admin.site.unregister(User)
admin.site.unregister(Group)

#Companies
from django.contrib import admin
from .models import Companies

admin.site.register(Companies)

```

python培训第三讲 1:00:00