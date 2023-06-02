# -*- coding: utf-8 -*-
import numpy as np
from typing import Dict, TypeVar, Union

from sympl import DataArray as SymplDataArray
from sympl._core.typingx import PropertyDict as SymplPropertyDict

try:
    import cupy as cp
except ImportError:
    cp = np


DataArray = SymplDataArray
DataArrayDict = Dict[str, DataArray]
ParameterDict = Dict[str, Union[bool, float, int]]
PropertyDict = SymplPropertyDict
Storage = Union[np.ndarray, cp.ndarray]
StorageDict = Dict[str, Storage]
Range = TypeVar("Range")
