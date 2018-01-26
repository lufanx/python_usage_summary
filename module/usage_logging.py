#!/usr/bin/env python

import logging

log_file = 'test.log'

LOG = logging.getLogger('test')
LOG.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)-6s %(asctime)s %(levelname)-6s: %(message)s')

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

LOG.addHandler(file_handler)
LOG.addHandler(console_handler)

LOG.debug('This is debug infomation!')
LOG.info('This is info infomation!')
LOG.warn('This is warn infomation!')
