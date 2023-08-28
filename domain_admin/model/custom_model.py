# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
from datetime import datetime

from peewee import CharField, DateTimeField, BooleanField, AutoField, IntegerField

from domain_admin.config import ADMIN_USERNAME, ADMIN_PASSWORD
from domain_admin.enums.role_enum import RoleEnum
from domain_admin.model.base_model import BaseModel
from domain_admin.utils import bcrypt_util


class CustomModel(BaseModel):
    """客户"""
    id = AutoField(primary_key=True)

    # 用户名
    username = CharField(unique=True, null=None)

    # 密码
    password = CharField()

    # 头像
    avatar_url = CharField(null=None, default='')

    # 账号状态
    status = BooleanField(default=True)

    # 创建时间
    create_time = DateTimeField(default=datetime.now)

    # 更新时间
    update_time = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'tb_custom'

