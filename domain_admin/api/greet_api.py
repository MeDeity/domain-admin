
from flask import request, g
from domain_admin.model.greet_model import GreetModel
from domain_admin.utils import datetime_util, domain_util

def add_greet():
    """
    添加Greet
    :return:
    """

    content = request.json['content']


    data = {
        # 基本信息
        'content': content
    }

    row = GreetModel.create(**data)

    return {'id': row.id}

def update_greet_by_id():
    """
    更新数据
    """
    data = request.json
    greet_id = request.json['id']

    data['update_time'] = datetime_util.get_datetime()
    data['content'] = data.get('content') or ''

    before_domain_row = GreetModel.get_by_id(greet_id)

    GreetModel.update(data).where(
        GreetModel.id == greet_id
    ).execute()



def delete_greet_by_id():
    """
    删除
    :return:
    """
    
    greet_id = request.json['id']

    # domain_service.check_permission_and_get_row(domain_id, current_user_id)

    GreetModel.delete().where(
        GreetModel.id == greet_id
    ).execute()


def delete_greet_by_ids():
    """
    批量删除
    """
    greet_ids = request.json['ids']

    GreetModel.delete().where(
        GreetModel.id.in_(greet_ids)
    ).execute()


def get_greet_by_id():

    greet_id = request.json.get('greet_id') or request.json['id']
    row = GreetModel.get_by_id(greet_id)
    return row


def get_all_greet_list():
    """
    获取用户的所有Greet数据
    :return:
    """
    rows = GreetModel.select()

    lst = [{'greet': row.content} for row in rows]

    return {
        'list': lst,
        'total': len(lst)
    }