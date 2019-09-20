import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def testDecl_202(self):
        input = """function abc : real;
        begin
        end"""
        expect = "Error on line 1 col 13: :"
        self.assertTrue(TestParser.test(input,expect,999))

    def testDecl_203(self):
        input = """function abc (a: float): real;
        begin
        end"""
        expect = "Error on line 1 col 17: float"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_simple_as(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        var m,b: INTeger;
        BEGIN
        m := 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_complex_as1(self):
        input = """Function JimTran2018 (m: ReaL): INTeger;
        BEGIN
        who()[9] := m + 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_complex_as2(self):
        input = """Function JimTran2018 (m: ReaL): INTeger;
        BEGIN
        who(10)[20] := 90;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))


    def testVarDecl_1(self):
        self.assertTrue(TestParser.test("Var m: ReaL;", "successful", 201))
    def testVarDecl_2(self):
        self.assertTrue(TestParser.test("Var m, n: INTeger;", "successful", 202))
    def testVarDecl_3(self):
        self.assertTrue(TestParser.test("Var newT_id: bOOlean;", "successful", 203))
    def testVarDecl_4(self):
        self.assertTrue(TestParser.test("Var m: int", "Error on line 1 col 7: int", 204))
    def testVarDecl_5(self):
        self.assertTrue(TestParser.test("Var m,b,c: ReaL;d : array[ 1 .. 5 ] of ReaL ;e , f : string ;", "successful", 205))
    def testVarDecl_6(self):
        self.assertTrue(TestParser.test("Var _zdsa214: INTeger;", "successful", 206))
    def testVarDecl_7(self):
        self.assertTrue(TestParser.test("Var 1sfd: boolean", "Error on line 1 col 4: 1", 207))
    def testVarDecl_8(self):
        self.assertTrue(TestParser.test("VAR m: INTeger; n, mmmm: ReaL;\n VAR arr: array [1 .. 500] of ReaL;", "successful", 208))
    def testVarDecl_9(self):
        self.assertTrue(TestParser.test("VAR e: ReaL; red, blue, green: INTeger;", "successful", 209))
    def testVarDecl_10(self):
        self.assertTrue(TestParser.test("VAR b d : ReaL", "Error on line 1 col 6: d", 210))

    """ Test Procedure """
    def testProcedureDecl_1(self):
        self.assertTrue(TestParser.test("Procedure when(); BEGIN END", "successful", 211))
    def testProcedureDecl_2(self):
        self.assertTrue(TestParser.test("Procedure sum(arr: array [1 .. 10] of ReaL); BEGIN END", "successful", 212))
    def testProcedureDecl_3(self):
        self.assertTrue(TestParser.test("ProcedurE jimtra; BEGIN END", "Error on line 1 col 16: ;", 213))
    def testProcedureDecl_4(self):
        self.assertTrue(TestParser.test("proceDURE sinister(); var m:ReaL; BEGIN END", "successful", 214))
    def testProcedureDecl_5(self):
        self.assertTrue(TestParser.test("Procedure _ididnewT(); var net: ReaL; BEGIN END", "successful", 215))
    def testProcedureDecl_6(self):
        self.assertTrue(TestParser.test("proceDURE when(); BEGIn ENd", "successful", 216))
    def testProcedureDecl_7(self):
        self.assertTrue(TestParser.test("prOCEdure ngonngu() BEGIN END", "Error on line 1 col 20: BEGIN", 217))
    def testProcedureDecl_8(self):
        self.assertTrue(TestParser.test("proceDURE tan(m:INTeger):INTeger; BEGIN END", "Error on line 1 col 24: :", 218))
    def testProcedureDecl_9(self):
        self.assertTrue(TestParser.test("proceDURE cho(n: ;); JimTran2018456122 @!###@@!!", "Error on line 1 col 17: ;", 219))
    def testProcedureDecl_10(self):
        self.assertTrue(TestParser.test("proceDURE gogogogogogo(); BEGIN END", "successful", 220))



    def test_complex_as3(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        who(10)[m+3*5] := m + 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_complex_as4(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        m := b[10] := who ()[3] := x := 1 ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))


    def test_complex_as5(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        who(2)[3+x] := m[b[2]] +3 ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_error_as1(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        m : = 1;
        END"""
        expect = "Error on line 3 col 10: :"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_error_as2(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        (9+2)[22] := 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_error_as3(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        m(9)[3+x] := 1
        END"""
        expect = "Error on line 4 col 8: END"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_space_in_assign_token(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        m(9)[3+x] : = 1;
        END"""
        expect = "Error on line 3 col 18: :"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_assign_string(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        BEGIN
        who(2)[m] := "Hello" ;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_ass_float_para(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        var m,b: INTeger;
        BEGIN
            f(9.7) := 1;
        END"""
        expect = "Error on line 4 col 19: :="
        self.assertTrue(TestParser.test(input,expect,232))

    def testBrk_cont_1(self):
        self.assertTrue(TestParser.test("""
            Procedure when();
            var e,m: INTeger;
            BEGIN
                for e := 0 to 6 do
                    if e = 3 then break;
                    else continue;
            END
        """, "successful", 233))

    def testBrk_cont_2(self):
        self.assertTrue(TestParser.test("""
            Procedure wrongBreak();
            BEGIN
                brek;
            END
        """, "Error on line 4 col 20: ;", 234))

    def testBrk_cont_3(self):
        self.assertTrue(TestParser.test("""
            Procedure wrongCont();
            BEGIN
                continu;
            END
        """, "Error on line 4 col 23: ;", 235))

    def testCompoundState_1(self):
        self.assertTrue(TestParser.test("""
            Function missBegin(): INTeger;
                return 10;
            END
        """, "Error on line 3 col 16: return", 236))

    def testCompoundState_2(self):
        self.assertTrue(TestParser.test("""
            Function missEnd(): real;
            BEGIN
                return 9.6;
        """, "Error on line 5 col 8: <EOF>", 237))

    def testCompoundState_3(self):
        self.assertTrue(TestParser.test("""
            Procedure nestedCompound();
            BEGIN
                newThis();
                BEGIN
                    BEGIN
                        newThese();
                    END
                    newThose();
                END
            END
        """, "successful", 238))

    def test_assign_many_array(self):
        input = """proceDURE JimTran2018 (m: ReaL);
        var m,b: INTeger;
        BEGIN
        m[1] := m[2] := m[3] := m[4] := 1;
        END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))


    def testProgram_1(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(); var m: INTeger; b: real; c: array[1 .. 2] of INTeger;
            BEGIN
                m := 100;
                b := 1e-5;
                c[1] := "string string string";
            END
        """, "successful", 240))

    def testProgram_2(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(); var e: INTeger;
            BEGIN
                for e := 0 to 3 do
                BEGIN
                END
            END
        """, "successful", 241))

    def testProgram_3(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(); var e: INTeger;
            BEGIN
                for e := 0 to 3 do
                BEGIN
                    for e:= 0 to 100 do
                    BEGIN
                        m := 2;
                    END
                END
            END
        """, "successful", 242))

    def testProgram_4(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(m,b: real); var e: INTeger;
            BEGIN
                for e := 10 downto e < 2 do
                BEGIN
                    m := b := 777;
                END
            END
        """, "successful", 243))

    def testProgram_5(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(arr: array[1 .. 2] of string); var e: INTeger;
            BEGIN
                for e := 0 to e >= 100 do
                BEGIN
                    arr[1] := arr[2] := "we are string";
                END
            END
        """, "successful", 244))

    def testProgram_6(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(); var e: INTeger;
            BEGIN
                for e := 0 to 3
                BEGIN
                END
            END
        """, "Error on line 5 col 16: BEGIN", 245))

    def testProgram_7(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(); var m: real;
            BEGIN
                if (e > 2) then e := e + 1;
            END
        """, "successful", 246))

    def testProgram_8(self):
        self.assertTrue(TestParser.test("""
            proceDURE when(); var m: real;
            BEGIN
                if (e > 2) then e := e + 1;
                else e := 0;
            END
        """, "successful", 247))

    def testProgram_9(self):
        self.assertTrue(TestParser.test("""
            proceDURE quadraticDelta(delta: real);
            BEGIN
                if (delta > 0)
                    putStringLn("2 solutions");
                else
                BEGIN
                    if (delta < 0) putStringLn("No solution");
                    else putStringLn("1 solution");
                END
            END
        """, "Error on line 5 col 20: putStringLn", 248))

    def testProgram_10(self):
        self.assertTrue(TestParser.test("""
            proceDURE compareGreater(m,b: real);
            BEGIN
                if (m > b) then
                    putStringLn("m is greater than b");
                else
                    putStringLn("b is greater or equal to m");
            END
        """, "successful", 249))

    def testProgram_11(self):
        self.assertTrue(TestParser.test("""
            proceDURE compoundIf(m,b: INTeger);
            BEGIN
                if (m < 0) then
                BEGIN
                    m := m+b;
                    b := 100;
                END
            END
        """, "successful", 250))

    def testProgram_12(self):
        self.assertTrue(TestParser.test("""
            Function when(x,y,z: string) : real; var m: INTeger;
            BEGIN
                x := "20031998";
            END
        """, "successful", 251))

    def testProgram_13(self):
        self.assertTrue(TestParser.test("""
            Function when(m: real;b: array[1 .. 10] of INTeger) : INTeger;
            BEGIN
                m := b[1] := 10;
                if (m > 0) then b[2] := b[1] / 2;
            else b[2] := 1;
            END
        """, "successful", 252))

    def testProgram_14(self):
        self.assertTrue(TestParser.test("""
            Function when() : string;
            BEGIN
                x := "chocolate";
            END
        """, "successful", 253))

    def testProgram_15(self):
        self.assertTrue(TestParser.test("""
            Function when(arr: array[1 .. 2] of INTeger) : INTeger; var e: INTeger;
            BEGIN
                m := 100;
                arr[1] := m + 1;
                for e := 0 to 10 do
                BEGIN
                    if (m > 10) then m := m - 1 * 2 +3;
                END

            END
        """, "successful", 254))

    def testProgram_16(self):
        self.assertTrue(TestParser.test("""
            Function when();
            BEGIN
                return;
            END
        """, "Error on line 2 col 27: ;", 255))

    def testProgram_17(self):
        self.assertTrue(TestParser.test("""
            proceDURE when();
            BEGIN
                return m + b;
            END
        """, "successful", 256))


    def testWith_stmt_1(self):
        self.assertTrue(TestParser.test("""
            proceDURE what();
            var e: INTeger;
            BEGIN

            END
            END
        """, "Error on line 7 col 12: END", 257))

    def testWith_stmt_2(self):
        self.assertTrue(TestParser.test("""
            proceDURE what();
            var flag: INTeger;
            BEGIN
                var:=100;
            END
        """, "Error on line 5 col 16: var", 258))

    def testWith_stmt_3(self):
        self.assertTrue(TestParser.test("""
            proceDURE what();
            BEGIN
                var(2);
            END
        """, "Error on line 4 col 16: var", 259))

    def testWith_stmt_4(self):
        self.assertTrue(TestParser.test("""
            proceDURE what();
            Function what():INTeger;
            BEGIN

            END
        """, "Error on line 3 col 12: Function", 260))

    def test_while_stmt(self):
        self.assertTrue(TestParser.test("""
            proceDURE wrongKeyword();
           var n,tong,e:INTeger;
           BEGIN
            tong:=0;
             for e:=1 to n D
                if (e mod 3=0) or (e mod 5=0) then
                    tong:=tong+e;
                    END
        """, "Error on line 6 col 27: D", 261))


    def testArrray_30(self):
        input = """
            Function poo(m:array [1..5] of INTeger):array [1..5] of INTeger;
            BEGIN

            END
        """
        expect = "Error on line 2 col 36: .5"
        self.assertTrue(TestParser.test(input,expect,262))

    def testArrray_31(self):
        input = """
            Procedure poo(m:array [1 .. 5] of INTeger):array [1..5] of INTeger;
            BEGIN

            END
        """
        expect = "Error on line 2 col 54: :"
        self.assertTrue(TestParser.test(input,expect,263))

    def testVarNew_32(self):
        input = """
            Procedure poo(m:array [1 .. 5] of INTeger);
            var m,b := INTeger;
            BEGIN

            END
        """
        expect = "Error on line 3 col 20: :="
        self.assertTrue(TestParser.test(input,expect,264))

    def testCompoundState_33(self):
        input = """
            Procedure jim();
            BEGIN
                BEGIN
                    BEGIN
                    END
                END
            END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_if_34(self):
        input = """
            Procedure jim();
            BEGIN
                if (m<0) then break; continue; else return;
            END
        """
        expect = "Error on line 4 col 47: else"
        self.assertTrue(TestParser.test(input,expect,266))

    def testExpression_6(self):
        self.assertTrue(TestParser.test("""
            Function nonAssocRelation(m,b,c: INTeger): boolean;
            begin
                return m > b > c;
            end
        """, "Error on line 4 col 29: >", 267))

    def testExpression_7(self):
        self.assertTrue(TestParser.test("""
            Function AndOr(andFLag: boolean; m,b: INTeger): INTeger;
            begin
                if (andFlag= true) then
                    return m and b;
                else
                    return m or b;
            end
        """, "successful", 268))

    def testExpression_8(self):
        self.assertTrue(TestParser.test("""
            Function XorOp(m,b: boolean): boolean;
            begin
                return m or not m and b;
            end
        """, "successful", 269))

    def testExpression_9(self):
        self.assertTrue(TestParser.test("""
            Function looopAnd(m,b,c: boolean): boolean;
            begin
                return m and then b;
            end
            Function looopOr(m,b,c: boolean): boolean;
            begin
                return m or else b or else c;
            end
        """, "successful", 270))


    def testExpression_10(self):
        self.assertTrue(TestParser.test("""
            Procedure for1();
            begin
                for k:=1 to 5 do
                k:=k+3;
                break
            end
        """, "Error on line 7 col 12: end", 271))

    def testVarNew_dec_16(self):
        self.assertTrue(TestParser.test("""
            Procedure for1();
            begin
                for k:=1 to 5 do
                k:=k+3;
                continue
            end
        """, "Error on line 7 col 12: end", 272))

    def testReturn_stmt_1(self):
        self.assertTrue(TestParser.test("""
            Procedure for1();
            begin
                for k:=1 to 5 do
                k:=k+3;
                continue;
                break;
            end
        """, "successful", 273))

    def testReturn_stmt_2(self):
        self.assertTrue(TestParser.test("""
            Procedure randofuction();
                var e,j: integer;
                begin
                 for e := 1 to n-1 do
                      for j := n downto e+1 do
                       if k[j] < k[j-1] then
                          Swap(k[j],k[j-1]);
                end
        """, "successful", 274))

    def testReturn_stmt_3(self):
        self.assertTrue(TestParser.test("""
            Var k : Array [1 ..0] Of Integer;
             e , j , n : Integer ;
             Procedure main();
             BEGIN
              For e := 1 To N Do
              Begin
               End
               e := 2 ;
               While e <= N Do e:= 1;

            END
        """, "successful", 275))

    def testBrk_cont_1(self):
        self.assertTrue(TestParser.test("""
            Procedure MAIN();
            Var e , n : Integer ;
             k , m : Real ;
              BEGIN
               e := 1 ;
               max := 1000000;
                While e <= n Do
                Begin value := value * k ;
                 e:= e+1 ;
                  End
                   END
        """, "successful", 276))

    def testBrk_cont_2(self):
        self.assertTrue(TestParser.test("""
            Var arr : aRRay [1 ..0] Of Integer;
            e , j , n : Integer ;
            Procedure main();q
            BEGIN
             println(" Length arr = ") ;
              For e := 1 To N Do
               Begin
                    println (" Different : ") ;
                   println ( k[1] ) ;
                    e := 2 ;
                End
            END
        """, "Error on line 4 col 29: q", 277))

    def testIfstmt_new(self):
        self.assertTrue(TestParser.test("""
            var k, b, c,  min: integer;
                Procedure mmaxxx(x, y: integer;m: integer);
                    begin
                    if z < m then m:= z;
                    end
        """, "successful", 278))

    def testCompoundnew_1(self):
        self.assertTrue(TestParser.test("""
            FUnctiON abcdmi(): boolean;

            end
        """, "Error on line 4 col 12: end", 279))

    def testCompoundnew_2(self):
        self.assertTrue(TestParser.test("""
            FUnctiON sesimi(): integer;
            begin
        """, "Error on line 4 col 8: <EOF>", 280))

    def testExpression_9(self):
        self.assertTrue(TestParser.test("""
            Function poo(e,j:integer): integer;
                var FirstKey : real;
             k : integer;
                begin
             k := e+1;
             if k > j then pv := 0;
             else
                    if k[k]> FirstKey then pv := k ;
                    else pv := e;
            end
        """, "successful", 281))

    def test_expr_has_SB(self):
        input = """FUnctiON poo(k:integer):string;
        begin
        return poo - (k+b)[k[2]+4];
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_return_callstt(self):
        input = """FUnctiON poo(k:integer):string;
        begin
        return poo(9);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_call_statement(self):
        input = """FUnctiON poo(k:integer):string;
        begin
            poo(2);
            poo(3, k+1, m(2));
            poo(k[2]);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_break_miss_semi(self):
        input = """FUnctiON poo(k:integer):string;
        begin
            break
        end
        """
        expect = "Error on line 4 col 8: end"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_continue_miss_semi(self):
        input = """FUnctiON poo(k:integer):string;
        begin
            continue
        end
        """
        expect = "Error on line 4 col 8: end"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_continue_new_1(self):
        input = """
            Procedure pro();
            begin
                for poo := k + b - 3 downto poo()[k + b - c*5] do
                    k := k+k*k;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_continue_new_2(self):
        input = """
            Procedure pro();
            begin
                k := print("\\\'hello\\\'");
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_continue_new_3(self):
        input = """
            Procedure pro();
            begin
                k := 12;
                m := 3;
                z := 69;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_continue_new_4(self):
        input = """
            Procedure pro(

            );
            begin

            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_continue_new_5(self):
        input = """
            Procedure pro();
            begin
                k := b[3] := 5 + c[-4];
                k := 12;
                m := 3;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_continue_new_6(self):
        input = """
            Procedure pro();
            begin
                k := poo := ____()[2];
                k := 5*5;
                m := 3-0;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_continue_new_7(self):
        input = """
            Procedure pro();
            begin
                ____ := _;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_continue_new_8(self):
        input = """
            Procedure pro();
            begin
                ______ := 12____;
            end
        """
        expect = "Error on line 4 col 28: ____"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_continue_new_9(self):
        input = """
            Procedure pro();
            begin
                a_____ := b____;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def testDecl_95(self):
        input = """
            var abc:array[-2 .. -5] of string;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def testDecl_96(self):
        input = """
            var smi:array[1+2 .. 3+4] of real;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def testDecl_97(self):
        input = """
            var sml:array [1 . . 5] of integer;
        """
        expect = "."
        self.assertTrue(TestParser.test(input,expect,297))

    def testDecl_200(self):
        input = """function abc (): boolean;
        begin
        end ;"""
        expect = "Error on line 3 col 12: ;"
        self.assertTrue(TestParser.test(input,expect,298))

    def testDecl_201(self):
        input = """function abc (): real
        begin
        end"""
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,998))


    def testFinal(self):
        input = """procedure foo();
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
