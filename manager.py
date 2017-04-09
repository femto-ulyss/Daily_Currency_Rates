import dbhandler
import ratesloader
import settingsloader


# Instantiate objects and define variables section
dbHandler = dbhandler.DatabaseHandler()
rates = ratesloader.Loader()
rates_list = rates.parse_rates_file()

# Checking conditions section
dbHandler.check_already_inserted()

# Main execution section
if dbHandler.check == 0:

    for i in rates_list:
        dbHandler.execute_query(settingsloader.insert_query + '(' + i + ' + 1)')
else:

    print('Something wrong! Rates already inserted!')

    """To do

    Add feature to program execution logging
    """