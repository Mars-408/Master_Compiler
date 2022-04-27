'''
    输入参数:
        Graph:NFA图(dict)
        HeadState:初始状态(int)
        TailState:终止状态(int)
    输出参数(字典类型):
        dict = {
            DFAGraph:这是转换的DFA的图(list)
            DFAStates:这是NFA对应DFA的状态集关系(Dict)
            StartState:起始状态(int)
            EndStates:终止状态集(list<int>)
        }
    输入图的数据类型(dict)
        Graph = {
            'State': 8,             节点的状态名(int)
            'Next':[                子节点的信息(list),list的每一个元素是一个二元组
                ('a',{...}),        对于子节点的元组类型,[0]代表弧上的标签,[1]代表表示子节点的字典类型
                ('#',{...}),        对于空字符,以#表示
                ('b',{'State': 1,'Next':[...]}),
                ...
            ]
        }
    输出图的数据结构(list)
        self.DFAGraph:这是一个DFA对应弧的列表,(起始状态,弧标签,终止状态)
        e.g:
            [(0, 'a', 1), 
            (0, 'b', 2), 
            (1, 'a', 3), 
            (1, 'b', 4), 
            (2, 'a', 3), 
            (2, 'b', 2), 
            (3, 'a', 3), 
            (3, 'b', 4), 
            (4, 'a', 3), 
            (4, 'b', 5), 
            (5, 'a', 3), 
            (5, 'b', 2)]
    DFAStates示例:
        {
            0: [6, 4, 7, 0, 2, 8], 
            1: [1, 9, 5, 10, 7, 4, 8, 0, 2], 
            2: [3, 5, 7, 4, 8, 0, 2], 
            3: [9, 1, 10, 5, 7, 4, 8, 0, 2],
            4: [11, 3, 12, 5, 7, 4, 8, 0, 2],
            5: [13, 3, 5, 7, 4, 8, 0, 2]
        }
'''
import json
class NFATODFA():
    def __init__(self,Graph,HeadState,TailState) -> None:
        self.NFAGraph = Graph           # 根节点的信息
        self.HeadState = HeadState      # NFA起始状态(int)
        self.TailState = TailState      # NFA终止状态(int)
        self.Director = dict()          # 快速索引,可直接直接由节点名称获取其子节点
        self.AllArc = set()             # 所有的路径,即所有路径上的标签
        self.DFAStates = dict()         # DFA的状态字典
        self.DFAGraph = []              # DFA的树
        self.Preprocess()               # 预处理图
        self.result = None

    def Preprocess(self,root = None):
        # 对图进行预处理
        #   Function1——得到快捷索引(self.Director)
        #   Function2——得到所有的弧的标签(self.AllArc)
        if root == None:
            Childs = self.NFAGraph.get('Next',None)
            self.Director[self.HeadState] = Childs 
        else:
            Childs = root.get('Next',None)
        if Childs == None:
            return
        for i in Childs:
            if i[0] != '#':
                self.AllArc.add(i[0])
            if i[1]['State'] not in list(self.Director.keys()):
                self.Director[i[1]['State']] = i[1]['Next']
                self.Preprocess(i[1])
    
    def Format(self):
        # retrun基本信息
        result = {
            'DFAGraph':self.DFAGraph,
            'DFAStates':self.DFAStates,
            'StartState':None,
            'EndStates':[],
            'GraphInfo':'起始节点  接受符号  到达状态\n',
        }
        for item in self.DFAGraph:
            result['GraphInfo'] += "{0:^6}    {1:^6}    {2:^6}\n".format(item[0],item[1],item[2])
        for key,value in self.DFAStates.items():
            if self.HeadState in value:
                result['StartState'] = key
            if self.TailState in value:
                result['EndStates'].append(key)
        self.result =  result

    def run(self):
        # 执行NFA->DFA的算法
        # 对于起始节点进行空串闭包，得到TO加入到状态栈
        State_Count = 0      # DFA状态计数
        Solve_Queue = []     # 状态机处理队列
        print("###################################")
        print("NFA转DFA↓")
        Init_State = self.e_closure([self.HeadState])
        self.DFAStates[State_Count] = Init_State
        Solve_Queue.append(State_Count)
        State_Count += 1    

        while(Solve_Queue.__len__() != 0 ):
            now_state = Solve_Queue.pop(0)
            now_states = self.DFAStates[now_state]
            for arc in self.AllArc:
                get_states = self.e_closure(self.move(now_states,arc))  
                if len(get_states) == 0:
                    continue
                # 判定字典中是否有这个元素
                IsAdd = True
                for key,value in self.DFAStates.items():
                    if value == get_states:
                        # 有该元素 添加一个路径即可
                        self.DFAGraph.append((now_state,arc,key))
                        IsAdd = False
                if IsAdd == True:
                    self.DFAStates[State_Count] = get_states
                    self.DFAGraph.append((now_state,arc,State_Count))
                    Solve_Queue.append(State_Count)
                    State_Count += 1
        self.Format()
        print("NFA转换结果")
        print(self.result)
        return self.result

    def WriteFile(self):
        # 将信息写入文件
        if self.result == None:
            js = json.dumps('Error')
        js = json.dumps(self.result)
        with open('NFAtoDFA', 'r+') as f:
            f.write(js)


    def move(self,states,arc):
        # 这里定义的是状态集合的弧转换算法
        #   states:表示状态集合,状态集合是一个List,其中的状态指代NFA中的状态
        #   arc:表示转换算法使用的弧
        #   return:是一个状态集合代表转换结果
        TransformList = []
        for state in states:
            # 对寻找state的所有arc弧转换
            Childs = self.Director[state]
            for item in Childs:
                if item[0] == arc:
                    TransformList.append(item[1]['State'])
        print("对状态{0}执行{1}弧转换,结果{2}".format(str(states),str(arc),str(TransformList)))
        return TransformList

    def e_closure(self,states):
        # 这里定义状态集合的空串闭包算法
        #   states:表示状态集合(list),其中的状态指代NFA中的状态
        #   return:是一个状态集合的计算结果
        debugst = set(states)
        waitting = states
        result = []
        while waitting.__len__()!= 0:
            # 提取一个节点state遍历他的所有子节点，寻找空串的连接符
            state = waitting.pop(0)
            result.append(state)
            for child in self.Director[state]:
                if child[0] == '#' and (child[1]['State'] not in waitting) and (child[1]['State'] not in result):
                    waitting.append(child[1]['State'])
        print("对状态{0}执行空串闭包,结果{1}".format( list(debugst), result ))
        return result