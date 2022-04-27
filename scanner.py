from ClassInfo import Tokens,Errors
from CodeEnum import TokensAndClasses



def Scanner(Source):
    source_length = len(Source)
    scaner = iter(range(source_length))             # 扫描器（迭代器）
    Line_Num = 1
    now_index = next(scaner)                        # 当前的下标
    while(True):
        try:
            now_symbol = Source[now_index]          # 当前提取的字符,在判断内部实现迭代
            # 遇到宏定义，暂时不考虑宏定义,跳过整行,下次跳出时为下一行的第一个字符的位置
            if(now_symbol == '#'):
                now_index = next(scaner)
                Errors(Line_Num,'#define...','不接受宏')
                while(Source[now_index] != '\n'):
                    now_index = next(scaner)

        
            # 遇到换行符 行号+1
            elif(now_symbol == '\n'):
                Line_Num += 1
                now_index = next(scaner)


            # 遇到标识符,判定首字符为字母或者下划线
            elif(now_symbol.isalpha() or now_symbol == '_'):
                identifier_content = now_symbol                     # 暂时保存这个标识符的内容
                now_index = next(scaner)
                now_symbol = Source[now_index]

                while(now_symbol.isalnum() or now_symbol == '_'):
                    identifier_content += now_symbol
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                Tokens(Line_Num,identifier_content,'标识符',True,89)


            # 遇到数字开头,那么必定是数字
            elif(now_symbol.isdigit()):
                is_valid = True 
                result = int(now_symbol)                    # 保存结果

                now_index = next(scaner)
                now_symbol = Source[now_index]

                if now_symbol.isdigit() or (now_symbol in 'xXbB'):
                    # 如果下一个字符依然是数字,后面分析其内容,否则就是一个个位数
                    if now_symbol.isdigit() and result != 0:
                        # 十进制
                        result = result * 10 + int(now_symbol)
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                        while(now_symbol >= '0' and now_symbol <= '9'):
                            result = result * 10 + int(Source[now_index])
                            now_index = next(scaner)
                            now_symbol = Source[now_index]
                        
                        # 下面解析浮点数
                        square = -1
                        if now_symbol == '.':
                            # 解析成浮点数
                            square = 1
                            now_index = next(scaner)
                            now_symbol = Source[now_index]
                            
                            while(now_symbol >= '0' and now_symbol <= '9'):
                                result = result +  int(now_symbol) * (0.1 ** square)
                                square += 1
                                now_index = next(scaner)
                                now_symbol = Source[now_index]
                            if now_symbol == '.' or now_symbol.isalpha():  
                                is_valid = False
                                if square == 1:
                                    Errors(Line_Num,str(result)+'.','错误的十进制数')
                                else:
                                    Errors(Line_Num,str(result)+str(now_symbol),'错误的浮点数')

                                while(now_symbol.isalnum() or now_symbol == '.'):
                                    now_index = next(scaner)
                                    now_symbol = Source[now_index]
                                continue


                    elif now_symbol == 'b' or now_symbol == 'B':
                        # 二进制
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                        while now_symbol == '1' or now_symbol == '0':
                            result = result * 2 + int(now_symbol)
                            now_index = next(scaner)
                            now_symbol = Source[now_index]
                        if now_symbol.isalnum():
                            is_valid = False
                            Errors(Line_Num,str(result)+str(now_symbol),'错误的二进制数')
                

                    elif now_symbol == 'x' or now_symbol == 'X':
                        # 十六进制
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                        while (now_symbol.lower() <= 'f' and now_symbol.lower() >= 'a') or now_symbol.isdigit():
                            result = result * 16 + int(now_symbol,16)
                            now_index = next(scaner)
                            now_symbol = Source[now_index]
                        if now_symbol.isalnum():
                            is_valid = False
                            Errors(Line_Num,str(result)+str(now_symbol),'错误的十六进制数')
                        
                    elif result == 0:
                        # 八进制
                        while now_symbol <= '7' and now_symbol >= '0':
                            result = result * 8 + int(now_symbol)
                            now_index = next(scaner)
                            now_symbol = Source[now_index]
                        if now_symbol.isalnum():
                            is_valid = False
                            Errors(Line_Num,str(result)+str(now_symbol),'错误的八进制数')
                            
                                 
                # 比如x.xxx的浮点数由此解析
                elif now_symbol == '.':
                    # 解析成浮点数
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                    square = 1
                    while(now_symbol >= '0' and now_symbol <= '9'):
                        result = result +  int(now_symbol) * (0.1 ** square)
                        square += 1
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                    if now_symbol == '.' or now_symbol.isalpha():  
                        is_valid = False
                        Errors(Line_Num,str(result)+'.','错误的浮点数')
                        while(now_symbol.isalnum() or now_symbol == '.'):
                            now_index = next(scaner)
                            now_symbol = Source[now_index]


                elif now_symbol.isalpha():
                    is_valid = False
                    Errors(Line_Num,result,'不合法的数字表示')
                if is_valid:
                    if int(result) != result: 
                        Tokens(Line_Num,result,'浮点数',True,TokensAndClasses.Num)
                    else:
                        Tokens(Line_Num,result,'数字',True,TokensAndClasses.Num)
                else:
                    # 循环到下一个可用的字符
                    while now_symbol.isalnum():
                        now_index = next(scaner)
                        now_symbol = Source[now_index]



            
            # 行注释,只解析行注释
            elif now_symbol == '/':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '/':
                    # 注释
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                    while(now_symbol != '\n'):
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                else:
                    # 除法运算
                    Tokens(Line_Num,'\\','运算符',True,TokensAndClasses.Div)              

            # 字符
            elif now_symbol == "'":
                now_index = next(scaner)
                now_symbol = Source[now_index]
                content = ""
                if now_symbol == '\\':
                    # 转义
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                    if now_symbol == 'n':
                        content = '\\n'
                    else:
                        content = '\\'+now_symbol      
                else:
                    # 普通字符
                    content = now_symbol
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol!= "'":
                    Errors(Line_Num,now_symbol,"''内只接受单字符")
                    while now_symbol != "'":
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, content,'字符',True,TokensAndClasses.Num)    
                    now_index = next(scaner)
                    now_symbol = Source[now_index]                





            # 遇到字符串
            elif now_symbol == '"':
                String = ''
                now_index = next(scaner)
                now_symbol = Source[now_index]
                while now_symbol != '"':
                    if now_symbol == '\\':
                        # 判定双引转义
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                        if now_symbol == '"':
                            String = String + '"'
                            now_index = next(scaner)
                            now_symbol = Source[now_index]
                        else:
                            String = String + "\\" +now_symbol  
                    else:
                        # 非转义
                        String = String + now_symbol
                        now_index = next(scaner)
                        now_symbol = Source[now_index]
                now_index = next(scaner)
                now_symbol = Source[now_index]
                Tokens(Line_Num, String,'字符串',True,TokensAndClasses.Str)

            elif now_symbol == '=':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '=':
                    Tokens(Line_Num, '==','运算符',True,TokensAndClasses.Eq)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]

                else:
                    Tokens(Line_Num, '=','运算符',True,TokensAndClasses.Assign)

            elif now_symbol == '+':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '+':
                    Tokens(Line_Num, '++','运算符',True,TokensAndClasses.Inc)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                elif now_symbol == '=':
                    Tokens(Line_Num, '+=','运算符',True,TokensAndClasses.Inc)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, '+','运算符',True,TokensAndClasses.Add)

            elif now_symbol == '-':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '-':
                    Tokens(Line_Num, '--','运算符',True,TokensAndClasses.Dec)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                elif now_symbol == '=':
                    Tokens(Line_Num, '-=','运算符',True,TokensAndClasses.Inc)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, '-','运算符',True,TokensAndClasses.Sub)

            elif now_symbol == '!':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '=':
                    Tokens(Line_Num, '!=','运算符',True,TokensAndClasses.Ne)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]

                else:
                    Tokens(Line_Num, '!','运算符',True,TokensAndClasses.Ne)

            elif now_symbol == '<':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '=':
                    Tokens(Line_Num, '<=','运算符',True,TokensAndClasses.Le)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                elif now_symbol == '<':
                    Tokens(Line_Num, '<<','运算符',True,TokensAndClasses.Shl)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, '<','运算符',True,TokensAndClasses.Lt)

            elif now_symbol == '>':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '=':
                    Tokens(Line_Num, '>=','运算符',True,TokensAndClasses.Ge)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                elif now_symbol == '>':
                    Tokens(Line_Num, '>>','运算符',True,TokensAndClasses.Shr)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, '>','运算符',True,TokensAndClasses.Gt)

            elif now_symbol == '|':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '|':
                    Tokens(Line_Num, '||','运算符',True,TokensAndClasses.Lor)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, '|','运算符',True,TokensAndClasses.Or)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
            elif now_symbol == '&':
                now_index = next(scaner)
                now_symbol = Source[now_index]
                if now_symbol == '&':
                    Tokens(Line_Num, '&&','运算符',True,TokensAndClasses.Lan)
                    now_index = next(scaner)
                    now_symbol = Source[now_index]
                else:
                    Tokens(Line_Num, '&','运算符',True,TokensAndClasses.And)

            elif now_symbol == '^':
                Tokens(Line_Num, '^','运算符',True,TokensAndClasses.Xor)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == '%':
                Tokens(Line_Num, '%','运算符',True,TokensAndClasses.Mod)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == '*':
                Tokens(Line_Num, '*','运算符',True,TokensAndClasses.Mul)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == '[':
                Tokens(Line_Num, '[','界符',True,TokensAndClasses.Brak)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == '?':
                Tokens(Line_Num, '?','运算符',True,TokensAndClasses.Cond)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == '~':
                Tokens(Line_Num, '~','运算符',True,TokensAndClasses.Cond)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == ',':
                Tokens(Line_Num, ',','运算符',True,TokensAndClasses.Cond)
                now_index = next(scaner)
                now_symbol = Source[now_index]
            elif now_symbol == ':':
                Tokens(Line_Num, ':','运算符',True,TokensAndClasses.Cond)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol in ';{}()]':
                Tokens(Line_Num, now_symbol,'界符',True,TokensAndClasses.Cond)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            elif now_symbol == '.':
                Tokens(Line_Num, now_symbol,'运算符',True,TokensAndClasses.Cond)
                now_index = next(scaner)
                now_symbol = Source[now_index]

            else:
                if now_symbol != ' ' and ord(now_symbol)!= 9 :
                    Errors(Line_Num,now_symbol,'怪字符')
                now_index = next(scaner)
                now_symbol = Source[now_index]

        except Exception as E:
            print(E)
            break
