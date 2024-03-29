# tree-sitter-legesher-python

This crate provides a Python grammar for the [tree-sitter][] parsing library.
To use this crate, add it to the `[dependencies]` section of your `Cargo.toml`
file. (Note that you will probably also need to depend on the
[`tree-sitter`][tree-sitter crate] crate to use the parsed result in any useful
way.)

```toml
[dependencies]
tree-sitter = "0.17"
tree-sitter-legesher-python = "0.17"
```

Typically, you will use the [language][language func] function to add this
grammar to a tree-sitter [Parser][], and then use the parser to parse some code:

```rust
let code = r#"
    def double(x):
        return x * 2
"#;
let mut parser = Parser::new();
parser.set_language(tree_sitter_python_legesher::language()).expect("Error loading Python grammar");
let parsed = parser.parse(code, None);
```

[language]: https://docs.rs/tree-sitter/*/tree_sitter/struct.Language.html
[language func]: https://docs.rs/tree-sitter-python/*/tree_sitter_python/fn.language.html
[parser]: https://docs.rs/tree-sitter/*/tree_sitter/struct.Parser.html
[tree-sitter]: https://tree-sitter.github.io/
[tree-sitter crate]: https://crates.io/crates/tree-sitter
