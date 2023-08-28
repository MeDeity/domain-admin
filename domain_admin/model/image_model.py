# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
from datetime import datetime

from peewee import CharField, DateTimeField, BooleanField, AutoField, ForeignKeyField,IntegerField

from domain_admin.config import ADMIN_USERNAME, ADMIN_PASSWORD
from domain_admin.enums.role_enum import RoleEnum
from domain_admin.model.base_model import BaseModel
from domain_admin.utils import bcrypt_util
from domain_admin.model.custom_model import CustomModel


class ImageModel(BaseModel):
    """图片"""
    id = AutoField(primary_key=True)

    # 内容
    description = CharField(unique=True, null=None)

    # 地址
    image_url = CharField(unique=True, null=None)

    # 状态(是否已经使用过)
    status = IntegerField(default=0)

    # 创建时间
    create_time = DateTimeField(default=datetime.now)

    # 更新时间
    update_time = DateTimeField(default=datetime.now)

    # 对应的用户
    customModel = ForeignKeyField(CustomModel)

    class Meta:
        table_name = 'tb_image'

