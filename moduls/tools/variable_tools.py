from moduls.const import VariableConst

class VariableTools:
    
    @staticmethod
    def compare_to_empty_str(previous, current)-> str:
        if current in VariableConst.EMPTY_STRING_OPTION:
            return previous
        return current
    
    def check_not_empty_str(input: str) -> bool:
        if input in VariableConst.EMPTY_STRING_OPTION:
            return False
        return True
    
    @staticmethod
    def check_id(id: int, name: str = "") -> None:
        if id is None:
            raise ValueError("{name} id cannot be None")
        if id <= 0:
            raise ValueError("{name} ID must be a positive integer")
    
    @staticmethod
    def no_one_can_be_none(*args) -> None:
        for arg in args:
            if arg in VariableConst.EMPTY_STRING_OPTION:
                raise ValueError("None value is not allowed")
    
    @staticmethod
    def one_can_be_not_none(*args) -> None:
        if all(arg in VariableConst.EMPTY_STRING_OPTION for arg in args):
            raise ValueError("At least one field must be not None")
