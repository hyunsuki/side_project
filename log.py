import os
import logging
import logging.handlers

class LogManager:
    def __init__(self, save_log_path, current_file_name): 
        self.log_max_size = 1024*1024*10
        self.log_file_count = 10
        self.save_log_path = save_log_path
        current_file_path = os.path.dirname(os.path.realpath(current_file_name))
        self.logger_name = current_file_path + '/' + current_file_name 
        self.logger_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    def getLogger(self, level = logging.DEBUG):
        logger = logging.getLogger(self.logger_name)

        if len(logger.handlers)> 0:
            return logger
        logger.setLevel(level)
        formatter = logging.Formatter(self.logger_format)
        file_handler = logging.handlers.RotatingFileHandler(self.save_log_path, maxBytes = self.log_max_size,  backupCount = self.log_file_count)
        console = logging.StreamHandler()

        console.setLevel(level)
        file_handler.setLevel(level)

        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)

        return logger


def main():
    m = LogManager('conf/log_info.log', 'log.py')
    logger = m.getLogger()
    logger.info('This is information!')

if __name__ == '__main__':
    main()
 
