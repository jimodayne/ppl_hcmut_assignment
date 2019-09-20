import unittest
from TestUtils import TestChecker
from AST import *
from StaticError import *

class CheckerSuite(unittest.TestCase):
    def test_redeclare_1(self):
        input = """
                var i: integer;
                procedure main();
                begin end
                procedure jim();
                begin
                end
                procedure i();
                begin
                    return;
                end
                """
        expect = 'Redeclared Procedure: i'
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_redeclare_2(self):
        input = """
                var i: integer;
                procedure main();
                begin end
                procedure jim();
                begin
                end
                function jim():integer;
                begin
                    return 6;
                end
                """
        expect = 'Redeclared Function: jim'
        self.assertTrue(TestChecker.test(input,expect,502))
    def test_redeclare_3(self):
        input = """
                var i: integer;
                var i: boolean;
                procedure main();
                begin end
                procedure jim();
                begin
                end
                """
        expect = 'Redeclared Variable: i'
        self.assertTrue(TestChecker.test(input,expect,503))
    def test_redeclare_4(self):
        input = """
                var i,j: real; k,j: integer;
                procedure main();
                begin end
                procedure jim();
                begin
                end
                """
        expect = 'Redeclared Variable: j'
        self.assertTrue(TestChecker.test(input,expect,504))
    def test_redeclare_5(self):
        input = """
                procedure main();
                begin end
                procedure jim(a,b,a: integer);
                begin
                end
                """
        expect = 'Redeclared Parameter: a'
        self.assertTrue(TestChecker.test(input,expect,505))
    def test_redeclare_6(self):
        input = """
                procedure main();
                begin end
                procedure jim(i: boolean;j:real);
                begin
                    with a,b:real;i:integer;b:real; do
                    begin end
                end
                """
        expect = 'Redeclared Variable: b'
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_redeclare_7(self):
        input = """
                procedure main();
                begin end
                procedure jim(jim: boolean;j:real);
                var J: array [1 .. 10] of real;
                begin
                end
                """
        expect = 'Redeclared Variable: J'
        self.assertTrue(TestChecker.test(input,expect,507))

    def test_redeclare_8(self):
        input = """
                procedure main();
                begin end
                procedure jim(i: boolean;j:real;i: string);
                begin
                    putIntLn(4);
                end
                """
        expect = 'Redeclared Parameter: i'
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_redeclare_9(self):
        input = """
                var getint: real;
                procedure main();
                begin end
                procedure jim(i: boolean;j:real);
                begin
                    getInt();
                end
                """
        expect = 'Redeclared Variable: getint'
        self.assertTrue(TestChecker.test(input,expect,509))
    def test_redeclare_10(self):
        input = """
                procedure main();
                begin end
                procedure jim(i: boolean;j:real);
                begin
                    putIntLn(4);
                end
                var putintLN: integer;
                """
        expect = 'Redeclared Variable: putintLN'
        self.assertTrue(TestChecker.test(input,expect,510))

    def test_undeclared_1(self):
        input = """
                procedure main();
                begin
                    a := 1;
                end
                procedure jim(i: boolean;j:real);
                begin
                    putIntLn(4);
                end
                """
        expect = 'Undeclared Identifier: a'
        self.assertTrue(TestChecker.test(input,expect,511))

    def test_undeclared_2(self):
        input = """
            var jim, _jimnew_: integer;
            var dung, nhu, thu, toan: String;
            procedure main();
            begin
                wth := 2 * 3 - 5 div 2;
                _jimnew_ := jim + 10 mod 5;
            end
        """
        expect = "Undeclared Identifier: wth"
        self.assertTrue(TestChecker.test(input,expect,512))

    def test_undeclared_3(self):
        input = """
            function jimnew(param: real):real;
            begin
                param := param + 1;
                return .2003;
            end
            PROCEDURE Main();
            var x: real;
            begin
                x := (not (jimnew(jimnew(jimnew(jimnew(jimnew)))) mod 2) and FALSE OR TRUE) * 1.1111999;
                putInt(x);
                return;
            end
        """
        expect = "Undeclared Identifier: jimnew"
        self.assertTrue(TestChecker.test(input,expect,513))

    def test_undeclared_4(self):
        input = """
            function jim(x:string; y: boolean; z:array [0 .. 10] of string):real;
            var abc, def: integer;
            begin
                if (y and then y) or FALSE then
                begin
                    putstringln(x);
                    abc := def * 5 - 4;
                end
                else
                begin
                    return jimnew;
                end
                return abc;
            end
            procedure main();
            var mnp:real;
                qr: array[0 .. 10] of string;
            begin
                mnp := jim("1", true, qr);
                return;
            end
        """
        expect = "Undeclared Identifier: jimnew"
        self.assertTrue(TestChecker.test(input,expect,514))


    def test_undeclared_5(self):
        input = """
            procedure main();
            var jimnew: integer;
                x: array[0 .. 100] of integer;
            begin
                jimnew := jim();
                jimnew_trl(X, jim(), jim * 1.0);
            end
            function jim():integer;
            var i,j:integer;
                slack: array[0 .. 100] of integer;
            begin
                jimnew_trl(slack, i + j, j + 1);
                return 2 - 1;
            end
            procedure jimnew_trl(s:array[0 .. 100] of integer; m,n:real);
            begin
                putStringLn("Lover in the night!");
                putBool(False and True OR False);
                putIntLn(s[1990]);
            end
        """
        expect = "Undeclared Identifier: jim"
        self.assertTrue(TestChecker.test(input,expect,515))

    def test_undeclared_6(self):
        input = """
            var jimnew, trl: array [1 .. 0] of integer;
            procedure maIN();
            begin
                putFloat(trl[10]);
                putFloatLn(jimnew(trl));
                putStringLn("False");
            end
        """
        expect = "Undeclared Function: jimnew"
        self.assertTrue(TestChecker.test(input,expect,516))

    def test_undeclared_7(self):

        input = """
                    procedure main();
                    begin
                        for i := 1 to 10 do
                            break;
                        return;
                    end"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,517))

    def test_undeclared_8(self):

        input = """
                    procedure main();
                    var c : integer;
                    begin
                        for b := 1 to 2 do
                            for a := 1 to 2 do
                                break;
                        return;
                    end"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,518))

    def test_undeclared_9(self):

        input = """
                    procedure main();
                    var b : integer;
                    begin
                        for b := 1 to 2 do
                            for a := 1 to 2 do
                                break;
                        return;
                    end"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,519))

    def test_undeclared_10(self):
        input = """ procedure main();
                    begin
                        with a: integer; do
                            a := 1;
                        c := 2;
                    end

                    """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,520))

    def test_undeclared_11(self):
        input = """ procedure main();
                    begin
                        with c: integer; do
                            a := 1;
                        c := 2;
                    end

                    """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,521))

    def test_undeclared_12(self):
        input = """ procedure main();
                    var b:integer;
                    begin
                        for b := 1 to 10 do
                            begin
                                with b : integer; do
                                    b := a;
                                c := 1;
                            end
                    end

                    """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,522))

    def test_undeclared_13(self):
        input = """ procedure main();
                    var b:integer;
                    begin
                        for b := 1 to 10 do
                            begin
                                with c: integer; do
                                    b := a;
                                c := 1;
                            end
                    end

                    """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,523))

    def test_undeclared_14(self):

        input = """ function jim(a:integer):array [1 .. 6] of integer;
                    var b: array [1 .. 6] of integer;
                    begin return b; end
                    procedure notMain();
                    var jim:integer;
                    begin
                        jim(1)[jim(1)[3]] := jim;
                    end

                    procedure main();
                    begin end        """
        expect = "Undeclared Function: jim"
        self.assertTrue(TestChecker.test(input,expect,524))

    def test_undeclared_15(self):

        input = """ function jim(a:integer):array [1 .. 9] of integer;
                    var b: array [1 .. 9] of integer;
                    begin return b; end
                    procedure notMain();
                    var jim:integer;
                    begin
                        blablaba(1,2,3,4,5)[jim[2]] := jim;
                    end

                    procedure main();
                    begin end        """
        expect = "Undeclared Function: blablaba"
        self.assertTrue(TestChecker.test(input,expect,525))

    def test_undeclared_16(self):
        input = """
        function b(): real;
        begin return 0; end
        procedure main();
        var b: real;
        begin
            b := b();
        end
        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,526))

    def test_undeclared_17(self):
        input = """
        procedure main();
        begin
            putIntLn(a);
        end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 527))

    def test_undeclared_18(self):
        input = """
        procedure main();
        begin
            putFloat(i);
        end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 528))

    def test_undeclared_19(self):
        input = """
        procedure jim();
        begin end
        procedure main();
        var i: integer; j: boolean;
        begin
            i := getInt();
            j := jim();
        end
        """
        expect = "Undeclared Function: jim"
        self.assertTrue(TestChecker.test(input, expect,529))

    def test_undeclared_20(self):
        input = """
        procedure main();
        begin
            with jim: integer; do i := 10;
            jim := 0;
        end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect,530))

    def test_missmatch_exp_1(self):
        input = """ procedure main();
                    var a: integer;
                    begin
                        a[2] := 1;
                    end

                    """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,531))

    def test_missmatch_exp_2(self):
        input = """ procedure main();
                    var a,b: real;
                    begin
                        a := 1.0;
                        b[1] := 1;
                    end

                    """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,532))

    def test_missmatch_exp_3(self):
        input = """ procedure main();
                    var arr: array [1 .. 9] of integer;
                        brr:integer;
                    begin
                        arr[1] := 1;
                        brr[2] := 1;
                    end

                    """
        expect = "Type Mismatch In Expression: ArrayCell(Id(brr),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,533))

    def test_missmatch_exp_4(self):
        input = """
        var i:integer;
        procedure main();
        var x,arr: integer;
        begin
            x := arr[i];
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 534))

    def test_missmatch_exp_5(self):
        input = """
        procedure main();
        var x, y: real;
        begin
            x := arr()[5] := 73.0;
            y := arr()[2.25];
        end

        function arr(): array [1 .. 5] of real;
        var arr: array [1 .. 5] of real;
        begin
            return arr;
        end

        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(arr),[]),FloatLiteral(2.25))"
        self.assertTrue(TestChecker.test(input, expect, 535))


    def test_missmatch_exp_6(self):
        input = '''
            var t: integer;
            procedure main();
            var arr: array[0 .. 10] of integer;
            begin
                if arr[1.5] + 50 * 10 then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input,expect,536))

    def test_missmatch_exp_7(self):
        input = '''
            var t: integer;
            procedure main();
            begin
                t := (jim() + 3)[jim() + 3] / 4 / 5;
            end

            function jim():integer;
            begin
                return 1;
            end
        '''
        expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(+,CallExpr(Id(jim),[]),IntLiteral(3)),BinaryOp(+,CallExpr(Id(jim),[]),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,537))

    def test_missmatch_exp_8(self):
        input = """
        procedure main();
        var x: integer;
        begin
            x := -1;
            x := not 2;
        end
        """
        expect = "Type Mismatch In Expression: " + str(UnaryOp("not", IntLiteral(2)))
        self.assertTrue(TestChecker.test(input, expect, 538))


    def test_missmatch_exp_9(self):
        input = """
        procedure main();
        var a:integer;
        begin
            a := jimnew(a, a);
        end
        function jimnew(a:integer; b:boolean):integer;
                    begin return 1; end

                    """
        expect = "Type Mismatch In Expression: CallExpr(Id(jimnew),[Id(a),Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,539))

    def test_missmatch_exp_10(self):
        input = """
        procedure main();
        var a: integer; y: real; z: boolean;
        begin
            y := -a;
            z := -z;
        end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 540))

    def test_missmatch_exp_11(self):
        input = '''
            procedure main();
            var a: real;
                b: integer;
            begin
                while not ("wtf" + "daf") > (4 / 5) do
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(wtf),StringLiteral(daf))"
        self.assertTrue(TestChecker.test(input,expect,541))

    def test_missmatch_exp_12(self):
        input = '''
            procedure main();
            begin
                if sumup(21, 19) then
                    return;
            end
            function sumup(a,b,c,d:integer):integer;
            begin
                return a+b+c+d;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sumup),[IntLiteral(21),IntLiteral(19)])"
        self.assertTrue(TestChecker.test(input,expect,542))

    def test_missmatch_exp_13(self):
        input = """
                procedure jimnew(x:real;y:integer);
                begin
                    return;
                end
                var arr,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 5] of real;
                begin
                    jimnew(1.5,2);
                    c := d[b] := d[c];
                end
                """
        expect = 'Type Mismatch In Expression: ArrayCell(Id(d),Id(c))'

        self.assertTrue(TestChecker.test(input,expect,543))

    def test_missmatch_exp_14(self):
        input = """
                var c: real; d: array[1 .. 5] of real;
                procedure main();
                begin
                    c[2] := 2.0;
                    jimnew(9,8);
                    d[a] := 0.3;

                end
                procedure jimnew(x:real;y:integer);
                var a,b: integer; c: boolean; d: string;
                begin
                    return;
                end
                """
        expect = 'Type Mismatch In Expression: ArrayCell(Id(c),IntLiteral(2))'
        self.assertTrue(TestChecker.test(input,expect,544))

    def test_missmatch_exp_15(self):
        input = '''
            function blablaa(a,b,c:integer):integer;
            begin
                return a + b + c;
            end
            procedure main();
            begin
                if blablaa(11, 11) then
                    return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(blablaa),[IntLiteral(11),IntLiteral(11)])"
        self.assertTrue(TestChecker.test(input,expect,545))

    def test_missmatch_exp_16(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 9] of real;
                begin
                    jimnew(7)[12] := b;
                    jimnew(8)[jimnew(1)[2]+c] := 1;
                end
                function jimnew(x:integer):array[1 .. 5] of integer;
                var a: array[1 .. 5] of integer; i: integer;
                begin
                    for i := 1 to 100 do
                        a[i] := i;
                    return a;
                end
                """
        expect = 'Type Mismatch In Expression: ArrayCell(CallExpr(Id(jimnew),[IntLiteral(8)]),BinaryOp(+,ArrayCell(CallExpr(Id(jimnew),[IntLiteral(1)]),IntLiteral(2)),Id(c)))'

        self.assertTrue(TestChecker.test(input,expect,546))

    def test_missmatch_exp_17(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 9] of real;
                begin
                    jimnew(7)[2+d[1]] := b;
                end
                function jimnew(x:integer):array[1 .. 5] of integer;
                var a: array[1 .. 5] of integer; i: integer;
                begin
                    for i := 1 to 100 do
                        a[i] := i;
                    return a;
                end
                """
        expect = 'Type Mismatch In Expression: ArrayCell(CallExpr(Id(jimnew),[IntLiteral(7)]),BinaryOp(+,IntLiteral(2),ArrayCell(Id(d),IntLiteral(1))))'

        self.assertTrue(TestChecker.test(input,expect,547))

    def test_missmatch_exp_18(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 9] of real; e: real;
                begin
                    e := c + d[1] - a;
                    e := c + d[1] * d;
                end
                function jimnew(x:integer):array[1 .. 5] of integer;
                var a: array[1 .. 5] of integer; i: integer;
                begin
                    for i := 1 to 100 do
                        a[i] := i;
                    return a;
                end
                """
        expect = 'Type Mismatch In Expression: BinaryOp(*,ArrayCell(Id(d),IntLiteral(1)),Id(d))'

        self.assertTrue(TestChecker.test(input,expect,548))

    def test_missmatch_exp_19(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 9] of real; e: real;
                begin
                    e := c + d[1] - a;
                    e := (jimnew(7)[12] - 2.5) div 15;
                end
                function jimnew(x:integer):array[1 .. 5] of integer;
                var a: array[1 .. 5] of integer; i: integer;
                begin
                    for i := 1 to 100 do
                        a[i] := i;
                    return a;
                end
                """
        expect = 'Type Mismatch In Expression: BinaryOp(div,BinaryOp(-,ArrayCell(CallExpr(Id(jimnew),[IntLiteral(7)]),IntLiteral(12)),FloatLiteral(2.5)),IntLiteral(15))'
        self.assertTrue(TestChecker.test(input,expect,549))

    def test_missmatch_exp_20(self):
        input = '''
            function sum(a,b,c,d:integer):integer;
            begin
                return a + b + c + d;
            end
            procedure main();
            begin
                while sum(22, 20, 33) do
                    break;
                return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[IntLiteral(22),IntLiteral(20),IntLiteral(33)])"
        self.assertTrue(TestChecker.test(input,expect,550))

    def test_missmatch_exp_21(self):
        input = '''
            function sum(a,b,c,d:integer):real;
            begin
                return a + b + c + d;
            end
            procedure main();
            begin
                while sum(22, 20, 33, True) do
                    break;
                return;
            end
        '''
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[IntLiteral(22),IntLiteral(20),IntLiteral(33),BooleanLiteral(True)])"
        self.assertTrue(TestChecker.test(input,expect,551))

    def test_missmatch_exp_22(self):
        input = """
        function boo(): string;
        begin
            return "Jim is " + "Handsome";
        end
        procedure main();
        var i: string;
        begin end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(Jim is ),StringLiteral(Handsome))"
        self.assertTrue(TestChecker.test(input, expect, 552))

    def test_missmatch_exp_23(self):
        input = """
        procedure main();
        var i: string;
        begin end

        function boo(): string;
        begin
            return "Jim is " + "verryy Handsome";
        end

        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(Jim is ),StringLiteral(verryy Handsome))"
        self.assertTrue(TestChecker.test(input, expect, 553))

    def test_missmatch_exp_24(self):
        input = """
        procedure main();
        var a: boolean;
        begin
            a := a and 0;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 554))

    def test_missmatch_exp_25(self):
        input = """
        procedure main();
        var a, b: boolean;
        begin
            a := a or b;
            b := 1 and 0;
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,IntLiteral(1),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 555))

    def test_missmatch_stm_1(self):
        input = """
        procedure main();
        var j, x, y: integer; i: real;
        begin
            i := i + 20.0 - 100;
            if (x <> y) then j := i;
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(j),Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 556))

    def test_missmatch_stm_2(self):
        input = """
                procedure main();
                var c: string;
                begin
                    c := "something";
                end
                function jim(x:integer):real;
                begin
                    return 1;
                end
                var a,b: integer; c: boolean; d: string;
                """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(c),StringLiteral(something))'
        self.assertTrue(TestChecker.test(input, expect, 557))

    def test_missmatch_stm_3(self):
        input = """
                procedure main();
                var c: string;
                begin
                    c := a := "the new here";
                end
                function jimnew(x:integer):real;
                begin
                    return 2;
                end
                var a,b: integer; c: boolean; d: string;
                """
        expect = 'Type Mismatch In Statement: AssignStmt(Id(a),StringLiteral(the new here))'
        self.assertTrue(TestChecker.test(input, expect, 558))

    def test_missmatch_stm_4(self):
        input = """
        procedure main();
        var a: real;
        begin
            if a + 1 then begin end
        end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(1)),[],[])"

        self.assertTrue(TestChecker.test(input, expect, 559))

    def test_missmatch_stm_5(self):
        input = """
        procedure main();
        var boo: real;
        begin
            if boo + 10.0 then begin end
        end
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(boo),FloatLiteral(10.0)),[],[])"
        self.assertTrue(TestChecker.test(input, expect, 560))

    def test_missmatch_stm_6(self):
        input = """procedure main();
                   begin return True; end"""
        expect = "Type Mismatch In Statement: Return(Some(BooleanLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,561))

    def test_missmatch_stm_7(self):
        input = """procedure main();
                   begin return 100; end"""
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(100)))"
        self.assertTrue(TestChecker.test(input,expect,562))

    def test_missmatch_stm_8(self):

        input = """
                   function boo():integer;
                   begin return 9/4.35; end

                   procedure main();
                   begin return; end"""
        expect = "Type Mismatch In Statement: Return(Some(BinaryOp(/,IntLiteral(9),FloatLiteral(4.35))))"
        self.assertTrue(TestChecker.test(input,expect,563))


    def test_missmatch_stm_9(self):
        input = """
                   procedure main();
                   begin return; end

                   function boo():integer;
                   begin return 1/1; end
                   """
        expect = "Type Mismatch In Statement: Return(Some(BinaryOp(/,IntLiteral(1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,564))

    def test_missmatch_stm_10(self):
        input = """
                procedure main();
                var a,b: integer; c: boolean; d: string;
                begin
                    if 3.25 then
                    begin
                        if (c) then
                        begin end
                    end
                end
                """
        expect = 'Type Mismatch In Statement: If(FloatLiteral(3.25),[If(Id(c),[],[])],[])'
        self.assertTrue(TestChecker.test(input,expect,565))

    def test_missmatch_stm_11(self):
        input = """
                procedure main();
                var a,b: integer; c: boolean; d: string;
                begin
                    if ("snsd") then
                    begin
                        if (c) then
                        begin end
                    end
                end
                """
        expect = 'Type Mismatch In Statement: If(StringLiteral(snsd),[If(Id(c),[],[])],[])'
        self.assertTrue(TestChecker.test(input,expect,566))

    def test_missmatch_stm_12(self):
        input = '''
            procedure main();
            begin end
            procedure CC16KHM(leader:String);
            var isNhu: boolean;
                i: real;
            begin
                with j, i: integer; do
                begin
                    for i := j to j div 10 do
                        if isNhu then break;
                    return leader;
                end
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(Id(leader)))"
        self.assertTrue(TestChecker.test(input,expect,567))

    def test_missmatch_stm_12(self):
        input = '''
            procedure main();
            begin end
            procedure CC16KHM(leader:String);
            var isNhu: boolean;
                i: real;
            begin
                with j, i: integer; do
                begin
                    for i := j to j div 10 do
                        if isNhu then break;
                    return 2;
                end
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,568))

    def test_missmatch_stm_13(self):
        input = '''
            procedure main();
            begin end
            procedure CC16KHM(leader:String);
            var isNhu: boolean;
                i: real;
            begin
                with j, i: integer; do
                begin
                    for i := j to j div 10 do
                        if isNhu then break;
                    return True;
                end
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(BooleanLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,569))

    def test_missmatch_stm_14(self):
        input = '''
            procedure main();
            begin end
            procedure CC16KHM(leader:String);
            var isNhu: boolean;
                i: real;
            begin
                with j, i: integer; do
                begin
                    for i := j to j div 10 do
                        if isNhu then break;
                    return "True";
                end
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(StringLiteral(True)))"
        self.assertTrue(TestChecker.test(input,expect,568))

    def test_missmatch_stm_15(self):
        input = '''
            procedure main();
            begin end
            procedure CC16KHM(leader:String);
            var isNhu: boolean;
                i: real;
            begin
                with j, i: integer; do
                begin
                    for i := j to j div 10 do
                        if isNhu then break;
                    return 9.9;
                end
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(9.9)))"
        self.assertTrue(TestChecker.test(input,expect,568))

    def test_missmatch_stm_16(self):
        input = """
                var b: integer;
                procedure main();
                var a: integer;
                begin
                    for a := 1 to 10 do
                    begin end
                    for a := 1.0 to 10.0 do
                    begin
                        putIntLn(1);
                    end
                end
                """
        expect = 'Type Mismatch In Statement: For(Id(a),FloatLiteral(1.0),FloatLiteral(10.0),True,[CallStmt(Id(putIntLn),[IntLiteral(1)])])'
        self.assertTrue(TestChecker.test(input,expect,569))

    def test_missmatch_stm_16(self):
        input = """
                var b: integer;
                procedure main();
                var a: integer;
                begin
                    for a := 1 to 7 do
                    begin end
                    for a := 1 to 5.0 do
                    begin
                        putIntLn(1);
                    end
                end
                """
        expect = 'Type Mismatch In Statement: For(Id(a),IntLiteral(1),FloatLiteral(5.0),True,[CallStmt(Id(putIntLn),[IntLiteral(1)])])'
        self.assertTrue(TestChecker.test(input,expect,570))

    def test_missmatch_stm_16(self):
        input = """
                var b: integer;
                procedure main();
                var a: integer;
                begin
                    for a := 1 to 7 do
                    begin end
                    for a := 1 to True do
                    begin
                        putFloat(1.0);
                    end
                end
                """
        expect = 'Type Mismatch In Statement: For(Id(a),IntLiteral(1),BooleanLiteral(True),True,[CallStmt(Id(putFloat),[FloatLiteral(1.0)])])'
        self.assertTrue(TestChecker.test(input,expect,571))

    def test_missmatch_stm_17(self):
        input = """
                var b: integer;
                procedure main();
                var a: integer;
                begin
                    for a := 1 to 7 do
                    begin end
                    for a := 1 to "true" do
                    begin
                        putSTring("1");
                    end
                end
                """
        expect = 'Type Mismatch In Statement: For(Id(a),IntLiteral(1),StringLiteral(true),True,[CallStmt(Id(putSTring),[StringLiteral(1)])])'
        self.assertTrue(TestChecker.test(input,expect,572))

    def test_missmatch_stm_18(self):
        input = '''
            var t: array[1 .. 9] of integer;
                a,b:integer;
            procedure main();
            var boo: real;
            begin
                boo := func(t);
            end
            function Func(ab: array[1 .. 9] of integer):integer;
            var t: integer;
            begin
                ab[ab[10]] := t := 10;
                return a>b;
            end
        '''
        expect = "Type Mismatch In Statement: Return(Some(BinaryOp(>,Id(a),Id(b))))"
        self.assertTrue(TestChecker.test(input,expect,573))

    def test_missmatch_stm_19(self):
        input = '''
            var t: array[1 .. 9] of integer;
            procedure main();
            var boo: real;
            begin
                boo := func(t);
            end
            function Func(ab: array[1 .. 9] of integer):integer;
            var t: integer;
            begin
                ab[ab[9]] := t := 10;
                return 2/1-5*6 or 1+2 = 3;
            end
        '''
        expect = "Type Mismatch In Expression: BinaryOp(or,BinaryOp(-,BinaryOp(/,IntLiteral(2),IntLiteral(1)),BinaryOp(*,IntLiteral(5),IntLiteral(6))),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,574))

    def test_missmatch_stm_20(self):
        input = '''
            var t: array[1 .. 9] of integer;
            procedure main();
            var boo: real;
            begin
                boo := func(t);
            end
            function Func(ab: array[1 .. 9] of integer):integer;
            var t: integer;
            begin
                ab[ab[20]] := t := 10;
                return "alooo"+"im jim";
            end
        '''
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(alooo),StringLiteral(im jim))"
        self.assertTrue(TestChecker.test(input,expect,575))

    def test_not_ret_1(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 12313] of real;
                begin
                    c := 1.5 * jimnew(1.5,2.2);
                end
                function jimnew(x,y:real):real;
                begin

                end
                """
        expect = 'Function jimnew Not Return'
        self.assertTrue(TestChecker.test(input,expect,576))

    def test_not_ret_2(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 12313] of real;
                begin
                    c := 1.5 * jimnew(1.5,2.2);
                end
                function jimnew(x,y:real):real;
                begin
                    putIntLn(15);
                    putFloat(1.5);
                end
                """
        expect = 'Function jimnew Not Return'
        self.assertTrue(TestChecker.test(input,expect,577))

    def test_not_ret_3(self):
        input = """
                var a,b: integer; c: boolean; d: string;
                procedure main();
                var c: real; d: array[1 .. 12313] of real;
                begin
                    c := 1.5 * jimnew(1.5,2.2);
                end
                function jimnew(x,y:real):real;
                begin
                    putIntLn(15);
                end
                """
        expect = 'Function jimnew Not Return'
        self.assertTrue(TestChecker.test(input,expect,578))

    def test_not_ret_4(self):
        input = """
        function boo(): integer;
        begin end
        procedure main();
        begin end
        """
        expect = "Function boo Not Return"
        self.assertTrue(TestChecker.test(input, expect, 579))

    def test_not_ret_5(self):
        input = '''
            function boo(a,b:integer;c:real):integer;
            begin
                putStringLn("Hello, this is boo function");
                c := a := b := 10;
                if a = b then
                    return 0;
                for a := b to a + b do
                    return 0;
                while a < 10 do
                    return 0;
            end
            procedure main();
            var otr: integer;
            begin
                otr := boo(0, 8, 7.5);
            end
        '''
        expect = "Function boo Not Return"
        self.assertTrue(TestChecker.test(input,expect,580))

    def test_not_ret_6(self):
        input = """

        procedure main();
        begin end

        function lamdbdaaa(): integer;
        begin
            while (true) do return 1;

        end
        function countt(): integer;
        var i: integer;
        begin
            for i := 0 to 1 do return i;
        end

        """
        expect = "Function lamdbdaaa Not Return"
        self.assertTrue(TestChecker.test(input, expect, 581))

    def test_not_ret_8(self):
        input = """

        procedure main();
        begin end

        function lamdbdaaa(): integer;
        begin
            while (true) do return 1;
            return 0;
        end

        function countt(): integer;
        var i: integer;
        begin
            for i := 0 to 1 do return i;
        end

        """
        expect = "Function countt Not Return"
        self.assertTrue(TestChecker.test(input, expect, 582))

    def test_not_ret_9(self):
        input = """

        procedure main();
        var c: real; d: array[1 .. 12313] of real;
        begin
            c := 1.5 * jimnew(1.5,2.2);
        end
            var a,b: integer; c: boolean; d: string;

            function jimnew(x,y:real):real;
            var i: integer;
            begin
                i := 0;
                if a <> b then
                    return 7;
                return 5;
            end

            function boo(x:integer):boolean;
            begin
                if a < b then
                    return 2 < x;
                else
                    with x: boolean; do
                        if a >= b then
                            return x;
                putIntLn(22);
            end
                """
        expect = 'Function boo Not Return'
        self.assertTrue(TestChecker.test(input, expect, 583))

    def test_not_ret_7(self):
        input = """

        procedure main();
        var c: real; d: array[1 .. 12313] of real;
        begin
            c := 1.5 * jimnew(1.5,2.2);
        end
            var a,b: integer; c: boolean; d: string;

            function jimnew(x,y:real):real;
            var i: integer;
            begin
                i := 0;
                if a <> b then
                    return 7;
            end

            function boo(x:integer):boolean;
            begin
                if a < b then
                    return 2 < x;
                else
                    with x: boolean; do
                        if a >= b then
                            return x;
                putIntLn(22);
                return;
            end
                """
        expect = 'Function jimnew Not Return'
        self.assertTrue(TestChecker.test(input, expect, 584))

    def test_break_1(self):
        input = """
        procedure main();
        begin
            break;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 585))

    def test_break_2(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 100 do break;
            i:= 1;
            break;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 586))

    def test_break_5(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 100 do return;
            break;
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect,587))

    def test_break_3(self):
        input = '''
            procedure main();
            begin
                if 5 > 6 then
                begin
                    if 1 <4 then
                    begin
                        putStringLn("Jim dep trai new");
                        break;
                    end
                end
                return;
            end
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,588))

    def test_break_4(self):
        input = '''
            procedure main();
            begin
                if 5 > 6 then
                begin
                    if 1 <4 then
                    begin
                        putStringLn("Jim dep trai new");
                    end
                end
                break;
                return;
            end
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,589))

    def test_Continue_1(self):
        input = """
        procedure main();
        begin
            Continue;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 590))

    def test_Continue_2(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 100 do Continue;
            i:= 1;
            Continue;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 591))

    def test_Continue_5(self):
        input = """
        procedure main();
        var i: integer;
        begin
            for i := 0 to 100 do return;
            Continue;
        end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect,592))

    def test_Continue_3(self):
        input = '''
            procedure main();
            begin
                if 5 > 6 then
                begin
                    if 1 <4 then
                    begin
                        putStringLn("Jim dep trai new");
                        Continue;
                    end
                end
                return;
            end
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,593))

    def test_Continue_4(self):
        input = '''
            procedure main();
            begin
                if 5 > 6 then
                begin
                    if 1 <4 then
                    begin
                        putStringLn("Jim dep trai new");
                    end
                end
                Continue;
                return;
            end
        '''
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,594))

    def test_no_entry_1(self):
        input = """
        function factorial(x: integer): integer;
        begin
            if x < 2 then return 1;
            return x*factorial(x - 1);
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 595))

    def test_no_entry_2(self):
        input = """
        function sum(x: integer): integer;
        begin
            return x+x+x;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 596))

    def test_no_entry_3(self):
        input = '''
            procedure jim();
            begin
                quynhnhu();
            end
            procedure quynhnhu();
            begin
                jim();
            end
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,597))

    def test_no_entry_4(self):
        input = '''
            procedure foo();
            begin
                return;
            end
            procedure _main_();
            begin
                foo();
            end
        '''
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,598))

    def test_no_entry_5(self):

        input = """
                   var main: integer;
                   procedure __init__();
                   begin return; end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,599))

    def test_no_entry_6(self):

        input = """
                   var a: array [1 .. 2] of boolean;
                   function main(a:inteGER) : integer;
                   begin return; end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,600))
