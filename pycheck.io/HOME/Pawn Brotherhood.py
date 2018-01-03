# code - ascii -

def safe_pawns(pawns):
    
    safe = 0
    
    #转化成数组便于排序
    listP = list(pawns)
    #用第二个数字key排序
    listP.sort(key=lambda x:x[1])
    # 如果是最后一排，肯定不安全,记下最后一排的数字(ASCII码)
    minNum = ord(listP[0][1])
    
    for p in listP[1::]:
        if ord(p[1]) > minNum :
            #左下方守卫
            guardian1 = chr(ord(p[0])-1) + chr(ord(p[1])-1)
            #右下方守卫
            guardian2 = chr(ord(p[0])+1) + chr(ord(p[1])-1)
            #检查守卫们是否存在
            if (guardian1 in listP) or (guardian2 in listP):
                safe += 1
        else:
            continue
            
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
