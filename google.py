
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
emepty = "000000"

for Sub_String in some_string:
    #print(Sub_String, end=' \n')
    if Sub_String == 'a':
        Output_string = Output_string + a
    if Sub_String == 'b':
        Output_string = Output_string + b
    if Sub_String == 'c':
        Output_string = Output_string + c
    if Sub_String == 'd':
        Output_string = Output_string + d
    if Sub_String == 'e':
        Output_string = Output_string + e
    if Sub_String == 'f':
        Output_string = Output_string + f
    if Sub_String == 'g':
        Output_string = Output_string + g
    if Sub_String == 'h':
        Output_string = Output_string + h
    if Sub_String == 'i':
        Output_string = Output_string + i
    if Sub_String == 'j':
        Output_string = Output_string + j
    if Sub_String == 'k':
        Output_string = Output_string + k
    if Sub_String == 'l':
        Output_string = Output_string + l
    if Sub_String == 'm':
        Output_string = Output_string + m
    if Sub_String == 'n':
        Output_string = Output_string + n
    if Sub_String == 'o':
        Output_string = Output_string + o
    if Sub_String == 'p':
        Output_string = Output_string + p
    if Sub_String == 'q':
        Output_string = Output_string + q
    if Sub_String == 'r':
        Output_string = Output_string + r
    if Sub_String == 's':
        Output_string = Output_string + s
    if Sub_String == 't':
        Output_string = Output_string + t
    if Sub_String == 'u':
        Output_string = Output_string + u
    if Sub_String == 'v':
        Output_string = Output_string + v
    if Sub_String == 'w':
        Output_string = Output_string + w
    if Sub_String == 'x':
        Output_string = Output_string + x
    if Sub_String == 'y':
        Output_string = Output_string + y
    if Sub_String == 'z':
        Output_string = Output_string + z
    if Sub_String == ' ':
        Output_string = Output_string + emepty
print("output: "+ Output_string + " = "+str(len(Output_string)))
print("\n")

#110000111010100000010100111000111000100010
#000001110000111010100000010100111000111000100010
