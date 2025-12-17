"""
三元计算核心模块
实现三态逻辑(-1, 0, +1)的基础运算
"""

import numpy as np
from typing import Union, List, Tuple, Dict
from dataclasses import dataclass
from enum import IntEnum

class TernaryState(IntEnum):
    """三元状态枚举"""
    FALSE = -1
    UNKNOWN = 0
    TRUE = 1
    
    def __str__(self):
        return self.name

@dataclass
class TernaryValue:
    """三元值封装"""
    value: TernaryState
    
    def __post_init__(self):
        if not isinstance(self.value, TernaryState):
            raise ValueError("值必须是TernaryState枚举")
    
    @classmethod
    def from_float(cls, value: float, 
                   thresholds: Tuple[float, float] = (-0.33, 0.33)) -> 'TernaryValue':
        """从浮点数创建三元值"""
        if value < thresholds[0]:
            return cls(TernaryState.FALSE)
        elif value > thresholds[1]:
            return cls(TernaryState.TRUE)
        else:
            return cls(TernaryState.UNKNOWN)
    
    @classmethod
    def from_bool(cls, value: bool) -> 'TernaryValue':
        """从布尔值创建三元值"""
        return cls(TernaryState.TRUE if value else TernaryState.FALSE)

class TernaryLogic:
    """三元逻辑运算引擎"""
    
    # 真值表定义
    AND_TABLE = {
        (TernaryState.FALSE, TernaryState.FALSE): TernaryState.FALSE,
        (TernaryState.FALSE, TernaryState.UNKNOWN): TernaryState.FALSE,
        (TernaryState.FALSE, TernaryState.TRUE): TernaryState.FALSE,
        (TernaryState.UNKNOWN, TernaryState.FALSE): TernaryState.FALSE,
        (TernaryState.UNKNOWN, TernaryState.UNKNOWN): TernaryState.UNKNOWN,
        (TernaryState.UNKNOWN, TernaryState.TRUE): TernaryState.UNKNOWN,
        (TernaryState.TRUE, TernaryState.FALSE): TernaryState.FALSE,
        (TernaryState.TRUE, TernaryState.UNKNOWN): TernaryState.UNKNOWN,
        (TernaryState.TRUE, TernaryState.TRUE): TernaryState.TRUE,
    }
    
    OR_TABLE = {
        (TernaryState.FALSE, TernaryState.FALSE): TernaryState.FALSE,
        (TernaryState.FALSE, TernaryState.UNKNOWN): TernaryState.UNKNOWN,
        (TernaryState.FALSE, TernaryState.TRUE): TernaryState.TRUE,
        (TernaryState.UNKNOWN, TernaryState.FALSE): TernaryState.UNKNOWN,
        (TernaryState.UNKNOWN, TernaryState.UNKNOWN): TernaryState.UNKNOWN,
        (TernaryState.UNKNOWN, TernaryState.TRUE): TernaryState.TRUE,
        (TernaryState.TRUE, TernaryState.FALSE): TernaryState.TRUE,
        (TernaryState.TRUE, TernaryState.UNKNOWN): TernaryState.TRUE,
        (TernaryState.TRUE, TernaryState.TRUE): TernaryState.TRUE,
    }
    
    NOT_TABLE = {
        TernaryState.FALSE: TernaryState.TRUE,
        TernaryState.UNKNOWN: TernaryState.UNKNOWN,
        TernaryState.TRUE: TernaryState.FALSE,
    }
    
    @staticmethod
    def and_gate(a: Union[TernaryState, TernaryValue], 
                 b: Union[TernaryState, TernaryValue]) -> TernaryState:
        """三元与门"""
        a_val = a.value if isinstance(a, TernaryValue) else a
        b_val = b.value if isinstance(b, TernaryValue) else b
        return TernaryLogic.AND_TABLE[(a_val, b_val)]
    
    @staticmethod
    def or_gate(a: Union[TernaryState, TernaryValue], 
                b: Union[TernaryState, TernaryValue]) -> TernaryState:
        """三元或门"""
        a_val = a.value if isinstance(a, TernaryValue) else a
        b_val = b.value if isinstance(b, TernaryValue) else b
        return TernaryLogic.OR_TABLE[(a_val, b_val)]
    
    @staticmethod
    def not_gate(a: Union[TernaryState, TernaryValue]) -> TernaryState:
        """三元非门"""
        a_val = a.value if isinstance(a, TernaryValue) else a
        return TernaryLogic.NOT_TABLE[a_val]
    
    @staticmethod
    def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        """
        三元矩阵乘法
        
        Args:
            A, B: 三元矩阵，元素应为-1, 0, 1
            
        Returns:
            结果矩阵，元素在[-1, 0, 1]范围内
        """
        m, n = A.shape
        n, p = B.shape
        result = np.zeros((m, p), dtype=int)
        
        for i in range(m):
            for j in range(p):
                sum_val = 0
                for k in range(n):
                    sum_val += A[i, k] * B[k, j]
                # 裁剪到三元范围
                result[i, j] = max(-1, min(1, sum_val))
        
        return result
    
    @staticmethod
    def batch_convert(values: np.ndarray, 
                      thresholds: Tuple[float, float] = (-0.33, 0.33)) -> np.ndarray:
        """批量转换浮点数为三元值"""
        result = np.zeros_like(values, dtype=int)
        result[values < thresholds[0]] = -1
        result[values > thresholds[1]] = 1
        return result

class TernaryNeuron:
    """三元神经元"""
    
    def __init__(self, weights: np.ndarray, bias: float = 0.0):
        self.weights = weights
        self.bias = bias
        self.ternary_logic = TernaryLogic()
    
    def forward(self, inputs: np.ndarray) -> TernaryState:
        """前向传播"""
        # 转换为三元值
        ternary_inputs = self.ternary_logic.batch_convert(inputs)
        
        # 计算加权和
        weighted_sum = np.dot(ternary_inputs, self.weights) + self.bias
        
        # 激活函数
        return TernaryValue.from_float(weighted_sum).value