class DevConfig(object):
    mode = "local"

    if mode == "remoteDev":
        MONGO_HOST = "172.31.43.5"
        MONGO_USERNAME = ""
        MONGO_PASSWORD = ""

        MYSQL_HOST = "172.31.34.192"
        MYSQL_USERNAME = "ubuntu"
        MYSQL_PASSWORD = "password"
        MYSQL_DATABASE = "amazon"
        MYSQL_TABLE_REVIEWS = "amazonreviews"

    elif mode == "local":
        MONGO_HOST = "127.0.0.1"
        MONGO_USERNAME = ""
        MONGO_PASSWORD = ""

        MYSQL_HOST = "127.0.0.1"
        MYSQL_USERNAME = "ubuntu"
        MYSQL_PASSWORD = "password"
        MYSQL_DATABASE = "amazon"
        MYSQL_TABLE_REVIEWS = "amazonreviews"

class Config_local:
    MONGO_HOST = "127.0.0.1"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

    MYSQL_HOST = "127.0.0.1"
    MYSQL_USERNAME = "ubuntu"
    MYSQL_PASSWORD = "password"
    MYSQL_DATABASE = "amazon"
    MYSQL_TABLE_REVIEWS = "amazonreviews"

class Config_remoteDev:
    MONGO_HOST = "MONGO_IP"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

    MYSQL_HOST = "MYSQL_IP"
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "password"
    MYSQL_DATABASE = "amazon"
    MYSQL_TABLE_REVIEWS = "amazonreviews"

