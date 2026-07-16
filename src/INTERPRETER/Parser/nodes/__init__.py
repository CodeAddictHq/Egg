from .statements import (
    ElifStatementNode,
    StatementNode,
    ElseStatementNode,
    FunReturnNode,
    ForLoopNode,
    WhileLoopNode,
    LoopStopNode,
    LoopSkipNode,
    FunCallNode,
    MethodCallNode,
    IfStatementNode,
    FunDefineNode,
    OneNode,
)

from .programe import (
    ProgrameNode,
)

from .opr import (
    BinOpNode,
    BinCompNode,
    BinInNode,
    UnaryOpNode,
)

from .var import (
    ListNode,
    DictNode,
    DictAccessNode,
    DictUpdateNode,
    ListAccessNode,
    ListUpdateNode,
    IdentifierNode,
    StrNode,
    IntNode,
    FloatNode,
    BoolNode,
    VarRmNode,
    VarAssignNode,
    VarDeclNode,
)


# Check all imports
_imports = {
    ElifStatementNode,
    StatementNode,
    ElseStatementNode,
    FunReturnNode,
    ForLoopNode,
    WhileLoopNode,
    LoopStopNode,
    LoopSkipNode,
    FunCallNode,
    IfStatementNode,
    FunDefineNode,
    OneNode,
    ProgrameNode,
    BinOpNode,
    BinCompNode,
    BinInNode,
    UnaryOpNode,
    ListNode,
    DictNode,
    DictAccessNode,
    ListAccessNode,
    IdentifierNode,
    StrNode,
    IntNode,
    FloatNode,
    BoolNode,
    VarRmNode,
    VarAssignNode,
    VarDeclNode,
}

#for item in _imports:
 #   print(f"{item.__name__}: OK")