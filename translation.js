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
 * TODO: create object variable of all files that need keyword translations
 *       - differentiate between what files need to be initially translated
           and which files are changed as a result of tree-sitter configuration
 * TODO: pull keyword language translation for programming language from the
 *       legesher-translations repository
 * TODO: take file variable and find the keywords in files that need to be
         exchanged with the translated keyword
 * TODO: change the associated keywords with the translation
 * TODO: run tree-sitter configuration to rebuild parser bindings
 * TODO: run tests to confirm bindings are correct
 *
 */

//  TODO: create variable of all files that need keyword translations
// preFiles : all of the files that need to be initially translated before the
//            the tree-sitter configuration

const _ = require('lodash');
const fs = require('fs');

// TODO: there are files with special formatting that need special conditions
const preFiles = [
  'examples/compound-statement-without-trailing-newline.py',
  // 'examples/crlf-line-endings.py',
  // 'examples/mixed-spaces-tabs.py',
  // 'examples/multiple-newlines.py',
  // 'examples/python2-grammar-crlf.py',
  // 'examples/python2-grammar.py',
  // 'examples/python3-grammar-crlf.py',
  // 'examples/python3-grammar.py',
  // 'examples/python3.8_grammar.py',
  // 'examples/simple-numbers.py',
  // 'examples/simple-statements-without-trailing-newline.py',
  // 'examples/tabs.py',
  // 'examples/trailing-whitespace.py',
  // 'grammar.js',
  // 'queries/highlights.scm',
  // 'test/corpus/expressions.txt',
  // 'test/corpus/literals.txt',
  // 'test/corpus/statements.txt',
  // 'test/highlight/keywords.py',
];

// postFiles : all of the files that are translated as a result of running the
//            the tree-sitter configuration. These need to be checked for the
//            correct translation
const postFiles = [
  'src/parser.c',
  'src/grammar.json',
  'src/node-types.json',
];

// TODO: pull keyword language translation for programming language from the
//       legesher-translations repository
// TODO: Translation API isn't created yet, so use keywords file in the meantime
const keywordsFile = require('./keywords.json');

// TODO: take file variable and find the keywords in files that need to be
//      exchanged with the translated keyword
/**
 * Read in pre files and search through text for keyword list
 * @param {file} file that needs to be searched
 * @return {string} data text for files
 */
function parsePreFile(file) {
  let data = '';
  const readStream = fs.createReadStream(file, 'utf8');

  readStream.on('data', function(chunk) {
    data += chunk;
  }).on('end', function() {
    console.log(data);
  });
  return data;
}

/**
 * Map out each keyword
 * @param {array} keywords list of keywords
 * @param {string} fileData of files that need to be searched
 * @return {string} data text for files
 */
function simpleReplaceKeywords(keywords, fileData) {
  _.forIn(keywords, function(value, key) {
    console.log('filedata before: ', fileData);
    _.replace(fileData, key, value);
    console.log('fileData after: ', fileData);
  });

  console.log('final:', fileData);
  return fileData;
}
/**
 * Map out each keyword
 * @param {string} key keyword
 * @param {string} value value
 * @param {string} fileData of files that need to be searched
 * @return {string} data text for files
 */
// function simpleReplaceKeyword(key, value, fileData) {
//   console.log('key', key, 'value', value, 'fileData', fileData);
//
//   if (_.includes(fileData, key)) {
//     // replace
//     console.log('matched with', key);
//   }
//   return fileData;
// }

/**
 * Search for keyword list in files
 * @param {array} files The first number
 * @param {array} keywords list of keywords
 */
function checkFiles(files, keywords) {
  _.map(files, function(v, k) {
    // console.log('KEY:', k, 'VALUE:', v);
  });
}

/**
 * Translate files
 * @param {array} pre list of files that need to be searched
 * @param {array} post list of files that need to be checked
 * @param {array} keywords list of keywords
 */
function translate(pre, post, keywords) {
  _.each(pre, function(file) {
    const f = parsePreFile(file);
    simpleReplaceKeywords(keywords, f);
  });

  // checkFiles(pre);
  // checkFiles(post);
};

translate(preFiles, postFiles, keywordsFile);