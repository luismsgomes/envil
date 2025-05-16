from typing import Optional
import os


__version__ = "0.2.0"


FALSY_STRINGS = {"0", "false", "f", "no", "n"}


class EnvironmentVariableNotSet(Exception):
    def __init__(self, varname: str):
        self.varname: str = varname

    def __str__(self):
        return f"{self.__class__.__name__}({self.varname!r})"


def get_int(varname: str, default: Optional[int]=None) -> int:
    if varname in os.environ:
        return int(os.environ[varname])
    if default is None:
        raise EnvironmentVariableNotSet(varname)
    return default


def get_float(varname, default: Optional[float]=None) -> float:
    if varname in os.environ:
        return float(os.environ[varname])
    if default is None:
        raise EnvironmentVariableNotSet(varname)
    return default


def get_bool(varname, default: Optional[bool]=None, falsy_strings: Optional[set[str]]=None) -> bool:
    if falsy_strings is None:
        falsy_strings = FALSY_STRINGS
    if varname in os.environ:
        return os.environ[varname].lower() not in falsy_strings
    if default is None:
        raise EnvironmentVariableNotSet(varname)
    return default


def get_str(varname, default: Optional[str]=None) -> str:
    if varname in os.environ:
        return os.environ[varname]
    if default is None:
        raise EnvironmentVariableNotSet(varname)
    return default


__all__ = ["EnvironmentVariableNotSet", "get_int", "get_float", "get_bool", "get_str"]
