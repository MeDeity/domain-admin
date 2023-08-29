from domain_admin.model.greet_model import GreetModel
from domain_admin.log import logger
from domain_admin.utils import domain_util
from peewee import chunked, fn


def add_greet_from_file(filename, user_id):
    logger.info('user_id: %s, filename: %s', user_id, filename)

    lst = list(domain_util.parse_greet_from_file(filename))

    lst = [
        {
            'domain': item.domain,
        } for item in lst
    ]

    for batch in chunked(lst, 500):
        GreetModel.insert_many(batch).on_conflict_ignore().execute()