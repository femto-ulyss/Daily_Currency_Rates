from xml.dom import minidom
from urllib import request
import settingsloader
import os


class Loader:

    def __init__(self):

        if settingsloader.proxy_usage == 1:
            proxy = request.ProxyHandler({settingsloader.proxy_protocol: settingsloader.proxy_string})
            opener = request.build_opener(proxy)
            request.install_opener(opener)

        self.web_file = request.urlopen(settingsloader.target_url)
        self.data = self.web_file.read()
        self.file_name = 'tmp_' + settingsloader.target_url.split('/')[-1].replace('.asp', '.xml')

        local_file = open(self.file_name, 'wb')
        local_file.write(self.data)
        self.web_file.close()

    def parse_rates_file (self):

        doc = minidom.parse(self.file_name)
        currency = doc.getElementsByTagName('Valute')

        rate_list = []

        for rate in currency:
            rate_list.append('\'' + rate.getElementsByTagName('Name')[0].firstChild.data + '\', ' +
                             '\'' + rate.getElementsByTagName('NumCode')[0].firstChild.data + '\', ' +
                             rate.getElementsByTagName('Value')[0].firstChild.data[0:5].replace(',','.') + ', ' +
                             rate.getElementsByTagName('Nominal')[0].firstChild.data + ', SYSDATE')

        self.web_file.close()
        os.remove(self.file_name)
        return rate_list
