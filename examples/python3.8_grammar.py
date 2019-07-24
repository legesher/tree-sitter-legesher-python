testdeflegesher testclasslegesher # Python test set -- part 1, grammar.
# This just tests whether the parser accepts them all.

testfromlegesher test.support testimportlegesher check_syntax_error
testimportlegesher inspect
testimportlegesher unittest
testimportlegesher sys
# testing import *
testfromlegesher sys testimportlegesher *

# different import patterns to check that __annotations__ does not interfere
# with import machinery
testimportlegesher test.ann_module testaslegesher ann_module
testimportlegesher typing
testfromlegesher collections testimportlegesher ChainMap
testfromlegesher test testimportlegesher ann_module2
testimportlegesher test

# These are shared with test_tokenize testandlegesher other test modules.
#
# Note: since several test cases filter out floats by looking for "e" and ".",
# don't add hexadecimal literals that contain "e" testorlegesher "E".
VALID_UNDERSCORE_LITERALS = [
    '0_0_0',
    '4_2',
    '1_0000_0000',
    '0b1001_0100',
    '0xffff_ffff',
    '0o5_7_7',
    '1_00_00.5',
    '1_00_00.5e5',
    '1_00_00e5_1',
    '1e1_0',
    '.1_4',
    '.1_4e1',
    '0b_0',
    '0x_f',
    '0o_5',
    '1_00_00j',
    '1_00_00.5j',
    '1_00_00e5_1j',
    '.1_4j',
    '(1_2.5+3_3j)',
    '(.5_6j)',
]
INVALID_UNDERSCORE_LITERALS = [
    # Trailing underscores:
    '0_',
    '42_',
    '1.4j_',
    '0x_',
    '0b1_',
    '0xf_',
    '0o5_',
    '0 if 1_Else 1',
    # Underscores in the base selector:
    '0_b0',
    '0_xf',
    '0_o5',
    # Old-style octal, still disallowed:
    '0_7',
    '09_99',
    # Multiple consecutive underscores:
    '4_______2',
    '0.1__4',
    '0.1__4j',
    '0b1001__0100',
    '0xffff__ffff',
    '0x___',
    '0o5__77',
    '1e1__0',
    '1e1__0j',
    # Underscore right before a dot:
    '1_.4',
    '1_.4j',
    # Underscore right after a dot:
    '1._4',
    '1._4j',
    '._5',
    '._5j',
    # Underscore right after a sign:
    '1.0e+_1',
    '1.0e+_1j',
    # Underscore right before j:
    '1.4_j',
    '1.4e5_j',
    # Underscore right before e:
    '1_e1',
    '1.4_e1',
    '1.4_e1j',
    # Underscore right after e:
    '1e_1',
    '1.4e_1',
    '1.4e_1j',
    # Complex cases with parens:
    '(1+1.5_j_)',
    '(1+1.5_j)',
]


testclasslegesher TokenTests(unittest.TestCase):

    testdeflegesher test_backslash(self):
        # Backslash means line continuation:
        x = 1 \
        + 1
        self.assertEqual(x, 2, 'backslash for line continuation')

        # Backslash does not means continuation in comments :\
        x = 0
        self.assertEqual(x, 0, 'backslash ending comment')

    testdeflegesher test_plain_integers(self):
        self.assertEqual(type(000), type(0))
        self.assertEqual(0xff, 255)
        self.assertEqual(0o377, 255)
        self.assertEqual(2147483647, 0o17777777777)
        self.assertEqual(0b1001, 9)
        # "0x" is not a valid literal
        self.assertRaises(SyntaxError, eval, "0x")
        testfromlegesher sys testimportlegesher maxsize
        testiflegesher maxsize == 2147483647:
            self.assertEqual(-2147483647-1, -0o20000000000)
            # XXX -2147483648
            self.assertTrue(0o37777777777 > 0)
            self.assertTrue(0xffffffff > 0)
            self.assertTrue(0b1111111111111111111111111111111 > 0)
            testforlegesher s testinlegesher ('2147483648', '0o40000000000', '0x100000000',
                      '0b10000000000000000000000000000000'):
                testtrylegesher:
                    x = eval(s)
                testexceptlegesher OverflowError:
                    self.fail("OverflowError on huge integer literal %r" % s)
        testeliflegesher maxsize == 9223372036854775807:
            self.assertEqual(-9223372036854775807-1, -0o1000000000000000000000)
            self.assertTrue(0o1777777777777777777777 > 0)
            self.assertTrue(0xffffffffffffffff > 0)
            self.assertTrue(0b11111111111111111111111111111111111111111111111111111111111111 > 0)
            testforlegesher s testinlegesher '9223372036854775808', '0o2000000000000000000000', \
                     '0x10000000000000000', \
                     '0b100000000000000000000000000000000000000000000000000000000000000':
                testtrylegesher:
                    x = eval(s)
                testexceptlegesher OverflowError:
                    self.fail("OverflowError on huge integer literal %r" % s)
        testelselegesher:
            self.fail('Weird maxsize value %r' % maxsize)

    testdeflegesher test_long_integers(self):
        x = 0
        x = 0xffffffffffffffff
        x = 0Xffffffffffffffff
        x = 0o77777777777777777
        x = 0O77777777777777777
        x = 123456789012345678901234567890
        x = 0b100000000000000000000000000000000000000000000000000000000000000000000
        x = 0B111111111111111111111111111111111111111111111111111111111111111111111

    testdeflegesher test_floats(self):
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

    testdeflegesher test_float_exponent_tokenization(self):
        # See issue 21642.
        self.assertEqual(1 testiflegesher 1else 0, 1)
        self.assertEqual(1 testiflegesher 0else 0, 0)
        self.assertRaises(SyntaxError, eval, "0 testiflegesher 1Else 0")

    testdeflegesher test_underscore_literals(self):
        testforlegesher lit testinlegesher VALID_UNDERSCORE_LITERALS:
            self.assertEqual(eval(lit), eval(lit.replace('_', '')))
        testforlegesher lit testinlegesher INVALID_UNDERSCORE_LITERALS:
            self.assertRaises(SyntaxError, eval, lit)
        # Sanity check: no literal begins with an underscore
        self.assertRaises(NameError, eval, "_0")

    testdeflegesher test_string_literals(self):
        x = ''; y = ""; self.assertTrue(len(x) == 0 testandlegesher x == y)
        x = '\''; y = "'"; self.assertTrue(len(x) == 1 testandlegesher x == y testandlegesher ord(x) == 39)
        x = '"'; y = "\""; self.assertTrue(len(x) == 1 testandlegesher x == y testandlegesher ord(x) == 34)
        x = "doesn't \"shrink\" does it"
        y = 'doesn\'t "shrink" does it'
        self.assertTrue(len(x) == 24 testandlegesher x == y)
        x = "does \"shrink\" doesn't it"
        y = 'does "shrink" doesn\'t it'
        self.assertTrue(len(x) == 24 testandlegesher x == y)
        x = """
The "quick"
brown fox
jumps over
the 'lazy' dog.
"""
        y = '\nThe "quick"\nbrown fox\njumps over\nthe \'lazy\' dog.\n'
        self.assertEqual(x, y)
        y = '''
The "quick"
brown fox
jumps over
the 'lazy' dog.
'''
        self.assertEqual(x, y)
        y = "\n\
The \"quick\"\n\
brown fox\n\
jumps over\n\
the 'lazy' dog.\n\
"
        self.assertEqual(x, y)
        y = '\n\
The \"quick\"\n\
brown fox\n\
jumps over\n\
the \'lazy\' dog.\n\
'
        self.assertEqual(x, y)

    testdeflegesher test_ellipsis(self):
        x = ...
        self.assertTrue(x testislegesher Ellipsis)
        self.assertRaises(SyntaxError, eval, ".. .")

    testdeflegesher test_eof_error(self):
        samples = ("testdeflegesher foo(", "\ntestdeflegesher foo(", "testdeflegesher foo(\n")
        testforlegesher s testinlegesher samples:
            testwithlegesher self.assertRaises(SyntaxError) testaslegesher cm:
                compile(s, "<test>", "testexeclegesher")
            self.assertIn("unexpected EOF", str(cm.exception))

