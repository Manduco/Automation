
#https://www.google.com/search?q=Braille&rlz=1C5CHFA_enUS907US907&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj_laLOpf7sAhVCp1kKHRKgDGsQ_AUoAXoECCoQAw&biw=1600&bih=821#imgrc=42oALdD5qUGb_M
global Output_string
some_string = ''

some_string = input("enter something ")

k = len(some_string)
print("you entered : "+ some_string)
print("length = "+ str(k))

Output_string = ""
#1 4
#2 5dwdewdew3e
#3 6

#13
a,b,c,d,e,f,g = "100000","110000","100100","100110","100010","110100","110110"
h,i,j,k,l,m,n = "110010","010100","010110","101000","111000","101100","101110"
o,p,q,r,s,t,u = "101010","111100","111110","111010","011100","011110","101001"
v,w,x,y,z = "111001","010111","101101","101111","101011"
emepty, captial= "000000","000001"

for Sub_String in some_string:
    #print(Sub_String, end=' \n')
    if Sub_String == 'a' or Sub_String =="A":
        Output_string = Output_string + a
    if Sub_String == 'b'or Sub_String =="B":
        Output_string = Output_string + b
    if Sub_String == 'c'or Sub_String =="C":
        Output_string = Output_string + c
    if Sub_String == 'd'or Sub_String =="D":
        Output_string = Output_string + d
    if Sub_String == 'e'or Sub_String =="E":
        Output_string = Output_string + e
    if Sub_String == 'f'or Sub_String =="F":
        Output_string = Output_string + f
    if Sub_String == 'g'or Sub_String =="G":
        Output_string = Output_string + g
    if Sub_String == 'h'or Sub_String =="H":
        Output_string = Output_string + h
    if Sub_String == 'i'or Sub_String =="I":
        Output_string = Output_string + i
    if Sub_String == 'j'or Sub_String =="J":
        Output_string = Output_string + j
    if Sub_String == 'k'or Sub_String =="K":
        Output_string = Output_string + k
    if Sub_String == 'l'or Sub_String =="L":
        Output_string = Output_string + l
    if Sub_String == 'm'or Sub_String =="M":
        Output_string = Output_string + m
    if Sub_String == 'n'or Sub_String =="N":
        Output_string = Output_string + n
    if Sub_String == 'o'or Sub_String =="O":
        Output_string = Output_string + o
    if Sub_String == 'p'or Sub_String =="P":
        Output_string = Output_string + p
    if Sub_String == 'q'or Sub_String =="Q":
        Output_string = Output_string + q
    if Sub_String == 'r'or Sub_String =="R":
        Output_string = Output_string + r
    if Sub_String == 's'or Sub_String =="S":
        Output_string = Output_string + s
    if Sub_String == 't'or Sub_String =="T":
        Output_string = Output_string + t
    if Sub_String == 'u'or Sub_String =="U":
        Output_string = Output_string + u
    if Sub_String == 'v'or Sub_String =="V":
        Output_string = Output_string + v
    if Sub_String == 'w'or Sub_String =="W":
        Output_string = Output_string + w
    if Sub_String == 'x'or Sub_String =="X":
        Output_string = Output_string + x
    if Sub_String == 'y'or Sub_String =="Y":
        Output_string = Output_string + y
    if Sub_String == 'z'or Sub_String =="Z":
        Output_string = Output_string + z
    if Sub_String == ' ':
        Output_string = Output_string + emepty
    if Sub_String.isupper() :
        Output_string = captial + Output_string
print("output: "+ Output_string + " = "+str(len(Output_string)))
print("\n")

#110000111010100000010100111000111000100010
#0000011100001110101000000101001110001110001000A10
