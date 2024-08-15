#-- coding:UTF-8 --
def bw(bwstr):
    paperline = []
    loop = []
    p = 0
    error = ""
    for i in range(65536):
        paperline.append(0)
    i = 0
    while i<len(bwstr):
        if bwstr[i] == '>':
            if p == 65535:
                error = error+"第"+str(i+1)+"个字符：坐标越界"
                break
            else:
                p+=1
        elif bwstr[i] == '<':
            if p == 0:
                error = error+"error:第"+str(i+1)+"个字符：坐标越界\n"
                return error
            else:
                p-=1
        elif bwstr[i] == '+':
            paperline[p]+=1
        elif bwstr[i] == '-':
            paperline[p]-=1
        elif bwstr[i] == '.':
            print(chr(paperline[p]),end='')
        elif bwstr[i] == ',':
            paperline[p] = ord(input())
        elif bwstr[i] == '[':
            if paperline[p] == 0:
                while 1:
                    if i==len(bwstr)-1:
                        if bwstr[i]!=']':
                            return
                    if bwstr[i]==']':
                        break
                    i+=1
            else:
                loop.append(i-1)
        elif bwstr[i] == ']':
            i = loop.pop()
        i+=1
        

file_path=input("请输入文件路径：")
with open(file_path, "r",encoding='utf-8') as file:
    content = file.read()
    bw(content)
    print('')
                        
                        
                        