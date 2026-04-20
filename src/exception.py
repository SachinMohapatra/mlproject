import sys   #use to manipulate python run time env

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  #python stores 3 things when an error happens (type, value, traceback) we are ignoring first 2 here and we are storing traceback
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno, str(error)   #exc_tb.tb_lineno tells you exactly where the error has occured
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):
        return self.error_message