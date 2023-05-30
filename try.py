# import writescr;

# script = writescr.Script();
# # script.read_file("writescr.py");
# # script.print_file();
# # script.write_text("writescr.py");
# # script.print_file();
# # script.write_func();
# # script.hello_world3();



# class DataBase(object):
#     def __init__(self) -> None:
#         self.info = "";
#         pass;
#     def pr(self):
#         print(self.info);
#     @staticmethod
#     def hello_world():
#         print("that`s db");
# def hello():
#     def suck():
#         def bro():
#             print("bro");
#         return bro;
#         print("suck");
    
#     return suck;

# r = lambda x:True;
# r1 = lambda x,y:x+y;
# print(r1(10,20))
# print(r(2),r(10),r(20));
# res = hello();
# res()();
# def say(name = "igor",*kargs,**args):
#     print(name,kargs[0] + " " + kargs[1]);
#     args["hel"]();
#     args["hel"]()
# def change_info(Database,val):
#     DataBase.info = val;



# # say("igor","borov","ren",hel = hello);
# # db = DataBase();
# # change_info(db,"holla");
# # db.pr();
# # db.hello_world();
# def make_pretty(func):
#     def inner():
#         func();
#         print("innter");
#     return inner;


import asyncio

async def main():
    print("hello");
    await asyncio.sleep(2);
    await hello();
    

async def hello():
    print("hel");
    await asyncio.sleep(3);
async def m():
    task1 = asyncio.create_task(main());
    task2 = asyncio.create_task(main());
    task3 = asyncio.create_task(main());
    await task2;
    await task1;
    await task3;



r = u'юнікод рядок ';
print(r*5);
print(isinstance(r,str),
      isinstance(r,object));

mas = [i for i in range(10)];
def fn(i):
    pritn(i*2)
map(fn,mas);
print(map(fn,mas));
for itr,val in enumerate(mas):
    print(itr,val);

import scipy

