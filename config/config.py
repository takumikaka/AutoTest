# -*- coding: utf-8 -*-

import logging
import os

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(prj_path, "log", "log.txt")
file_name = os.path.join(prj_path, "file", "test.html")

logging.basicConfig(level = logging.DEBUG,
                   format = "[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s %(lineno)d] %(message)s",
                   datefmt = "%Y-%m-%d %H:%M:%S",
                   filename = log_file,
                   filemode = "a")

db_host = "localhost"
db_user = "root"
db_passwd = "Raspberry2019"
db = "autotest"
db_charset = "utf8"
