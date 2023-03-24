# -*- coding: utf-8 -*-
"""
@File    : whois_util.py
@Date    : 2023-03-24
"""
import requests
import whois

from domain_admin.log import logger


def get_domain_info_by_request(domain):
    """
    该方案有防爬，也不可行
    :param domain:
    :return:
    """
    from parsel import Selector
    from dateutil import parser

    url = 'https://www.whois.com/whois/' + domain

    data = {}

    res = requests.get(url, timeout=5)

    logger.debug(res.text)

    if res.ok:
        sel = Selector(res.text)
        text = sel.css('#registrarData::text').get("")
        rows = text.split("\n")
        logger.debug(text)

        for row in rows:
            row_split = row.split(': ')
            if len(row_split) == 2:
                label, value = row_split
                data[label] = value

    logger.debug('domain info: %s', data)

    start_time = data.get('Creation Date')
    expire_time = data.get('Registrar Registration Expiration Date')

    if start_time:
        start_time = parser.parse(start_time)

    if expire_time:
        expire_time = parser.parse(expire_time)

    result = {
        'start_time': start_time,
        'expire_time': expire_time
    }

    return result


def get_domain_info_by_whois(domain):
    domain_info = whois.query(domain, ignore_returncode=True)

    return {
        'start_time': domain_info.creation_date,
        'expire_time': domain_info.expiration_date
    }


def get_domain_info(domain: str):
    """
    获取域名信息
    :param domain:
    :return:
    """

    res = get_domain_info_by_whois(domain)

    return res