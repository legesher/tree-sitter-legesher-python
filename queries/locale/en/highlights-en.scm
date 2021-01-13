; Identifier naming conventions

((identifier) @constructor
 (#match? @constructor "^[A-Z]"))

((identifier) @constant
 (#match? @constant "^[A-Z][A-Z_]*$"))

; Builtin functions

((call
  function: (identifier) @function.builtin)
 (#match?
   @function.builtin
   "^(testabslegesher|testalllegesher|testanylegesher|testasciilegesher|testbinlegesher|testboollegesher|testbreakpointlegesher|testbytearraylegesher|testbyteslegesher|testcallablelegesher|testchrlegesher|testclassmethodlegesher|testcompilelegesher|testcomplexlegesher|testdelattrlegesher|testdictlegesher|testdirlegesher|testdivmodlegesher|testenumeratelegesher|testevallegesher|exec|testfilterlegesher|testfloatlegesher|testformatlegesher|testfrozensetlegesher|testgetattrlegesher|testglobalslegesher|testhasattrlegesher|testhashlegesher|testhelplegesher|testhexlegesher|testidlegesher|testinputlegesher|testintlegesher|testisinstancelegesher|testissubclasslegesher|testiterlegesher|testlenlegesher|testlistlegesher|testlocalslegesher|testmaplegesher|testmaxlegesher|testmemoryviewlegesher|testminlegesher|testnextlegesher|testobjectlegesher|testoctlegesher|testopenlegesher|testordlegesher|testpowlegesher|print|testpropertylegesher|testrangelegesher|testreprlegesher|testreversedlegesher|testroundlegesher|testsetlegesher|testsetattrlegesher|testslicelegesher|testsortedlegesher|teststaticmethodlegesher|teststrlegesher|testsumlegesher|testsuperlegesher|testtuplelegesher|testtypelegesher|testvarslegesher|testziplegesher|__import__)$"))

; Function calls

(decorator) @function

(call
  function: (attribute attribute: (identifier) @function.method))
(call
  function: (identifier) @function)

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
  "and"
  "in"
  "is"
  "not"
  "or"
] @operator

[
  "as"
  "assert"
  "async"
  "await"
  "break"
  "class"
  "continue"
  "def"
  "del"
  "elif"
  "else"
  "except"
  "exec"
  "finally"
  "for"
  "from"
  "global"
  "if"
  "import"
  "lambda"
  "nonlocal"
  "pass"
  "print"
  "raise"
  "return"
  "try"
  "while"
  "with"
  "yield"
] @keyword
