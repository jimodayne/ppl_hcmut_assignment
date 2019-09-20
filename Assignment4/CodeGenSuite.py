import unittest
from TestUtils import TestCodeGen
from AST import *
from functools import reduce

class CheckCodeGenSuite(unittest.TestCase):

    def test_code_1(self):
        input = """
                procedure main();
                begin
                    putInt(1);
                end
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,1))

    def test_code_2(self):
        input = """
                procedure main();
                begin
                    putIntln(20);
                end
                """
        expect = "20\n"
        self.assertTrue(TestCodeGen.test(input,expect,2))

    def test_code_3(self):
        input = """
                procedure main();
                begin
                    putFloat(18/2);
                end
                """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input,expect,3))

    def test_code_4(self):
        input = """
                procedure main();
                begin
                    putFloATln(21.e-5);
                end
                """
        expect = "2.1E-4\n"
        self.assertTrue(TestCodeGen.test(input,expect,4))
    def test_code_5(self):
        input = """
                procedure main();
                begin
                    putString("Hello World");
                end
                """
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,5))
    def test_code_6(self):
        input = """
                procedure main();
                begin
                    putInt(2);
                end
                """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,6))
    def test_code_7(self):
        input = """
                procedure main();
                begin
                    putIntln(100);
                end
                """
        expect = "100\n"
        self.assertTrue(TestCodeGen.test(input,expect,7))
    def test_code_8(self):
        input = """
                procedure main();
                begin
                    putFloat(100/2);
                end
                """
        expect = "50.0"
        self.assertTrue(TestCodeGen.test(input,expect,8))

    def test_code_9(self):
        input = """
                procedure main();
                begin
                    putFloatLN(2+3+5.0);
                end
                """
        expect = "10.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,9))

    def test_code_10(self):
        input = """
                procedure main();
                begin
                    putString("Hello World!\\n");
                end
                """
        expect = "Hello World!\n"
        self.assertTrue(TestCodeGen.test(input,expect,10))

    def test_code_11(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(20); end
                    var a:integer;"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,11))

    def test_code_12(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(10 + 1); end"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,1))

    def test_code_13(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(1 + 1 + 2); end"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,13))

    def test_code_14(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(10*12); end"""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,14))

    def test_code_15(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(7 diV 4); end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,15))

    def test_code_16(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(3 mod 2); end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,16))

    def test_code_17(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putFloat(3/2); end"""
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input,expect,17))

    def test_code_18(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putBool(tRUe); end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,18))

    def test_code_19(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putBool(True); end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,19))

    def test_code_20(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putBool(false or false); end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,20))

    def test_code_21(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    var a:integer;
                    begin putInt(3);
                    end
                    """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,21))

    def test_code_22(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putInt(100 + 100);
                        end"""
        expect = "200"
        self.assertTrue(TestCodeGen.test(input,expect,22))

    def test_code_23(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin putInt(100 + 200 + 200);
                    end"""
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,23))

    def test_code_24(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putInt(100*110-1);
                    end"""
        expect = "10999"
        self.assertTrue(TestCodeGen.test(input,expect,24))

    def test_code_25(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putInt(10 div 4);
                    end"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,25))

    def test_code_26(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin putInt(10 mod 4);
                    end"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,26))

    def test_code_27(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin
                    putFloat(6/4+1);
                end"""
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input,expect,27))

    def test_code_28(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putBool(false);
                    end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,28))

    def test_code_29(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putBool(True and then false);
                         end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,29))

    def test_code_30(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putBool(True or false);
                     end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,30))


    def test_code_31(self):
        """Simple program: int main() {} """
        input = """procedure
                main();
                begin
                    putBool(1 < 40);
                 end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,31))

    def test_code_32(self):
        """Simple program: int main() {} """
        input = """procedure main();
                    begin
                        putBool(1 + 3 <= 4);
                    end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,32))

    def test_code_33(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin
                    putInt(-10);
                end"""
        expect = "-10"
        self.assertTrue(TestCodeGen.test(input,expect,33))

    def test_code_34(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin
                    putFloat(-1.5);
                     end"""
        expect = "-1.5"
        self.assertTrue(TestCodeGen.test(input,expect,34))

    def test_code_35(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin putBool(not true);
                end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,35))

    def test_code_36(self):
        """Simple program: int main() {} """
        input = """procedure main();
                begin putBool((1.3 >= 3.2) and (2.2 = 3.3)); end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,36))

    def test_code_37(self):
        """Simple program: int main() {} """
        input = """ procedure main();
                    var a:integer;
                    begin
                        b := a := 2;
                        putInt(a);
                    end
                    var b:real;"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,37))

    def test_code_38(self):
        """Simple program: int main() {} """
        input = """ procedure main();
                    var a:integer;
                    begin
                        b := a := 2;
                        putFloat(b);
                    end
                    var b:real;"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,38))

    def test_code_39(self):
        """Simple program: int main() {} """
        input = """ var b:real;
                    procedure main();
                    var a:integer;
                    begin
                        b := a := 2;
                        putFloat(b + a);
                    end
                    """
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input,expect,39))

    def test_code_40(self):
        """Simple program: int main() {} """
        input = """ procedure main();
                    var a:boolean;
                    begin
                        a := not true;
                        putBool(a);
                    end
                    """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,40))

    def test_code_41(self):
        input = """
                procedure main();
                var a: integer;
                begin
                    a := 2;
                    putInt(a);
                end
                """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,41))

    def test_code_42(self):
        input = """
                procedure jim();
                begin
                    a := 4;
                    putIntLn(a);
                end
                procedure main();
                var a: integer;
                begin
                    jim();
                    a := 1;
                    putInt(a);
                end
                var a: integer;
                """
        expect = "4\n1"
        self.assertTrue(TestCodeGen.test(input,expect,42))

    def test_code_43(self):
        input = """
                procedure jim();
                var a: integer;
                begin
                    a := 8;
                    putIntLn(a);
                end
                procedure main();
                begin
                    jim();
                    a := 3;
                    putInt(a);
                end
                var a: integer;
                """
        expect = "8\n3"
        self.assertTrue(TestCodeGen.test(input,expect,43))

    def test_code_44(self):
        input = """
                procedure jim(a: integer);
                begin
                    a := a * 3;
                end
                procedure main();
                begin
                    a := 3;
                    putIntln(a);
                    jim(a);
                    putInt(a);
                end
                var a: integer;
                """
        expect = "3\n3"
        self.assertTrue(TestCodeGen.test(input,expect,44))

    def test_code_45(self):
        input = """
                procedure main();
                var a: integer;
                begin
                    a := 3;
                    putIntln(a+2);
                end
                var a: string;
                """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,45))

    def test_code_46(self):
    	input = Program([FuncDecl(Id("main"),[],[],
        [CallStmt(Id("putFloat"),
        [FloatLiteral(20.03)]),CallStmt(Id("putLn"),[]),
        CallStmt(Id("putFloat"),
        [FloatLiteral(20.03)]),Return()],VoidType())])

    	expect = """20.03\n20.03"""
    	self.assertTrue(TestCodeGen.test(input,expect,46))

    def test_code_47(self):
        input = """
                var a: integer;
                procedure main();
                var b: integer;
                begin
                    a := b := 3;
                    putIntLn(a);
                    jim(a);
                    putIntLn(a);
                    putInt(b);
                end
                procedure jim(a: integer);
                begin
                    a := 5;
                end
                """
        expect = "3\n3\n3"
        self.assertTrue(TestCodeGen.test(input,expect,47))

    def test_code_48(self):
        input = """
                var a: integer;
                procedure main();
                var b: integer;
                begin
                    a := b := 3;
                    putIntLn(a);
                    putIntLN(b);
                    jim(b);
                    putIntLn(a);
                    putInt(b);
                end
                procedure jim(a: integer);
                begin
                    a := 5;
                end
                """
        expect = "3\n3\n3\n3"
        self.assertTrue(TestCodeGen.test(input,expect,48))

    def test_code_49(self):
        input = """
                function foo():integer;
                begin
                    a := 5;
                    return a;
                end
                var a: integer;
                procedure main();
                begin
                    jim(foo());
                    putInt(a);
                end
                procedure jim(a: integer);
                begin
                    a := 7;
                end
                """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,49))

    def test_code_50(self):
        input = """
                function foo():integer;
                begin
                    a := 10;
                    return a;
                end
                var a: integer;
                procedure main();
                begin
                    jim(foo());
                    putInt(a);
                end
                procedure jim(a:integer);
                begin
                    a := 7;
                end
                """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,50))


    def test_code_51(self):
    	input = """
            procedure foo____();
            var count:integer;
            begin
                count:=5;
                while ( count > 0 ) do
                begin
                    with a:integer ;do
                    begin
                        if true = false then
                            PUTINT(1);
                        else
                            PUTInt(3);
                    end
                 count := count-1;
                 end
                 return ;
            end

            procedure main();
            begin
                fOo____();
            end
        """
    	expect = "33333"
    	self.assertTrue(TestCodeGen.test(input,expect,51))

    def test_code_52(self):
    	input = """
            procedure foo____();
            var count:integer;
            a:integer;
            begin
                count:=5;
                a:=5;
                while ( count > 0 ) do
                begin
                    with a:integer ;do
                    begin
                        a:=10;

                        if true = false then
                            PUTINT(1);
                        else
                            PUTInt(2);
                        putint(a);
                    end
                 count := count-1;
                 putint(a);
                 end
                 return ;
            end

            procedure main();
            begin
                fOo____();
            end
        """
    	expect = "21052105210521052105"
    	self.assertTrue(TestCodeGen.test(input,expect,52))


    def test_code_53(self):
    	input = """
            function funCcall(a:integer):integer;
            begin
                if a = 0 then
                    return 1;
                else
                    return 1+funCcall(a-1);

            end

            procedure main();
            begin
                putInt(funCcall(10));
            end
        """
    	expect = "11"
    	self.assertTrue(TestCodeGen.test(input,expect,53))

    def test_code_54(self):
    	input = """
            function funCcall(a:integer):integer;
            begin
                for a:=0 to 100 do
                    if a = 4 then
                        a:=( 10 div 5) + 20;

                if true = ( true and true ) and then ( 3 > 2) then
                    return 1;
                else
                    with a:integer ;do
                        return 2;

            end

            procedure main();
            begin
                putInt(funCcall(10));
            end
        """
    	expect = "1"
    	self.assertTrue(TestCodeGen.test(input,expect,54))

    def test_code_55(self):
    	input = """
            function funCcall(a:integer; b:integer; c:real):integer;
            var d:real;
            begin
                d:=c:=a:=b:=2;
                putInt(a);
                putFloatLn(d);
                return 1;

            end

            procedure main();
            begin
                putInt(funCcall(10,10,2.0));
            end
        """
    	expect = "22.0\n1"
    	self.assertTrue(TestCodeGen.test(input,expect,55))


    def test_code_56(self):
    	input = """
            function funCcall(a:integer; b:integer; c:real):integer;
            var d:real;
            begin
                d:=c:=a:=b:=2;
                putInt(a);
                putFloatLn(d);
                return 1;

            end

            procedure main();
            begin
                putInt(funCcall(10,10,2.0));
            end
        """
    	expect = "22.0\n1"
    	self.assertTrue(TestCodeGen.test(input,expect,56))

    def test_code_57(self):
    	input = """
            function funCcall():boolean;
            begin

                return (1<2) or else (2>1);

            end

            procedure main();
            begin
                putBool(funCcall());
            end
        """
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,57))

    def test_code_58(self):
    	input = """
            function funCcall():String;
            begin

                return "hello";

            end

            procedure main();
            begin
                putString(funCcall());
            end
        """
    	expect = "hello"
    	self.assertTrue(TestCodeGen.test(input,expect,58))

    def test_code_59(self):
    	input = """
            function jim():boolean;
            begin
                a:=a+1;
                return false;
            end
            procedure funCcall();
            begin
                if jim() or else jim() or else jim() then
                    a:=a+1;
            end

            procedure main();
            begin
                a:=0;
    funCcall();

                putint(a);
            end
            var a:integer;
        """
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,59))

    def test_code_60(self):
    	input = """
             function jim():boolean;
             begin
                 a:=a+1;
                 return false;
             end
            procedure funCcall();
            begin
                with c:boolean; do
                begin
                c:=truE;
                if jim() or else jim() or else c then
                    a:=a+1;
                end
            end

            procedure main();
            begin
                            a:=0;

                funCcall();
                putint(a);
            end
            var a:integer;
        """
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,60))

    def test_code_61(self):
    	input = """
             function jim():boolean;
             begin
                 a:=a+1;
                 return true;
             end
            procedure funCcall();
            begin
                with c:boolean; do
                begin
                c:=False;
                if jim() and then jim() and then c then
                    a:=a+1;
                end
            end

            procedure main();
            begin
                            a:=0;
                funCcall();
                putint(a);
            end
            var a:integer;
        """
    	expect = "2"
    	self.assertTrue(TestCodeGen.test(input,expect,61))

    def test_code_62(self):
        """Simple program: int main() {} """
        input = """
                    procedure HanoiTower(n : integer; start_disk : string; desination_disk : string; auxiliary_disk : string);
                    begin
                        if (n = 1) (* If only has 1 disk left *)
                            then
                                begin
                                    putString("Move 1 disk from ");
                                    putString(start_disk);
                                    putString(" to ");
                                    putStringLn(desination_disk);
                                    return;
                                end

                        HanoiTower(n - 1, start_disk, auxiliary_disk, desination_disk);

                        putString("Move 1 disk from ");
                        putString(start_disk);
                        putString(" to ");
                        putStringLn(desination_disk);

                        HanoiTower(n - 1, auxiliary_disk, desination_disk, start_disk);
                    end


                    procedure main();
                    begin
                        HanoiTower(3, "A", "C", "B");
                    end
                    """
        expect = """Move 1 disk from A to C
