import multiprocessing
 
def print_records(records):
    """
    function to print record(tuples) in records(list)
    """
    for record in records:
        print("Name: {0}\nScore: {1}, {2}\n".format(record[0], record[1], record[2]))
 
def insert_record(record, records):
    """
    function to add a new record to records(list)
    """
    records.append(record)
    print("New record added!\n")
 
if __name__ == '__main__':
    # creating a list in server process memory
    records = multiprocessing.Manager().list([('Sam', 10, 1), ('Adam', 9, 2), ('Kevin',9, 3)])
    # new record to be inserted in records
    new_record = ('Jeff', 8, 7)
    
    # creating new processes
    p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
    p2 = multiprocessing.Process(target=print_records, args=(records,))
    
    # running process p1 to insert new record
    p1.start()
    p1.join()
    
    # running process p2 to print records
    p2.start()
    p2.join()