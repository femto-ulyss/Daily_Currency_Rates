from xml.dom import minidom


settings_file = open('Settings.xml','r')
settings = minidom.parse(settings_file)

target_url = settings.getElementsByTagName('url')[0].firstChild.data
proxy_usage = settings.getElementsByTagName('proxyUsage')[0].firstChild.data
proxy_protocol = settings.getElementsByTagName('proxyProtocol')[0].firstChild.data
proxy_string = settings.getElementsByTagName('proxyString')[0].firstChild.data
db_host = settings.getElementsByTagName('dbHost')[0].firstChild.data
db_port = settings.getElementsByTagName('dbPort')[0].firstChild.data
db_name = settings.getElementsByTagName('dbName')[0].firstChild.data
db_login = settings.getElementsByTagName('dbLogin')[0].firstChild.data
db_password = settings.getElementsByTagName('dbPassword')[0].firstChild.data
check_query = settings.getElementsByTagName('checkQuery')[0].firstChild.data
insert_query = settings.getElementsByTagName('insetQuery')[0].firstChild.data

settings_file.close()