1)
file=open('1.txt','r')
text=file.read()
print(text)
2)file=open("1.txt",'r')
b=file.readlines(1)
print(b)
3)def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("holaa\n")
                myfile.write("Java Exercises\n")
                myfile.write("akaka")
        txt = open(fname)
        print(txt.read())
file_read('1.txt')
4)file=open("1.txt",'r')
lines = file.readlines()
last_lines = lines[-1]
print(last_lines)
5)file=open("1.txt",'r')
lines = file.readlines()
print(lines)
7)
def file_read(fname):
        content_array = []
        with open(fname) as f:     
                for i in f:
                        content_array.append(i)
                print(content_array)
file_read('1.txt')
8)
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('1.txt'))
9)
file = open("1.txt","r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1
print(Counter)

10)
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())
print(word_count("1.txt"))
11)
import os
from typing import Sized
filepath='1.txt'
size=os.path.getsize(filepath)
print(size)
12)
names=['Ali','Bauyrzhan','Gulzhan','Dilnaz']
with open('abc.txt', "w") as myfile:
        for c in names:
                myfile.write("%s\n" % c)
13)
with open('1.txt','r') as f1, open('A.txt','a') as f2:
    for line in f1:
             f2.write(line)
14)
with open('1.txt') as fh1, open('A.txt') as fh2:
    for l1, l2 in zip(fh1, fh2):
        print(l1+l2)
15)
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('1.txt'))
16)
f = open('1.txt','r')
print(f.closed)
f.close()
print(f.closed)
18)file = open("1.txt", "r")
data = file.read()
words = data.split()
print(len(words))
19)
20)import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
21)
import string
def letters_file_line(n):
   with open("1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(5)