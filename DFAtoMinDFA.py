import itertools


class DFAtoMinDFA():
    def __init__(self,Graph,Head,Tail):
        self.Graph = Graph          # 输入的图
        self.GraphDict = dict()     # 输入进行预处理转为字典
        self.Head = Head            # 初态
        self.Tail = set(Tail)       # 终态集
        self.AllState = set()       # 图中的所有状态
        self.AllArc = set()         # 图中的所有弧
        self.EqualClass = None      # 等价类(list)
        self.CutResult = None       # 剪除完毕的图
        self.GraphInfo = '起始节点  接受符号  到达状态\n'
        self.Preprocess()

    def Preprocess(self):
        # 对图进行预处理 获取self.AllState、self.AllArc
        for item in self.Graph:
            if item[0] not in list(self.GraphDict.keys()):
                self.GraphDict[item[0]] = dict()
            self.GraphDict[item[0]][item[1]] = item[2]
            self.AllState.add(item[0])
            self.AllState.add(item[2])
            self.AllArc.add(item[1])

    def run(self):
        # 运行
        print("###################################")
        print("DFA转MFA↓")
        print("所有的状态:"+str(self.AllState))
        print("所有的弧:"+str(self.AllArc))
        print("图:"+str(self.Graph))
        print("快速图索引:"+str(self.GraphDict))
        self.Equivalence()
        print("等价类划分结果"+str(self.EqualClass))
        self.CutGraph()
        return self.Format()

    def Format(self):
        for item in self.CutResult:
            self.GraphInfo += "{0:^6}    {1:^6}    {2:^6}\n".format(item[0],item[1],item[2])
        result = {
            'StartState':self.Head,
            'EndStates':self.Tail,
            'GraphInfo':self.GraphInfo,
        }
        return result

    def Equivalence(self):
        # 寻找等价类
        print("划分状态等价类")
        TerminusStates = list(self.Tail)                    # 初始划分
        NOTerminusStates = list(self.AllState - self.Tail)
        result = [NOTerminusStates,TerminusStates]
        Temp = result
        
        nums = itertools.permutations(self.AllArc)
        for arcsss in  nums:
            Count = 0
            while True:
                if Count == result.__len__():
                    break
                result[0],result[Count] = result[Count],result[0]
                print("处理单元:"+str(result)+"Count:" + str(Count))
                for arc in arcsss:
                    now = result.pop(0)
                    External = []
                    Internal = []
                    for item in now:
                        Get_Node = self.GraphDict.get(item,None)
                        if Get_Node == None:
                            Internal.append(item)
                            continue
                        Get_Next = Get_Node.get(arc,None)
                        if Get_Next == None:
                            Internal.append(item)
                            continue
                        if Get_Next in now:
                            Internal.append(item)
                            continue
                        else:
                            External.append(item)
                    if External.__len__()!= 0:
                        result.insert(0,External)
                    if Internal.__len__()!= 0:
                        result.insert(0,Internal)
                    print("对{0}进行转换{1}探测,探测结果内部{2},外部{3}".format(str(now),str(arc),str(Internal),str(External)))
                T1 = Temp
                T2 = result
                T1.sort()
                T2.sort()
                if T2 != T1:
                    Count = 0
                else:
                    Count +=1
        print("划分结果"+str(result))
        self.EqualClass = result

    def CutGraph(self):
        # 对图进行修剪
        scissor = dict()                    # 生成一个字典
        for item in self.EqualClass:        
            # 遍历等价类，选取每个等价类中的代表生成scissor
            scissor[item[0]] = False,None
            for i in item[1:]:
                scissor[i] = True,item[0]
        result = []
        for item in self.Graph:
            # 循环图中的每一条边
            Append = list(item)
            if scissor[item[0]][0]:
                # 如果被合并节点发出了一条边——让主节点发出
                Append[0] = scissor[item[0]][1]

            if scissor[item[2]][0]:
                # 如果被合并的节点收入了一条边——让主节点接收
                Append[2] = scissor[item[2]][1]
            if Append not in result:
                result.append(Append)
        self.CutResult = result
        # 处理起始结点以及终止节点
        if scissor[self.Head][0] is True:
            self.Head = scissor[self.Head][1]
        Temp = []
        for item in self.Tail:
            if scissor[item][0] is True:
                Temp.append(scissor[item][1])
        Temp = list(set(Temp))

if "__main__" == __name__:
    DtoM = DFAtoMinDFA([(0, 'a', 1), (1, 's', 2), (2, 'b', 3)],0,[3])
    DtoM.run()