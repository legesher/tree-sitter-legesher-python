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
 * TODO: pull keyword language translation for programming language from the
 *       legesher-translations repository
 * TODO: take file variable and find the keywords in files that need to be
         exchanged with the translated keyword
 * TODO: change the associated keywords with the translation
 * TODO: run tree-sitter configuration to rebuild parser bindings
 * TODO: run tests to confirm bindings are correct
 *
 */
'use strict';
const _ = require('lodash');
const fs = require('fs');

// TODO: pull keyword language translation for programming language from the
//       legesher-translations repository
// NOTE: Translation API isn't created yet
const translationFile = require('./keywords.json');

/** @param {array} preFiles list of files with simple replace translations */
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
];

/** @param {array} specialFiles list of files with special translation rules */
const specialFiles = [
  // 'test/corpus/expressions.txt',
  // 'test/corpus/literals.txt',
  // 'test/corpus/statements.txt',
  // 'test/highlight/keywords.py',
];

/** @param {array} postFiles list of files translated as a result of running
 *         the tree-sitter configuration.
 */
const postFiles = [
  'src/parser.c',
  'src/grammar.json',
  'src/node-types.json',
];

/**
 * Create the path for the new translation file with the abbreviation
 *   The file variable will come in this format:
 *     'examples/compound-statement-without-trailing-newline.py'
 *   The ab variable will come in this format:
 *     'en'
 *   The returned string will be in this format:
 *     'examples/compound-statement-without-trailing-newline-en.py'
 * @param {string} file original name of the file
 * @param {string} ab translation language abbreviation
 * @return {string} new path for translation file
 */
function createNewFilePath(file, ab) {
  const f = _.split(file, '.py');
  return `${f[0]}-${ab}.py`;
}

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
  }).on('error', function(err) {
    console.log(err);
  }).on('end', function() {
    console.log('INSIDE END - this is the data from the parsed file:', data);
  });
  console.log('RETURN PARSE - this is the data from the parsed file:', data);
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
 * Translate PreFiles
 * @param {array} pre list of files that need to be searched
 * @param {array} tra translation data
 */
function translatePre(pre, tra) {
  _.each(pre, function(file) {
    const fn = createNewFilePath(file, tra.translationAbbreviation);
    const f = parsePreFile(file);
    console.log('f: ', f);
    console.log(fn);
    simpleReplaceKeywords(tra.python, f);
  });
};

/**
 * Translate Special Condition Files
 * @param {array} spe list of special files need to be searched with conditions
 * @param {array} tra translation data
 */
function translateSpecial(spe, tra) {};

/**
 * Run Tree-Sitter configuration with new translated files
 */
function runTreeSitter() {};

/**
 * Translate Post Files
 * @param {array} post list of files that need to be checked after run
 * @param {array} tra translation data
 */
function translatePost(post, tra) {};

/**
 * Search for keyword list in files
 * @param {array} pre list of files that need to be searched
 * @param {array} spe list of special files need to be searched with conditions
 * @param {array} post list of files that need to be checked after run
 * @param {array} tra translation data
 */
function checkFiles(pre, spe, post, tra) {
  _.map(pre, function(v, k) {
    // console.log('KEY:', k, 'VALUE:', v);
  });
}

/**
 * Run full translation of Tree-Sitter-Legesher-Python
 * @param {array} pre list of files that need to be searched
 * @param {array} spe list of special files need to be searched with conditions
 * @param {array} post list of files that need to be checked after run
 * @param {array} tra translation data
 */
function translate(pre, spe, post, tra) {
  translatePre(pre, tra);
  translateSpecial(spe, tra);
  runTreeSitter();
  translatePost(post, tra);
  checkFiles(pre, spe, post, tra);
};

translate(preFiles, specialFiles, postFiles, translationFile);