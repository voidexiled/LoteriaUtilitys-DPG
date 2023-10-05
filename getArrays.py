import os
import numpy as np

def divide_chunks(l, n):
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  

def getArrayFromFile(file_path="tables.txt"):
    file = open(file_path, "r")
    tables = []
    size = 4
    current_row = 0
    lines = file.read()
    rows = lines.split("\n")
    
    while "" in rows:
        rows.remove("")
        
    rows = [[int(num) for num in s.split()] for s in rows]
    tables = list(divide_chunks(rows, 4))
    return tables

tables = getArrayFromFile()
print(tables[0])