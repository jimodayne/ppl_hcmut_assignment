
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """ Test ID """
    def testID_1(self):
        self.assertTrue(TestLexer.test("DUYxy123a","DUYxy123a,<EOF>",1))
    def testID_2(self):
        self.assertTrue(TestLexer.test("aef!@#123","aef,Error Token !",2))
    def testID_3(self):
        self.assertTrue(TestLexer.test("helo423","helo423,<EOF>",3))
    def testID_4(self):
        self.assertTrue(TestLexer.test("Z123xyxy","Z123xyxy,<EOF>",4))
    def testID_5(self):
        self.assertTrue(TestLexer.test("69Jjim123deptrai","69,Jjim123deptrai,<EOF>",5))
    def testID_6(self):
        self.assertTrue(TestLexer.test("_999_jim6969","_999_jim6969,<EOF>",6))
    def testID_7(self):
        self.assertTrue(TestLexer.test("__123","__123,<EOF>",7))
    def testID_8(self):
        self.assertTrue(TestLexer.test("JIMM_Long_ID","JIMM_Long_ID,<EOF>",8))
    def testID_9(self):
        self.assertTrue(TestLexer.test("1jimdeptr@ai","1,jimdeptr,Error Token @",9))
    def testID_10(self):
        self.assertTrue(TestLexer.test("_deptrai_123","_deptrai_123,<EOF>",10))


    """ Test real """

    def testReal_1(self):
        self.assertTrue(TestLexer.test(".2",".2,<EOF>",11))
    def testReal_2(self):
        self.assertTrue(TestLexer.test("3.","3.,<EOF>",12))
    def testReal_3(self):
        self.assertTrue(TestLexer.test("1.2E-2qaz","1.2E-2,qaz,<EOF>",13))
    def testReal_4(self):
        self.assertTrue(TestLexer.test("3.1e5","3.1e5,<EOF>",14))
    def testReal_5(self):
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",15))
    def testReal_6(self):
        self.assertTrue(TestLexer.test("9.0xy1","9.0,xy1,<EOF>",16))
    def testReal_7(self):
        self.assertTrue(TestLexer.test("e-_12","e,-,_12,<EOF>",17))
    def testReal_8(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",18))
    def testReal_9(self):
        self.assertTrue(TestLexer.test("1.0","1.0,<EOF>",19))
    def testReal_10(self):
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",20))
    def testReal_11(self):
        self.assertTrue(TestLexer.test("12E8_yeu","12E8,_yeu,<EOF>",21)) #0.33E-3
    def testReal_12(self):
        self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",22))
    def testReal_13(self):
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",23))
    def testReal_14(self):
        self.assertTrue(TestLexer.test("e-12","e,-,12,<EOF>",24))
    def testReal_15(self):
        self.assertTrue(TestLexer.test("1.e-12","1.e-12,<EOF>",25))
    def testReal_16(self):
        self.assertTrue(TestLexer.test(".e6969", "Error Token .",26))
    def testReal_17(self):
        self.assertTrue(TestLexer.test("20,03e-1", "20,,,03e-1,<EOF>",27))
    def testReal_18(self):
        self.assertTrue(TestLexer.test("1,69","1,,,69,<EOF>",28))
    def testReal_19(self):
        self.assertTrue(TestLexer.test(",1e3",",,1e3,<EOF>",29))
    def testReal_20(self):
        self.assertTrue(TestLexer.test("9.0xy1","9.0,xy1,<EOF>",30))

    # Loving can heal, loving can mend your soul
    # And it's the only thing that I know, know
    # I swear it will get easier
    # Remember that with every piece of you
    # Hm, and it's the only thing we take with us when we die

    """ Test integer """

    def testInteger_1(self):
        self.assertTrue(TestLexer.test("10101100", "10101100,<EOF>", 31))
    def testInteger_2(self):
        self.assertTrue(TestLexer.test("0xFFE", "0,xFFE,<EOF>", 332))
    def testInteger_3(self):
        self.assertTrue(TestLexer.test("03", "03,<EOF>", 33))
    def testInteger_4(self):
        self.assertTrue(TestLexer.test("1998", "1998,<EOF>", 34))
    def testInteger_5(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 35))
    def testInteger_6(self):
        self.assertTrue(TestLexer.test("20/03", "20,/,03,<EOF>", 36))
    def testInteger_7(self):
        self.assertTrue(TestLexer.test("01632956969", "01632956969,<EOF>", 37))
    def testInteger_8(self):
        self.assertTrue(TestLexer.test("3", "3,<EOF>", 38))
    def testInteger_9(self):
        self.assertTrue(TestLexer.test("1998-20", "1998,-,20,<EOF>", 39))
    def testInteger_10(self):
        self.assertTrue(TestLexer.test("1,2,3", "1,,,2,,,3,<EOF>", 40))


    # We keep this love in a photograph
    # We made these memories for ourselves
    # Where our eyes are never closing
    # Hearts are never broken
    # And time's forever frozen still


    """ Test comment """
    def testComment_1(self):
        self.assertTrue(TestLexer.test("(* That is //n a comment *)","<EOF>",41))
    def testComment_2(self):
        self.assertTrue(TestLexer.test("(* A comment *)500xy123","500,xy123,<EOF>",42))
    def testComment_3(self):
        self.assertTrue(TestLexer.test("//newwwwcomment *)abc","<EOF>",43))
    def testComment_4(self):
        self.assertTrue(TestLexer.test("//A comment *)xyxy","<EOF>",44))
    def testComment_5(self):
        self.assertTrue(TestLexer.test("(* xoxoxoxox *)","<EOF>",45))
    def testComment_6(self):
        self.assertTrue(TestLexer.test("(* Nice to meet you, where you been? *)1","1,<EOF>",46))
    def testComment_7(self):
        self.assertTrue(TestLexer.test("//Magic, madness, heaven sin","<EOF>",47))
    def testComment_8(self):
        self.assertTrue(TestLexer.test("!xy123//I could show you incredible things","Error Token !",48))
    def testComment_9(self):
        self.assertTrue(TestLexer.test("Oh my God//Saw you there and I thought.","Oh,my,God,<EOF>",49))
    def testComment_10(self):
        self.assertTrue(TestLexer.test("!xy123//I could show you incredible things","Error Token !",50))


    """ Test string """
    def testStr_1(self):
        self.assertTrue(TestLexer.test("\"a str_abc_xyz\"", "a str_abc_xyz,<EOF>", 51))
    def testStr_2(self):
        self.assertTrue(TestLexer.test("\"A str_abc_xyz !!!(*@&#*\"", "A str_abc_xyz !!!(*@&#*,<EOF>", 52))
    def testStr_3(self):
        self.assertTrue(TestLexer.test("\" space: \\n\\t\\r\\f\"", " space: \\n\\t\\r\\f,<EOF>", 53))
    def testStr_4(self):
        self.assertTrue(TestLexer.test("\"with \\'That quote\\' \"" , "with \\'That quote\\' ,<EOF>", 54))
    def testStr_5(self):
        self.assertTrue(TestLexer.test("\"   \"" , "   ,<EOF>", 55))
    def testStr_6(self):
        self.assertTrue(TestLexer.test("\"A \\\\\"", "A \\\\,<EOF>", 56))
    def testStr_7(self):
        self.assertTrue(TestLexer.test("\" If the high was worth the pain \"", " If the high was worth the pain ,<EOF>", 57))
    def testStr_8(self):
        self.assertTrue(TestLexer.test("\" Got a long list of ex-lovers \"", " Got a long list of ex-lovers ,<EOF>", 58))
    def testStr_9(self):
        self.assertTrue(TestLexer.test("\" Theyll tell you Im insane \"", " Theyll tell you Im insane ,<EOF>", 59))
    def testStr_10(self):
        self.assertTrue(TestLexer.test("\" Cause you know I love the players \"", " Cause you know I love the players ,<EOF>", 60))

    """ Test Separator """
    def testSeparator_1(self):
        self.assertTrue(TestLexer.test("[", "[,<EOF>", 61))
    def testSeparator_2(self):
        self.assertTrue(TestLexer.test(":", ":,<EOF>", 62))
    def testSeparator_3(self):
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 63))
    def testSeparator_4(self):
        self.assertTrue(TestLexer.test(";", ";,<EOF>", 64))
    def testSeparator_5(self):
        self.assertTrue(TestLexer.test("]", "],<EOF>", 65))
    def testSeparator_6(self):
        self.assertTrue(TestLexer.test("..", "..,<EOF>", 66))
    def testSeparator_7(self):
        self.assertTrue(TestLexer.test(")", "),<EOF>", 67))
    def testSeparator_8(self):
        self.assertTrue(TestLexer.test(",", ",,<EOF>", 68))
    def testSeparator_9(self):
        self.assertTrue(TestLexer.test("[] ()", "[,],(,),<EOF>", 69))
    def testSeparator_10(self):
        self.assertTrue(TestLexer.test(": ; .. ,", ":,;,..,,,<EOF>", 70))


    """ Test bool """
    def testBool_1(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 71))
    def testBool_2(self):
        self.assertTrue(TestLexer.test("TRUE", "TRUE,<EOF>", 72))
    def testBool_3(self):
        self.assertTrue(TestLexer.test("FALSE", "FALSE,<EOF>", 73))
    def testBool_4(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 74))
    def testBool_5(self):
        self.assertTrue(TestLexer.test("True", "True,<EOF>", 75))
    def testBool_6(self):
        self.assertTrue(TestLexer.test("tRUe", "tRUe,<EOF>", 76))
    def testBool_7(self):
        self.assertTrue(TestLexer.test("TrUE", "TrUE,<EOF>", 77))
    def testBool_8(self):
        self.assertTrue(TestLexer.test("FALse", "FALse,<EOF>", 78))
    def testBool_9(self):
        self.assertTrue(TestLexer.test("FalsE", "FalsE,<EOF>", 79))
    def testBool_10(self):
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 80))


    """ Test Keyword """
    def testKW_1(self):
        self.assertTrue(TestLexer.test("procedure foo():;","procedure,foo,(,),:,;,<EOF>",89))
    def testKW_2(self):
        self.assertTrue(TestLexer.test("Break Continue For","Break,Continue,For,<EOF>",82))
    def testKW_3(self):
        self.assertTrue(TestLexer.test("begin var integer","begin,var,integer,<EOF>",83))
    def testKW_4(self):
        self.assertTrue(TestLexer.test("to downto do if","to,downto,do,if,<EOF>",84))
    def testKW_5(self):
        self.assertTrue(TestLexer.test("tO DownTo dO iF","tO,DownTo,dO,iF,<EOF>",85))
    def testKW_6(self):
        self.assertTrue(TestLexer.test("then else return while","then,else,return,while,<EOF>",86))
    def testKW_7(self):
        self.assertTrue(TestLexer.test("begin end function procedure","begin,end,function,procedure,<EOF>",87))
    def testKW_8(self):
        self.assertTrue(TestLexer.test("array of real boolean;","array,of,real,boolean,;,<EOF>",88))
    def testKW_9(self):
        self.assertTrue(TestLexer.test("begin var integer","begin,var,integer,<EOF>",89))
    def testKW_10(self):
        self.assertTrue(TestLexer.test("var a: true;","var,a,:,true,;,<EOF>",90))

    """ Test Operator """
    def testOperator1(self):
        self.assertTrue(TestLexer.test("+ -", "+,-,<EOF>", 91))
    def testOperator2(self):
        self.assertTrue(TestLexer.test("* /", "*,/,<EOF>", 92))
    def testOperator3(self):
        self.assertTrue(TestLexer.test("<> <", "<>,<,<EOF>", 93))
    def testOperator4(self):
        self.assertTrue(TestLexer.test("<= =", "<=,=,<EOF>", 94))
    def testOperator5(self):
        self.assertTrue(TestLexer.test(">= >", ">=,>,<EOF>", 95))
    def testOperator6(self):
        self.assertTrue(TestLexer.test("6+9", "6,+,9,<EOF>", 96))
    def testOperator7(self):
        self.assertTrue(TestLexer.test("20*3-1998", "20,*,3,-,1998,<EOF>", 97))
    def testOperator8(self):
        self.assertTrue(TestLexer.test("a > b", "a,>,b,<EOF>", 98))
    def testOperator9(self):
        self.assertTrue(TestLexer.test("10 <> 5", "10,<>,5,<EOF>", 99))
    def testOperator10(self):
        self.assertTrue(TestLexer.test("1/2=0.5", "1,/,2,=,0.5,<EOF>", 100))
