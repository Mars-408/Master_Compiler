'''
    由正规式转换为NFA
    输入:输入是一个字符串,内容是要转换的正规式
'''
import json



class ExpressToNFA:
    def __init__(self,express):
        self.Sigma = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'# 字符表
        self.ReverseExpress = None      # 逆波兰式
        self.TempGraph = None           # 转换函数处理的结果
        self.States = None              # NFA所有的状态
        self.GraphInfo = '起始节点  接受符号  到达状态\n'             # 图的信息
        self.express = express               # 表达式信息
        self.result = None              # 结果

    def run(self):
        express = self.express
        print("###################################")
        print("表达式转NFA↓")
        self.Reverse(express)
        print("1.后缀表达式"+str(self.ReverseExpress))
        self.ExpressionToNFA()
        print("2.转换结果"+str(self.ReverseExpress))
        self.States = self.BFS(self.TempGraph['Head'],[])
        self.States = list(set(self.States))
        self.Format()
        print("3.格式化结果"+str(self.result))
        return self.result

    def WriteFile(self):
        # 将信息写入文件
        if self.result == None:
            js = json.dumps('Error')
        js = json.dumps(self.result)
        with open('ExpressToNFA.txt', 'w+') as f:
            f.write(js)

    def Reverse(self,express):
        # 将中缀运算符转换为后缀运算符
        Express = list(express)
        expressionStack = ["#"]  # 表达式栈   
        operationStack = []      # 操作栈

        # 预处理,在表达式之间添加连接符.
        DotIndex = []
        for i in range(Express.__len__()-1):
            Prior = Express[i]
            Back = Express[i+1]
            # 前后都是字母
            if (Prior in self.Sigma) and (Back in self.Sigma):
                DotIndex.append(i+1)
            # 前是 (b|a)b或a*b这种情况
            elif (Prior in [')','*']) and (Back in self.Sigma):
                DotIndex.append(i+1)
            # a()这种情况
            elif (Prior in self.Sigma) and (Back in ['(']):
                DotIndex.append(i+1)
            # ()()这种情况
            elif (Prior in [')']) and (Back in ['(']):
                DotIndex.append(i+1)   
        InsertCount = 0
        for i in DotIndex:
            Express.insert(i+InsertCount,'.')
            InsertCount += 1

        # 转为逆波兰式算法
        for item in Express:
            if item in self.Sigma:
                expressionStack.append(item)

            elif item == '(':
                operationStack.append(item)

            elif item == ')':
                while( operationStack[-1] != '(' ):
                    expressionStack.append(operationStack.pop())
                operationStack.pop()            

            elif item == '*':
                expressionStack.append(item)

            elif item == '.':
                if(operationStack.__len__() == 0  or operationStack[-1] == '|' or operationStack[-1] == '('):
                    operationStack.append(item)
                else:
                    while( operationStack[-1] == '*' or operationStack[-1] == '.' ):
                        expressionStack.append(operationStack.pop())
                        if operationStack.__len__() == 0:
                            break
                    if( operationStack.__len__() == 0 or operationStack[-1] == '|' or operationStack[-1] == '('):
                        operationStack.append(item)

            elif item == '|':
                if(operationStack.__len__() == 0 or operationStack[-1] == '('):
                    operationStack.append(item)
                else:
                    while( operationStack[-1] == '*' or operationStack[-1] == '.' or operationStack[-1] == '|' ):
                        expressionStack.append(operationStack.pop())
                        if operationStack.__len__() == 0:
                            break
                    if( operationStack.__len__() == 0 or operationStack[-1] == '('):
                        operationStack.append(item)
        while(operationStack.__len__()!=0):
            expressionStack.append(operationStack.pop())
        expressionStack.remove('#')
        self.ReverseExpress = expressionStack

    def ExpressionToNFA(self):
        # 将后缀表达式转换成NFA
        Temp_Stack = []     # 保存暂时的自动机节点
        Now_Count = 0
        for i in self.ReverseExpress:
            if i in self.Sigma:
                # 遇到字母表
                Node_A = {
                    'State':Now_Count,
                    'Next':[],
                }
                Node_B = {
                    'State':Now_Count+1,
                    'Next':[],
                }
                Node_A['Next'].append( (i , Node_B) )
                Now_Count += 2
                Object = {
                            'Head':Node_A,
                            'Tail':Node_B,
                        }
                Temp_Stack.append(Object)

            elif i == '*':
                if len(Temp_Stack) == 0:
                    raise TypeError("正规式异常")
                Node_A = {
                    'State':Now_Count,
                    'Next':[],
                }
                Node_B = {
                    'State':Now_Count+1,
                    'Next':[],
                }
                Stack_Pop = Temp_Stack.pop(-1)

                Now_Count += 2
                Node_A['Next'].append( ( '#' ,  Stack_Pop['Head'] ) )
                Node_A['Next'].append( ( '#' , Node_B ) )
                Stack_Pop['Tail']['Next'].append( ( '#' , Node_B )  )
                Stack_Pop['Tail']['Next'].append( ( '#' , Stack_Pop['Head'] )  )
                Object = {
                    'Head':Node_A,
                    'Tail':Node_B,
                }
                Temp_Stack.append(Object)

            elif i == '.':
                if len(Temp_Stack) < 2:
                    raise TypeError("正规式异常")
                Stack_Pop_2 = Temp_Stack.pop(-1)    
                Stack_Pop_1 = Temp_Stack.pop(-1)
                Stack_Pop_2
                Stack_Pop_1['Tail']['Next'].append(('#',Stack_Pop_2['Head']))
                Object = {
                    'Head':Stack_Pop_1['Head'],
                    'Tail':Stack_Pop_2['Tail'],
                }
                Temp_Stack.append(Object)

            elif i == '|':
                if len(Temp_Stack) < 2:
                    raise TypeError("正规式异常")
                Node_A = {
                    'State':Now_Count,
                    'Next':[],
                }
                Node_B = {
                    'State':Now_Count+1,
                    'Next':[],
                }
                Stack_Pop_2 = Temp_Stack.pop(-1)
                Stack_Pop_1 = Temp_Stack.pop(-1)
                Now_Count += 2
                Node_A['Next'].append( ( '#' , Stack_Pop_1['Head'] ) )
                Node_A['Next'].append( ( '#' , Stack_Pop_2['Head'] ) )
                Stack_Pop_1['Tail']['Next'].append( ( '#' , Node_B )  )
                Stack_Pop_2['Tail']['Next'].append( ( '#' , Node_B )  )
                Object = {
                    'Head':Node_A,
                    'Tail':Node_B,
                }
                Temp_Stack.append(Object)
        if len(Temp_Stack)==1:
            self.TempGraph = Temp_Stack[0]
        else:
            raise TypeError("正规式异常")

    def BFS(self,Graph,alreadyPrint = []):
        # 对图进行BFS搜索，获取图的信息
        M = Graph.get('Next',None)
        if M == None:
            return 
        for i in M:
            alreadyPrint.append(Graph['State'])
            self.GraphInfo += "{0:^6}    {2:^6}    {1:^6}\n".format(Graph['State'],i[1]['State'],i[0])
            if i[1]['State'] not in alreadyPrint:
                self.BFS(i[1],alreadyPrint)
        return alreadyPrint

    def Format(self):
        # 对结果格式化输出
        result = {
            'Express' :self.express,
            'Head':self.TempGraph['Head']['State'],
            'Tail':self.TempGraph['Tail']['State'],
            'States':self.States,
            'GraphInfo':self.GraphInfo,
            'HeadGraph':self.TempGraph['Head']
        }
        self.result = result


