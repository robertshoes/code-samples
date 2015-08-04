"""
This classes work together in order
to parse a file containing data delimited by '|'
and creates another file with INSERTs statement
for an ORACLE table called verifone_data
"""


class OpenFile:
    """
    Class wrapper for opening a file
    """
    def __init__(self, file_name=''):
        self.file_name = file_name
        self.file_handler = None
        self.file_handler = open(self.file_name)
    def open_file(self):
        self.file_handler = open(self.file_name)
        return self.file_handler
    def close_file(self):
        try:
            self.file_handler.close()            
        except:
            return False
        return True
    def read_file_lines(self):
        return self.file_handler.readlines()
    def read_entire_file(self):
        return self.file_handler.read()
    

class ProcessFile:
    """
    Class that uses OpenFile class in order to process
    the input file and create the final file
    with the insert statements.
    """
    def __init__(self, file_object=None):
        if not file_object:
            print "This is not an object"
        elif not isinstance(file_object, OpenFile):
            print "Cannot do anything without an OpenFile instance!"
        else:
            print "ProcessFile instance created...Starting the process"
            print type(file_object)
            self.file_object = file_object
            self.my_output_file = open(r'C:\insert_verifone.sql', 'w')
            self.insert_str = "insert into verifone_data values (%d, %d, %d, %s);"
            self.counter = 0
            self.accu = 0
        
    def process(self):        
        for line in self.file_object.read_file_lines():
            the_line = line.split('|')
            #print the_line
            self.counter = self.counter + 1
            #self.my_output_file.write(self.insert_str % (the_line[0], the_line[1], the_line[2], the_line[16]))
            self.my_output_file.write("insert into verifone_data values("+the_line[0]+",'"+the_line[1]+ "','"+ the_line[2]+"','"+the_line[16].rstrip('\n')+"');\n")
            if self.counter == 100000:
                self.accu = self.accu + self.counter
                print "We have " + str(self.counter) + " more processed."
                print "===========>Total: " + str(self.accu)
                self.counter = 0
        self.my_output_file.close()
        return self.file_object.close_file()
            
        
            
            
        

if __name__ == '__main__':
    obj = ProcessFile(OpenFile(r'D:\MigracionXP\pel\WLS_IVRBalance.20100428.output'))
    msg = obj.process()
    if msg:
        print "File processed sucessfuly!"
