from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

def flat_arr(lst):
    return list(reduce(lambda a,b: a+b if(isinstance(b,list)) else a+[b],lst,[]))


class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return Program(flat_arr([self.visit(x) for x in ctx.declaration()]))

    def visitDeclaration(self,ctx:MPParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    def visitVarDeclaration(self, ctx:MPParser.VarDeclarationContext):
        return flat_arr([self.visit(x) for x in ctx.varDeclarationList()])


    def visitVarDeclarationList(self, ctx:MPParser.VarDeclarationListContext):
        if ctx.primitiveType():
            id = self.visit(ctx.identifierList())
            priType = self.visit(ctx.primitiveType())
            return list(map(lambda a: VarDecl(a,priType),id))
        else:
            id = self.visit(ctx.identifierList())
            comType = self.visit(ctx.arrDeclaration())
            return list(map(lambda a: VarDecl(a,comType),id))

    def visitArrDeclaration(self,ctx:MPParser.ArrDeclarationContext):
        if ctx.upArrSign():
            low = -int(ctx.INTLIT(0).getText())
        else:
            low = int(ctx.INTLIT(0).getText())
        if ctx.downArrSign():
            up = -int(ctx.INTLIT(1).getText())
        else:
            up = int(ctx.INTLIT(1).getText())
        eleType = self.visit(ctx.primitiveType())
        return ArrayType(low,up,eleType)


    def visitIdentifierList(self, ctx:MPParser.IdentifierListContext):
        return [Id(x.getText()) for x in ctx.identifier()]

    def visitPrimitiveType(self, ctx:MPParser.PrimitiveTypeContext):
        if ctx.INTEGER():
            return IntType()
        elif ctx.REAL():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()

    #def __init__(self, name, param, local, body, returnType=VoidType()):
    def visitFunctionDeclaration(self, ctx: MPParser.FunctionDeclarationContext):
        name = self.visit(ctx.funcName())
        if ctx.parameterList():
            paralist =flat_arr(self.visit(ctx.parameterList()))
        else:
            paralist = []
        type = self.visit(ctx.returnType())

        if ctx.varDeclaration():
            localvar =  self.visit(ctx.varDeclaration())
        else:
            localvar = []

        body = self.visit(ctx.compoundStatement())
        return FuncDecl(name,paralist,localvar,body,type)

    def visitFuncName(self, ctx:MPParser.FuncNameContext):
        return self.visit(ctx.identifier())

    #param: list(VarDecl)
    def visitParameterList(self, ctx:MPParser.ParameterListContext):
        return [self.visit(x) for x in ctx.parameterDeclaration()]

    def visitParameterDeclaration(self, ctx:MPParser.ParameterDeclarationContext):
        id = self.visit(ctx.identifierList())
        type = self.visit(ctx.returnType())
        return list(map(lambda a: VarDecl(a,type),id))

    def visitReturnType(self, ctx:MPParser.ReturnTypeContext):
        return self.visit(ctx.getChild(0))

    #name: Id
    #param: list(VarDecl)
    #returnType: Type => VoidType for Procedure
    #local:list(VarDecl)
    #body: list(Stmt)
    def visitProcedureDeclaration(self, ctx:MPParser.ProcedureDeclarationContext):
        name = self.visit(ctx.procedureName())
        paralist = flat_arr(self.visit(ctx.parameterList())) if ctx.parameterList() else []
        localvar = self.visit(ctx.varDeclaration()) if ctx.varDeclaration() else []
        body = self.visit(ctx.compoundStatement())
        return FuncDecl(name,paralist,localvar,body)

    def visitIdentifier(self, ctx:MPParser.IdentifierContext):
        return Id(ctx.IDENT().getText())

    # STATEMENT
    def visitStatements(self, ctx:MPParser.StatementsContext):
        return flat_arr([self.visit(x) for x in ctx.statement()])

    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitSemiStateRule(self, ctx:MPParser.SemiStateRuleContext):
        return self.visit(ctx.statementwithSemi())

    def visitNonSemiStateRule(self, ctx:MPParser.NonSemiStateRuleContext):
        return self.visit(ctx.statementwithNoSemi())

    def visitStatementwithSemi(self, ctx:MPParser.StatementwithSemiContext):
        if ctx.assignmentStatement():
            return self.visit(ctx.assignmentStatement())
        elif ctx.breakStatement(): # DONE
            return Break()
        elif ctx.continueStatement(): # DONE
            return Continue()
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.callStatement():
            return self.visit(ctx.callStatement())
        # CANNOT USE return self.visit(ctx.getChild(0))

    def visitStatementwithNoSemi(self, ctx:MPParser.StatementwithNoSemiContext):
        return self.visit(ctx.getChild(0))

    def visitLhs(self, ctx:MPParser.LhsContext):
        if ctx.indexExpression():
            return self.visit(ctx.indexExpression())
        else:
            return self.visit(ctx.identifier())

    def visitCompoundStatement(self, ctx:MPParser.CompoundStatementContext):
        return self.visit(ctx.statements()) if ctx.statements() else []

    def visitAssignmentStatement(self, ctx:MPParser.AssignmentStatementContext):
        lhs = [self.visit(x) for x in ctx.lhs()]
        exp = self.visit(ctx.expression())
        lhs.append(exp)
        arr = []
        for i in range(len(lhs)-1,0,-1):
            arr.append(Assign(lhs[i-1],lhs[i]))
        return arr

    #id:Id
    #expr1,expr2:Expr
    #loop:list(Stmt)
    #up:Boolean
    def visitForStatement(self, ctx:MPParser.ForStatementContext):
        id = self.visit(ctx.identifier())
        exp1 = self.visit(ctx.expression(0))
        exp2 = self.visit(ctx.expression(1))
        up = True if ctx.TO() else False
        #loop = ctx.statement()
        loop = flat_arr([self.visit(ctx.statement())])
        return For(id,exp1,exp2,up,loop)

    def visitReturnStatement(self, ctx:MPParser.ReturnStatementContext):
        return (Return(self.visit(ctx.expression())) if ctx.expression() else Return())

    def visitWithStatement(self, ctx:MPParser.WithStatementContext):
        varlist= flat_arr([self.visit(x) for x in ctx.varDeclarationList()])
        stmt = flat_arr([self.visit(ctx.statement())])
        return With(varlist,stmt)

    def visitWhileStatement(self, ctx:MPParser.WhileStatementContext):
        exp = self.visit(ctx.expression())
        stmt = flat_arr([self.visit(ctx.statement())])
        return While(exp,stmt)

    def visitCallStatement(self, ctx:MPParser.CallStatementContext):
        id = self.visit(ctx.identifier())
        explist = self.visit(ctx.expressionList()) if ctx.expressionList() else []
        return CallStmt(id,explist)

    def visitInvocationExpression(self, ctx:MPParser.InvocationExpressionContext):
        id = self.visit(ctx.identifier())
        explist = self.visit(ctx.expressionList()) if ctx.expressionList() else []
        return CallExpr(id,explist)

    def visitExpressionList(self, ctx:MPParser.ExpressionListContext):
        return [self.visit(x) for x in ctx.expression()]


    def visitIfStatement(self, ctx:MPParser.IfStatementContext):
        exp = self.visit(ctx.expression())
        thenstmt = flat_arr([self.visit(ctx.statement(0))])
        elsestmt = flat_arr([self.visit(ctx.statement(1))]) if ctx.ELSE() else []
        return If(exp,thenstmt,elsestmt)

    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visit(ctx.getChild(0))

    def visitCalExpression(self, ctx:MPParser.CalExpressionContext):
        return self.visit(ctx.exp0())


    # def visitExp0(self, ctx:MPParser.Exp0Context):
    #     if ctx.getChildCount() == 4:
    #         op = 'andthen' if ctx.AND() else 'orelse'
    #         exp0 = self.visit(ctx.exp0())
    #         exp1 = self.visit(ctx.exp1())
    #         return BinaryOp(op,exp0,exp1)
    #     else:
    #         return self.visit(ctx.exp1())

    def visitExp0(self, ctx:MPParser.Exp0Context):
        if ctx.getChildCount() == 4:
            op = 'andthen' if ctx.AND() else 'orelse'
            exp0 = self.visit(ctx.exp0(0))
            exp1 = self.visit(ctx.exp0(1))
            return BinaryOp(op,exp0,exp1)
        else:
            return self.visit(ctx.exp1())

    def visitExp1(self, ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 3:
            exp0 = self.visit(ctx.exp2(0))
            exp1 = self.visit(ctx.exp2(1))
            op = self.visit(ctx.relationalOperator())
            return BinaryOp(op,exp0,exp1)
        else:
            return self.visit(ctx.exp2(0))

    def visitExp2(self, ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 3:
            exp0 = self.visit(ctx.exp2())
            exp1 = self.visit(ctx.exp3())
            op = self.visit(ctx.additiveOperator())
            return BinaryOp(op,exp0,exp1)
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 3:
            exp0 = self.visit(ctx.exp3())
            exp1 = self.visit(ctx.exp4())
            op = self.visit(ctx.multiplicativeOperator())
            return BinaryOp(op,exp0,exp1)
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp4())
            return UnaryOp(op,body)
        else:
            return self.visit(ctx.exp6())

    # def visitExp5(self, ctx:MPParser.Exp5Context):
    #     if ctx.getChildCount() == 4:
    #         arr = self.visit(ctx.exp6())
    #         exp = self.visit(ctx.expression())
    #         return ArrayCell(arr,exp)
    #     else:
    #         return self.visit(ctx.exp6())

    def visitExp6(self, ctx:MPParser.Exp6Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp0())
        elif ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.identifier():
            return self.visit(ctx.identifier())
        elif ctx.invocationExpression():
            return self.visit(ctx.invocationExpression())
        else:
            return self.visit(ctx.indexExpression())

    def visitIndexExpression(self, ctx:MPParser):
        return self.visit(ctx.getChild(0))

    def visitIndex1(self, ctx:MPParser.Index1Context):
        id = self.visit(ctx.identifier())
        if ctx.getChildCount() == 7:
            explist = self.visit(ctx.expressionList())
            exp = self.visit(ctx.expression())
            medt = CallExpr(id,explist)
            return ArrayCell(medt,exp)
        elif ctx.getChildCount() == 6:
            explist = []
            exp = self.visit(ctx.expression())
            medt = CallExpr(id,explist)
            return ArrayCell(medt,exp)
        else:
            exp = self.visit(ctx.expression())
            return ArrayCell(id,exp)

    def visitIndex2(self, ctx:MPParser.Index2Context):
            med = self.visit(ctx.expression(0))
            exp = self.visit(ctx.expression(1))
            return ArrayCell(med,exp)


    def visitIndex3(self, ctx:MPParser.Index3Context):
            med = self.visit(ctx.literals())
            exp = self.visit(ctx.expression())
            return ArrayCell(med,exp)


    def visitLiterals(self, ctx:MPParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.REALLIT():
            return FloatLiteral(float(ctx.REALLIT().getText()))
        elif ctx.boollit():
            return self.visit(ctx.boollit())
        else:
            return StringLiteral(ctx.STRINGLIT().getText())

    def visitBoollit(self, ctx:MPParser.BoollitContext):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)


    def visitRelationalOperator(self, ctx:MPParser.RelationalOperatorContext):
        return ctx.getChild(0).getText()

    def visitAdditiveOperator(self, ctx:MPParser.AdditiveOperatorContext):
        return ctx.getChild(0).getText()

    def visitMultiplicativeOperator(self, ctx:MPParser.MultiplicativeOperatorContext):
        return ctx.getChild(0).getText()
