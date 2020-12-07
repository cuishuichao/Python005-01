# -*- coding: utf-8 -*-
from configparser import ConfigParser


def red_db_config(filename='config.ini', section='mysql'):
    """
    读取数据库配置文件
    :param filename: 配置文件名称
    :param section: 数据库配置部分
    :return: 字典
    """
    # 创建解析器并读取ini配置文件
    parser = ConfigParser()
    parser.read(filename)

    # 判断读取的部分是否存在
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return dict(items)


if __name__ == '__main__':
    print(red_db_config())