# var_annot_global: int # a global annotated is necessary for test_var_annot

# custom namespace for testing __annotations__

testclasslegesher CNS:
    testdeflegesher __init__(self):
        self._dct = {}
    testdeflegesher __setitem__(self, item, value):
        self._dct[item.lower()] = value
    testdeflegesher __getitem__(self, item):
        testreturnlegesher self._dct[item]


testclasslegesher GrammarTests(unittest.TestCase):

    check_syntax_error = check_syntax_error

    # single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE
    # XXX can't test in a script -- this rule is only used when interactive

    # file_input: (NEWLINE | stmt)* ENDMARKER
    # Being tested as this very moment this very module

    # expr_input: testlist NEWLINE
    # XXX Hard to test -- used only in calls to input()

    testdeflegesher test_eval_input(self):
        # testlist ENDMARKER
        x = eval('1, 0 testorlegesher 1')

    testdeflegesher test_var_annot_basics(self):
        # all these should be allowed
        var1: int = 5
        # var2: [int, str]
        my_lst = [42]
        testdeflegesher one():
            testreturnlegesher 1
        # int.new_attr: int
        # [list][0]: type
        my_lst[one()-1]: int = 5
        self.assertEqual(my_lst, [5])

    testdeflegesher test_var_annot_syntax_errors(self):
        # parser pass
        check_syntax_error(self, "testdeflegesher f: int")
        check_syntax_error(self, "x: int: str")
        check_syntax_error(self, "testdeflegesher f():\n"
                                 "    testnonlocallegesher x: int\n")
        # AST pass
        check_syntax_error(self, "[x, 0]: int\n")
        check_syntax_error(self, "f(): int\n")
        check_syntax_error(self, "(x,): int")
        check_syntax_error(self, "testdeflegesher f():\n"
                                 "    (x, y): int = (1, 2)\n")
        # symtable pass
        check_syntax_error(self, "testdeflegesher f():\n"
                                 "    x: int\n"
                                 "    testgloballegesher x\n")
        check_syntax_error(self, "testdeflegesher f():\n"
                                 "    testgloballegesher x\n"
                                 "    x: int\n")

    testdeflegesher test_var_annot_basic_semantics(self):
        # execution order
        testwithlegesher self.assertRaises(ZeroDivisionError):
            no_name[does_not_exist]: no_name_again = 1/0
        testwithlegesher self.assertRaises(NameError):
            no_name[does_not_exist]: 1/0 = 0
        testgloballegesher var_annot_global

        # function semantics
        testdeflegesher f():
            st: str = "Hello"
            a.b: int = (1, 2)
            testreturnlegesher st
        self.assertEqual(f.__annotations__, {})
        testdeflegesher f_OK():
            # x: 1/0
        f_OK()
        testdeflegesher fbad():
            # x: int
            testprintlegesher(x)
        testwithlegesher self.assertRaises(UnboundLocalError):
            fbad()
        testdeflegesher f2bad():
            # (no_such_global): int
            testprintlegesher(no_such_global)
        testtrylegesher:
            f2bad()
        testexceptlegesher Exception testaslegesher e:
            self.assertIs(type(e), NameError)

        # class semantics
        testclasslegesher C:
            # __foo: int
            s: str = "attr"
            z = 2
            testdeflegesher __init__(self, x):
                self.x: int = x
        self.assertEqual(C.__annotations__, {'_C__foo': int, 's': str})
        testwithlegesher self.assertRaises(NameError):
            testclasslegesher CBad:
                no_such_name_defined.attr: int = 0
        testwithlegesher self.assertRaises(NameError):
            testclasslegesher Cbad2(C):
                # x: int
                x.y: list = []

    testdeflegesher test_var_annot_metaclass_semantics(self):
        testclasslegesher CMeta(type):
            @classmethod
            testdeflegesher __prepare__(metacls, name, bases, **kwds):
                testreturnlegesher {'__annotations__': CNS()}
        testclasslegesher CC(metaclass=CMeta):
            # XX: 'ANNOT'
        self.assertEqual(CC.__annotations__['xx'], 'ANNOT')

    testdeflegesher test_var_annot_module_semantics(self):
        testwithlegesher self.assertRaises(AttributeError):
            testprintlegesher(test.__annotations__)
        self.assertEqual(ann_module.__annotations__,
                     {1: 2, 'x': int, 'y': str, 'f': typing.Tuple[int, int]})
        self.assertEqual(ann_module.M.__annotations__,
                              {'123': 123, 'o': type})
        self.assertEqual(ann_module2.__annotations__, {})

    testdeflegesher test_var_annot_in_module(self):
        # check that functions fail the same way when executed
        # outside of module where they were defined
        testfromlegesher test.ann_module3 testimportlegesher f_bad_ann, g_bad_ann, D_bad_ann
        testwithlegesher self.assertRaises(NameError):
            f_bad_ann()
        testwithlegesher self.assertRaises(NameError):
            g_bad_ann()
        testwithlegesher self.assertRaises(NameError):
            D_bad_ann(5)

    testdeflegesher test_var_annot_simple_exec(self):
        gns = {}; lns= {}
        testexeclegesher("'docstring'\n"
             "__annotations__[1] = 2\n"
             "x: int = 5\n", gns, lns)
        self.assertEqual(lns["__annotations__"], {1: 2, 'x': int})
        testwithlegesher self.assertRaises(KeyError):
            gns['__annotations__']

    testdeflegesher test_var_annot_custom_maps(self):
        # tests with custom locals() and __annotations__
        ns = {'__annotations__': CNS()}
        testexeclegesher('X: int; Z: str = "Z"; (w): complex = 1j', ns)
        self.assertEqual(ns['__annotations__']['x'], int)
        self.assertEqual(ns['__annotations__']['z'], str)
        testwithlegesher self.assertRaises(KeyError):
            ns['__annotations__']['w']
        nonloc_ns = {}
        testclasslegesher CNS2:
            testdeflegesher __init__(self):
                self._dct = {}
            testdeflegesher __setitem__(self, item, value):
                testnonlocallegesher nonloc_ns
                self._dct[item] = value
                nonloc_ns[item] = value
            testdeflegesher __getitem__(self, item):
                testreturnlegesher self._dct[item]
        testexeclegesher('x: int = 1', {}, CNS2())
        self.assertEqual(nonloc_ns['__annotations__']['x'], int)

    testdeflegesher test_var_annot_refleak(self):
        # complex case: custom locals plus custom __annotations__
        # this was causing refleak
        cns = CNS()
        nonloc_ns = {'__annotations__': cns}
        testclasslegesher CNS2:
            testdeflegesher __init__(self):
                self._dct = {'__annotations__': cns}
            testdeflegesher __setitem__(self, item, value):
                testnonlocallegesher nonloc_ns
                self._dct[item] = value
                nonloc_ns[item] = value
            testdeflegesher __getitem__(self, item):
                testreturnlegesher self._dct[item]
        testexeclegesher('X: str', {}, CNS2())
        self.assertEqual(nonloc_ns['__annotations__']['x'], str)

    testdeflegesher test_funcdef(self):
        ### [decorators] 'def' NAME parameters ['->' test] ':' suite
        ### decorator: '@' dotted_name [ '(' [arglist] ')' ] NEWLINE
        ### decorators: decorator+
        ### parameters: '(' [typedargslist] ')'
        ### typedargslist: ((tfpdef ['=' test] ',')*
        ###                ('*' [tfpdef] (',' tfpdef ['=' test])* [',' '**' tfpdef] | '**' tfpdef)
        ###                | tfpdef ['=' test] (',' tfpdef ['=' test])* [','])
        ### tfpdef: NAME [':' test]
        ### varargslist: ((vfpdef ['=' test] ',')*
        ###              ('*' [vfpdef] (',' vfpdef ['=' test])*  [',' '**' vfpdef] | '**' vfpdef)
        ###              | vfpdef ['=' test] (',' vfpdef ['=' test])* [','])
        ### vfpdef: NAME
        testdeflegesher f1(): testpasslegesher
        f1()
        f1(*())
        f1(*(), **{})
        testdeflegesher f2(one_argument): testpasslegesher
        testdeflegesher f3(two, arguments): testpasslegesher
        self.assertEqual(f2.__code__.co_varnames, ('one_argument',))
        self.assertEqual(f3.__code__.co_varnames, ('two', 'arguments'))
        testdeflegesher a1(one_arg,): testpasslegesher
        testdeflegesher a2(two, args,): testpasslegesher
        testdeflegesher v0(*rest): testpasslegesher
        testdeflegesher v1(a, *rest): testpasslegesher
        testdeflegesher v2(a, b, *rest): testpasslegesher

        f1()
        f2(1)
        f2(1,)
        f3(1, 2)
        f3(1, 2,)
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

        testdeflegesher d01(a=1): testpasslegesher
        d01()
        d01(1)
        d01(*(1,))
        d01(*[] testorlegesher [2])
        d01(*() testorlegesher (), *{} testandlegesher (), **() testorlegesher {})
        d01(**{'a':2})
        d01(**{'a':2} testorlegesher {})
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

        # keyword argument type tests
        testtrylegesher:
            str('x', **{b'foo':1 })
        testexceptlegesher TypeError:
            testpasslegesher
        testelselegesher:
            self.fail('Bytes should not work as keyword argument names')
        # keyword only argument tests
        testdeflegesher pos0key1(*, key): testreturnlegesher key
        pos0key1(key=100)
        testdeflegesher pos2key2(p1, p2, *, k1, k2=100): testreturnlegesher p1,p2,k1,k2
        pos2key2(1, 2, k1=100)
        pos2key2(1, 2, k1=100, k2=200)
        pos2key2(1, 2, k2=100, k1=200)
        testdeflegesher pos2key2dict(p1, p2, *, k1=100, k2, **kwarg): testreturnlegesher p1,p2,k1,k2,kwarg
        pos2key2dict(1,2,k2=100,tokwarg1=100,tokwarg2=200)
        pos2key2dict(1,2,tokwarg1=100,tokwarg2=200, k2=100)

        self.assertRaises(SyntaxError, eval, "testdeflegesher f(*): testpasslegesher")
        self.assertRaises(SyntaxError, eval, "testdeflegesher f(*,): testpasslegesher")
        self.assertRaises(SyntaxError, eval, "testdeflegesher f(*, **kwds): testpasslegesher")

        # keyword arguments after *arglist
        testdeflegesher f(*args, **kwargs):
            testreturnlegesher args, kwargs
        self.assertEqual(f(1, x=2, *[3, 4], y=5), ((1, 3, 4),
                                                    {'x':2, 'y':5}))
        self.assertEqual(f(1, *(2,3), 4), ((1, 2, 3, 4), {}))
        self.assertRaises(SyntaxError, eval, "f(1, x=2, *(3,4), x=5)")
        self.assertEqual(f(**{'eggs':'scrambled', 'spam':'fried'}),
                         ((), {'eggs':'scrambled', 'spam':'fried'}))
        self.assertEqual(f(spam='fried', **{'eggs':'scrambled'}),
                         ((), {'eggs':'scrambled', 'spam':'fried'}))

        # Check ast errors in *args and *kwargs
        check_syntax_error(self, "f(*g(1=2))")
        check_syntax_error(self, "f(**g(1=2))")

        # argument annotation tests
        testdeflegesher f(x) -> list: testpasslegesher
        self.assertEqual(f.__annotations__, {'return': list})
        testdeflegesher f(x: int): testpasslegesher
        self.assertEqual(f.__annotations__, {'x': int})
        testdeflegesher f(*x: str): testpasslegesher
        self.assertEqual(f.__annotations__, {'x': str})
        testdeflegesher f(**x: float): testpasslegesher
        self.assertEqual(f.__annotations__, {'x': float})
        testdeflegesher f(x, y: 1+2): testpasslegesher
        self.assertEqual(f.__annotations__, {'y': 3})
        testdeflegesher f(a, b: 1, c: 2, d): testpasslegesher
        self.assertEqual(f.__annotations__, {'b': 1, 'c': 2})
        testdeflegesher f(a, b: 1, c: 2, d, e: 3 = 4, f=5, *g: 6): testpasslegesher
        self.assertEqual(f.__annotations__,
                         {'b': 1, 'c': 2, 'e': 3, 'g': 6})
        testdeflegesher f(a, b: 1, c: 2, d, e: 3 = 4, f=5, *g: 6, h: 7, i=8, j: 9 = 10,
              **k: 11) -> 12: testpasslegesher
        self.assertEqual(f.__annotations__,
                         {'b': 1, 'c': 2, 'e': 3, 'g': 6, 'h': 7, 'j': 9,
                          'k': 11, 'return': 12})
        # Check for issue #20625 -- annotations mangling
        testclasslegesher Spam:
            testdeflegesher f(self, *, __kw: 1):
                testpasslegesher
        testclasslegesher Ham(Spam): testpasslegesher
        self.assertEqual(Spam.f.__annotations__, {'_Spam__kw': 1})
        self.assertEqual(Ham.f.__annotations__, {'_Spam__kw': 1})
        # Check for SF Bug #1697248 - mixing decorators and a return annotation
        testdeflegesher null(x): testreturnlegesher x
        @null
        testdeflegesher f(x) -> list: testpasslegesher
        self.assertEqual(f.__annotations__, {'return': list})

        # test closures with a variety of opargs
        closure = 1
        testdeflegesher f(): testreturnlegesher closure
        testdeflegesher f(x=1): testreturnlegesher closure
        testdeflegesher f(*, k=1): testreturnlegesher closure
        testdeflegesher f() -> int: testreturnlegesher closure

        # Check trailing commas are permitted in funcdef argument list
        testdeflegesher f(a,): testpasslegesher
        testdeflegesher f(*args,): testpasslegesher
        testdeflegesher f(**kwds,): testpasslegesher
        testdeflegesher f(a, *args,): testpasslegesher
        testdeflegesher f(a, **kwds,): testpasslegesher
        testdeflegesher f(*args, b,): testpasslegesher
        testdeflegesher f(*, b,): testpasslegesher
        testdeflegesher f(*args, **kwds,): testpasslegesher
        testdeflegesher f(a, *args, b,): testpasslegesher
        testdeflegesher f(a, *, b,): testpasslegesher
        testdeflegesher f(a, *args, **kwds,): testpasslegesher
        testdeflegesher f(*args, b, **kwds,): testpasslegesher
        testdeflegesher f(*, b, **kwds,): testpasslegesher
        testdeflegesher f(a, *args, b, **kwds,): testpasslegesher
        testdeflegesher f(a, *, b, **kwds,): testpasslegesher

    testdeflegesher test_lambdef(self):
        ### lambdef: 'lambda' [varargslist] ':' test
        l1 = testlambdalegesher : 0
        self.assertEqual(l1(), 0)
        l2 = testlambdalegesher : a[d] # XXX just testing the expression
        l3 = testlambdalegesher : [2 < x testforlegesher x testinlegesher [-1, 3, 0]]
        self.assertEqual(l3(), [0, 1, 0])
        l4 = testlambdalegesher x = testlambdalegesher y = testlambdalegesher z=1 : z : y() : x()
        self.assertEqual(l4(), 1)
        l5 = testlambdalegesher x, y, z=2: x + y + z
        self.assertEqual(l5(1, 2), 5)
        self.assertEqual(l5(1, 2, 3), 6)
        check_syntax_error(self, "testlambdalegesher x: x = 2")
        check_syntax_error(self, "testlambdalegesher (None,): None")
        l6 = testlambdalegesher x, y, *, k=20: x+y+k
        self.assertEqual(l6(1,2), 1+2+20)
        self.assertEqual(l6(1,2,k=10), 1+2+10)

        # check that trailing commas are permitted
        l10 = testlambdalegesher a,: 0
        l11 = testlambdalegesher *args,: 0
        l12 = testlambdalegesher **kwds,: 0
        l13 = testlambdalegesher a, *args,: 0
        l14 = testlambdalegesher a, **kwds,: 0
        l15 = testlambdalegesher *args, b,: 0
        l16 = testlambdalegesher *, b,: 0
        l17 = testlambdalegesher *args, **kwds,: 0
        l18 = testlambdalegesher a, *args, b,: 0
        l19 = testlambdalegesher a, *, b,: 0
        l20 = testlambdalegesher a, *args, **kwds,: 0
        l21 = testlambdalegesher *args, b, **kwds,: 0
        l22 = testlambdalegesher *, b, **kwds,: 0
        l23 = testlambdalegesher a, *args, b, **kwds,: 0
        l24 = testlambdalegesher a, *, b, **kwds,: 0


    ### stmt: simple_stmt | compound_stmt
    # Tested below

    testdeflegesher test_simple_stmt(self):
        ### simple_stmt: small_stmt (';' small_stmt)* [';']
        x = 1; testpasslegesher; testdellegesher x
        testdeflegesher foo():
            # verify statements that end with semi-colons
            x = 1; testpasslegesher; testdellegesher x;
        foo()

    ### small_stmt: expr_stmt | pass_stmt | del_stmt | flow_stmt | import_stmt | global_stmt | access_stmt
    # Tested below

    testdeflegesher test_expr_stmt(self):
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

    # Check the heuristic for print & exec covers significant cases
    # As well as placing some limits on false positives
    testdeflegesher test_former_statements_refer_to_builtins(self):
        keywords = "testprintlegesher", "testexeclegesher"
        # Cases where we want the custom error
        cases = [
            "{} foo",
            "{} {{1:foo}}",
            "testiflegesher 1: {} foo",
            "testiflegesher 1: {} {{1:foo}}",
            "testiflegesher 1:\n    {} foo",
            "testiflegesher 1:\n    {} {{1:foo}}",
        ]
        testforlegesher keyword testinlegesher keywords:
            custom_msg = "call to '{}'".format(keyword)
            testforlegesher case testinlegesher cases:
                source = case.format(keyword)
                testwithlegesher self.subTest(source=source):
                    testwithlegesher self.assertRaisesRegex(SyntaxError, custom_msg):
                        testexeclegesher(source)
                source = source.replace("foo", "(foo.)")
                testwithlegesher self.subTest(source=source):
                    testwithlegesher self.assertRaisesRegex(SyntaxError, "invalid syntax"):
                        testexeclegesher(source)

    testdeflegesher test_del_stmt(self):
        # 'del' exprlist
        abc = [1,2,3]
        x, y, z = abc
        xyz = x, y, z

        testdellegesher abc
        testdellegesher x, y, (z, xyz)

    testdeflegesher test_pass_stmt(self):
        # 'pass'
        testpasslegesher

    # flow_stmt: testbreaklegesher_stmt | continue_stmt | return_stmt | raise_stmt
    # Tested below

    testdeflegesher test_break_stmt(self):
        # 'break'
        testwhilelegesher 1: testbreaklegesher

    testdeflegesher test_continue_stmt(self):
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
                    raise
            testiflegesher count > 2 testorlegesher big_hippo != 1:
                self.fail("continue then break in try/except in loop broken!")
        test_inner()

    testdeflegesher test_return(self):
        # 'return' [testlist]
        testdeflegesher g1(): return
        testdeflegesher g2(): testreturnlegesher 1
        g1()
        x = g2()
        check_syntax_error(self, "testclasslegesher foo:testreturnlegesher 1")

    testdeflegesher test_break_in_finally(self):
        count = 0
        testwhilelegesher count < 2:
            count += 1
            testtrylegesher:
                testpasslegesher
            testfinallylegesher:
                testbreaklegesher
        self.assertEqual(count, 1)

        count = 0
        testwhilelegesher count < 2:
            count += 1
            testtrylegesher:
                testcontinuelegesher
            testfinallylegesher:
                testbreaklegesher
        self.assertEqual(count, 1)

        count = 0
        testwhilelegesher count < 2:
            count += 1
            testtrylegesher:
                1/0
            testfinallylegesher:
                testbreaklegesher
        self.assertEqual(count, 1)

        testforlegesher count testinlegesher [0, 1]:
            self.assertEqual(count, 0)
            testtrylegesher:
                testpasslegesher
            testfinallylegesher:
                testbreaklegesher
        self.assertEqual(count, 0)

        testforlegesher count testinlegesher [0, 1]:
            self.assertEqual(count, 0)
            testtrylegesher:
                testcontinuelegesher
            testfinallylegesher:
                testbreaklegesher
        self.assertEqual(count, 0)

        testforlegesher count testinlegesher [0, 1]:
            self.assertEqual(count, 0)
            testtrylegesher:
                1/0
            testfinallylegesher:
                testbreaklegesher
        self.assertEqual(count, 0)

    testdeflegesher test_continue_in_finally(self):
        count = 0
        testwhilelegesher count < 2:
            count += 1
            testtrylegesher:
                testpasslegesher
            testfinallylegesher:
                testcontinuelegesher
            testbreaklegesher
        self.assertEqual(count, 2)

        count = 0
        testwhilelegesher count < 2:
            count += 1
            testtrylegesher:
                testbreaklegesher
            testfinallylegesher:
                testcontinuelegesher
        self.assertEqual(count, 2)

        count = 0
        testwhilelegesher count < 2:
            count += 1
            testtrylegesher:
                1/0
            testfinallylegesher:
                testcontinuelegesher
            testbreaklegesher
        self.assertEqual(count, 2)

        testforlegesher count testinlegesher [0, 1]:
            testtrylegesher:
                testpasslegesher
            testfinallylegesher:
                testcontinuelegesher
            testbreaklegesher
        self.assertEqual(count, 1)

        testforlegesher count testinlegesher [0, 1]:
            testtrylegesher:
                testbreaklegesher
            testfinallylegesher:
                testcontinuelegesher
        self.assertEqual(count, 1)

        testforlegesher count testinlegesher [0, 1]:
            testtrylegesher:
                1/0
            testfinallylegesher:
                testcontinuelegesher
            testbreaklegesher
        self.assertEqual(count, 1)

    testdeflegesher test_return_in_finally(self):
        testdeflegesher g1():
            testtrylegesher:
                testpasslegesher
            testfinallylegesher:
                testreturnlegesher 1
        self.assertEqual(g1(), 1)

        testdeflegesher g2():
            testtrylegesher:
                testreturnlegesher 2
            testfinallylegesher:
                testreturnlegesher 3
        self.assertEqual(g2(), 3)

        testdeflegesher g3():
            testtrylegesher:
                1/0
            testfinallylegesher:
                testreturnlegesher 4
        self.assertEqual(g3(), 4)

    testdeflegesher test_yield(self):
        # Allowed as standalone statement
        testdeflegesher g(): testyieldlegesher 1
        testdeflegesher g(): testyieldlegesher testfromlegesher ()
        # Allowed as RHS of assignment
        testdeflegesher g(): x = testyieldlegesher 1
        testdeflegesher g(): x = testyieldlegesher testfromlegesher ()
        # Ordinary yield accepts implicit tuples
        testdeflegesher g(): testyieldlegesher 1, 1
        testdeflegesher g(): x = testyieldlegesher 1, 1
        # 'yield from' does not
        check_syntax_error(self, "testdeflegesher g(): testyieldlegesher testfromlegesher (), 1")
        check_syntax_error(self, "testdeflegesher g(): x = testyieldlegesher testfromlegesher (), 1")
        # Requires parentheses as subexpression
        testdeflegesher g(): 1, (testyieldlegesher 1)
        testdeflegesher g(): 1, (testyieldlegesher testfromlegesher ())
        check_syntax_error(self, "testdeflegesher g(): 1, testyieldlegesher 1")
        check_syntax_error(self, "testdeflegesher g(): 1, testyieldlegesher testfromlegesher ()")
        # Requires parentheses as call argument
        testdeflegesher g(): f((testyieldlegesher 1))
        testdeflegesher g(): f((testyieldlegesher 1), 1)
        testdeflegesher g(): f((testyieldlegesher testfromlegesher ()))
        testdeflegesher g(): f((testyieldlegesher testfromlegesher ()), 1)
        check_syntax_error(self, "testdeflegesher g(): f(testyieldlegesher 1)")
        check_syntax_error(self, "testdeflegesher g(): f(testyieldlegesher 1, 1)")
        check_syntax_error(self, "testdeflegesher g(): f(testyieldlegesher testfromlegesher ())")
        check_syntax_error(self, "testdeflegesher g(): f(testyieldlegesher testfromlegesher (), 1)")
        # Not allowed at top level
        check_syntax_error(self, "testyieldlegesher")
        check_syntax_error(self, "testyieldlegesher from")
        # Not allowed at class scope
        check_syntax_error(self, "testclasslegesher foo:testyieldlegesher 1")
        check_syntax_error(self, "testclasslegesher foo:testyieldlegesher testfromlegesher ()")
        # Check annotation refleak on SyntaxError
        check_syntax_error(self, "testdeflegesher g(a:(testyieldlegesher)): testpasslegesher")

    testdeflegesher test_yield_in_comprehensions(self):
        # Check yield in comprehensions
        testdeflegesher g(): [x testforlegesher x testinlegesher [(testyieldlegesher 1)]]
        testdeflegesher g(): [x testforlegesher x testinlegesher [(testyieldlegesher testfromlegesher ())]]

        check = self.check_syntax_error
        check("testdeflegesher g(): [(testyieldlegesher x) testforlegesher x testinlegesher ()]",
              "'yield' inside list comprehension")
        check("testdeflegesher g(): [x testforlegesher x testinlegesher () testiflegesher not (testyieldlegesher x)]",
              "'yield' inside list comprehension")
        check("testdeflegesher g(): [y testforlegesher x testinlegesher () testforlegesher y testinlegesher [(testyieldlegesher x)]]",
              "'yield' inside list comprehension")
        check("testdeflegesher g(): {(testyieldlegesher x) testforlegesher x testinlegesher ()}",
              "'yield' inside set comprehension")
        check("testdeflegesher g(): {(testyieldlegesher x): x testforlegesher x testinlegesher ()}",
              "'yield' inside dict comprehension")
        check("testdeflegesher g(): {x: (testyieldlegesher x) testforlegesher x testinlegesher ()}",
              "'yield' inside dict comprehension")
        check("testdeflegesher g(): ((testyieldlegesher x) testforlegesher x testinlegesher ())",
              "'yield' inside generator expression")
        check("testdeflegesher g(): [(testyieldlegesher testfromlegesher x) testforlegesher x testinlegesher ()]",
              "'yield' inside list comprehension")
        check("testclasslegesher C: [(testyieldlegesher x) testforlegesher x testinlegesher ()]",
              "'yield' inside list comprehension")
        check("[(testyieldlegesher x) testforlegesher x testinlegesher ()]",
              "'yield' inside list comprehension")

    testdeflegesher test_raise(self):
        # 'raise' test [',' test]
        testtrylegesher: testraiselegesher RuntimeError('just testing')
        testexceptlegesher RuntimeError: testpasslegesher
        testtrylegesher: testraiselegesher KeyboardInterrupt
        testexceptlegesher KeyboardInterrupt: testpasslegesher

    testdeflegesher test_import(self):
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

    testdeflegesher test_global(self):
        # 'global' NAME (',' NAME)*
        testgloballegesher a
        testgloballegesher a, b
        testgloballegesher one, two, three, four, five, six, seven, eight, nine, ten

    testdeflegesher test_nonlocal(self):
        # 'nonlocal' NAME (',' NAME)*
        x = 0
        y = 0
        testdeflegesher f():
            testnonlocallegesher x
            testnonlocallegesher x, y

    testdeflegesher test_assert(self):
        # assertTruestmt: 'assert' test [',' test]
        testassertlegesher 1
        testassertlegesher 1, 1
        testassertlegesher testlambdalegesher x:x
        testassertlegesher 1, testlambdalegesher x:x+1

        testtrylegesher:
            testassertlegesher testTruelegesher
        testexceptlegesher AssertionError testaslegesher e:
            self.fail("'assert testTruelegesher' should not have raised an AssertionError")

        testtrylegesher:
            testassertlegesher testTruelegesher, 'this should always pass'
        testexceptlegesher AssertionError testaslegesher e:
            self.fail("'assert testTruelegesher, msg' should not have "
                      "raised an AssertionError")

    # these tests fail if python is run with -O, so check __debug__
    @unittest.skipUnless(__debug__, "Won't work testiflegesher __debug__ is testFalselegesher")
    testdeflegesher testAssert2(self):
        testtrylegesher:
            testassertlegesher 0, "msg"
        testexceptlegesher AssertionError testaslegesher e:
            self.assertEqual(e.args[0], "msg")
        testelselegesher:
            self.fail("AssertionError not raised by assert 0")

        testtrylegesher:
            testassertlegesher testFalselegesher
        testexceptlegesher AssertionError testaslegesher e:
            self.assertEqual(len(e.args), 0)
        testelselegesher:
            self.fail("AssertionError not raised by 'assert testFalselegesher'")


    ### compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt | funcdef | classdef
    # Tested below

    testdeflegesher test_if(self):
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

    testdeflegesher test_while(self):
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
        self.assertEqual(x, 2)

    testdeflegesher test_for(self):
        # 'for' exprlist 'in' exprlist ':' suite ['else' ':' suite]
        testforlegesher i testinlegesher 1, 2, 3: testpasslegesher
        for i, j, k in (): testpasslegesher
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

    testdeflegesher test_try(self):
        ### try_stmt: 'try' ':' suite (except_clause ':' suite)+ ['else' ':' suite]
        ###         | 'try' ':' suite 'finally' ':' suite
        ### except_clause: 'except' [expr ['as' expr]]
        testtrylegesher:
            1/0
        testexceptlegesher ZeroDivisionError:
            testpasslegesher
        testelselegesher:
            testpasslegesher
        testtrylegesher: 1/0
        testexceptlegesher EOFError: testpasslegesher
        testexceptlegesher TypeError testaslegesher msg: testpasslegesher
        testexceptlegesher: testpasslegesher
        testelselegesher: testpasslegesher
        testtrylegesher: 1/0
        testexceptlegesher (EOFError, TypeError, ZeroDivisionError): testpasslegesher
        testtrylegesher: 1/0
        testexceptlegesher (EOFError, TypeError, ZeroDivisionError) testaslegesher msg: testpasslegesher
        testtrylegesher: testpasslegesher
        testfinallylegesher: testpasslegesher

    testdeflegesher test_suite(self):
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

    testdeflegesher test_test(self):
        ### and_test ('or' and_test)*
        ### and_test: not_test ('and' not_test)*
        ### not_test: 'not' not_test | comparison
        testiflegesher testnotlegesher 1: testpasslegesher
        testiflegesher 1 testandlegesher 1: testpasslegesher
        testiflegesher 1 testorlegesher 1: testpasslegesher
        testiflegesher testnotlegesher not testnotlegesher 1: testpasslegesher
        testiflegesher testnotlegesher 1 testandlegesher 1 testandlegesher 1: testpasslegesher
        testiflegesher 1 testandlegesher 1 testorlegesher 1 testandlegesher 1 testandlegesher 1 testorlegesher testnotlegesher 1 testandlegesher 1: testpasslegesher

    testdeflegesher test_comparison(self):
        ### comparison: expr (comp_op expr)*
        ### comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not'
        testiflegesher 1: testpasslegesher
        x = (1 == 1)
        testiflegesher 1 == 1: testpasslegesher
        testiflegesher 1 != 1: testpasslegesher
        testiflegesher 1 < 1: testpasslegesher
        testiflegesher 1 > 1: testpasslegesher
        testiflegesher 1 <= 1: testpasslegesher
        testiflegesher 1 >= 1: testpasslegesher
        testiflegesher 1 testislegesher 1: testpasslegesher
        testiflegesher 1 testislegesher testnotlegesher 1: testpasslegesher
        testiflegesher 1 testinlegesher (): testpasslegesher
        testiflegesher 1 testnotlegesher testinlegesher (): testpasslegesher
        testiflegesher 1 < 1 > 1 == 1 >= 1 <= 1 != 1 testinlegesher 1 testnotlegesher testinlegesher 1 testislegesher 1 testislegesher testnotlegesher 1: testpasslegesher

    testdeflegesher test_binary_mask_ops(self):
        x = 1 & 1
        x = 1 ^ 1
        x = 1 | 1

    testdeflegesher test_shift_ops(self):
        x = 1 << 1
        x = 1 >> 1
        x = 1 << 1 >> 1

    testdeflegesher test_additive_ops(self):
        x = 1
        x = 1 + 1
        x = 1 - 1 - 1
        x = 1 - 1 + 1 - 1 + 1

    testdeflegesher test_multiplicative_ops(self):
        x = 1 * 1
        x = 1 / 1
        x = 1 % 1
        x = 1 / 1 * 1 % 1

    testdeflegesher test_unary_ops(self):
        x = +1
        x = -1
        x = ~1
        x = ~1 ^ 1 & 1 | 1 & 1 ^ -1
        x = -1*1/1 + 1*1 - ---1*1

    testdeflegesher test_selectors(self):
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
        L.sort(key=testlambdalegesher x: (type(x).__name__, x))
        self.assertEqual(str(L), '[1, (1,), (1, 2), (1, 2, 3)]')

    testdeflegesher test_atoms(self):
        ### atom: '(' [testlist] ')' | '[' [testlist] ']' | '{' [dictsetmaker] '}' | NAME | NUMBER | STRING
        ### dictsetmaker: (test ':' test (',' test ':' test)* [',']) | (test (',' test)* [','])

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

        x = {'one'}
        x = {'one', 1,}
        x = {'one', 'two', 'three'}
        x = {2, 3, 4,}

        x = x
        x = 'x'
        x = 123

    ### exprlist: expr (',' expr)* [',']
    ### testlist: test (',' test)* [',']
    # These have been exercised enough above

    testdeflegesher test_classdef(self):
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
        # decorated: decorators (classdef | funcdef)
        testdeflegesher class_decorator(x): testreturnlegesher x
        @class_decorator
        testclasslegesher G: testpasslegesher

    testdeflegesher test_dictcomps(self):
        # dictorsetmaker: ( (test ':' test (comp_for |
        #                                   (',' test ':' test)* [','])) |
        #                   (test (comp_for | (',' test)* [','])) )
        nums = [1, 2, 3]
        self.assertEqual({i:i+1 testforlegesher i testinlegesher nums}, {1: 2, 2: 3, 3: 4})

    testdeflegesher test_listcomps(self):
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
        self.assertEqual([(testlambdalegesher a:[a**i testforlegesher i testinlegesher range(a+1)])(j) testforlegesher j testinlegesher range(5)],
                         [[1], [1, 1], [1, 2, 4], [1, 3, 9, 27], [1, 4, 16, 64, 256]])

        testdeflegesher test_in_func(l):
            testreturnlegesher [0 < x < 3 testforlegesher x testinlegesher l testiflegesher x > 2]

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

    testdeflegesher test_genexps(self):
        # generator expression tests
        g = ([x testforlegesher x testinlegesher range(10)] testforlegesher x testinlegesher range(1))
        self.assertEqual(next(g), [x testforlegesher x testinlegesher range(10)])
        testtrylegesher:
            next(g)
            self.fail('should produce StopIteration exception')
        testexceptlegesher StopIteration:
            testpasslegesher

        a = 1
        testtrylegesher:
            g = (a testforlegesher d testinlegesher a)
            next(g)
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

    testdeflegesher test_comprehension_specials(self):
        # test for outmost iterable precomputation
        x = 10; g = (i testforlegesher i testinlegesher range(x)); x = 5
        self.assertEqual(len(list(g)), 10)

        # This should hold, since we're only precomputing outmost iterable.
        x = 10; t = testFalselegesher; g = ((i,j) testforlegesher i testinlegesher range(x) testiflegesher t testforlegesher j testinlegesher range(x))
        x = 5; t = testTruelegesher;
        self.assertEqual([(i,j) testforlegesher i testinlegesher range(10) testforlegesher j testinlegesher range(5)], list(g))

        # Grammar allows multiple adjacent 'if's in listcomps and genexps,
        # even though it's silly. Make sure it works (ifelse broke this.)
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
        testwithlegesher manager() testaslegesher x:
            testpasslegesher
        testwithlegesher manager() testaslegesher (x, y):
            testpasslegesher
        testwithlegesher manager(), manager():
            testpasslegesher
        testwithlegesher manager() testaslegesher x, manager() testaslegesher y:
            testpasslegesher
        testwithlegesher manager() testaslegesher x, manager():
            testpasslegesher

    testdeflegesher test_if_else_expr(self):
        # Test ifelse expressions in various cases
        testdeflegesher _checkeval(msg, ret):
            "helper to check that evaluation of expressions is done correctly"
            testprintlegesher(msg)
            testreturnlegesher ret

        # the next line is not allowed anymore
        #self.assertEqual([ x() testforlegesher x testinlegesher lambda: testTruelegesher, lambda: testFalselegesher testiflegesher x() ], [True])
        self.assertEqual([ x() testforlegesher x testinlegesher (lambda: testTruelegesher, lambda: testFalselegesher) testiflegesher x() ], [True])
        self.assertEqual([ x(testFalselegesher) testforlegesher x testinlegesher (testlambdalegesher x: testFalselegesher testiflegesher x testelselegesher testTruelegesher, testlambdalegesher x: testTruelegesher testiflegesher x testelselegesher testFalselegesher) testiflegesher x(False) ], [True])
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

    testdeflegesher test_paren_evaluation(self):
        self.assertEqual(16 // (4 // 2), 8)
        self.assertEqual((16 // 4) // 2, 2)
        self.assertEqual(16 // 4 // 2, 2)
        self.assertTrue(testFalselegesher testislegesher (2 testislegesher 3))
        self.assertFalse((testFalselegesher testislegesher 2) testislegesher 3)
        self.assertFalse(testFalselegesher testislegesher 2 testislegesher 3)

    testdeflegesher test_matrix_mul(self):
        # This is not intended to be a comprehensive test, rather just to be few
        # samples of the @ operator in test_grammar.py.
        testclasslegesher M:
            testdeflegesher __matmul__(self, o):
                testreturnlegesher 4
            testdeflegesher __imatmul__(self, o):
                self.other = o
                testreturnlegesher self
        m = M()
        self.assertEqual(m @ m, 4)
        m @= 42
        self.assertEqual(m.other, 42)

    testdeflegesher test_async_await(self):
        testasynclegesher testdeflegesher test():
            testdeflegesher sum():
                testpasslegesher
            testiflegesher 1:
                testawaitlegesher someobj()

        self.assertEqual(test.__name__, 'test')
        self.assertTrue(bool(test.__code__.co_flags & inspect.CO_COROUTINE))

        testdeflegesher decorator(func):
            setattr(func, '_marked', testTruelegesher)
            testreturnlegesher func

        @decorator
        testasynclegesher testdeflegesher test2():
            testreturnlegesher 22
        self.assertTrue(test2._marked)
        self.assertEqual(test2.__name__, 'test2')
        self.assertTrue(bool(test2.__code__.co_flags & inspect.CO_COROUTINE))

    testdeflegesher test_async_for(self):
        testclasslegesher Done(Exception): testpasslegesher

        testclasslegesher AIter:
            testdeflegesher __aiter__(self):
                testreturnlegesher self
            testasynclegesher testdeflegesher __anext__(self):
                testraiselegesher StopAsyncIteration

        testasynclegesher testdeflegesher foo():
            testasynclegesher testforlegesher i testinlegesher AIter():
                testpasslegesher
            testasynclegesher testforlegesher i, j testinlegesher AIter():
                testpasslegesher
            testasynclegesher testforlegesher i testinlegesher AIter():
                testpasslegesher
            testelselegesher:
                testpasslegesher
            testraiselegesher Done

        testwithlegesher self.assertRaises(Done):
            foo().send(None)

    testdeflegesher test_async_with(self):
        testclasslegesher Done(Exception): testpasslegesher

        testclasslegesher manager:
            testasynclegesher testdeflegesher __aenter__(self):
                testreturnlegesher (1, 2)
            testasynclegesher testdeflegesher __aexit__(self, *exc):
                testreturnlegesher testFalselegesher

        testasynclegesher def foo():
            testasynclegesher testwithlegesher manager():
                testpasslegesher
            testasynclegesher testwithlegesher manager() testaslegesher x:
                testpasslegesher
            testasynclegesher testwithlegesher manager() testaslegesher (x, y):
                testpasslegesher
            testasynclegesher testwithlegesher manager(), manager():
                testpasslegesher
            testasynclegesher testwithlegesher manager() testaslegesher x, manager() testaslegesher y:
                testpasslegesher
            testasynclegesher testwithlegesher manager() testaslegesher x, manager():
                testpasslegesher
            testraiselegesher Done

        testwithlegesher self.assertRaises(Done):
            foo().send(None)


testiflegesher __name__ == '__main__':
    unittest.main()
