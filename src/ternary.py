"""
Green Computing Architecture - 三元逻辑核心
极简实现版
"""

class TernaryLogic:
    """三元逻辑运算"""
    
    TRUE = 1
    UNKNOWN = 0
    FALSE = -1
    
    @staticmethod
    def AND(a, b):
        """三元与运算"""
        if a == -1 or b == -1:
            return -1
        elif a == 0 or b == 0:
            return 0
        else:
            return 1
    
    @staticmethod
    def OR(a, b):
        """三元或运算"""
        if a == 1 or b == 1:
            return 1
        elif a == 0 or b == 0:
            return 0
        else:
            return -1
    
    @staticmethod
    def NOT(a):
        """三元非运算"""
        return -a
    
    @staticmethod
    def to_ternary(value):
        """将值转换为三元"""
        if value > 0.33:
            return 1
        elif value < -0.33:
            return -1
        else:
            return 0

# 快捷函数
def TAND(a, b):
    return TernaryLogic.AND(a, b)

def TOR(a, b):
    return TernaryLogic.OR(a, b)

def TNOT(a):
    return TernaryLogic.NOT(a)