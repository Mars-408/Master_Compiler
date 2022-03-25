from enum import Enum


class Errors:
    Errors_List = []
    def __init__(self,line_num,content,details)  :
        # 创建错误信息并且加入到类变量中
        self.line_num = line_num
        self.content = content
        self.details = details
        Errors.Errors_List.append(self)
    

    @classmethod
    def format_output(self)  :
        # 打印错误信息的方法
        Error_result = ''
        Error_result = '{0:^5}{1:^10}{2:^20}\n'.format('Line','Error','Detail')
        for item in self.Errors_List:
            Error_result += '{0:^5}{1:^10}{2:^20}\n'.format(item.line_num,item.content,item.details)
        return Error_result


    @classmethod
    def reset(self)  :
        # 重置这个错误信息,每次词法分析之前必须执行
        Errors.Errors_List = []



class Tokens:
    Tokens_List = []
    def __init__(self,line_num,word,type,valid,code):
        # 创建一个Token
        self.line_num = line_num
        self.word = word
        self.type = type
        self.code = code
        self.valid = valid
        Tokens.Tokens_List.append(self)
    

    @classmethod
    def format_output(self)  :
        # 打印Token内容
        Token_result = ''
        Token_result = '{0:^5}{1:^22}{2:^14}{3:^9}{4:^9}\n'.format('Line','Content','Type','Valid','Code')
        for item in Tokens.Tokens_List:
            Token_result += '{0:^5}{1:^21}{2:^14}{3:^9}{4:^9}\n'.format(item.line_num , item.word , item.type , str(item.valid) , item.code  )
        return Token_result


    @classmethod
    def reset(self)  :
        # 重置这个错误信息,每次词法分析之前必须执行
        Tokens.Tokens_List = []

class TokensAndClasses(Enum):
    Num = 128
    Fun = 129
    Sys = 130
    Glo = 131
    Loc = 132
    Id = 133
    
    Char = 134
    Else = 135
    Enum = 136
    If = 137
    Int = 138
    Return = 139
    Sizeof = 140
    While = 141

    Assign = 142
    Cond = 143
    Lor = 144
    Lan = 145
    Or = 146
    Xor = 147
    And = 148
    Eq = 149
    Ne = 150
    Lt = 151
    Gt = 152
    Le = 153
    Ge = 154
    Shl = 155
    Shr = 156
    Add = 157
    Sub = 158
    Mul = 159
    Div = 160
    Mod = 161
    Inc = 162
    Dec = 163
    Brak = 164