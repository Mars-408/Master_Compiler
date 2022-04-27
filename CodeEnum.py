from enum import Enum

class Types(Enum):
    Int = 1
    Char = 2
    Ptr = 3


class TokensAndClasses:
    Str = 127

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