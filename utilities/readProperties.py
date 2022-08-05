import configparser

config = configparser.RawConfigParser()
# config.read(r".\\Configurations\\config.ini")

config.read(r"C:\Users\mperiyasamy\PycharmProjects\infor\Configurations\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
