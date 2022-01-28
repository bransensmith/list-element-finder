from datetime import datetime
from info import names1 # importing name list


def tmux_check(file_location):
    # get current date
    current_time = datetime.now().strftime('%m/%d/%y')

    # open text file and read contents
    opened_file = open(file_location, 'r')

    with opened_file as start_check:
        lines = start_check.readlines()

        # find rows in text that match current date
        date_matches = [match for match in lines if current_time in match]

        # iterate through returned rows
        for i in date_matches:

            # look for text in string (our case is a name)
            name_found = [word for word in names1 if word in i]

            # list to string
            change_type = ''.join(name_found)

            # if name is found in our list, remove name from list
            if change_type in names1:
                names1.remove(change_type)

    # close .txt file
    opened_file.close()


    # list return an object
    if names1:
        # function here
