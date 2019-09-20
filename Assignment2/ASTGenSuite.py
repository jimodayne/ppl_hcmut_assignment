
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_var_decl_1(self):
        """Simple var declaration {} """
        input = """var a,b,c: integer; """
        expect = str(Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_var_decl_2(self):
        """Simple array declaration """
        input = """var a,b,c: array [-1 .. 4] of real;"""
        expect = str(Program([VarDecl(Id('a'),ArrayType(-1,4,FloatType())),VarDecl(Id('b'),ArrayType(-1,4,FloatType())),VarDecl(Id('c'),ArrayType(-1,4,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_func_decl_1(self):
        """More complex program"""
        input = """function foo():INTEGER; begin end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_func_decl_2(self):
        input = """function minmax():boolean;
        var i,j:integer;
           m, k: real;
        begin
        end"""
        expect = str(Program([FuncDecl(Id('minmax'),[],[VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType()),VarDecl(Id('m'),FloatType()),VarDecl(Id('k'),FloatType())],[],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_func_decl_3(self):
        input = """function main(a:real):real;
        var i,j:integer;
        begin
        end"""
        expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType())],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_assign_1(self):
        input = """function foo():integer;
                begin
                    a := 1;
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),IntLiteral(1))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_assign_2(self):
        input = """function main():integer;
                begin
                    i := 1.125;
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('i'),FloatLiteral(1.125))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_assign_3(self):
        input = """function foo():integer;
                begin
                    a := b := c := "dog";
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('c'),StringLiteral('dog')),Assign(Id('b'),Id('c')),Assign(Id('a'),Id('b'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_assign_4(self):
        input = """function main():integer;
                begin
                    anh := da := di := 1/3 + "cuoc doi";
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('di'),BinaryOp(r'+',BinaryOp(r'/',IntLiteral(1),IntLiteral(3)),StringLiteral('cuoc doi'))),Assign(Id('da'),Id('di')),Assign(Id('anh'),Id('da'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_index_1(self):
        input = """function foo():integer;
                begin
                    a := foo()[0];
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(0)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_index_2(self):
        input = """function main():integer;
                begin
                    a := foo(1,2)[0];
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('a'),ArrayCell(CallExpr(Id('foo'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(0)))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_index_3(self):
        input = """function main():integer;
                begin
                    a := arr(1,1)[3+x];
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('a'),ArrayCell(CallExpr(Id('arr'),[IntLiteral(1),IntLiteral(1)]),BinaryOp(r'+',IntLiteral(3),Id('x'))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_index_4(self):
        input = """function foo():integer;
                begin
                    i := a[b[2]];
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[Assign(Id('i'),ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_index_5(self):
        input = """function main():boolean;
                begin
                    ikn := 2[2];
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('ikn'),ArrayCell(IntLiteral(2),IntLiteral(2)))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_index_6(self):
        input = """function main():boolean;
                begin
                    m := 1[2-1];
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(Id('m'),ArrayCell(IntLiteral(1),BinaryOp(r'-',IntLiteral(2),IntLiteral(1))))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_index_7(self):
        input = """function main():string;
                begin
                    m := a[5] := 1.0["null"];
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Assign(ArrayCell(Id('a'),IntLiteral(5)),ArrayCell(FloatLiteral(1.0),StringLiteral('null'))),Assign(Id('m'),ArrayCell(Id('a'),IntLiteral(5)))],StringType())]))
        self.assertTrue(TestAST.test(input,expect,315))


    def test_for_1(self):
        input = """Procedure main();
                begin
                    for a:= 1 downto 10 do begin end
                end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[For(Id('a'),IntLiteral(1),IntLiteral(10),False,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_for_2(self):
        input = """Procedure foo();
                begin
                    for a:= 1 to 10 do begin end
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[For(Id('a'),IntLiteral(1),IntLiteral(10),True,[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_for_3(self):
        input = """Procedure foo();
                begin
                    for a:= 1 to 10 do m:= 1+2;
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[For(Id('a'),IntLiteral(1),IntLiteral(10),True,[Assign(Id('m'),BinaryOp(r'+',IntLiteral(1),IntLiteral(2)))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_for_4(self):
        input = """Procedure foo();
                begin
                    for a:= 5 downto 1 do
                        begin
                            m:= 1+2;
                            n:= False;
                            s := "hom nay toi buon";
                        end
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[For(Id('a'),IntLiteral(5),IntLiteral(1),False,[Assign(Id('m'),BinaryOp(r'+',IntLiteral(1),IntLiteral(2))),Assign(Id('n'),BooleanLiteral(False)),Assign(Id('s'),StringLiteral('hom nay toi buon'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_for_5(self):
        input = """Procedure foo();
                begin
                    for a:= 5 downto 1 do
                        for i:= 1 to 10 do
                            print(i);
                end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[For(Id('a'),IntLiteral(5),IntLiteral(1),False,[For(Id('i'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id('print'),[Id('i')])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_while_1(self):
        input = """procedure jim(a:real);
                begin
                    while a > b do a:=1;
                end"""
        expect = str(Program([FuncDecl(Id('jim'),[VarDecl(Id('a'),FloatType())],[],[While(BinaryOp(r'>',Id('a'),Id('b')),[Assign(Id('a'),IntLiteral(1))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_while_2(self):
        input = """procedure jim(a:real);
                begin
                    while b < (5+2*3) do
                    begin
                        a:=1;
                        foo(2);
                    end
                end"""
        expect = str(Program([FuncDecl(Id('jim'),[VarDecl(Id('a'),FloatType())],[],[While(BinaryOp(r'<',Id('b'),BinaryOp(r'+',IntLiteral(5),BinaryOp(r'*',IntLiteral(2),IntLiteral(3)))),[Assign(Id('a'),IntLiteral(1)),CallStmt(Id('foo'),[IntLiteral(2)])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_while_3(self):
        input = """procedure jim(a:real);
                begin
                    while b < (5+2*3) do
                        while c >= d do
                            fiboo(1,2);
                end"""
        expect = str(Program([FuncDecl(Id('jim'),[VarDecl(Id('a'),FloatType())],[],[While(BinaryOp(r'<',Id('b'),BinaryOp(r'+',IntLiteral(5),BinaryOp(r'*',IntLiteral(2),IntLiteral(3)))),[While(BinaryOp(r'>=',Id('c'),Id('d')),[CallStmt(Id('fiboo'),[IntLiteral(1),IntLiteral(2)])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_while_4(self):
        input = """procedure jim(a:real);
                begin
                    while a > b do
                        for i:= 1 to b do
                            return;
                end"""
        expect = str(Program([FuncDecl(Id('jim'),[VarDecl(Id('a'),FloatType())],[],[While(BinaryOp(r'>',Id('a'),Id('b')),[For(Id('i'),IntLiteral(1),Id('b'),True,[Return(None)])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_complex_assign_1(self):
        input = """
        procedure main();
        var vector: array [-1 .. 3] of integer;
            begin
                vector[1] := vector[2] := vector[3] := 0;
            end
        """
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('vector'),ArrayType(-1,3,IntType()))],[Assign(ArrayCell(Id('vector'),IntLiteral(3)),IntLiteral(0)),Assign(ArrayCell(Id('vector'),IntLiteral(2)),ArrayCell(Id('vector'),IntLiteral(3))),Assign(ArrayCell(Id('vector'),IntLiteral(1)),ArrayCell(Id('vector'),IntLiteral(2)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_complex_assign_2(self):
        input = """
        procedure main();
        var vector: array [1 .. 3] of integer;
            begin
                vector(x+1)[1] := vector[3] := false;
            end
        """
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('vector'),ArrayType(1,3,IntType()))],[Assign(ArrayCell(Id('vector'),IntLiteral(3)),BooleanLiteral(False)),Assign(ArrayCell(CallExpr(Id('vector'),[BinaryOp(r'+',Id('x'),IntLiteral(1))]),IntLiteral(1)),ArrayCell(Id('vector'),IntLiteral(3)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_complex_assign_3(self):
        input = """
        procedure new(x: real);
        var i, j: integer;
            arr: array [1 .. 3] of boolean;
            begin
                i := j := vector[2] := foo()[1] := x;
            end
        """
        expect = str(Program([FuncDecl(Id('new'),[VarDecl(Id('x'),FloatType())],[VarDecl(Id('i'),IntType()),VarDecl(Id('j'),IntType()),VarDecl(Id('arr'),ArrayType(1,3,BoolType()))],[Assign(ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(1)),Id('x')),Assign(ArrayCell(Id('vector'),IntLiteral(2)),ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(1))),Assign(Id('j'),ArrayCell(Id('vector'),IntLiteral(2))),Assign(Id('i'),Id('j'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_call_stmt_1(self):
        input = """
        procedure main(); var i: integer;
            begin
                for i := 1 to 100 do
                begin
                    print("Count: ");
                    push(i);
                end
            end
        """
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('i'),IntType())],[For(Id('i'),IntLiteral(1),IntLiteral(100),True,[CallStmt(Id('print'),[StringLiteral('Count: ')]),CallStmt(Id('push'),[Id('i')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_call_stmt_2(self):
        input = """
        procedure main(); var m: integer;
        begin
            for m := 0 to 10 do
            begin
                if (i mod 2 = 0) then
                    pushInArray(i);
            end
        end
        """
        expect = str(Program([FuncDecl(Id('main'),[],[VarDecl(Id('m'),IntType())],[For(Id('m'),IntLiteral(0),IntLiteral(10),True,[If(BinaryOp(r'=',BinaryOp('mod',Id('i'),IntLiteral(2)),IntLiteral(0)),[CallStmt(Id('pushInArray'),[Id('i')])],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_if_stmt_1(self):
        input = """
        procedure ifFunc(a,b: integer);
            begin
                if a>b then return;
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())],[],[If(BinaryOp(r'>',Id('a'),Id('b')),[Return(None)],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_if_stmt_2(self):
        input = """
        procedure ifFunc();
            begin
                if a>b then a := b;
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[],[],[If(BinaryOp(r'>',Id('a'),Id('b')),[Assign(Id('a'),Id('b'))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_if_stmt_3(self):
        input = """
        procedure ifFunc();
            begin
                if a>b then
                begin
                    a := b;
                    b := False;
                end
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[],[],[If(BinaryOp(r'>',Id('a'),Id('b')),[Assign(Id('a'),Id('b')),Assign(Id('b'),BooleanLiteral(False))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_if_stmt_4(self):
        input = """
        procedure ifFunc();
            begin
                if a>b then for i:= -1 downto 5 do break;
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[],[],[If(BinaryOp(r'>',Id('a'),Id('b')),[For(Id('i'),UnaryOp(r'-',IntLiteral(1)),IntLiteral(5),False,[Break()])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_if_stmt_5(self):
        input = """
        procedure ifFunc();
            begin
                if a>b then a := b; else b:= a;
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[],[],[If(BinaryOp(r'>',Id('a'),Id('b')),[Assign(Id('a'),Id('b'))],[Assign(Id('b'),Id('a'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_if_stmt_6(self):
        input = """
        procedure ifFunc();
            begin
                if a>b then
                begin
                    m := "blabla";
                    for i:= -1 downto 5 do break;
                END
                else return;
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[],[],[If(BinaryOp('>',Id('a'),
        Id('b')),[Assign(Id('m'),StringLiteral('blabla')),For(Id('i'),UnaryOp('-',
        IntLiteral(1)),IntLiteral(5),False,[Break()])],[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_if_stmt_7(self):
        input = """
        procedure ifFunc();
            begin
                if a>b then
                begin
                    m := "blabla";
                    for i:= -1 downto 5 do break;
                END
                else
                begin
                    m := "nlalbla";
                    for n:= 1 to 50 do return;
                END
                return;
            end
        """
        expect = str(Program([FuncDecl(Id('ifFunc'),[],[],
        [If(BinaryOp('>',Id('a'),Id('b')),[Assign(Id('m'),StringLiteral('blabla')),
        For(Id('i'),UnaryOp('-',IntLiteral(1)),IntLiteral(5),False,[Break()])],
        [Assign(Id('m'),StringLiteral('nlalbla')),For(Id('n'),
        IntLiteral(1),IntLiteral(50),True,[Return(None)])]),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_return_1(self):
        input = """
        procedure returnFunc(a,b: integer);
            begin
                if a>b then return 1;
            end
        """
        expect = str(Program([FuncDecl(Id('returnFunc'),
        [VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType())],[],
        [If(BinaryOp('>',Id('a'),Id('b')),[Return(IntLiteral(1))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_return_2(self):
        input = """
        procedure returnFunc(a,b: boolean);
            begin
                if a>b then return false;
            end
        """
        expect = str(Program([FuncDecl(Id('returnFunc'),
        [VarDecl(Id('a'),BoolType()),VarDecl(Id('b'),BoolType())],[],
        [If(BinaryOp('>',Id('a'),Id('b')),
        [Return(BooleanLiteral(False))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))


    def test_return_3(self):
        input = """
        procedure returntestcase9(a,b: string);
            begin
                if m>n then return a > c or else not d >= -1;
            end
        """
        expect = str(Program([FuncDecl(Id('returntestcase9'),
        [VarDecl(Id('a'),StringType()),VarDecl(Id('b'),StringType())],[],
        [If(BinaryOp('>',Id('m'),Id('n')),[Return(BinaryOp('orelse',
        BinaryOp('>',Id('a'),Id('c')),BinaryOp('>=',UnaryOp('not',Id('d')),UnaryOp('-',IntLiteral(1)))))],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_return_4(self):
        input = """
        procedure returntestcase9(a,b: string);
            begin
                if m>n then return a > c or else not d >= -1;
                else return m < 1 and then not (n < m);
            end
        """
        expect = str(Program([FuncDecl(Id('returntestcase9'),
        [VarDecl(Id('a'),StringType()),VarDecl(Id('b'),StringType())],[],
        [If(BinaryOp('>',Id('m'),Id('n')),[Return(BinaryOp('orelse',
        BinaryOp('>',Id('a'),Id('c')),BinaryOp('>=',UnaryOp('not',Id('d')),
        UnaryOp('-',IntLiteral(1)))))],[Return(BinaryOp('andthen',BinaryOp('<',Id('m'),
        IntLiteral(1)),UnaryOp('not',BinaryOp('<',Id('n'),Id('m')))))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_with_1(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin
            with a: integer; do return;
         end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],
        [With([VarDecl(Id('a'),IntType())],[Return(None)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_with_2(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin
            with a: boolean; do
                begin
                    b := 1;
                    with b: string; do
                        a := 1;
                end
         end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[With([VarDecl(Id('a'),BoolType())],
        [Assign(Id('b'),IntLiteral(1)),With([VarDecl(Id('b'),StringType())],
        [Assign(Id('a'),IntLiteral(1))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_with_3(self):
        """Simple program: function with withstatement"""
        input = """function foo(): integer;
         begin
            with a: array [-1 .. 3] of real; do
                begin
                    with b: string; do
                        b := a;
                    break;
                end
         end"""
        expect = str(Program([FuncDecl(Id('foo'),[],[],[With([VarDecl(Id('a'),
        ArrayType(-1,3,FloatType()))],[With([VarDecl(Id('b'),StringType())],
        [Assign(Id('b'),Id('a'))]),Break()])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_with_4(self):
        """Simple program: function with withstatement"""
        input = """function withpro(): integer;
         begin
            with myarr: array [-1 .. 3] of real; c: string; do
                begin
                    with a: integer; do
                        a := "jim";
                    break;
                end
         end"""
        expect = str(Program([FuncDecl(Id('withpro'),[],[],
        [With([VarDecl(Id('myarr'),ArrayType(-1,3,FloatType())),VarDecl(Id('c'),StringType())],
        [With([VarDecl(Id('a'),IntType())],[Assign(Id('a'),StringLiteral('jim'))]),Break()])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_break_1(self):
        """Simple program: function with break"""
        input = """function main(): integer; begin
           break;
         end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Break()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_break_2(self):
        """Simple program: function with break"""
        input = """function main(): integer;
        begin
           break;
           Break;
           BREAK;
        end"""
        expect = str(Program([FuncDecl(Id('main'),[],[],[Break(),Break(),Break()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_continue_1(self):
        """Simple program: function with break"""
        input = """function jim(): integer; begin
           continue;
         end"""
        expect = str(Program([FuncDecl(Id('jim'),[],[],[Continue()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_continue_2(self):
        """Simple program: function with break"""
        input = """function jim(): boolean;
        begin
           continue;
           Continue;
           CONTINUE;
          end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],[Continue(),Continue(),Continue()],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_call_1(self):
        """Simple program: function with break"""
        input = """function jim(): boolean;
        begin
            fibo();
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],
        [CallStmt(Id('fibo'),[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_call_2(self):
        """Simple program: function with break"""
        input = """function jim(): boolean;
        begin
            fibo(1);
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],
        [CallStmt(Id('fibo'),[IntLiteral(1)])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_call_3(self):
        """Simple program: function with break"""
        input = """function jim(): boolean;
        begin
            fibo("string");
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],
        [CallStmt(Id('fibo'),[StringLiteral('string')])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_call_4(self):
        """Simple program: function with break"""
        input = """function jim(): boolean;
        begin
            fibo(1,2,3);
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],[CallStmt(Id('fibo'),
        [IntLiteral(1),IntLiteral(2),IntLiteral(3)])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_call_5(self):
        """Simple program: function with break"""
        input = """function jim(): boolean;
        begin
            fibo(1,2,arr[1]);
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],[CallStmt(Id('fibo'),
        [IntLiteral(1),IntLiteral(2),ArrayCell(Id('arr'),IntLiteral(1))])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_call_6(self):
        """Simple program: function with break"""
        input = """function jim(): string;
        begin
            fibo(min(1,2)[1+x],2,arr[1]);
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],[CallStmt(Id('fibo'),
        [ArrayCell(CallExpr(Id('min'),[IntLiteral(1),IntLiteral(2)]),BinaryOp(r'+',IntLiteral(1),
        Id('x'))),IntLiteral(2),ArrayCell(Id('arr'),IntLiteral(1))])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_call_7(self):
        """Simple program: function with break"""
        input = """function jim(): string;
        begin
            main(12e3,min(1*1/1,-2/3)[-1+x],2,arr[1],a>b and then c>d);
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[],[],[CallStmt(Id('main'),
        [FloatLiteral(12000.0),ArrayCell(CallExpr(Id('min'),[BinaryOp(r'/',
        BinaryOp(r'*',IntLiteral(1),IntLiteral(1)),IntLiteral(1)),
        BinaryOp(r'/',UnaryOp(r'-',IntLiteral(2)),IntLiteral(3))]),
        BinaryOp(r'+',UnaryOp(r'-',IntLiteral(1)),Id('x'))),IntLiteral(2),
        ArrayCell(Id('arr'),IntLiteral(1)),BinaryOp('andthen',
        BinaryOp(r'>',Id('a'),Id('b')),BinaryOp(r'>',Id('c'),Id('d')))])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_call_8(self):
        """Simple program: function with break"""
        input = """function jim(m: real; a: integer): string;
        begin
            foo(x/y+a/b);
         end
        """
        expect = str(Program([FuncDecl(Id('jim'),[VarDecl(Id('m'),FloatType()),
        VarDecl(Id('a'),IntType())],[],[CallStmt(Id('foo'),[BinaryOp(r'+',
        BinaryOp(r'/',Id('x'),Id('y')),BinaryOp(r'/',Id('a'),Id('b')))])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_call_9(self):
        """Simple program: function with break"""
        input = """function tamsu(tuoi: real; ba,muoi: integer): string;
        begin
            foo("em","da","di");
         end
        """
        expect = str(Program([FuncDecl(Id('tamsu'),[VarDecl(Id('tuoi'),FloatType()),
        VarDecl(Id('ba'),IntType()),VarDecl(Id('muoi'),IntType())],[],
        [CallStmt(Id('foo'),[StringLiteral('em'),StringLiteral('da'),StringLiteral('di')])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_call_10(self):
        """Simple program: function with break"""
        input = """function tamsu(tuoi: real; ba,muoi: integer): boolean;
        var artist:string;
        begin
            artisit := "Trinh Thang Binh";
            foo("het",1/3,"quang","doi");
         end
        """
        expect = str(Program([FuncDecl(Id('tamsu'),[VarDecl(Id('tuoi'),FloatType()),
        VarDecl(Id('ba'),IntType()),VarDecl(Id('muoi'),IntType())],
        [VarDecl(Id('artist'),StringType())],[Assign(Id('artisit'),StringLiteral('Trinh Thang Binh')),
        CallStmt(Id('foo'),[StringLiteral('het'),BinaryOp(r'/',IntLiteral(1),IntLiteral(3)),
        StringLiteral('quang'),StringLiteral('doi')])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,359))


    def test_compound_1(self):
    	input = """procedure jim();
		Begin
		end"""
    	expect = str(Program([FuncDecl(Id('jim'),[],[],[],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,360))

    def test_compound_2(self):
    	input = """procedure jim();
		Begin
            Begin
                a:=50;
            End
		end"""
    	expect = str(Program([FuncDecl(Id('jim'),[],[],[Assign(Id('a'),IntLiteral(50))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,361))

    def test_compound_3(self):
    	input = """procedure jim();
		Begin
            Begin
                a:=1;
            End
            Begin
                b:=-2;
            ENd
            Begin
                c:=3;
            End
		end"""
    	expect = str(Program([FuncDecl(Id('jim'),[],[],[Assign(Id('a'),IntLiteral(1)),Assign(Id('b'),UnaryOp(r'-',IntLiteral(2))),Assign(Id('c'),IntLiteral(3))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,362))

    def test_compound_4(self):
    	input = """procedure main();
		Begin
            For i:=1 to 10 do
            Begin
                a:=1;
                Begin
                    b:=-2;
                    Begin
                        c:= "test363";
                    end
                end
            End
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[],[],[For(Id('i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id('a'),IntLiteral(1)),Assign(Id('b'),UnaryOp(r'-',IntLiteral(2))),Assign(Id('c'),StringLiteral('test363'))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,363))

    def test_exp_1(self):
    	input = """procedure jimexp();
		begin
            a:=c or d and c And then e;
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('a'),BinaryOp('andthen',BinaryOp('or',Id('c'),BinaryOp('and',Id('d'),Id('c'))),Id('e')))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,364))

    def test_exp_2(self):
    	input = """procedure jimexp();
		begin
            a:= 2+3;
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('a'),BinaryOp(r'+',IntLiteral(2),IntLiteral(3)))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,365))

    def test_exp_3(self):
    	input = """procedure jimexp();
		begin
            a:= 2+3-1*2+foo(2);
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('a'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(2),IntLiteral(3)),BinaryOp(r'*',IntLiteral(1),IntLiteral(2))),CallExpr(Id('foo'),[IntLiteral(2)])))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,366))

    def test_exp_4(self):
    	input = """procedure jimexp();
		begin
            a:= 2+3-1*2+foo(2)+arr(1,2)[1];
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('a'),BinaryOp(r'+',BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'+',IntLiteral(2),IntLiteral(3)),BinaryOp(r'*',IntLiteral(1),IntLiteral(2))),CallExpr(Id('foo'),[IntLiteral(2)])),ArrayCell(CallExpr(Id('arr'),[IntLiteral(1),IntLiteral(2)]),IntLiteral(1))))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,367))

    def test_exp_5(self):
    	input = """procedure jimexp();
		begin
            i:= (a div b) div m;
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('i'),BinaryOp('div',BinaryOp('div',Id('a'),Id('b')),Id('m')))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,368))

    def test_exp_6(self):
    	input = """procedure jimexp();
		begin
            i:= a div (-b div m);
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('i'),BinaryOp('div',Id('a'),BinaryOp('div',UnaryOp(r'-',Id('b')),Id('m'))))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,369))

    def test_exp_7(self):
    	input = """procedure jimexp();
		begin
            i:= not(true or false);
		end"""
    	expect = str(Program([FuncDecl(Id('jimexp'),[],[],[Assign(Id('i'),UnaryOp('not',BinaryOp('or',BooleanLiteral(True),BooleanLiteral(False))))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,370))

    def test_complex_1(self):
    	input = """procedure main();
		begin
		while main() do
			for i := 0 to 1+1 do
				a := a + 1;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[],[],[While(CallExpr(Id('main'),[]),[For(Id('i'),IntLiteral(0),BinaryOp(r'+',IntLiteral(1),IntLiteral(1)),True,[Assign(Id('a'),BinaryOp(r'+',Id('a'),IntLiteral(1)))])])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,371))

    def test_complex_2(self):
    	input = """procedure main();
		begin
		while main() do
			for i := 0 to 40-1 do
				i := x / 2;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[],[],[While(CallExpr(Id('main'),[]),[For(Id('i'),IntLiteral(0),BinaryOp(r'-',IntLiteral(40),IntLiteral(1)),True,[Assign(Id('i'),BinaryOp(r'/',Id('x'),IntLiteral(2)))])])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,372))

    def test_complex_3(self):
    	input = """procedure main(a:real);
		begin
		if main() then
			for i := 0 to 40-1 do
				i := x / 2;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[If(CallExpr(Id('main'),[]),[For(Id('i'),IntLiteral(0),BinaryOp(r'-',IntLiteral(40),IntLiteral(1)),True,[Assign(Id('i'),BinaryOp(r'/',Id('x'),IntLiteral(2)))])],[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,373))

    def test_complex_4(self):
    	input = """
        function hmm(a,b:real):real;
        var x:string;
        begin
            if i=100 then abc:=a;
            else begin
                i:=a;
                while (a <= a) do
                begin
                    i:=x-c+123;
                end
                abc:=hmm(a+1,x);
            end
        end"""
    	expect = str(Program([FuncDecl(Id('hmm'),[VarDecl(Id('a'),FloatType()),VarDecl(Id('b'),FloatType())],[VarDecl(Id('x'),StringType())],[If(BinaryOp(r'=',Id('i'),IntLiteral(100)),[Assign(Id('abc'),Id('a'))],[Assign(Id('i'),Id('a')),While(BinaryOp(r'<=',Id('a'),Id('a')),[Assign(Id('i'),BinaryOp(r'+',BinaryOp(r'-',Id('x'),Id('c')),IntLiteral(123)))]),Assign(Id('abc'),CallExpr(Id('hmm'),[BinaryOp(r'+',Id('a'),IntLiteral(1)),Id('x')]))])],FloatType())]))
    	self.assertTrue(TestAST.test(input,expect,374))

    def test_complex_5(self):
    	input = """procedure main(a:real);
		begin
		if main() then
			if a < 1 then a := b := 100;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[If(CallExpr(Id('main'),[]),[If(BinaryOp(r'<',Id('a'),IntLiteral(1)),[Assign(Id('b'),IntLiteral(100)),Assign(Id('a'),Id('b'))],[])],[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,375))

    def test_complex_6(self):
    	input = """procedure main(a:real);
		begin
		if main() then
			if a >= 1 then return 100;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[If(CallExpr(Id('main'),[]),[If(BinaryOp(r'>=',Id('a'),IntLiteral(1)),[Return(IntLiteral(100))],[])],[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,376))

    def test_complex_7(self):
    	input = """procedure main(a:real);
		begin
		if main() then
			begin
                if a < 5 then continue;
                print(ifunction(1));
                i := i + 1;
            end
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[If(CallExpr(Id('main'),[]),[If(BinaryOp(r'<',Id('a'),IntLiteral(5)),[Continue()],[]),CallStmt(Id('print'),[CallExpr(Id('ifunction'),[IntLiteral(1)])]),Assign(Id('i'),BinaryOp(r'+',Id('i'),IntLiteral(1)))],[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,377))

    def test_complex_8(self):
    	input = """procedure main(a:real);
		begin
		if main() then
			if a < 1 then a := b := 100;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[If(CallExpr(Id('main'),[]),[If(BinaryOp(r'<',Id('a'),IntLiteral(1)),[Assign(Id('b'),IntLiteral(100)),Assign(Id('a'),Id('b'))],[])],[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,378))

    def test_complex_9(self):
    	input = """procedure main(a:real);
		begin
		    isetcolor("FFFFFFFF");
            light:=ligne+1;
            flag:=false;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[CallStmt(Id('isetcolor'),[StringLiteral('FFFFFFFF')]),Assign(Id('light'),BinaryOp(r'+',Id('ligne'),IntLiteral(1))),Assign(Id('flag'),BooleanLiteral(False))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,379))

    def test_complex_10(self):
    	input = """procedure main(a:real);
		begin
		   with a,i: array[-1 .. 2] of String; m:boolean; do break;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[With([VarDecl(Id('a'),ArrayType(-1,2,StringType())),VarDecl(Id('i'),ArrayType(-1,2,StringType())),VarDecl(Id('m'),BoolType())],[Break()])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,380))

    def test_complex_11(self):
    	input = """procedure main(a:integer);
		begin
		   with a: array[-1 .. 2] of String; m:boolean; do
           Begin
                with i: array[2 .. -1] of real; m:boolean; do break;
           end
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[With([VarDecl(Id('a'),ArrayType(-1,2,StringType())),VarDecl(Id('m'),BoolType())],[With([VarDecl(Id('i'),ArrayType(2,-1,FloatType())),VarDecl(Id('m'),BoolType())],[Break()])])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,381))

    def test_complex_12(self):
    	input = """procedure main(a:integer);
		begin
		   arr[1+x]:=x1;
           arr_function(3,arr+1);
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[Assign(ArrayCell(Id('arr'),BinaryOp(r'+',IntLiteral(1),Id('x'))),Id('x1')),CallStmt(Id('arr_function'),[IntLiteral(3),BinaryOp(r'+',Id('arr'),IntLiteral(1))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,382))

    def test_complex_13(self):
    	input = """procedure main(a:integer);
		begin
		   random(x_a,y_a,arr[x_a]);
           random_int:=random(s[N],dimmention);
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[CallStmt(Id('random'),[Id('x_a'),Id('y_a'),ArrayCell(Id('arr'),Id('x_a'))]),Assign(Id('random_int'),CallExpr(Id('random'),[ArrayCell(Id('s'),Id('N')),Id('dimmention')]))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,383))

    def test_complex_14(self):
    	input = """procedure main(a:integer);
		  begin
              printf("hello");
          end
         var i: array[-1 .. 2] of integer;
		"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[CallStmt(Id('printf'),[StringLiteral('hello')])],VoidType()),VarDecl(Id('i'),ArrayType(-1,2,IntType()))]))
    	self.assertTrue(TestAST.test(input,expect,384))

    def test_complex_15(self):
    	input = """procedure main(m:integer);
		begin
		   if m<0 Then
               n:=-1;
           else
               m:=1;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('m'),IntType())],[],[If(BinaryOp(r'<',Id('m'),IntLiteral(0)),[Assign(Id('n'),UnaryOp(r'-',IntLiteral(1)))],[Assign(Id('m'),IntLiteral(1))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,385))

    def test_complex_16(self):
    	input = """procedure main();
		begin
		While 1 = d Do
            d:=1;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[],[],[While(BinaryOp(r'=',IntLiteral(1),Id('d')),[Assign(Id('d'),IntLiteral(1))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,386))

    def test_complex_17(self):
    	input = """procedure main();
		begin
		If (a / c) <> 1 THEN
            While a = c Do
                A:=1;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[],[],[If(BinaryOp(r'<>',BinaryOp(r'/',Id('a'),Id('c')),IntLiteral(1)),[While(BinaryOp(r'=',Id('a'),Id('c')),[Assign(Id('A'),IntLiteral(1))])],[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,387))

    def test_complex_18(self):
    	input = """procedure main(a:real);
		begin
		if a+b mod 3 =0 then
            println("divi 3");
        else
            print();
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[If(BinaryOp(r'=',BinaryOp(r'+',Id('a'),BinaryOp('mod',Id('b'),IntLiteral(3))),IntLiteral(0)),[CallStmt(Id('println'),[StringLiteral('divi 3')])],[CallStmt(Id('print'),[])])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,388))

    def test_complex_19(self):
    	input = """
        function hmm(a,b:real):real;
        var x:string;
        begin
            With a:real; do
                foo("abc","cbd",m[1]);
        end"""
    	expect = str(Program([FuncDecl(Id('hmm'),[VarDecl(Id('a'),FloatType()),VarDecl(Id('b'),FloatType())],[VarDecl(Id('x'),StringType())],[With([VarDecl(Id('a'),FloatType())],[CallStmt(Id('foo'),[StringLiteral('abc'),StringLiteral('cbd'),ArrayCell(Id('m'),IntLiteral(1))])])],FloatType())]))
    	self.assertTrue(TestAST.test(input,expect,389))

    def test_complex_20(self):
    	input = """
        function jim():real;begin end
        procedure main();begin end
		"""
    	expect = str(Program([FuncDecl(Id('jim'),[],[],[],FloatType()),FuncDecl(Id('main'),[],[],[],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,390))

    def test_complex_21(self):
    	input = """procedure main(name:string);
		begin
		      writeln("Input your name: ");
              read(name);
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('name'),StringType())],[],[CallStmt(Id('writeln'),[StringLiteral('Input your name: ')]),CallStmt(Id('read'),[Id('name')])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,391))

    def test_complex_22(self):
    	input = """procedure main(a:real);
		begin
    		rea:= 1.2+ 3.4-5.6+7.8;
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[Assign(Id('rea'),BinaryOp(r'+',BinaryOp(r'-',BinaryOp(r'+',FloatLiteral(1.2),FloatLiteral(3.4)),FloatLiteral(5.6)),FloatLiteral(7.8)))],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,392))

    def test_complex_23(self):
    	input = """procedure main(a:real);
		begin
		      foo(a(a)[a+b]);
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[CallStmt(Id('foo'),[ArrayCell(CallExpr(Id('a'),[Id('a')]),BinaryOp(r'+',Id('a'),Id('b')))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,393))

    def test_complex_24(self):
    	input = """procedure main(a:real);
		begin
		    while True do
            begin
                break;
                return;
            end
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[While(BooleanLiteral(True),[Break(),Return(None)])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,394))

    def test_complex_25(self):
    	input = """procedure main(a:real);
		begin
    		  For i:=0 To 10 do
              begin end
              For i:=10 To 1 do
              begin end
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),FloatType())],[],[For(Id('i'),IntLiteral(0),IntLiteral(10),True,[]),For(Id('i'),IntLiteral(10),IntLiteral(1),True,[])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,395))

    def test_complex_26(self):
    	input = """procedure main(a:integer);
		begin
		   with a: array[-1 .. 2] of String; m:boolean; do
           Begin
                a:=a(a,b)[a]+123;
                return a;
           end
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[With([VarDecl(Id('a'),ArrayType(-1,2,StringType())),VarDecl(Id('m'),BoolType())],[Assign(Id('a'),BinaryOp(r'+',ArrayCell(CallExpr(Id('a'),[Id('a'),Id('b')]),Id('a')),IntLiteral(123))),Return(Id('a'))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,396))

    def test_complex_27(self):
    	input = """procedure main(a:integer);
		begin
		   nooolll("sallow",2018);
           toString("lady","gaga");
           tellMe("somethinggirl");
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[CallStmt(Id('nooolll'),[StringLiteral('sallow'),IntLiteral(2018)]),CallStmt(Id('toString'),[StringLiteral('lady'),StringLiteral('gaga')]),CallStmt(Id('tellMe'),[StringLiteral('somethinggirl')])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,397))

    def test_complex_28(self):
    	input = """procedure main(a:integer);
		begin
		   println("Enter i: ");
           read();
           println("Enter j: ");
           read();
           println("i + j = ",i+j);
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('a'),IntType())],[],[CallStmt(Id('println'),[StringLiteral('Enter i: ')]),CallStmt(Id('read'),[]),CallStmt(Id('println'),[StringLiteral('Enter j: ')]),CallStmt(Id('read'),[]),CallStmt(Id('println'),[StringLiteral('i + j = '),BinaryOp(r'+',Id('i'),Id('j'))])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,398))

    def test_complex_29(self):
    	input = """procedure jim(a:integer);
		  begin
              if (arr[m]<i) then low:=sallow+1;
              else if (arr[m]>i) then up:=m1;
              else return;
          end
		"""
    	expect = str(Program([FuncDecl(Id('jim'),[VarDecl(Id('a'),IntType())],[],[If(BinaryOp(r'<',ArrayCell(Id('arr'),Id('m')),Id('i')),[Assign(Id('low'),BinaryOp(r'+',Id('sallow'),IntLiteral(1)))],[If(BinaryOp(r'>',ArrayCell(Id('arr'),Id('m')),Id('i')),[Assign(Id('up'),Id('m1'))],[Return(None)])])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,399))

    def test_complex_30(self):
    	input = """procedure main(m:integer);
		begin
		   println("Hello World");
           println("End of Assignment 2");
		end"""
    	expect = str(Program([FuncDecl(Id('main'),[VarDecl(Id('m'),IntType())],[],[CallStmt(Id('println'),[StringLiteral('Hello World')]),CallStmt(Id('println'),[StringLiteral('End of Assignment 2')])],VoidType())]))
    	self.assertTrue(TestAST.test(input,expect,400))
