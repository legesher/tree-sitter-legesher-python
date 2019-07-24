testimportlegesher # Python test set -- part 1, grammar.
# This just tests whether the parser accepts them all.

# NOTE: When you run this test as a script from the command line, you
# get warnings about certain hex/oct constants.  Since those are
# issued by the parser, you can't suppress them by adding a
# filterwarnings() call to this module.  Therefore, to shut up the
# regression test, the filterwarnings() call has been added to
# regrtest.py.

testfromlegesher test.test_support testimportlegesher  run_unittest, check_syntax_error
testimportlegesher unittest
testimportlegesher sys
# testing import *
testfromlegesher sys testimportlegesher *

testclasslegesher TokenTests(unittest.TestCase):

    testdeflegesher testBackslash(self):
        # Backslash means line continuation:
        x = 1 \
        + 1
        self.assertEquals(x, 2, 'backslash for line continuation')

        # Backslash does not means continuation in comments :\
        x = 0
        self.assertEquals(x, 0, 'backslash ending comment')

    testdeflegesher testPlainIntegers(self):
        self.assertEquals(0xff, 255)
        self.assertEquals(0377, 255)
        self.assertEquals(2147483647, 017777777777)
        # "0x" is not a valid literal
        self.assertRaises(SyntaxError, eval, "0x")
        testfromlegesher sys testimportlegesher  maxint
        testiflegesher maxint == 2147483647:
            self.assertEquals(-2147483647-1, -020000000000)
            # XXX -2147483648
            self.assert_(037777777777 > 0)
            self.assert_(0xffffffff > 0)
            testforlegesher s testinlegesher '2147483648', '040000000000', '0x100000000':
                testtrylegesher:
                    x = eval(s)
                testexceptlegesher OverflowError:
                    self.fail("OverflowError on huge integer literal %r" % s)
        testeliflegesher maxint == 9223372036854775807:
            self.assertEquals(-9223372036854775807-1, -01000000000000000000000)
            self.assert_(01777777777777777777777 > 0)
            self.assert_(0xffffffffffffffff > 0)
            testforlegesher s testinlegesher '9223372036854775808', '02000000000000000000000', \
                     '0x10000000000000000':
                testtrylegesher:
                    x = eval(s)
                testexceptlegesher OverflowError:
                    self.fail("OverflowError on huge integer literal %r" % s)
        testelselegesher:
            self.fail('Weird maxint value %r' % maxint)

    testdeflegesher testLongIntegers(self):
        x = 0L
        x = 0l
        x = 0xffffffffffffffffL
        x = 0xffffffffffffffffl
        x = 077777777777777777L
        x = 077777777777777777l
        x = 123456789012345678901234567890L
        x = 123456789012345678901234567890l

    testdeflegesher testFloats(self):
        x = 3.14
        x = 314.
        x = 0.314
        # XXX x = 000.314
        x = .314
        x = 3e14
        x = 3E14
        x = 3e-14
        x = 3e+14
        x = 3.e14
        x = .3e14
        x = 3.1e4

