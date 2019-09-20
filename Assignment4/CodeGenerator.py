'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType(list(), VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):

        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)

        var_lst = [x for x in ast.decl if type(x) is VarDecl]
        func_lst = [x for x in ast.decl if type(x) is FuncDecl]

        for x in var_lst:
            e = self.visit(x, e)

        for i in func_lst:
            lst = [x.varType for x in i.param]
            e.sym.append(Symbol(i.name.name, MType(lst,i.returnType), CName(self.className)))

        for x in func_lst:
            self.visit(x, e)

        # generate default constructor

        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c




    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame


        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name


        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))


        for x in consdecl.param + consdecl.local:
            glenv = self.visit(x,SubBody(frame, glenv.sym))


        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv.sym)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        if ast.name.name.lower()=="main":
            ast.name.name = "main"



        subctxt = o
        frame = Frame(ast.name, ast.returnType)

        self.genMETHOD(ast, subctxt, frame)

        # return SubBody(None, [Symbol(ast.name, MType(lst, ast.returnType), CName(self.className))] + subctxt.sym)

    def visitVarDecl(self, ast, o):
        ctxt = o


        if ctxt.frame is not None:
            frame = ctxt.frame
            index = frame.getNewIndex()
            txt = self.emit.emitVAR(index,ast.variable.name,ast.varType,frame.getStartLabel(), frame.getEndLabel(),frame)
            self.emit.printout(txt)
            return SubBody(ctxt.frame,[Symbol(ast.variable.name, ast.varType, index)]+ctxt.sym)

        else:
            txt = self.emit.emitATTRIBUTE(ast.variable.name,ast.varType,False,None)
            self.emit.printout(txt)
            return SubBody(None, ctxt.sym+[Symbol(ast.variable.name,ast.varType, CName(self.className))])


    def visitWhile(self, ast, o):
        ctxt = o
        frame = o.frame
        sym = o.sym

        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(),frame))

        expcode, exptyp = self.visit(ast.exp, Access(frame, sym, False, True))
        self.emit.printout(expcode)
        self.emit.printout(self.emit.jvm.emitIFEQ(frame.getBreakLabel()))

        list(map(lambda x: self.visit(x, SubBody(frame, sym)), ast.sl))
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))


        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(),frame))
        frame.exitLoop()


    def visitFor(self, ast ,o):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease

        ctxt = o
        frame = ctxt.frame

        frame.enterLoop()

        exp1, exp1typ = self.visit(ast.expr1,Access(frame, ctxt.sym, False, False))
        self.emit.printout(exp1)

        idstore,idtyp = self.visit(ast.id, Access(frame, ctxt.sym, True, False))
        self.emit.printout(idstore)

        idload,idtypnew = self.visit(ast.id, Access(frame, ctxt.sym, False, False))

        # Lan dau tien
        self.emit.printout(idload + self.emit.emitPUSHICONST(1,frame))

        #if up -1, if downto +1
        if ast.up:
            self.emit.printout(self.emit.emitADDOP('-', IntType(), frame))
        else:
            self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))

        self.emit.printout(idstore)

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(), frame))

        exp2, exp2typ = self.visit(ast.expr2,Access(frame, ctxt.sym, False, False))

        if ast.up:
            self.emit.printout(idload + self.emit.emitPUSHICONST(1,frame)+self.emit.emitADDOP('+', IntType(), frame))
            self.emit.printout(idstore)
        else:
            self.emit.printout(idload + self.emit.emitPUSHICONST(1,frame)+self.emit.emitADDOP('-', IntType(), frame))
            self.emit.printout(idstore)

        if ast.up:
            self.emit.printout(idload + exp2 + self.emit.emitREOP("<=", IntType(), frame))
        else:
            self.emit.printout(idload + exp2 + self.emit.emitREOP(">=", IntType(), frame))

        self.emit.printout(self.emit.jvm.emitIFEQ(frame.getBreakLabel()))
        list(map(lambda x: self.visit(x, SubBody(frame, ctxt.sym)), ast.loop))

        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()






    def visitIf(self, ast, o):
        ctxt = o
        frame =  ctxt.frame
        labelExit = frame.getNewLabel()

        exprcode, exptyp = self.visit(ast.expr,Access(frame, ctxt.sym, False, False))
        self.emit.printout(exprcode)

        flagThen = self.checkFuncNoReturn(ast.thenStmt)


        if len(ast.elseStmt) == 0:
            self.emit.printout(self.emit.jvm.emitIFEQ(labelExit))
            list(map(lambda x: self.visit(x, SubBody(frame, ctxt.sym)), ast.thenStmt))
            if not flagThen:
                self.emit.printout(self.emit.emitGOTO(labelExit,frame))


        else:
            labelElse = frame.getNewLabel()
            flagElse = self.checkFuncNoReturn(ast.elseStmt)
            self.emit.printout(self.emit.jvm.emitIFEQ(labelElse))
            list(map(lambda x: self.visit(x, SubBody(frame, ctxt.sym)), ast.thenStmt))

            if not flagThen:
                self.emit.printout(self.emit.emitGOTO(labelExit,frame))


            self.emit.printout(self.emit.emitLABEL(labelElse,frame))
            list(map(lambda x: self.visit(x, SubBody(frame, ctxt.sym)), ast.elseStmt))

            if not flagElse:
                self.emit.printout(self.emit.emitGOTO(labelExit,frame))

        self.emit.printout(self.emit.emitLABEL(labelExit,frame))


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

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame

        sym = self.lookup(ast.method.name.lower(), ctxt.sym, lambda x: x.name.lower())

        for x in ctxt.sym:
            if x.name.lower() == sym.name.lower():
                ast.method.name = x.name
                # print(ast.method.name)

        cname = sym.value.value

        ctype = sym.mtype
        i = 0
        in_ = ("", list())

        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, ctxt.sym, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                 in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1]+[typ1])
            else:
                in_ = (in_[0] + str1, in_[1]+[typ1])
            i += 1
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))


    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        sym = self.lookup(ast.method.name.lower(), ctxt.sym, lambda x: x.name.lower())

        for x in ctxt.sym:
            if x.name.lower() == sym.name.lower():
                ast.method.name = x.name

        cname = sym.value.value

        ctype = sym.mtype
        i = 0
        in_ = ("", list())

        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, ctxt.sym, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                 in_ = (in_[0] + str1 + self.emit.emitI2F(frame), in_[1]+[typ1])
            else:
                in_ = (in_[0] + str1, in_[1]+[typ1])
            i += 1

        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), ctype.rettype





    def visitBreak(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        brkLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(brkLabel,frame))

    def visitContinue(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        conLabel = frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(conLabel,frame))



    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        right,righttyp = self.visit(ast.exp, Access(frame, nenv, False, True))
        left,lefttyp = self.visit(ast.lhs, Access(frame, nenv, True, False))

        self.emit.printout(right)

        if type(righttyp) is IntType and type(lefttyp) is FloatType:
            self.emit.printout(self.emit.emitI2F(frame))

        self.emit.printout(left)
        return


    def visitBinaryOp(self, ast, o):

        ctxt = o
        frame = ctxt.frame
        #lexeme = ast.op
        leftcode, lefttyp = self.visit(ast.left, o)
        rightcode, righttyp = self.visit(ast.right, o)
        retyp = lefttyp
        result = ""

        if ast.op in ['+', '-']:
            if type(lefttyp) is type(righttyp):
                return leftcode + rightcode + self.emit.emitADDOP(ast.op, lefttyp, frame), retyp
            else:
                retyp = FloatType()
                if type(lefttyp) is IntType:
                    return leftcode + self.emit.emitI2F(frame) + rightcode + self.emit.emitADDOP(ast.op, retyp, frame), retyp
                else:
                    return leftcode  + rightcode + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, retyp, frame), retyp
        elif ast.op == '*':
            if type(lefttyp) is type(righttyp):
                return leftcode + rightcode + self.emit.emitMULOP(ast.op, lefttyp, frame), retyp
            else:
                retyp = FloatType()
                if type(lefttyp) is IntType:
                    return leftcode + self.emit.emitI2F(frame) + rightcode + self.emit.emitMULOP(ast.op, retyp, frame), retyp
                else:
                    return leftcode  + rightcode + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, retyp, frame), retyp
        elif ast.op == '/':
            retyp = FloatType()
            if type(lefttyp) is type(righttyp):
                if type(lefttyp) is IntType:
                    return leftcode + self.emit.emitI2F(frame) + rightcode + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, retyp, frame), retyp
                else:
                    return leftcode + rightcode + self.emit.emitMULOP(ast.op, retyp, frame), retyp
            else:
                if type(lefttyp) is IntType:
                    return leftcode + self.emit.emitI2F(frame) + rightcode + self.emit.emitMULOP(ast.op, retyp, frame), retyp
                else:
                    return leftcode + rightcode + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, retyp, frame), retyp

        elif ast.op.lower() == "div":
            return leftcode + rightcode + self.emit.emitDIV(frame), IntType()

        elif ast.op.lower() == "mod":
            return leftcode + rightcode + self.emit.emitMOD(frame), IntType()

        elif ast.op.lower() == "and":
            return leftcode + rightcode + self.emit.emitANDOP(frame), BoolType()

        elif ast.op.lower() == "or":
            return leftcode + rightcode + self.emit.emitOROP(frame), BoolType()

        elif ast.op in ['>','>=','<','<=','<>','=']:
            retyp = BoolType()
            if type(lefttyp) is type(righttyp):
                return leftcode + rightcode + self.emit.emitREOP(ast.op, lefttyp, frame), retyp
            else:
                if type(lefttyp) is IntType:
                    return leftcode + self.emit.emitI2F(frame) + rightcode + self.emit.emitREOP(ast.op, FloatType(), frame), retyp
                else:
                    return leftcode + rightcode + self.emit.emitI2F(frame) + self.emit.emitREOP(ast.op, FloatType(), frame), retyp

        #TODO andthen & orelse
        #if 5 > 3 and then 2 > 1

        elif ast.op.lower() == 'andthen':
            retyp = BoolType()
            labelLz = frame.getNewLabel()
            # labelTh = frame.getNewLabel()
            result += leftcode
            result += self.emit.emitDUP(frame)
            result += self.emit.jvm.emitIFEQ(labelLz)
            result += rightcode
            result += self.emit.emitANDOP(frame)
            result += self.emit.emitLABEL(labelLz,frame)
            return result, retyp

        elif ast.op.lower() == 'orelse':
            retyp = BoolType()
            labelLz = frame.getNewLabel()
            result += leftcode
            result += self.emit.emitDUP(frame)
            result += self.emit.jvm.emitIFNE(labelLz)
            result += rightcode
            result += self.emit.emitOROP(frame)
            result += self.emit.emitLABEL(labelLz,frame)
            return result, retyp



    # TODO: visitWith
    def visitWith(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym

        frame.enterScope(False)
        labelSta = frame.getStartLabel()
        labelEnd = frame.getEndLabel()

        for x in ast.decl:
            # print(type(sym))
            if type(sym) is SubBody:
                sym = self.visit(x,SubBody(frame, sym.sym))
            else:
                sym = self.visit(x,SubBody(frame, sym))

        self.emit.printout(self.emit.emitLABEL(labelSta,frame))

        list(map(lambda x: self.visit(x, SubBody(frame, sym.sym)), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(labelEnd,frame))
        frame.exitScope()

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        unacode,unatyp = self.visit(ast.body,o)

        if ast.op is '-':
            return unacode + self.emit.emitNEGOP(unatyp,frame), unatyp
        if ast.op.lower() == 'not':
            return unacode + self.emit.emitNOT(BoolType(),frame), unatyp


    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        #ast: BooleanLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST('"' + ast.value + '"',StringType(), frame), StringType()



    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        refunctyp = frame.returnType

        if ast.expr:
            expcode,exptyp = self.visit(ast.expr, Access(frame,o.sym,False, True))
            self.emit.printout(expcode)


            if type(exptyp) is not type(refunctyp) and type(refunctyp) is FloatType:
                self.emit.printout(self.emit.emitI2F(frame))

        self.emit.printout(self.emit.emitRETURN(refunctyp,frame))


    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        isLeft = ctxt.isLeft


        sym = self.lookup(ast.name.lower(), ctxt.sym, lambda x: x.name.lower())


        if isLeft:
            if type(sym.value) is CName:
                name = self.className+"/"+sym.name
                return self.emit.emitPUTSTATIC(name,sym.mtype,frame), sym.mtype
            else:
                return self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value,frame), sym.mtype

        else:
            if type(sym.value) is CName:
                name =self.className+"/"+sym.name
                return self.emit.emitGETSTATIC(name,sym.mtype,frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name,sym.mtype,sym.value,frame), sym.mtype
