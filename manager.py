import dbhandler
import ratesloader
import settingsloader


db_worker = dbhandler.Worker()
rates = ratesloader.Loader()
rates_list = rates.parse_rates_file()

db_worker.check_already_inserted()

if db_worker.check == 0:

    for i in rates_list:
        db_worker.execute_query(settingsloader.insert_query + '(' + i + ' + 1)')
else:

    print('Somthing wrong! Rates already inserted!')