#use like python <filename> <num1> <num2> --operation <operation_name>


import argparse

parser = argparse.ArgumentParser(description='calculate with some integers.')

parser.add_argument("num1",help = "1st num",type = int)
parser.add_argument("num2",help = "2nd num", type = int)
parser.add_argument("--operation", choices= ["add","a","subtract","s","multiply","m","division","d"])

args = parser.parse_args()
num1 = args.num1
num2 = args.num2


if args.operation in ["add","a"]:
    print("Addition:",num1+num2)
    
elif args.operation in ["s","subtract"]:
    print("Subraction: ",num1-num2)
    
elif args.operation in ["m","multiply"]:
    print("Multiply: ",num1*num2)
    
elif args.operation in ["d","division"]:
    print("Division: ",num1/num2)
