
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MType([' + ','.join(str(i) for i in self.partype) + ']' + ',' + str(self.rettype) + ')'

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ')'

class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType())),
                   Symbol("putInt",MType([IntType()],VoidType())),
                   Symbol("getFloat",MType([],FloatType())),
                   Symbol("putFloat",MType([FloatType()],VoidType())),
                   Symbol("putFloatLn",MType([FloatType()],VoidType())),
                   Symbol("putBool",MType([BoolType()],VoidType())),
                   Symbol("putBoolLn",MType([BoolType()],VoidType())),
                   Symbol("putString",MType([StringType()],VoidType())),
                   Symbol("putStringLn",MType([StringType()],VoidType())),
                   Symbol("putLn",MType([],VoidType()))]

    # global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def checkRedeclared(self,sym,kind,env):
        if self.lookup(sym.name.lower(),env,lambda x:x.name.lower()):
            raise Redeclared(kind,sym.name)
        else:
            return sym

    def visitProgram(self,ast, c):
        global_lst = []+self.global_envi

        for i in ast.decl:
            if type(i) is VarDecl:
                global_lst.append(self.checkRedeclared(Symbol(i.variable.name,i.varType),Variable(),global_lst))
            else:
                method = i.name.name
                kind = Procedure() if type(i.returnType) is VoidType else Function()
                param = [x.varType for x in i.param]
                reType = i.returnType
                global_lst.append(self.checkRedeclared(Symbol(method,MType(param,reType)),kind,global_lst))
        re = self.lookup("main",global_lst,lambda x: x.name.lower())

        if re is None or type(re.mtype) is not MType or re.mtype.partype or type(re.mtype.rettype) is not VoidType:
            raise NoEntryPoint()
        program_decl = [self.visit(x,global_lst) for x in ast.decl]
        return

    def checkFuncNoReturn(self,list):
        check = False
        for i in list:
            if type(i) is If:
                a = self.checkFuncNoReturn(i.thenStmt)
                b = self.checkFuncNoReturn(i.elseStmt) if i.elseStmt != [] else False
                check = a and b
            if type(i) is With:
                check = self.checkFuncNoReturn(i.stmt)
            if type(i) is Return:
                check = True

        return check

    def visitFuncDecl(self,ast, c):

        method = ast.name.name
        param = []
        for i in ast.param:
            param.append(self.checkRedeclared(Symbol(i.variable.name,i.varType),Parameter(),param))
        for i in ast.local:
            param.append(self.checkRedeclared(Symbol(i.variable.name,i.varType),Variable(),param))

        body = [self.visit(x,(param+c,False,ast.returnType)) for x in ast.body]
        flag = self.checkFuncNoReturn(ast.body)
        # print("test: ", flag)
        if flag == False:
            if type(ast.returnType) is not VoidType:
                raise FunctionNotReturn(method)


        typeParam = [x.varType for x in ast.param]
        return Symbol(method,MType(typeParam,ast.returnType))



    def visitBreak(self,ast,c):
        flag = c[1]
        if not flag:
            raise BreakNotInLoop()



    def visitContinue(sef,ast,c):
        flag = c[1]
        if not flag:
            raise ContinueNotInLoop()

    def visitWith(self,ast,c):
        varlst = []
        for x in ast.decl:
            varlst.append(self.checkRedeclared(Symbol(x.variable.name,x.varType),Variable(),varlst))
        stm = [self.visit(x,(varlst+c[0],c[1],c[2])) for x in ast.stmt]

    def visitVarDecl(self,ast,c):
        name = ast.variable.name
        typ = ast.varType
        return Symbol(name,typ)

    def visitFor(self,ast,c):
        id = self.visit(ast.id,c)
        exp1 = self.visit(ast.expr1,c)
        exp2 = self.visit(ast.expr2,c)
        if type(id) is not IntType or type(exp1) is not IntType or type(exp2) is not IntType:
            raise TypeMismatchInStatement(ast)
        loop = [self.visit(x,(c[0],True,c[2])) for x in ast.loop]

    def visitWhile(self,ast,c):
        exptyp = self.visit(ast.exp,c)
        if type(exptyp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        stm = [self.visit(x,(c[0],True,c[2])) for x in ast.sl]



    def visitIf(self,ast,c):
        exp = self.visit(ast.expr,c)
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        thstm = [self.visit(x,c) for x in ast.thenStmt]
        elstm = [self.visit(x,c) for x in ast.elseStmt]



    def visitAssign(self,ast,c):
        lhstyp = self.visit(ast.lhs,c)
        exptyp = self.visit(ast.exp,c)

        if type(lhstyp) is ArrayType or type(lhstyp) is StringType:
            raise TypeMismatchInStatement(ast)
        if type(lhstyp) is MType:
            if type(lhstyp.rettype) is not type(exptyp) and not (type(lhstyp.rettype) is FloatType and type(exptyp) is IntType):
                raise TypeMismatchInStatement(ast)
        elif type(exptyp) is MType:
            if type(exptyp.rettype) is not type(lhstyp) and not (type(lhstyp) is FloatType and type(exptyp.rettype) is IntType):
                raise TypeMismatchInStatement(ast)
        elif type(lhstyp) is not type(exptyp) and not (type(lhstyp) is FloatType and type(exptyp) is IntType):
            raise TypeMismatchInStatement(ast)


    def visitArrayCell(self,ast,c):
        e1typ = self.visit(ast.arr,c)
        e2typ = self.visit(ast.idx,c)

        if type(e2typ) is not IntType or type(e1typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return e1typ.eleType

    def visitReturn(self,ast,c):
        check = False
        exprtyp = self.visit(ast.expr,c) if ast.expr is not None else None
        if exprtyp is None and type(c[2]) is VoidType:
            check = True
        if type(exprtyp) is type(c[2]):
            if type(exprtyp) is ArrayType:
                if type(exprtyp.eleType) is type(c[2].eleType):
                    if exprtyp.upper == c[2].upper and exprtyp.lower == c[2].lower:
                        check = True
                    else:
                        check = False
            else:
                check = True
        else:
            if type(exprtyp) is IntType and type(c[2]) is FloatType:
                check = True
        if not check:
            raise TypeMismatchInStatement(ast)

        return exprtyp









    def visitBinaryOp(self,ast,c):

        lefttyp = self.visit(ast.left,c)
        righttyp = self.visit(ast.right,c)

        if type(lefttyp) is StringType or type(lefttyp) is ArrayType or type(righttyp) is StringType or type(righttyp) is ArrayType:

            raise TypeMismatchInExpression(ast)
        if ast.op.lower() in ['andthen','orelse','and','or']:
            if type(lefttyp) is not BoolType or type(righttyp) is not BoolType:

                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op in ['>','<','<=','>=','<>','=']:
            if type(lefttyp) is BoolType or type(righttyp) is BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op in ['+','-','*']:

            if type(lefttyp) is BoolType or type(righttyp) is BoolType:

                raise TypeMismatchInExpression(ast)
            if type(lefttyp) is FloatType or type(righttyp) is FloatType:
                return FloatType()
            else:
                return IntType()
        if ast.op.lower() in ['div','mod']:
            if type(lefttyp) is not IntType or type(righttyp) is not IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()
        if ast.op is '/':
            if type(lefttyp) is BoolType or type(righttyp) is BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return FloatType()
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        bodytyp = self.visit(ast.body,c)
        if type(bodytyp) is StringType or type(bodytyp) is ArrayType:
            raise TypeMismatchInExpression(ast)
        if ast.op is '-':
            if type(bodytyp) is BoolType:
                raise TypeMismatchInExpression(ast)
            if type(bodytyp) is FloatType:
                return FloatType()
            else:
                return IntType()
        else:
            # not
            if type(bodytyp) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()


    def visitCallStmt(self,ast,c):

        at = [self.visit(x,c) for x in ast.param]
        # check xem co ton tai method trong list ko?
        res = self.lookup(ast.method.name.lower(),c[0],lambda x: x.name.lower())
        if res is None or type(res.mtype) is not MType or type(res.mtype.rettype) is not VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        # elif len(res.mtype.partype) != len(at) or
        #     print("blablaba")
        #

        #     else:
        if len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)
        if True in [type(a) is ArrayType for a in at] or True in [type(a) is ArrayType for a in res.mtype.partype]:
            for a,b in zip(at,res.mtype.partype):
                if type(a) is ArrayType:
                    if type(a.eleType) is not type(b) and not (type(a.eleType) is IntType and type(b) is FloatType):
                        if type(b) is not ArrayType:
                            raise TypeMismatchInStatement(ast)
                        elif type(a.eleType) is not type(b.eleType) or a.upper != b.upper or a.lower != b.lower:
                            raise TypeMismatchInStatement(ast)
                elif type(b) is ArrayType:
                    if type(b.eleType) is not type(a) and not (type(b.eleType) is FloatType and type(a) is IntType):
                        raise TypeMismatchInStatement(ast)
        for a,b in zip(at,res.mtype.partype):
            if type(a) is not type(b):
                if not(type(a) is IntType and type(b) is FloatType):
                    raise TypeMismatchInStatement(ast)
        return res.mtype.rettype


    def visitCallExpr(self,ast,c):

        at = [self.visit(x,c) for x in ast.param]
        res = self.lookup(ast.method.name.lower(),c[0],lambda x: x.name.lower())


        # for a,b in test:
        #     print(a,b)


        # res chua Symbol(id(name),mtype([],rettype))
        if res is None or type(res.mtype) is not MType or type(res.mtype.rettype) is VoidType:
            raise Undeclared(Function(),ast.method.name)

        elif len(res.mtype.partype) != len(at) or True in [(type(a) != type(b) and not (type(a) is IntType and type(b) is FloatType)) for a,b in zip(at,res.mtype.partype)] or type(res.mtype.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)

        elif True in [type(x) is ArrayType for x in res.mtype.partype]:
            for a,b in zip(at,res.mtype.partype):
                if type(a) is ArrayType:
                    if type(a.eleType) is not type(b.eleType) or (a.lower != b.lower) or (a.upper != b.upper):
                        raise TypeMismatchInExpression(ast)

        return res.mtype.rettype




    def visitId(self,ast,c):
        res = self.lookup(ast.name.lower(),c[0],lambda x:x.name.lower())
        if res:
            if type(res.mtype) is not MType:
                return res.mtype
            else:
                raise Undeclared(Identifier(),ast.name)
        else:
            raise Undeclared(Identifier(),ast.name)


    def visitIntLiteral(self,ast,c):
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    # def visitArrayType(self,ast,c):
    #     return ast
