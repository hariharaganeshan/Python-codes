import os
import sys
import pandas as pd
import csv
import xlrd

input_file_loc = sys.argv[1]  ## extact source file location
input_file_name = sys.argv[2] ## extact source file name 
output_file_loc = sys.argv[3] ## extact target file location
length_arg = len(sys.argv)

print(length_arg)

if length_arg == 5:
	Saperator = sys.argv[4] ##saperator as argument
else:
	Saperator = "|"  ##default saperator

filename, file_extension = os.path.splitext(input_file_name)

print("input_file_loc = " + input_file_loc)
print("filename = " + filename)
print("file_extension = " + file_extension)
print("output_file_loc = " + output_file_loc)
print("Saperator = " + Saperator)

input_file = input_file_loc+"/"+input_file_name

print("input_file = " + input_file)


xls = pd.ExcelFile(input_file)
print(xls.sheet_names)
all_worksheets = xls.sheet_names


i=0

for worksheet_name in all_worksheets:
	current_worksheet_name = all_worksheets[i]
	
	output_file = output_file_loc+"/"+filename+"_"+current_worksheet_name+".csv"
	print("output_file = " + output_file)
	
	df = pd.read_excel(input_file,sheet_name=current_worksheet_name)
	df.columns = df.columns.str.strip()
	df.to_csv(output_file,sep=Saperator,index=False,quoting=csv.QUOTE_NONNUMERIC)
	i=i+1

	
	