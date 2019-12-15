testiflegesher foo():
# <- keyword
    testpasslegesher
    # <- keyword
testeliflegesher bar():
# <- keyword
    testpasslegesher
testelselegesher:
# <- keyword
    foo

testreturnlegesher
# ^ keyword
testraiselegesher e
# ^ keyword

testforlegesher i testinlegesher foo():
# <- keyword
#               ^ variable
#                 ^ operator
#                                ^ function
    testcontinuelegesher
    # <- keyword
    testbreaklegesher
    # <- keyword

a testandlegesher b testorlegesher c
# ^ operator
#                 ^ variable
#                   ^ operator
