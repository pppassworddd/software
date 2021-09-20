kws = ["auto","break","case","char","const","continue","default","do",
"double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static",
"struct","switch","typedef","union","unsigned","void","volatile","while"]
badchar = ["/*","//","'"]                 #注释符和字符串的符号
ifkws = ["if","else","else if","{","}"]
ifkws2 = ["if","else","else if"]
filename = input("please tell me where the code is:")
level = int(input())
kwsum = 0
scnum = []
case_num = 0
ifelsenum = 0                  
#记录if-else的数量
if_elseifnum =0
wordlist=[]
ifstack = []         #以列表的方式实现栈，用来记录if-else的对应关系
with open(filename) as lines:
    for line in lines:
        wordlist = line.split()            #逐个字符串判断是否是关键词，并且将所有带关键词的字符串和括号储存到ifstack中
        i=0
        while i < len(wordlist):
            if (any (bad in wordlist[i] for bad in badchar)):break
            if (any (kw in wordlist[i] for kw in kws)):
                ifstack.append(wordlist[i])
                kwsum+=1
            if('{' in wordlist[i] and '}' not in wordlist[i]):
                ifstack.append('{')
            if('}' in wordlist[i] and '{' not in wordlist[i]):
                ifstack.append('}')
            i += 1
    print ("total num: ", kwsum)
level -= 1
if level > 0 :
    i=0
    while i < len(ifstack):               #碰到switch找后面跟的case个数，直到碰到下一个switch
        if('switch' in ifstack[i]):
            scnum.append(case_num)
            case_num=0
        else: 
            if('case' in ifstack[i]):
                case_num+=1
        i += 1
    scnum.append(case_num)
    del(scnum[0])
    print ("switch num: ", len(scnum))
    print ("case num: ", (" ").join(str(i) for i in scnum))


level -= 1
if level > 0 :
    i=0
    while i <len(ifstack):                           #保留所有括号和if语句，以及带括括号的其他关键词
        if(any(kw in ifstack[i] for kw in ifkws)):
            if('else' in ifstack[i] and 'if'  in ifstack[i+1]):
                del (ifstack[i])
                del (ifstack[i])
                ifstack.insert(i,'elseif')
            else:
                if('if' in ifstack[i]):
                    del ifstack[i]
                    ifstack.insert(i,'if')
                if('else' in ifstack[i]):
                    del ifstack[i]
                    ifstack.insert(i,'else')
            i+=1
        else:
            del(ifstack[i])

    i= 0 
    while i <len(ifstack):                       #去掉所有带括号的其他关键词
        if(any (kw in ifstack[i] for kw in kws) and not any(kw1 in ifstack[i] for kw1 in ifkws2)):
            del(ifstack[i])
        else:
            i+=1
    i= 0

    print(ifstack)
    print("ifstack")
    time = 5
    while time >=0 :
        time -= 1
        i=0
        while i <len(ifstack):                       #去掉所有相邻的左右括号
            if('{' in ifstack[i] and '}' in ifstack[i+1]):
                del(ifstack[i])
                del(ifstack[i])
            else:
                i+=1
        i=0
        while i <len(ifstack):                       #去掉所有相邻的左右括号
            if('{' in ifstack[i] and '}' in ifstack[i+1]):
                del(ifstack[i])
                del(ifstack[i])
            else:
                i+=1
      
        i= 0

        while i <len(ifstack):                       #对于相邻的if 和else，删去并记录，对于相邻的elseif和else，删去并记录，同时删去在这之前相邻的elseif和if（删除if停止）       
            if('if' in ifstack[i] and 'else' in ifstack[i+1] and not 'elseif' in ifstack[i+1] and not 'elseif' in ifstack[i]):
                ifelsenum += 1
                del(ifstack[i])
                del(ifstack[i])
            else:
                if('elseif' in ifstack[i] and 'else' in ifstack[i+1] and not 'elseif' in ifstack[i+1]):
                    if_elseifnum += 1
                    del(ifstack[i])
                    del(ifstack[i])
                    j=i-1
                    while j >= 0 :
                        if('elseif' in ifstack[j]):
                            del(ifstack[j])
                            j -= 1
                        else:
                            if('if' in ifstack[j]):
                                del(ifstack[j])
                                break
                else:
                    i+=1
    
    print ("if-else num: ", ifelsenum)
    level-=1
    if level > 0:
        print ("if-elseif-else num: ", if_elseifnum)


    