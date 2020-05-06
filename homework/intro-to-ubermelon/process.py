log_file = open("um-server-01.txt")


def sales_reports(log_file):  # defining a function 
    for line in log_file:     # staring from the first line in log_file
        line = line.rstrip()  # removing white spaces from right end of each line
        day = line[0:3]       # variable day is set as first 3 characters
        if day == "Mon":      #if first 3 char is word Mon
            print(line)       #print the whole line


sales_reports(log_file)       #calling the function




