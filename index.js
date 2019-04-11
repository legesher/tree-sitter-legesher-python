try {
  module.exports = require("./build/Release/tree_sitter_legesher_python_binding");
} catch (error) {
  try {
    module.exports = require("./build/Debug/tree_sitter_legesher_python_binding");
  } catch (_) {
    throw error
  }
}