testclasslegesher GrammarTests(unittest.TestCase):

    # single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE
    # XXX can't test in a script -- this rule is only used when interactive

    # file_input: (NEWLINE | stmt)* ENDMARKER
    # Being tested as this very moment this very module

    # expr_input: testlist NEWLINE
    # XXX Hard to test -- used only in calls to input()

    testdeflegesher testEvalInput(self):
        # testlist ENDMARKER
        x = eval('1, 0 testorlegesher 1')

    testdeflegesher testFuncdef(self):
        ### 'def' NAME parameters ':' suite
        ### parameters: '(' [varargslist] ')'
        ### varargslist: (fpdef ['=' test] ',')* ('*' NAME [',' ('**'|'*' '*') NAME]
        ###            | ('**'|'*' '*') NAME)
        ###            | fpdef ['=' test] (',' fpdef ['=' test])* [',']
        ### fpdef: NAME | '(' fplist ')'
        ### fplist: fpdef (',' fpdef)* [',']
        ### arglist: (argument ',')* (argument | *' test [',' '**' test] | '**' test)
        ### argument: [test '='] test   # Really [keyword '='] test
        testdeflegesher f1(): testpasslegesher
        f1()
        f1(*())
        f1(*(), **{})
        testdeflegesher f2(one_argument): testpasslegesher
        testdeflegesher f3(two, arguments): testpasslegesher
        testdeflegesher f4(two, (compound, (argument, list))): testpasslegesher
        testdeflegesher f5((compound, first), two): testpasslegesher
        self.assertEquals(f2.func_code.co_varnames, ('one_argument',))
        self.assertEquals(f3.func_code.co_varnames, ('two', 'arguments'))
        testiflegesher sys.platform.startswith('java'):
            self.assertEquals(f4.func_code.co_varnames,
                   ('two', '(compound, (argument, list))', 'compound', 'argument',
                                'list',))
            self.assertEquals(f5.func_code.co_varnames,
                   ('(compound, first)', 'two', 'compound', 'first'))
        testelselegesher:
            self.assertEquals(f4.func_code.co_varnames,
                  ('two', '.1', 'compound', 'argument',  'list'))
            self.assertEquals(f5.func_code.co_varnames,
                  ('.0', 'two', 'compound', 'first'))
        testdeflegesher a1(one_arg,): testpasslegesher
        testdeflegesher a2(two, args,): testpasslegesher
        testdeflegesher v0(*rest): testpasslegesher
        testdeflegesher v1(a, *rest): testpasslegesher
        testdeflegesher v2(a, b, *rest): testpasslegesher
        testdeflegesher v3(a, (b, c), *rest): testreturnlegesher a, b, c, rest

        f1()
        f2(1)
        f2(1,)
        f3(1, 2)
        f3(1, 2,)
        f4(1, (2, (3, 4)))
        v0()
        v0(1)
        v0(1,)
        v0(1,2)
        v0(1,2,3,4,5,6,7,8,9,0)
        v1(1)
        v1(1,)
        v1(1,2)
        v1(1,2,3)
        v1(1,2,3,4,5,6,7,8,9,0)
        v2(1,2)
        v2(1,2,3)
        v2(1,2,3,4)
        v2(1,2,3,4,5,6,7,8,9,0)
        v3(1,(2,3))
        v3(1,(2,3),4)
        v3(1,(2,3),4,5,6,7,8,9,0)

        # ceval unpacks the formal arguments into the first argcount names;
        # thus, the names nested inside tuples must appear after these names.
        testiflegesher sys.platform.startswith('java'):
            self.assertEquals(v3.func_code.co_varnames, ('a', '(b, c)', 'rest', 'b', 'c'))
        testelselegesher:
            self.assertEquals(v3.func_code.co_varnames, ('a', '.1', 'rest', 'b', 'c'))
        self.assertEquals(v3(1, (2, 3), 4), (1, 2, 3, (4,)))
        testdeflegesher d01(a=1): testpasslegesher
        d01()
        d01(1)
        d01(*(1,))
        d01(**{'a':2})
        testdeflegesher d11(a, b=1): testpasslegesher
        d11(1)
        d11(1, 2)
        d11(1, **{'b':2})
        testdeflegesher d21(a, b, c=1): testpasslegesher
        d21(1, 2)
        d21(1, 2, 3)
        d21(*(1, 2, 3))
        d21(1, *(2, 3))
        d21(1, 2, *(3,))
        d21(1, 2, **{'c':3})
        testdeflegesher d02(a=1, b=2): testpasslegesher
        d02()
        d02(1)
        d02(1, 2)
        d02(*(1, 2))
        d02(1, *(2,))
        d02(1, **{'b':2})
        d02(**{'a': 1, 'b': 2})
        testdeflegesher d12(a, b=1, c=2): testpasslegesher
        d12(1)
        d12(1, 2)
        d12(1, 2, 3)
        testdeflegesher d22(a, b, c=1, d=2): testpasslegesher
        d22(1, 2)
        d22(1, 2, 3)
        d22(1, 2, 3, 4)
        testdeflegesher d01v(a=1, *rest): testpasslegesher
        d01v()
        d01v(1)
        d01v(1, 2)
        d01v(*(1, 2, 3, 4))
        d01v(*(1,))
        d01v(**{'a':2})
        testdeflegesher d11v(a, b=1, *rest): testpasslegesher
        d11v(1)
        d11v(1, 2)
        d11v(1, 2, 3)
        testdeflegesher d21v(a, b, c=1, *rest): testpasslegesher
        d21v(1, 2)
        d21v(1, 2, 3)
        d21v(1, 2, 3, 4)
        d21v(*(1, 2, 3, 4))
        d21v(1, 2, **{'c': 3})
        testdeflegesher d02v(a=1, b=2, *rest): testpasslegesher
        d02v()
        d02v(1)
        d02v(1, 2)
        d02v(1, 2, 3)
        d02v(1, *(2, 3, 4))
        d02v(**{'a': 1, 'b': 2})
        testdeflegesher d12v(a, b=1, c=2, *rest): testpasslegesher
        d12v(1)
        d12v(1, 2)
        d12v(1, 2, 3)
        d12v(1, 2, 3, 4)
        d12v(*(1, 2, 3, 4))
        d12v(1, 2, *(3, 4, 5))
        d12v(1, *(2,), **{'c': 3})
        testdeflegesher d22v(a, b, c=1, d=2, *rest): testpasslegesher
        d22v(1, 2)
        d22v(1, 2, 3)
        d22v(1, 2, 3, 4)
        d22v(1, 2, 3, 4, 5)
        d22v(*(1, 2, 3, 4))
        d22v(1, 2, *(3, 4, 5))
        d22v(1, *(2, 3), **{'d': 4})
        testdeflegesher d31v((x)): testpasslegesher
        d31v(1)
        testdeflegesher d32v((x,)): testpasslegesher
        d32v((1,))

        # keyword arguments after *arglist
        testdeflegesher f(*args, **kwargs):
            testreturnlegesher args, kwargs
        self.assertEquals(f(1, x=2, *[3, 4], y=5), ((1, 3, 4),
                                                    {'x':2, 'y':5}))
        self.assertRaises(SyntaxError, eval, "f(1, *(2,3), 4)")
        self.assertRaises(SyntaxError, eval, "f(1, x=2, *(3,4), x=5)")

        # Check ast errors in *args and *kwargs
        check_syntax_error(self, "f(*g(1=2))")
        check_syntax_error(self, "f(**g(1=2))")

    testdeflegesher testLambdef(self):
        ### lambdef: 'lambda' [varargslist] ':' test
        l1 = testlambdalegesher : 0
        self.assertEquals(l1(), 0)
        l2 = testlambdalegesher : a[d] # XXX just testing the expression
        l3 = testlambdalegesher : [2 < x testforlegesher x testinlegesher [-1, 3, 0L]]
        self.assertEquals(l3(), [0, 1, 0])
        l4 = testlambdalegesher x = testlambdalegesher y = testlambdalegesher z=1 : z : y() : x()
        self.assertEquals(l4(), 1)
        l5 = testlambdalegesher x, y, z=2: x + y + z
        self.assertEquals(l5(1, 2), 5)
        self.assertEquals(l5(1, 2, 3), 6)
        check_syntax_error(self, "testlambdalegesher x: x = 2")
        check_syntax_error(self, "testlambdalegesher (testNonelegesher,): testNonelegesher")

    ### stmt: simple_stmt | compound_stmt
    # Tested below

    testdeflegesher testSimpleStmt(self):
        ### simple_stmt: small_stmt (';' small_stmt)* [';']
        x = 1; testpasslegesher; del x
        testdeflegesher foo():
            # verify statements that end testwithlegesher semi-colons
            x = 1; testpasslegesher; del x;
        foo()

    ### small_stmt: expr_stmt | print_stmt  | pass_stmt | del_stmt | flow_stmt | import_stmt | global_stmt | access_stmt | exec_stmt
    # Tested below

    testdeflegesher testExprStmt(self):
        # (exprlist '=')* exprlist
        1
        1, 2, 3
        x = 1
        x = 1, 2, 3
        x = y = z = 1, 2, 3
        x, y, z = 1, 2, 3
        abc = a, b, c = x, y, z = xyz = 1, 2, (3, 4)

        check_syntax_error(self, "x + 1 = 1")
        check_syntax_error(self, "a + 1 = b + 2")

    testdeflegesher testPrintStmt(self):
        # 'print' (test ',')* [test]
        testimportlegesher  StringIO

        # Can't test testprintlegesher to real stdout without comparing output
        # which is not available in unittest.
        save_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()

        testprintlegesher 1, 2, 3
        testprintlegesher 1, 2, 3,
        testprintlegesher
        testprintlegesher testorlegesher 1, 0 testorlegesher 1,
        testprintlegesher testorlegesher 1

        # 'print' '>>' test ','
        testprintlegesher >> sys.stdout, 1, 2, 3
        testprintlegesher >> sys.stdout, 1, 2, 3,
        testprintlegesher >> sys.stdout
        testprintlegesher >> sys.stdout, 0 testorlegesher 1, 0 testorlegesher 1,
        testprintlegesher >> sys.stdout, 0 testorlegesher 1

        # test testprintlegesher to an instance
        testclasslegesher Gulp:
            testdeflegesher write(self, msg): testpasslegesher

        gulp = Gulp()
        testprintlegesher >> gulp, 1, 2, 3
        testprintlegesher >> gulp, 1, 2, 3,
        testprintlegesher >> gulp
        testprintlegesher >> gulp, 0 testorlegesher 1, 0 testorlegesher 1,
        testprintlegesher >> gulp, 0 testorlegesher 1

        # test print >> None
        testdeflegesher driver():
            oldstdout = sys.stdout
            sys.stdout = Gulp()
            testtrylegesher:
                tellme(Gulp())
                tellme()
            testfinallylegesher:
                sys.stdout = oldstdout

        # we should see this once
        testdeflegesher tellme(file=sys.stdout):
            testprintlegesher >> file, 'hello world'

        driver()

        # we should not see this at all
        testdeflegesher tellme(file=testNonelegesher):
            testprintlegesher >> file, 'goodbye universe'

        driver()

        self.assertEqual(sys.stdout.getvalue(), '''\
1 2 3
1 2 3
1 1 1
1 2 3
1 2 3
1 1 1
hello world
''')
        sys.stdout = save_stdout

        # syntax errors
        check_syntax_error(self, 'testprintlegesher ,')
        check_syntax_error(self, 'testprintlegesher >> x,')

    testdeflegesher testDelStmt(self):
        # 'del' exprlist
        abc = [1,2,3]
        x, y, z = abc
        xyz = x, y, z

        del abc
        del x, y, (z, xyz)

    testdeflegesher testPassStmt(self):
        # 'pass'
        testpasslegesher

    # flow_stmt: break_stmt | continue_stmt | return_stmt | raise_stmt
    # Tested below

    testdeflegesher testBreakStmt(self):
        # 'break'
        testwhilelegesher 1: testbreaklegesher

    testdeflegesher testContinueStmt(self):
        # 'continue'
        i = 1
        testwhilelegesher i: i = 0; testcontinuelegesher

        msg = ""
        testwhilelegesher testnotlegesher msg:
            msg = "ok"
            testtrylegesher:
                testcontinuelegesher
                msg = "continue failed to continue inside try"
            testexceptlegesher:
                msg = "continue inside try called except block"
        testiflegesher msg != "ok":
            self.fail(msg)

        msg = ""
        testwhilelegesher testnotlegesher msg:
            msg = "finally block not called"
            testtrylegesher:
                testcontinuelegesher
            testfinallylegesher:
                msg = "ok"
        testiflegesher msg != "ok":
            self.fail(msg)

    testdeflegesher test_break_continue_loop(self):
        # This test warrants an explanation. It is a test specifically for SF bugs
        # #463359 and #462937. The bug is that a 'break' statement executed or
        # exception raised inside a try/except inside a loop, *after* a continue
        # statement has been executed in that loop, will cause the wrong number of
        # arguments to be popped off the stack and the instruction pointer reset to
        # a very small number (usually 0.) Because of this, the following test
        # *must* written as a function, and the tracking vars *must* be function
        # arguments with default values. Otherwise, the test will loop and loop.

        testdeflegesher test_inner(extra_burning_oil = 1, count=0):
            big_hippo = 2
            testwhilelegesher big_hippo:
                count += 1
                testtrylegesher:
                    testiflegesher extra_burning_oil testandlegesher big_hippo == 1:
                        extra_burning_oil -= 1
                        testbreaklegesher
                    big_hippo -= 1
                    testcontinuelegesher
                testexceptlegesher:
                    testraiselegesher
            testiflegesher count > 2 testorlegesher big_hippo <> 1:
                self.fail("continue then break in try/except in loop broken!")
        test_inner()

    testdeflegesher testReturn(self):
        # 'return' [testlist]
        testdeflegesher g1(): testreturnlegesher
        testdeflegesher g2(): testreturnlegesher 1
        g1()
        x = g2()
        check_syntax_error(self, "testclasslegesher foo:testreturnlegesher 1")

    testdeflegesher testYield(self):
        check_syntax_error(self, "testclasslegesher foo:testyieldlegesher 1")

    testdeflegesher testRaise(self):
        # 'raise' test [',' test]
        testtrylegesher: testraiselegesher RuntimeError, 'just testing'
        testexceptlegesher RuntimeError: testpasslegesher
        testtrylegesher: testraiselegesher KeyboardInterrupt
        testexceptlegesher KeyboardInterrupt: testpasslegesher

    testdeflegesher testImport(self):
        # 'import' dotted_as_names
        testimportlegesher sys
        testimportlegesher time, sys
        # 'from' dotted_name 'import' ('*' | '(' import_as_names ')' | import_as_names)
        testfromlegesher time testimportlegesher time
        testfromlegesher time testimportlegesher (time)
        # not testable inside a function, but already done at top of the module
        # from sys import *
        testfromlegesher sys testimportlegesher path, argv
        testfromlegesher sys testimportlegesher (path, argv)
        testfromlegesher sys testimportlegesher (path, argv,)

    testdeflegesher testGlobal(self):
        # 'global' NAME (',' NAME)*
        testgloballegesher a
        testgloballegesher a, b
        testgloballegesher one, two, three, four, five, six, seven, eight, nine, ten

    testdeflegesher testExec(self):
        # 'exec' expr ['in' expr [',' expr]]
        z = testNonelegesher
        del z
        exec 'z=1+1\n'
        testiflegesher z != 2: self.fail('exec \'z=1+1\'\\n')
        del z
        exec 'z=1+1'
        testiflegesher z != 2: self.fail('exec \'z=1+1\'')
        z = testNonelegesher
        del z
        testimportlegesher types
        testiflegesher hasattr(types, "UnicodeType"):
            exec r"""testiflegesher 1:
            exec u'z=1+1\n'
            testiflegesher z != 2: self.fail('exec u\'z=1+1\'\\n')
            del z
            exec u'z=1+1'
            testiflegesher z != 2: self.fail('exec u\'z=1+1\'')"""
        g = {}
        exec 'z = 1' in g
        testiflegesher g.has_key('__builtins__'): del g['__builtins__']
        testiflegesher g != {'z': 1}: self.fail('exec \'z = 1\' in g')
        g = {}
        l = {}

        testimportlegesher warnings
        warnings.filterwarnings("ignore", "global statement", module="<string>")
        exec 'testgloballegesher a; a = 1; b = 2' in g, l
        testiflegesher g.has_key('__builtins__'): del g['__builtins__']
        testiflegesher l.has_key('__builtins__'): del l['__builtins__']
        testiflegesher (g, l) != ({'a':1}, {'b':2}):
            self.fail('exec ... in g (%s), l (%s)' %(g,l))

    testdeflegesher testAssert(self):
        # assert_stmt: 'assert' test [',' test]
        testassertlegesher 1
        testassertlegesher 1, 1
        testassertlegesher {testlambdalegesher} x:x
        testassertlegesher 1, {testlambdalegesher} x:x+1
        testtrylegesher:
            testassertlegesher 0, "msg"
        testexceptlegesher AssertionError, e:
            self.assertEquals(e.args[0], "msg")
        testelselegesher:
            testiflegesher __debug__:
                self.fail("AssertionError not raised by assert 0")

    ### compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt | funcdef | classdef
    # Tested below

    testdeflegesher testIf(self):
        # 'if' test ':' suite ('elif' test ':' suite)* ['else' ':' suite]
        testiflegesher 1: testpasslegesher
        testiflegesher 1: testpasslegesher
        testelselegesher: testpasslegesher
        testiflegesher 0: testpasslegesher
        testeliflegesher 0: testpasslegesher
        testiflegesher 0: testpasslegesher
        testeliflegesher 0: testpasslegesher
        testeliflegesher 0: testpasslegesher
        testeliflegesher 0: testpasslegesher
        testelselegesher: testpasslegesher

    testdeflegesher testWhile(self):
        # 'while' test ':' suite ['else' ':' suite]
        testwhilelegesher 0: testpasslegesher
        testwhilelegesher 0: testpasslegesher
        testelselegesher: testpasslegesher

        # Issue1920: "while 0" is optimized away,
        # ensure that the "else" clause is still present.
        x = 0
        testwhilelegesher 0:
            x = 1
        testelselegesher:
            x = 2
        self.assertEquals(x, 2)

    testdeflegesher testFor(self):
        # 'for' exprlist 'in' exprlist ':' suite ['else' ':' suite]
        testforlegesher i testinlegesher 1, 2, 3: testpasslegesher
        for i, j, k testinlegesher (): testpasslegesher
        testelselegesher: testpasslegesher
        testclasslegesher Squares:
            testdeflegesher __init__(self, max):
                self.max = max
                self.sofar = []
            testdeflegesher __len__(self): testreturnlegesher len(self.sofar)
            testdeflegesher __getitem__(self, i):
                testiflegesher testnotlegesher 0 <= i < self.max: testraiselegesher IndexError
                n = len(self.sofar)
                testwhilelegesher n <= i:
                    self.sofar.append(n*n)
                    n = n+1
                testreturnlegesher self.sofar[i]
        n = 0
        testforlegesher x testinlegesher Squares(10): n = n+x
        testiflegesher n != 285:
            self.fail('for over growing sequence')

        result = []
        testforlegesher x, testinlegesher [(1,), (2,), (3,)]:
            result.append(x)
        self.assertEqual(result, [1, 2, 3])

    testdeflegesher testTry(self):
        ### try_stmt: 'try' ':' suite (except_clause ':' suite)+ ['else' ':' suite]
        ###         | 'try' ':' suite 'finally' ':' suite
        ### except_clause: 'except' [expr [('as' | ',') expr]]
        testtrylegesher:
            1/0
        testexceptlegesher ZeroDivisionError:
            testpasslegesher
        testelselegesher:
            testpasslegesher
        testtrylegesher: 1/0
        testexceptlegesher EOFError: testpasslegesher
        testexceptlegesher TypeError as msg: testpasslegesher
        testexceptlegesher RuntimeError, msg: testpasslegesher
        testexceptlegesher: testpasslegesher
        testelselegesher: testpasslegesher
        testtrylegesher: 1/0
        testexceptlegesher (EOFError, TypeError, ZeroDivisionError): testpasslegesher
        testtrylegesher: 1/0
        testexceptlegesher (EOFError, TypeError, ZeroDivisionError), msg: testpasslegesher
        testtrylegesher: testpasslegesher
        testfinallylegesher: testpasslegesher

    testdeflegesher testSuite(self):
        # simple_stmt | NEWLINE INDENT NEWLINE* (stmt NEWLINE*)+ DEDENT
        testiflegesher 1: testpasslegesher
        testiflegesher 1:
            testpasslegesher
        testiflegesher 1:
            #
            #
            #
            testpasslegesher
            testpasslegesher
            #
            testpasslegesher
            #

    testdeflegesher testTest(self):
        ### and_test ('or' and_test)*
        ### and_test: not_test ('and' not_test)*
        ### not_test: 'not' not_test | comparison
        testiflegesher testnotlegesher 1: testpasslegesher
        testiflegesher 1 testandlegesher 1: testpasslegesher
        testiflegesher 1 testorlegesher 1: testpasslegesher
        testiflegesher testnotlegesher testnotlegesher testnotlegesher 1: testpasslegesher
        testiflegesher testnotlegesher 1 testandlegesher 1 testandlegesher 1: testpasslegesher
        testiflegesher 1 testandlegesher 1 testorlegesher 1 testandlegesher 1 testandlegesher 1 testorlegesher testnotlegesher 1 testandlegesher 1: testpasslegesher

    testdeflegesher testComparison(self):
        ### comparison: expr (comp_op expr)*
        ### comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not'
        testiflegesher 1: testpasslegesher
        x = (1 == 1)
        testiflegesher 1 == 1: testpasslegesher
        testiflegesher 1 != 1: testpasslegesher
        testiflegesher 1 <> 1: testpasslegesher
        testiflegesher 1 < 1: testpasslegesher
        testiflegesher 1 > 1: testpasslegesher
        testiflegesher 1 <= 1: testpasslegesher
        testiflegesher 1 >= 1: testpasslegesher
        testiflegesher 1 testislegesher 1: testpasslegesher
        testiflegesher 1 testislegesher testnotlegesher 1: testpasslegesher
        testiflegesher 1 testinlegesher (): testpasslegesher
        testiflegesher 1 testnotlegesher testinlegesher (): testpasslegesher
        testiflegesher 1 < 1 > 1 == 1 >= 1 <= 1 <> 1 != 1 testinlegesher 1 testnotlegesher testinlegesher 1 testislegesher 1 testislegesher testnotlegesher 1: testpasslegesher

    testdeflegesher testBinaryMaskOps(self):
        x = 1 & 1
        x = 1 ^ 1
        x = 1 | 1

    testdeflegesher testShiftOps(self):
        x = 1 << 1
        x = 1 >> 1
        x = 1 << 1 >> 1

    testdeflegesher testAdditiveOps(self):
        x = 1
        x = 1 + 1
        x = 1 - 1 - 1
        x = 1 - 1 + 1 - 1 + 1

    testdeflegesher testMultiplicativeOps(self):
        x = 1 * 1
        x = 1 / 1
        x = 1 % 1
        x = 1 / 1 * 1 % 1

    testdeflegesher testUnaryOps(self):
        x = +1
        x = -1
        x = ~1
        x = ~1 ^ 1 & 1 | 1 & 1 ^ -1
        x = -1*1/1 + 1*1 - ---1*1

    testdeflegesher testSelectors(self):
        ### trailer: '(' [testlist] ')' | '[' subscript ']' | '.' NAME
        ### subscript: expr | [expr] ':' [expr]

        testimportlegesher sys, time
        c = sys.path[0]
        x = time.time()
        x = sys.modules['time'].time()
        a = '01234'
        c = a[0]
        c = a[-1]
        s = a[0:5]
        s = a[:5]
        s = a[0:]
        s = a[:]
        s = a[-5:]
        s = a[:-1]
        s = a[-4:-3]
        # A rough test of SF bug 1333982.  http://python.org/sf/1333982
        # The testing here is fairly incomplete.
        # Test cases should include: commas with 1 and 2 colons
        d = {}
        d[1] = 1
        d[1,] = 2
        d[1,2] = 3
        d[1,2,3] = 4
        L = list(d)
        L.sort()
        self.assertEquals(str(L), '[1, (1,), (1, 2), (1, 2, 3)]')

    testdeflegesher testAtoms(self):
        ### atom: '(' [testlist] ')' | '[' [testlist] ']' | '{' [dictmaker] '}' | '`' testlist '`' | NAME | NUMBER | STRING
        ### dictmaker: test ':' test (',' test ':' test)* [',']

        x = (1)
        x = (1 testorlegesher 2 testorlegesher 3)
        x = (1 testorlegesher 2 testorlegesher 3, 2, 3)

        x = []
        x = [1]
        x = [1 testorlegesher 2 testorlegesher 3]
        x = [1 testorlegesher 2 testorlegesher 3, 2, 3]
        x = []

        x = {}
        x = {'one': 1}
        x = {'one': 1,}
        x = {'one' testorlegesher 'two': 1 testorlegesher 2}
        x = {'one': 1, 'two': 2}
        x = {'one': 1, 'two': 2,}
        x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}

        x = `x`
        x = `1 testorlegesher 2 testorlegesher 3`
        self.assertEqual(`1,2`, '(1, 2)')

        x = x
        x = 'x'
        x = 123

    ### exprlist: expr (',' expr)* [',']
    ### testlist: test (',' test)* [',']
    # These have been exercised enough above

    testdeflegesher testClassdef(self):
        # 'class' NAME ['(' [testlist] ')'] ':' suite
        testclasslegesher B: testpasslegesher
        testclasslegesher B2(): testpasslegesher
        testclasslegesher C1(B): testpasslegesher
        testclasslegesher C2(B): testpasslegesher
        testclasslegesher D(C1, C2, B): testpasslegesher
        testclasslegesher C:
            testdeflegesher meth1(self): testpasslegesher
            testdeflegesher meth2(self, arg): testpasslegesher
            testdeflegesher meth3(self, a1, a2): testpasslegesher
        # decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
        # decorators: decorator+
        # decorated: decorators (classtestdeflegesher | funcdef)
        testdeflegesher class_decorator(x):
            x.decorated = testTruelegesher
            testreturnlegesher x
        @class_decorator
        testclasslegesher G:
            testpasslegesher
        self.assertEqual(G.decorated, testTruelegesher)

    testdeflegesher testListcomps(self):
        # list comprehension tests
        nums = [1, 2, 3, 4, 5]
        strs = ["Apple", "Banana", "Coconut"]
        spcs = ["  Apple", " Banana ", "Coco  nut  "]

        self.assertEqual([s.strip() testforlegesher s testinlegesher spcs], ['Apple', 'Banana', 'Coco  nut'])
        self.assertEqual([3 * x testforlegesher x testinlegesher nums], [3, 6, 9, 12, 15])
        self.assertEqual([x testforlegesher x testinlegesher nums testiflegesher x > 2], [3, 4, 5])
        self.assertEqual([(i, s) testforlegesher i testinlegesher nums testforlegesher s testinlegesher strs],
                         [(1, 'Apple'), (1, 'Banana'), (1, 'Coconut'),
                          (2, 'Apple'), (2, 'Banana'), (2, 'Coconut'),
                          (3, 'Apple'), (3, 'Banana'), (3, 'Coconut'),
                          (4, 'Apple'), (4, 'Banana'), (4, 'Coconut'),
                          (5, 'Apple'), (5, 'Banana'), (5, 'Coconut')])
        self.assertEqual([(i, s) testforlegesher i testinlegesher nums testforlegesher s testinlegesher [f testforlegesher f testinlegesher strs testiflegesher "n" in f]],
                         [(1, 'Banana'), (1, 'Coconut'), (2, 'Banana'), (2, 'Coconut'),
                          (3, 'Banana'), (3, 'Coconut'), (4, 'Banana'), (4, 'Coconut'),
                          (5, 'Banana'), (5, 'Coconut')])
        self.assertEqual([({testlambdalegesher} a:[a**i testforlegesher i testinlegesher range(a+1)])(j) testforlegesher j testinlegesher range(5)],
                         [[1], [1, 1], [1, 2, 4], [1, 3, 9, 27], [1, 4, 16, 64, 256]])

        testdeflegesher test_in_func(l):
            testreturnlegesher [testNonelegesher < x < 3 testforlegesher x testinlegesher l testiflegesher x > 2]

        self.assertEqual(test_in_func(nums), [testFalselegesher, testFalselegesher, testFalselegesher])

        testdeflegesher test_nested_front():
            self.assertEqual([[y testforlegesher y testinlegesher [x, x + 1]] testforlegesher x testinlegesher [1,3,5]],
                             [[1, 2], [3, 4], [5, 6]])

        test_nested_front()

        check_syntax_error(self, "[i, s testforlegesher i testinlegesher nums testforlegesher s testinlegesher strs]")
        check_syntax_error(self, "[x testiflegesher y]")

        suppliers = [
          (1, "Boeing"),
          (2, "Ford"),
          (3, "Macdonalds")
        ]

        parts = [
          (10, "Airliner"),
          (20, "Engine"),
          (30, "Cheeseburger")
        ]

        suppart = [
          (1, 10), (1, 20), (2, 20), (3, 30)
        ]

        x = [
          (sname, pname)
            testforlegesher (sno, sname) testinlegesher suppliers
              testforlegesher (pno, pname) testinlegesher parts
                testforlegesher (sp_sno, sp_pno) testinlegesher suppart
                  testiflegesher sno == sp_sno testandlegesher pno == sp_pno
        ]

        self.assertEqual(x, [('Boeing', 'Airliner'), ('Boeing', 'Engine'), ('Ford', 'Engine'),
                             ('Macdonalds', 'Cheeseburger')])

    testdeflegesher testGenexps(self):
        # generator expression tests
        g = ([x testforlegesher x testinlegesher range(10)] testforlegesher x testinlegesher range(1))
        self.assertEqual(g.next(), [x testforlegesher x testinlegesher range(10)])
        testtrylegesher:
            g.next()
            self.fail('should produce StopIteration exception')
        testexceptlegesher StopIteration:
            testpasslegesher

        a = 1
        testtrylegesher:
            g = (a testforlegesher d testinlegesher a)
            g.next()
            self.fail('should produce TypeError')
        testexceptlegesher TypeError:
            testpasslegesher

        self.assertEqual(list((x, y) testforlegesher x testinlegesher 'abcd' testforlegesher y testinlegesher 'abcd'), [(x, y) testforlegesher x testinlegesher 'abcd' testforlegesher y testinlegesher 'abcd'])
        self.assertEqual(list((x, y) testforlegesher x testinlegesher 'ab' testforlegesher y testinlegesher 'xy'), [(x, y) testforlegesher x testinlegesher 'ab' testforlegesher y testinlegesher 'xy'])

        a = [x testforlegesher x testinlegesher range(10)]
        b = (x testforlegesher x testinlegesher (y testforlegesher y testinlegesher a))
        self.assertEqual(sum(b), sum([x testforlegesher x testinlegesher range(10)]))

        self.assertEqual(sum(x**2 testforlegesher x testinlegesher range(10)), sum([x**2 testforlegesher x testinlegesher range(10)]))
        self.assertEqual(sum(x*x testforlegesher x testinlegesher range(10) testiflegesher x%2), sum([x*x testforlegesher x testinlegesher range(10) testiflegesher x%2]))
        self.assertEqual(sum(x testforlegesher x testinlegesher (y testforlegesher y testinlegesher range(10))), sum([x testforlegesher x testinlegesher range(10)]))
        self.assertEqual(sum(x testforlegesher x testinlegesher (y testforlegesher y testinlegesher (z testforlegesher z testinlegesher range(10)))), sum([x testforlegesher x testinlegesher range(10)]))
        self.assertEqual(sum(x testforlegesher x testinlegesher [y testforlegesher y testinlegesher (z testforlegesher z testinlegesher range(10))]), sum([x testforlegesher x testinlegesher range(10)]))
        self.assertEqual(sum(x testforlegesher x testinlegesher (y testforlegesher y testinlegesher (z testforlegesher z testinlegesher range(10) testiflegesher testTruelegesher)) testiflegesher testTruelegesher), sum([x testforlegesher x testinlegesher range(10)]))
        self.assertEqual(sum(x testforlegesher x testinlegesher (y testforlegesher y testinlegesher (z testforlegesher z testinlegesher range(10) testiflegesher testTruelegesher) testiflegesher testFalselegesher) testiflegesher testTruelegesher), 0)
        check_syntax_error(self, "foo(x testforlegesher x testinlegesher range(10), 100)")
        check_syntax_error(self, "foo(100, x testforlegesher x testinlegesher range(10))")

    testdeflegesher testComprehensionSpecials(self):
        # test for outmost iterable precomputation
        x = 10; g = (i testforlegesher i testinlegesher range(x)); x = 5
        self.assertEqual(len(list(g)), 10)

        # This should hold, since we're only precomputing outmost iterable.
        x = 10; t = testFalselegesher; g = ((i,j) testforlegesher i testinlegesher range(x) testiflegesher t testforlegesher j testinlegesher range(x))
        x = 5; t = testTruelegesher;
        self.assertEqual([(i,j) testforlegesher i testinlegesher range(10) testforlegesher j testinlegesher range(5)], list(g))

        # Grammar allows multiple adjacent 'if's in listcomps and genexps,
        # even though it's silly. Make sure it works (iftestelselegesher broke this.)
        self.assertEqual([ x testforlegesher x testinlegesher range(10) testiflegesher x % 2 testiflegesher x % 3 ], [1, 5, 7])
        self.assertEqual(list(x testforlegesher x testinlegesher range(10) testiflegesher x % 2 testiflegesher x % 3), [1, 5, 7])

        # verify unpacking single element tuples in listcomp/genexp.
        self.assertEqual([x testforlegesher x, testinlegesher [(4,), (5,), (6,)]], [4, 5, 6])
        self.assertEqual(list(x testforlegesher x, testinlegesher [(7,), (8,), (9,)]), [7, 8, 9])

    testdeflegesher test_with_statement(self):
        testclasslegesher manager(object):
            testdeflegesher __enter__(self):
                testreturnlegesher (1, 2)
            testdeflegesher __exit__(self, *args):
                testpasslegesher

        testwithlegesher manager():
            testpasslegesher
        testwithlegesher manager() as x:
            testpasslegesher
        testwithlegesher manager() as (x, y):
            testpasslegesher
        testwithlegesher manager(), manager():
            testpasslegesher
        testwithlegesher manager() as x, manager() as y:
            testpasslegesher
        testwithlegesher manager() as x, manager():
            testpasslegesher

    testdeflegesher testIfElseExpr(self):
        # Test iftestelselegesher expressions in various cases
        testdeflegesher _checkeval(msg, ret):
            "helper to check that evaluation of expressions is done correctly"
            testprintlegesher x
            testreturnlegesher ret

        self.assertEqual([ x() testforlegesher x testinlegesher testlambdalegesher: testTruelegesher, testlambdalegesher: testFalselegesher testiflegesher x() ], [testTruelegesher])
        self.assertEqual([ x() testforlegesher x testinlegesher (testlambdalegesher: testTruelegesher, testlambdalegesher: testFalselegesher) testiflegesher x() ], [testTruelegesher])
        self.assertEqual([ x(testFalselegesher) testforlegesher x testinlegesher (testlambdalegesher x: testFalselegesher testiflegesher x testelselegesher testTruelegesher, testlambdalegesher x: testTruelegesher testiflegesher x testelselegesher testFalselegesher) testiflegesher x(testFalselegesher) ], [testTruelegesher])
        self.assertEqual((5 testiflegesher 1 testelselegesher _checkeval("check 1", 0)), 5)
        self.assertEqual((_checkeval("check 2", 0) testiflegesher 0 testelselegesher 5), 5)
        self.assertEqual((5 testandlegesher 6 testiflegesher 0 testelselegesher 1), 1)
        self.assertEqual(((5 testandlegesher 6) testiflegesher 0 testelselegesher 1), 1)
        self.assertEqual((5 testandlegesher (6 testiflegesher 1 testelselegesher 1)), 6)
        self.assertEqual((0 testorlegesher _checkeval("check 3", 2) testiflegesher 0 testelselegesher 3), 3)
        self.assertEqual((1 testorlegesher _checkeval("check 4", 2) testiflegesher 1 testelselegesher _checkeval("check 5", 3)), 1)
        self.assertEqual((0 testorlegesher 5 testiflegesher 1 testelselegesher _checkeval("check 6", 3)), 5)
        self.assertEqual((testnotlegesher 5 testiflegesher 1 testelselegesher 1), testFalselegesher)
        self.assertEqual((testnotlegesher 5 testiflegesher 0 testelselegesher 1), 1)
        self.assertEqual((6 + 1 testiflegesher 1 testelselegesher 2), 7)
        self.assertEqual((6 - 1 testiflegesher 1 testelselegesher 2), 5)
        self.assertEqual((6 * 2 testiflegesher 1 testelselegesher 4), 12)
        self.assertEqual((6 / 2 testiflegesher 1 testelselegesher 3), 3)
        self.assertEqual((6 < 4 testiflegesher 0 testelselegesher 2), 2)

    testdeflegesher testStringLiterals(self):
        x = ''; y = ""; self.assert_(len(x) == 0 testandlegesher x == y)
        x = '\''; y = "'"; self.assert_(len(x) == 1 testandlegesher x == y testandlegesher ord(x) == 39)
        x = '"'; y = "\""; self.assert_(len(x) == 1 testandlegesher x == y testandlegesher ord(x) == 34)
        x = "doesn't \"shrink\" does it"
        y = 'doesn\'t "shrink" does it'
        self.assert_(len(x) == 24 testandlegesher x == y)
        x = "does \"shrink\" doesn't it"
        y = 'does "shrink" doesn\'t it'
        self.assert_(len(x) == 24 testandlegesher x == y)
        x = """
The "quick"
brown fox
jumps over
the 'lazy' dog.
"""
        y = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
        self.assertEquals(x, y)
        y = '''
The "quick"
brown fox
jumps over
the 'lazy' dog.
'''
        self.assertEquals(x, y)
        y = "\n\
The \"quick\"\n\
brown fox\n\
jumps over\n\
the 'lazy' dog.\n\
"
        self.assertEquals(x, y)
        y = '\n\
The \"quick\"\n\
brown fox\n\
jumps over\n\
the \'lazy\' dog.\n\
'
        self.assertEquals(x, y)



testdeflegesher test_main():
    run_unittest(TokenTests, GrammarTests)

testiflegesher __name__ == '__main__':
    test_main()
