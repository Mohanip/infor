import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'C:\Users\mperiyasamy\PycharmProjects\infor\Logs\automation.log',
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
