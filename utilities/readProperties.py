import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getUrl():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUsername():
        user_name = config.get("common info", "username")
        return user_name

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
