# *-* coding = utf-8 *-*
import json

#def ReadFromTxt(fullpathOftxt,Jsonfilepath):
def ReadFromTxt(fullpathOftxt):
    flag = 0
    IP_list = []
    with open(fullpathOftxt,'r') as f:
        lines = f.readlines()
    for line in lines:
        if flag == 0:
            if line == '[tmp]\n':
                flag = 1
            else:
                pass
        else:
            if line == '\n':
                flag = 0
            else:
                IP_list.append(line[:-1])
    return json.dumps(IP_list)
    # with open(Jsonfilepath,'w') as m:
    #    m.writelines(json.dumps(IP_list))

