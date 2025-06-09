from moduls.const import VariableConst

class VariableTools:
    
    @staticmethod
    def compare_to_empty_str(previous: str, current: str)-> str:
        if current in VariableConst.EMPTY_STRING_OPTION:
            return previous
        return current
    
    @staticmethod
    def check_not_empty_str(input: str) -> bool:
        if input in VariableConst.EMPTY_STRING_OPTION:
            return False
        return True
    
    @staticmethod
    def check_id(id: int, name: str = "") -> None:
        if id is None:
            raise ValueError(f"{name} {VariableConst.EXEPTIONS_TEXT['ID_NONE']}")
        if id <= 0:
            raise ValueError(f"{name} {VariableConst.EXEPTIONS_TEXT['ID_NEGATIVE']}")
    
    @staticmethod
    def no_one_can_be_none(*args) -> None:
        for arg in args:
            if arg in VariableConst.EMPTY_STRING_OPTION:
                raise ValueError(f"{VariableConst.EXEPTIONS_TEXT['NO_ONE_CAN_BE_NONE']}: {arg} cannot be None")
            
    @staticmethod
    def no_one_can_be_empty_float(*args) -> None:
        for arg in args:
            if arg in VariableConst.EMPTY_FLOAT_OPTION:
                raise ValueError(f"{VariableConst.EXEPTIONS_TEXT['NO_ONE_CAN_BE_NONE']}")
    
    @staticmethod
    def least_must_be_not_none_float(*args) -> None:
        if all(arg in VariableConst.EMPTY_STRING_OPTION for arg in args):
            raise ValueError(f"{VariableConst.EXEPTIONS_TEXT['NO_ONE_CAN_BE_NONE']}")
    
    @staticmethod
    def one_can_be_not_none(*args) -> None:
        if all(arg in VariableConst.EMPTY_STRING_OPTION for arg in args):
            raise ValueError(f"{VariableConst.EXEPTIONS_TEXT['ONE_CAN_BE_NOT_NONE']}")

