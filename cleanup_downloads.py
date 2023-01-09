#!/usr/bin/python3
import os
import shutil
import sys
import datetime


def del_older_files(req_path, N=180):
  if not os.path.exists(req_path):
    print("Please provide valid path")
    sys.exit(1)
  if os.path.isfile(req_path):
    print("Please provide dictionary path")
    sys.exit(2)
  today=datetime.datetime.now()
  for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
      file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
      dif_days=(today-file_cre_date).days
      if dif_days > N:
        os.remove(each_file_path)
        print("File: ", each_file_path,dif_days)
    elif os.path.isdir(each_file_path):
      file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
      dif_days=(today-file_cre_date).days
      if dif_days > N:
        shutil.rmtree(each_file_path)
        print("Directory: ", each_file_path, dif_days)

def main(): 
    #req_path=input("Enter your path: ")
    req_path = "/Users/nasib/Downloads"
    del_older_files(req_path, 60)

## Main
if __name__ == "__main__":
    main()