Move 1 disk from A to B
Move 1 disk from C to B
Move 1 disk from A to C
Move 1 disk from B to A
Move 1 disk from B to C
Move 1 disk from A to C
"""
        self.assertTrue(TestCodeGen.test(input,expect,62))

    def test_code_63(self):
        """Simple program: int main() {} """
        input = """ function getFactorial(n : integer):integer;
                    begin
                        if (n = 1) then return 1;

                        return n * getFactorial(n - 1);
                    end

                    procedure main();
                    begin
                        putInt(getFactorial(5));
                    end
                    """
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,63))

    def test_code_64(self):
        """Simple program: int main() {} """
        input = """ function square(n : integer):integer;
                    begin return n*n; end

                    function addBy1(n : integer):integer;
                    begin return n + 1; end

                    function minusBy1(n : integer):integer;
                    begin return n - 1; end

                    function diff(a: real; b: real ):real;
                    begin
                        if isPositive(a - b) then return a - b;
                        else return b - a;
                    end

                    function isPositive(n : real):boolean;
                    begin return n >= 0; end

                    procedure main();
                    var n:integer; difference:real;
                    begin
                        n := 5;
                        difference := diff(square(addBy1(n)) , square(minusBy1(n)));
                        putFloatLn(difference);
                        putBoolLn(isPositive(difference));
                    end
                    """
        expect = """20.0
