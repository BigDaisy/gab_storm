# -*- coding: utf-8 -*-
import logging
import logging.handlers  # handlers要单独import

if __name__ == "__main__":

    logger = logging.getLogger()
    fh = logging.handlers.SysLogHandler(('localhost', 5140), logging.handlers.SysLogHandler.LOG_AUTH)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.warning("msg")
    logger.error("msg")
    print '1111111',logging.handlers.SysLogHandler