from domain_admin.model.greet_model import GreetModel
from domain_admin.log import logger
from domain_admin.utils import domain_util
from peewee import chunked, fn


def add_greet_from_file(filename, user_id):
    logger.info('user_id: %s, filename: %s', user_id, filename)

    lst = list(domain_util.parse_greet_from_file(filename))

    lst = [
        {
            'content': item,
        } for item in lst
    ]

    for batch in chunked(lst, 500):
        GreetModel.insert_many(batch).on_conflict_ignore().execute()

def update_greet(row_id,content):
    """
    更新信息
    :param row_id: id
    :return:
    """
    # logger.info("%s", model_to_dict(domain_row))

    greet_row = GreetModel.get_by_id(row_id)

    GreetModel.update(
        content=content,
    ).where(
        GreetModel.id == greet_row.id
    ).execute()
    

def get_greet_list():
    list=[]
    query = GreetModel.select()
    # 遍历记录并处理每一条记录
    for record in query:
        list.append(record)
    return list