true
"""
        self.assertTrue(TestCodeGen.test(input,expect,64))

    def test_code_65(self):
        """Simple program: int main() {} """
        input = """ procedure swap(a,b:real);
                    var temp:real;
                    begin
                        temp := a;
                        a := b;
                        b := temp;
                        putStringLn("Swap successful");
                        putString("a = "); putFloatLn(a);
                        putString("b = "); putFloatLn(b);
                    end

                    procedure main();
                    var a,b:integer;
                    begin
                        a := 20;
                        b := 10;
                        putString("a = "); putFloatLn(a);
                        putString("b = "); putFloatLn(b);

                        swap(a,b);
                    end
                    """
        expect = "a = 20.0\nb = 10.0\nSwap successful\na = 10.0\nb = 20.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,65))

    def test_code_66(self):
        """Simple program: int main() {} """
        input = """
                    procedure main();
                    begin
                        putInt(foo());
                    end

                    function foo():integer;
                    begin
                        with a:integer; do
                            if (3 < 1) then return 1;
                            else return 3;
                    end
                    """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,66))

    def test_code_67(self):
        """Simple program: int main() {} """
        input = """
                    var i:integer;
                    function f():integer;
                    begin
                        return 2;
                    end

                    procedure main();
                    var main:integer;
                    begin
                        main := g := f();
                        putIntLn(main);
                        with i:integer; main:integer; f:integer; do
                            begin
                                main := f := i := 10;
                                putIntLn(i);
                                putIntLn(main);
                                putIntLn(f);
                                putIntLn(g);
                            end
                        putIntLn(main);

                    end
                    var g:integer;
                    """
        expect = "2\n10\n10\n10\n2\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,67))

    def test_code_68(self):
        """Simple program: int main() {} """
        input = """
                    procedure toHexa(n : integer);
                    var quotient, remain:integer;
                    begin

                        if (n = 0) then return;

                        quotient := n div 16;
                        remain := n mod 16;

                        toHexa(quotient);

                        if (remain >= 0) and (remain <= 9) then putInt(remain);
                        else
                            begin
                                if remain = 10 then putString("A");
                                if remain = 11 then putString("B");
                                if remain = 12 then putString("C");
                                if remain = 13 then putString("D");
                                if remain = 14 then putString("E");
                                if remain = 15 then putString("F");
                            end

                    end

                    procedure main();
                    begin
                        toHexa(1001);
                    end
                    """
        expect = "3E9"
        self.assertTrue(TestCodeGen.test(input,expect,68))

    def test_code_69(self):
        """Simple program: int main() {} """
        input = """
                    procedure print2console(n : integer);
                    begin
                        if n = -1 then return;
                        putInt(n);
                        print2console(n - 1);
                        putInt(n);
                    end
                    procedure main();
                    begin
                        print2console(5);
                    end
                    """
        expect = "543210012345"
        self.assertTrue(TestCodeGen.test(input,expect,69))

    def test_code_70(self):
        """Simple program: int main() {} """
        input = """
                    procedure toBinary(n : integer);
                    var quotient, remain: integer;
                    begin
                        if n = 0 then return;

                        quotient := n div 2;
                        remain := n mod 2;

                        toBinary(quotient);

                        putInt(remain);
                    end

                    procedure main();
                    begin
                        toBinary(11);
                    end
                    """
        expect = "1011"
        self.assertTrue(TestCodeGen.test(input,expect,70))

    def test_code_71(self):
    	input = """
            function foo____(b:integer):integer;
            var c:integer;
            begin
            for c:=0 to 20 do
                putint(1);
            return 100;
            end

            procedure main();
            begin
                putint(foo____(0));
            end
        """
    	expect = "111111111111111111111100"
    	self.assertTrue(TestCodeGen.test(input,expect,71))

    def test_code_72(self):
    	input = """
            procedure printPytriangle(line:integer);
            var count,count_1:integer;
            begin
                for count:=0 to line do
                begin
                    for count_1:=0 to count+1 do
                        putString("*");
                    putln();
                end
            end

            procedure main();
            begin
                printPytriangle(5);
            end
        """
    	expect ="""**
