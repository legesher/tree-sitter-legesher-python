/* KEY OBJECTIVE: Keyword Translation
 * For every file in this repository that configures keywords and their
 * functionality, the keywords will need to be exchanged with the appropriate
 * translation.
 *
 * POSSIBLE DIRECTIONS:
 * 1. Keep the test keywords (eg. testprintlegesher) as a Test translation to
 *    properly have a base for change of translations and for testing.
 * 2. Keep all of the bindings of official translations within the
 *    tree-sitter-legesher-python repository.
 * 3. Utilize Translation API to configure translations for the
 *    tree-sitter-legesher-python repository to keep repository lightweight.
 * 4. Play around with how much of this functionality needs to be in the
 *    tree-sitter-legesher-python repository and how much can be part of the
 *    legesher repository and/or legesher-translation repository.
 *
 * STEPS FOR COMPLETION:
 * TODO: create variable of all files that need keyword translations
 * TODO: pull keyword language translation for programming language from the
 *       legesher-translations repository
 * TODO: take file variable and find the keywords in files that need to be
         exchanged with the translated keyword
 * TODO: change the associated keywords with the translation
 * TODO: run tree-sitter configuration to rebuild parser bindings
 * TODO: run tests to confirm bindings are correct
 *
 */

const files = [
  'examples/compound-statement-without-trailing-newline.py',
  'examples/crlf-line-endings.py',
  'examples/mixed-spaces-tabs.py',
  'examples/multiple-newlines.py',
  'examples/python2-grammar-crlf.py',
  'examples/python2-grammar.py',
  'examples/python3-grammar-crlf.py',
  'examples/python3-grammar.py',
  'examples/python3.8_grammar.py',
  'examples/simple-numbers',
  'examples/simple-statements-without-trailing-newline.py',
  'examples/tabs.py',
  'examples/trailing-whitespace.py',
  'grammar.js',
  'queries/highlights.scm',
  'src/grammar.json',
  'src/node-types.json',
  'src/parser.c',
  'test/corpus/expressions.txt',
  'test/corpus/literals.txt',
  'test/corpus/statements.txt',
  'test/highlight/keywords.py',
];