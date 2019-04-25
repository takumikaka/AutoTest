# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from config.config import *

def wfile():
    try:
        fp = open(file_name, "wb")
    except IOError as e:
        logging.info(str(e))
    else:
        #fp = open(file_name, "wb")
        fp.write("test".encode("utf_8"))
        fp.close()

def rfile():
    try:
        fp = open(file_name, "r")
    except IOError as e:
        logging.info(str(e))
    else:
        for i in fp:
            logging.info("file data is: {0}".format(i))
        fp.close()

if __name__ == "__main__":
    wfile()
    rfile()
    logging.info("Complete Done!")


