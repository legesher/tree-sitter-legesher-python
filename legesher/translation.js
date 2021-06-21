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
const files = require('./files.json').files;

/** @param {array} preFiles list of files with simple replace translations */
const preFiles = _.filter(files, {
  parseType: "pre"
});

/** @param {array} specialFiles list of files with special translation rules */
const specialFiles = _.filter(files, {
  parseType: "special"
});

/** @param {array} postFiles list of files translated as a result of running
 *         the tree-sitter configuration.
 */
const postFiles = _.filter(files, {
  parseType: "post"
});

/**
 * Create the path for the new translation file with the abbreviation
 *   The file variable will come in this format:
 *     'examples/compound-statement-without-trailing-newline.py'
 *   The ab variable will come in this format:
 *     'en'
 *   The returned string will be in this format:
 *     'examples/locale/en/compound-statement-without-trailing-newline-en.py'
 * @param {string} file original name of the file
 * @param {string} ab translation language abbreviation
 * @return {string} new path for translation file
 */
function createNewFilePath(file, ab) {
  let path = '';
  const f = _.split(file, new RegExp(`\.(py|scm|js)$`));
  if (_.includes(f[0], `/`)) {
    const g = _.split(f[0], `/`);
    path = `${g[0]}/locale/${ab}/${g[1]}-${ab}.${f[1]}`;
  } else {
    path = `locale/${ab}/${f[0]}-${ab}.${f[1]}`;
  }
  console.log(`new path created...`);
  return path;
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
    console.log(`file read stream completed...`);
    const fn = createNewFilePath(file, translationFile.translationAbbreviation);
    const newData = simpleReplaceKeywords(translationFile.python, data);
    createNewFile(fn, newData);
    return newData;
  });
}

/**
 * Read in special files and search through text for keyword list and add new
 * rules for their special replacement rules
 * @param {file} file that needs to be searched
 * @return {string} data text for files
 */
function parseSpeFile(file) {
  let data = '';
  const readStream = fs.createReadStream(file, 'utf8');

  readStream.on('data', function(chunk) {
    data += chunk;
  }).on('error', function(err) {
    console.log(err);
  }).on('end', function() {
    console.log(`file read stream completed...`);
    const fn = createNewFilePath(file, translationFile.translationAbbreviation);
    const newData = specialReplaceKeywords(translationFile.python, data);
    // createNewFile(fn, newData);
    return newData;
  });
}

/**
 * Map out each keyword
 * @param {array} keywords list of keywords
 * @param {string} fileData of files that need to be searched
 * @return {string} data text for files
 */
function simpleReplaceKeywords(keywords, fileData) {
  let newFile = fileData;
  _.forIn(keywords, function(value, key) {
    newFile = _.replace(newFile, new RegExp(key, 'g'), value);
  });
  if (_.includes(newFile, `name: 'python_legesher',`)) {
    newFile = _.replace(newFile, `name: 'python_legesher',`,
      `name: 'python_legesher_${translationFile.translationAbbreviation}',`);
  }
  console.log(`simple keywords replaced...`);
  return newFile;
}

/**
 * Special replacement rules for keywords
 * @param {array} keywords list of keywords
 * @param {string} fileData of files that need to be searched
 * @return {string} data text for files
 */
function specialReplaceKeywords(keywords, fileData) {
  let newFile = fileData;
  _.forIn(keywords, function(value, key) {
    newFile = _.replace(newFile, new RegExp(key, 'g'), value);
  });
  if (_.includes(newFile, `name: 'python_legesher',`)) {
    newFile = _.replace(newFile, `name: 'python_legesher',`,
      `name: 'python_legesher_${translationFile.translationAbbreviation}',`);
  }
  console.log(`simple keywords replaced...`);
  return newFile;
}

/**
 * Create a new file with translated content
 * @param {string} name filename
 * @param {string} data content for file
 */
function createNewFile(name, data) {
  fs.writeFile(name, data, function(err) {
    if (err) throw err;
    console.log(`new file saved!`);
  });
};

/**
 * Translate PreFiles
 * @param {array} pre list of files that need to be searched
 * @param {array} tra translation data
 */
function translatePre(pre, tra) {
  _.each(pre, function(file) {
    console.log(`Simple translation starting for ${file}`);
    parsePreFile(file);
  });
};

/**
 * Translate Special Condition Files
 * @param {array} spe list of special files need to be searched with conditions
 * @param {array} tra translation data
 */
function translateSpecial(spe, tra) {
  _.each(spe, function(file) {
    console.log(`Special translation starting for ${file}`);
    parseSpecialFile(file);
  });
};

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
  // translatePre(pre, tra);
  // translateSpecial(spe, tra);
  // runTreeSitter();
  // translatePost(post, tra);
  // checkFiles(pre, spe, post, tra);
};

translate(preFiles, specialFiles, postFiles, translationFile);

// linter changes
// newline at end
// first if statement tab in examples/locale/en/crlf-line-endings-en.py
// examples/locale/en/multiple-newlines-en.py needs newlines at the end of file
// line 309 in examples/python2-grammar.py
// trailing-whitespace is all messed up
// built in functions for highlights.scm
// exec function or __import__ is not tempalted out for highlights.scm