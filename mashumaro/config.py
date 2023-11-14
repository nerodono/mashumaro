from typing import Any, Callable, Dict, List, Literal, Optional, Type, Union

from mashumaro.core.const import Sentinel
from mashumaro.dialect import Dialect
from mashumaro.types import Discriminator, SerializationStrategy

__all__ = [
    "BaseConfig",
    "TO_DICT_ADD_BY_ALIAS_FLAG",
    "TO_DICT_ADD_OMIT_NONE_FLAG",
    "ADD_DIALECT_SUPPORT",
    "ADD_SERIALIZATION_CONTEXT",
    "SerializationStrategyValueType",
]


TO_DICT_ADD_BY_ALIAS_FLAG = "TO_DICT_ADD_BY_ALIAS_FLAG"
TO_DICT_ADD_OMIT_NONE_FLAG = "TO_DICT_ADD_OMIT_NONE_FLAG"
ADD_DIALECT_SUPPORT = "ADD_DIALECT_SUPPORT"
ADD_SERIALIZATION_CONTEXT = "ADD_SERIALIZATION_CONTEXT"


CodeGenerationOption = Literal[
    "TO_DICT_ADD_BY_ALIAS_FLAG",
    "TO_DICT_ADD_OMIT_NONE_FLAG",
    "ADD_DIALECT_SUPPORT",
    "ADD_SERIALIZATION_CONTEXT",
]


SerializationStrategyValueType = Union[
    SerializationStrategy, Dict[str, Union[str, Callable]]
]


class BaseConfig:
    debug: bool = False
    code_generation_options: List[CodeGenerationOption] = []  # type: ignore
    serialization_strategy: Dict[Any, SerializationStrategyValueType] = {}
    aliases: Dict[str, str] = {}
    serialize_by_alias: bool = False
    namedtuple_as_dict: bool = False
    allow_postponed_evaluation: bool = True
    dialect: Optional[Type[Dialect]] = None
    omit_none: Union[bool, Literal[Sentinel.MISSING]] = Sentinel.MISSING
    omit_default: Union[bool, Literal[Sentinel.MISSING]] = Sentinel.MISSING
    orjson_options: Optional[int] = 0
    json_schema: Dict[str, Any] = {}
    discriminator: Optional[Discriminator] = None
    lazy_compilation: bool = False
    sort_keys: bool = False
    allow_deserialization_not_by_alias: bool = False
