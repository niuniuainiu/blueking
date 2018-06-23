# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.db import models
class TestModel1(models.Model):
    name = models.CharField(verbose_name=u"组织名字",max_length=64,unique=True)
    foundtime = models.DateTimeField(verbose_name=u"建立时间",auto_now_add=True)
    modifier = models.CharField(verbose_name=u"建立用户", max_length=64)
    if_delete = models.BooleanField(verbose_name=u"是否删除", default=False)

class TestModel2(models.Model):
    name = models.CharField(verbose_name=u"组织名字",max_length=64,unique=True)
    foundtime = models.DateTimeField(verbose_name=u"建立时间",auto_now_add=True)
    modifier = models.CharField(verbose_name=u"建立用户", max_length=64)
    if_delete = models.BooleanField(verbose_name=u"是否删除", default=False)