***
****
*****
******
*******\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,72))

    def test_code_73(self):
    	input = """
            procedure printPytriangle(line:integer);
            var count,count_1:integer;
            begin
                for count:=line downto 0 do
                begin
                    for count_1:=count downto 0 do
                        putString("*");
                    putln();
                end
            end

            procedure main();
            begin
                printPytriangle(5);
            end
        """
    	expect ="""******
*****
****
***
**
*\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,73))

    def test_code_74(self):
    	input = """
            procedure printpyramid(wide:integer);
            begin
                        putString("****");
                        putLn();

            end

            procedure main();
            begin
                printpyramid(7);
            end
        """
    	expect ="""****\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,74))


    def test_code_75(self):
    	input = """
            procedure printString(wide:integer);
            begin
                        putString(" ");

            end
            procedure main();
            begin
                printString(7);
            end
        """
    	expect =""" """
    	self.assertTrue(TestCodeGen.test(input,expect,75))

    def test_code_76(self):
    	input = """
            procedure printpyramid(wide:integer);
            var count,count_1,count_2,count_4:integer;
            begin
                count:=2;
                if count/2 > 0.5 then
                 putInt(1);
            end
            procedure main();
            begin
                printpyramid(7);
            end
        """

    	expect ="""1"""
    	self.assertTrue(TestCodeGen.test(input,expect,76))

    def test_code_77(self):
    	input = """
            function capsocong(number:integer):integer;
            var count,sum:integer;
            begin
                sum:=0;
                for count:=1 to number+1 do
                    sum:=sum+count;
                return sum;
            end
            procedure main();
            var a:integer;
            begin
                putint(capsocong(8));
            end
        """

    	expect ="""45"""
    	self.assertTrue(TestCodeGen.test(input,expect,77))

    def test_code_78(self):
    	input = """
            function jim(number:integer):integer;
            var count,sum:integer;
            begin
                sum:=0;
                for count:=1 to number+1 do
                    sum:=sum+count;
                return sum;
            end
            procedure main();
            var a:integer;
            begin
                putint(jim(9));
            end
        """

    	expect ="""55"""
    	self.assertTrue(TestCodeGen.test(input,expect,78))


    def test_code_79(self):
    	input = """
            procedure drawSquareShape(wide:integer;range:integer);
            var count,count_1,sum:integer;
            begin
                sum:=0;
                for count:=0 to range+1 do
                begin
                    if count = 0 or else count = range then
                        for count_1:=0 to wide+1 do
                            putString("*");
                    else
                        for count_1:= 0 to wide+1 do
                        begin
                            if count_1 = 0 or else count_1 = range-1 then
                                putString("*");
                            else
                                putString(" ");
                        end

                    putLn();

                end

            end
            procedure main();
            var a:integer;
            begin
                drawSquareShape(4,5);
            end
        """

    	expect ="""******\n*   * \n*   * \n*   * \n*   * \n******\n*   * \n"""
    	self.assertTrue(TestCodeGen.test(input,expect,79))

    def test_code_80(self):
    	input = """
            function checkNumEven(number:integer):boolean;
            var count,count_1,sum:integer;
            begin
                if number / 2 = 0 then
                    return true ;
                else return false;

            end
            procedure main();
            var a:integer;
            begin
                putBool(checkNumEven(51));
            end
        """

    	expect ="""false"""
    	self.assertTrue(TestCodeGen.test(input,expect,80))

    def test_code_81(self):
        input = """
                procedure main();
                    begin
                        putInt(2147483647);
                    end
                """
        expect = "2147483647"
        self.assertTrue(TestCodeGen.test(input,expect,81))

    def test_code_82(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                procedure main();
                begin
                    putBool((1>0) and then foo());
                end
                """
        expect = "1\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,82))

    def test_code_83(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                procedure main();
                begin
                    putBool((1.4 >= 2) and then foo());
                end
                """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,83))

    def test_code_84(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                procedure main();
                begin
                    putBool((1.0>-1) and then not foo());
                end
                """
        expect = "1\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,84))

    def test_code_85(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                function jim():boolean;
                begin
                    putIntLn(2);
                    return not foo();
                end
                procedure main();
                begin
                    putBool(((20>3) and then (0=2)) and then jim());
                end
                """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,85))

    def test_code_86(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                function jim():boolean;
                begin
                    putIntLn(2);
                    return not foo();
                end
                procedure main();
                begin
                    putBool(((3>1) and then (0<>2)) and then jim());
                end
                """
        expect = "2\n1\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,86))

    def test_code_87(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                procedure main();
                begin
                    putBool((1>0) or else foo());
                end
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,87))

    def test_code_88(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                procedure main();
                begin
                    putBool((1>2) or else foo());
                end
                """
        expect = "1\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,88))

    def test_code_89(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    return false;
                end
                procedure main();
                begin
                    putBool((4>0) or else not foo());
                end
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,89))

    def test_code_90(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                function jim(x:real):boolean;
                begin
                    putIntLn(2);
                    return not foo();
                end
                procedure main();
                begin
                    putBool(((2>0) and then (1<>2)) or else jim(6/0));
                end
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,90))

    def test_code_91(self):
        input = """
                var i: integer;
                function foo():boolean;
                begin
                    putIntLn(1);
                    return false;
                end
                function jim(x:real):boolean;
                begin
                    putIntLn(2);
                    return not foo();
                end
                procedure main();
                begin
                    putBool(((6<0.0) or else (0=3)) and then jim(1/0));
                end
                """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,91))

    def test_code_92(self):
        input="""
            var pi:real;
            function sum(a:integer):integer;
            var i,sum: integer;
            BEGIN

                sum:=0;
                for i:=1 to a do
                    sum:=sum+i;
                return sum;
            end

            procedure main();
            begin
                putInt(sum(100));
            end
        """
        expect = "5050"
        self.assertTrue(TestCodeGen.test(input,expect,92))

    def test_code_93(self):
        input="""
            function sum(a:integer):integer;
            var sum,temp: integer;
            BEGIN

                sum:=0;
                with i: integer; do
                    for i:=1 to a do
                        begin
                            with n: integer; do
                                begin
                                    temp:=1;
                                    for n:=1 to i do
                                        temp:=temp*a;
                                end
                            sum:=sum+temp;
                        end
                return sum;
            end

            procedure main();
            begin
                putInt(sum(2));
            end
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,93))

    def test_code_94(self):
        input="""
            procedure main();
            var a: boolean;
             i,n : boolean;
            begin

                a:=false;

                for i:=1 to 20 do
                BEGIN
                    for n:=1 to 10 do
                        a:= not a;
                    a:= not a;
                end
                putBool(a);
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,94))

    def test_code_95(self):
        input="""
            procedure main();
            var a:integer;
            begin

                a:=0;
                while (a>=0) do
                BEGIN
                    a:=a+5;
                    with b:real; do
                        BEGIN
                            b:=a/1.5;
                            b:=b*3.3;
                            a:=a-6;
                        end
                    with c:boolean; do
                        c:= not false;
                end
                putInt(a);
            end
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,95))

    def test_code_96(self):
        input="""
            procedure main();
            Var a:integer;
            begin

                for a:=1 to 1000 do
                    BEGIN
                        if a<10 then continue;
                        if a<15 then putIntLn(a);
                        else break;
                    end
            end
        """
        expect = "10\n11\n12\n13\n14\n"
        self.assertTrue(TestCodeGen.test(input,expect,96))

    def test_code_97(self):
        input="""
            function foo(a: integer): integer;
            begin
                if a>1 then
                    return a+foo(a-1);
                else return 1;
            end
            procedure main();
            begin
                putInt(foo(5));
            end
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,97))

    def test_code_98(self):
        input="""
            function foo(a: integer): integer;
            begin
                if a>1 then
                    return a*foo(a-1);
                else return 0;
            end
            procedure main();

            begin
                putInt(foo(101));
            end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,98))

    def test_code_99(self):
        input="""
            function foo(a: integer): real;
            begin
                if a>1 then
                    return a/foo(a-1);
                else return 0.5;
            end
            procedure main();
            begin
                putfloat(foo(3));
            end
        """
        expect = "0.75"
        self.assertTrue(TestCodeGen.test(input,expect,99))

    def test_code_100(self):
        input="""
            function xor(a:boolean;b:boolean): boolean;
            begin
                return (a and  (not b)) or ((not a) and b);
            end
            function foo(a: boolean; i: integer): boolean;
            begin
                if i>1 then
                    return xor(a, foo(a,i-1));
                else return false;
            end
                    procedure main();
            begin
                putbool(foo(True,3));
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,100))
