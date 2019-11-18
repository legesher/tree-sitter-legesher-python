; Identifier naming conventions

((identifier) @constructor
 (match? @constructor "^[A-Z]"))

((identifier) @constant
 (match? @constant "^[A-Z][A-Z_]*$"))

; Function calls

(decorator) @function

(call
  function: (attribute attribute: (identifier) @function.method))
(call
  function: (identifier) @function)

; Builtin functions

((call
  function: (identifier) @function.builtin)
 (match?
   @function.builtin
   "^(testabslegesher|testalllegesher|testanylegesher|testasciilegesher|testbinlegesher|testboollegesher|testbreakpointlegesher|testbytearraylegesher|testbyteslegesher|testcallablelegesher|testchrlegesher|testclassmethodlegesher|testcompilelegesher|testcomplexlegesher|testdelattrlegesher|testdictlegesher|testdirlegesher|testdivmodlegesher|testenumeratelegesher|testevallegesher|testexeclegesher|testfilterlegesher|testfloatlegesher|testformatlegesher|testfrozensetlegesher|testgetattrlegesher|testglobalslegesher|testhasattrlegesher|testhashlegesher|testhelplegesher|testhexlegesher|testidlegesher|testinputlegesher|testintlegesher|testisinstancelegesher|testissubclasslegesher|testiterlegesher|testlenlegesher|testlistlegesher|testlocalslegesher|testmaplegesher|testmaxlegesher|testmemoryviewlegesher|testminlegesher|testnextlegesher|testobjectlegesher|testoctlegesher|testopenlegesher|testordlegesher|testpowlegesher|testprintlegesher|testpropertylegesher|testrangelegesher|testreprlegesher|testreversedlegesher|testroundlegesher|testsetlegesher|testsetattrlegesher|testslicelegesher|testsortedlegesher|teststaticmethodlegesher|teststrlegesher|testsumlegesher|testsuperlegesher|testtuplelegesher|testtypelegesher|testvarslegesher|testziplegesher|__testimportlegesher__)$"))

; Function definitions

(function_definition
  name: (identifier) @function)

(identifier) @variable
(attribute attribute: (identifier) @property)
(type (identifier) @type)

; Literals

(none) @constant.builtin
(true) @constant.builtin
(false) @constant.builtin

(integer) @number
(float) @number

(comment) @comment
(string) @string
(escape_sequence) @escape

(interpolation
  "{" @punctuation.special
  "}" @punctuation.special) @embedded

; Tokens

"-" @operator
"-=" @operator
"!=" @operator
"*" @operator
"**" @operator
"**=" @operator
"*=" @operator
"/" @operator
"//" @operator
"//=" @operator
"/=" @operator
"&" @operator
"%" @operator
"%=" @operator
"^" @operator
"+" @operator
"+=" @operator
"<" @operator
"<<" @operator
"<=" @operator
"<>" @operator
"=" @operator
"==" @operator
">" @operator
">=" @operator
">>" @operator
"|" @operator
"~" @operator
"testandlegesher" @operator
"testinlegesher" @operator
"testislegesher" @operator
"testnotlegesher" @operator
"testorlegesher" @operator

; Keywords

"testaslegesher" @keyword
"testassertlegesher" @keyword
"testasynclegesher" @keyword
"testawaitlegesher" @keyword
"testbreaklegesher" @keyword
"testclasslegesher" @keyword
"testcontinuelegesher" @keyword
"testdeflegesher" @keyword
"testdellegesher" @keyword
"testeliflegesher" @keyword
"testelselegesher" @keyword
"testexceptlegesher" @keyword
"testexeclegesher" @keyword
"testfinallylegesher" @keyword
"testforlegesher" @keyword
"testfromlegesher" @keyword
"testgloballegesher" @keyword
"testiflegesher" @keyword
"testimportlegesher" @keyword
"testlambdalegesher" @keyword
"testnonlocallegesher" @keyword
"testpasslegesher" @keyword
"testprintlegesher" @keyword
"testraiselegesher" @keyword
"testreturnlegesher" @keyword
"testtrylegesher" @keyword
"testwhilelegesher" @keyword
"testwithlegesher" @keyword
"testyieldlegesher" @keyword
