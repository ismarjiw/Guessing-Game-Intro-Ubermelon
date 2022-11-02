#opens file that contains the sales report logs log_file = open(um-server-01.txt)


#function that generates sale report for given line in log_file specifying the particular day to generate report  def generate_sales_reports(log_file):
    for line in log_file: # for each entry in log_file
        line = line.rstrip() # entry = stripping empty white space on R side
        day = line[0:3] # slicing the particular day of the week we want to isolate by 3 letters
        if day == Mon: # if that day is equal to Mon

generate_sales_reports(log_file)# calls the function with log_file as the parameter
