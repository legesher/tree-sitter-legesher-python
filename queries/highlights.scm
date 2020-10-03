; Identifier naming conventions

((identifier) @constructor
 (#match? @constructor "^[A-Z]"))

((identifier) @constant
 (#match? @constant "^[A-Z][A-Z_]*$"))

; Function calls

(decorator) @function

(call
  function: (attribute attribute: (identifier) @function.method))
(call
  function: (identifier) @function)

; Builtin functions

((call
  function: (identifier) @function.builtin)
 (#match?
   @function.builtin
   "^(testabslegesher|testalllegesher|testanylegesher|testasciilegesher|testbinlegesher|testboollegesher|testbreakpointlegesher|testbytearraylegesher|testbyteslegesher|testcallablelegesher|testchrlegesher|testclassmethodlegesher|testcompilelegesher|testcomplexlegesher|testdelattrlegesher|testdictlegesher|testdirlegesher|testdivmodlegesher|testenumeratelegesher|testevallegesher|testexeclegesher|testfilterlegesher|testfloatlegesher|testformatlegesher|testfrozensetlegesher|testgetattrlegesher|testglobalslegesher|testhasattrlegesher|testhashlegesher|testhelplegesher|testhexlegesher|testidlegesher|testinputlegesher|testintlegesher|testisinstancelegesher|testissubclasslegesher|testiterlegesher|testlenlegesher|testlistlegesher|testlocalslegesher|testmaplegesher|testmaxlegesher|testmemoryviewlegesher|testminlegesher|testnextlegesher|testobjectlegesher|testoctlegesher|testopenlegesher|testordlegesher|testpowlegesher|testprintlegesher|testpropertylegesher|testrangelegesher|testreprlegesher|testreversedlegesher|testroundlegesher|testsetlegesher|testsetattrlegesher|testslicelegesher|testsortedlegesher|teststaticmethodlegesher|teststrlegesher|testsumlegesher|testsuperlegesher|testtuplelegesher|testtypelegesher|testvarslegesher|testziplegesher|__testimportlegesher__)$"))

; Function definitions

(function_definition
  name: (identifier) @function)

(identifier) @variable
(attribute attribute: (identifier) @property)
(type (identifier) @type)

; Literals

[
  (none)
  (true)
  (false)
] @constant.builtin

[
  (integer)
  (float)
] @number

(comment) @comment
(string) @string
(escape_sequence) @escape

(interpolation
  "{" @punctuation.special
  "}" @punctuation.special) @embedded

[
  "-"
  "-="
  "!="
  "*"
  "**"
  "**="
  "*="
  "/"
  "//"
  "//="
  "/="
  "&"
  "%"
  "%="
  "^"
  "+"
  "->"
  "+="
  "<"
  "<<"
  "<="
  "<>"
  "="
  ":="
  "=="
  ">"
  ">="
  ">>"
  "|"
  "~"
  "testandlegesher"
  "testinlegesher"
  "testislegesher"
  "testnotlegesher"
  "testorlegesher"
] @operator

[
  "testaslegesher"
  "testassertlegesher"
  "testasynclegesher"
  "testawaitlegesher"
  "testbreaklegesher"
  "testclasslegesher"
  "testcontinuelegesher"
  "testdeflegesher"
  "testdellegesher"
  "testeliflegesher"
  "testelselegesher"
  "testexceptlegesher"
  "testexeclegesher"
  "testfinallylegesher"
  "testforlegesher"
  "testfromlegesher"
  "testgloballegesher"
  "testiflegesher"
  "testimportlegesher"
  "testlambdalegesher"
  "testnonlocallegesher"
  "testpasslegesher"
  "testprintlegesher"
  "testraiselegesher"
  "testreturnlegesher"
  "testtrylegesher"
  "testwhilelegesher"
  "testwithlegesher"
  "testyieldlegesher"
] @keyword
