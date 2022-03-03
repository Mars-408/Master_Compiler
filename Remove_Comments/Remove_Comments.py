def Remove_Comments(Sourse_Str):
    Remove_Comment = ''
    is_LineComment = False
    is_BlockComment = False
    is_String = False

    Count_Str = iter(range(len(Sourse_Str)))
    while True:
        try:
            element = next(Count_Str)
            Now_Scan = Sourse_Str[element:element+2]
            if Now_Scan[0] == '\"':
                # 遇到字符串边界符号
                Remove_Comment += Now_Scan[0]
                is_String = not is_String

            elif is_String and (Now_Scan[0] == '\n'):
                # 字符串没有结尾,抛错
                break

            elif (not is_String) and is_LineComment and (Now_Scan[0] == '\"'):
                is_LineComment = False

            elif (not is_String) and is_LineComment and (Now_Scan[0] == '\n'):
                # 行注释结束
                is_LineComment = False
                Remove_Comment += '\n'


            elif (not is_String) and is_BlockComment and (Now_Scan == '*/'):
                # 块注释结束
                is_BlockComment = False
                next(Count_Str)
                Remove_Comment += '\n'


            elif (not is_String) and is_LineComment or is_BlockComment:
                # 忽略
                continue

            elif (not is_String) and Now_Scan == '//':
                # 行注释开始
                is_LineComment = True
                next(Count_Str)

            elif (not is_String) and Now_Scan == '/*':
                # 块注释开始
                is_BlockComment = True
                next(Count_Str)
            else:
                # 开始记录
                Remove_Comment += Now_Scan[0]

        except StopIteration:
            break

    Remove_Comment = str(Remove_Comment)[:-1]
    return Remove_Comment