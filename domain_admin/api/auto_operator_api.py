# -*- coding: utf-8 -*-

from flask import request

from domain_admin.service import auto_operate_service


def handle():
    auto_operate_service.handle()
    return "流程处理完成"