# -*- coding: utf-8 -*-
import logging
import os
import pathlib
import time


def time_log():
    today = time.strftime("%Y-%m-%d", time.localtime())
    logdir = './python-{}'.format(today)

    if not pathlib.Path(logdir).exists():
        os.makedirs(logdir)

    logging.basicConfig(
        filename=os.path.join(logdir, 'test.log'),
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s'
    )
    logging.info('')


if __name__ == '__main__':
    time_log()



