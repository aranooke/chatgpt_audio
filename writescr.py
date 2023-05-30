import random;
class Script:
    def __init__(self) -> None:
        self.__name = None
        self.__text = "";
        self.__random = random.randint(0,20);
    def read_file(self,file_path):
        with open(file_path,"r") as f:
            self.__text = f.read();
    def print_file(self):
        print(self.__text);
    def find_text(self):
        self.__text.find("# Start the bot and listen for incoming updates");
    def write_text(self,file_path):
        with open(file_path,"a") as f:
            f.write("# Hello blyuhi \n")
    def write_func(self,file_path = "writescr.py"):
        with open(file_path,"a") as f:
            f.write(f'''
def hello_world{self.__random}():
    print('holla world ',end = '!!!!!!');
            ''')


# Start the bot and listen for incoming updates# Hello blyuhi 
# Hello blyuhi 

              
                    

            # Hello blyuhi 

# Hello blyuhi 

def hello_world3():
    print('holla world ',end = '!!!!!!')

            # Hello blyuhi 
# Hello blyuhi 
# Hello blyuhi 
