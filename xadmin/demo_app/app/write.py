#coding = utf-8

def writeIntoTxt(IP_list,fullpathOftxt,flag):
    rfile = open(fullpathOftxt,'r+')
    lines_list = rfile.readlines()
    identifier = ''
    if lines_list[0].endswith('\r\n'):
        identifier = '\r\n'
    elif lines_list[0].endswith('\n'):
        identifier = '\n'
    else:
        identifier = '\r'
    rfile.close()
    tarline = 0

    point = 0
    for i in range(lines_list.__len__()):
        if lines_list[i] == flag+identifier:
            point = 1
        else:
            if lines_list[i] == '\n' or lines_list[i].startswith('['):
                point = 0
            elif point == 1:
                lines_list[i] = ''
            else:
                pass

    for i in range(lines_list.__len__()):
        if lines_list[i] == flag+identifier:
            tarline = int(i)+1

    for i in IP_list:
        i = i+identifier
        lines_list.insert(tarline,i)
        tarline += 1

    wfile = open(fullpathOftxt,'w+')
    for j in range(lines_list.__len__()):
        wfile.write(lines_list[j])
    wfile.close()

