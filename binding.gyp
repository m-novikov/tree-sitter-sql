{
  "targets": [
    {
      "target_name": "tree_sitter_generate",
      "type": "none",
      "conditions": [
        ['OS!="win"', {
          "actions": [
            {
              "action_name": "generate_parser",
              "message": "Generating Parser UNIX...",
              "inputs": [],
              "outputs": ["src/parser.c", "grammar.json", "node-types.json", "node-types.json.rej"],
              "action": ["eval", "npm run gen"]
            }
          ]
        }],
        ['OS=="win"', {
          "actions": [
            {
              "action_name": "generate_parser",
              "message": "Generating Parser Windows ...",
              "inputs": [],
              "outputs": ["src/parser.c", "grammar.json", "node-types.json", "node-types.json.rej"],
              "action": ["npm run gen"]
            }
          ]
        }]
      ]
    },
    {
      "target_name": "tree_sitter_sql_binding",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c",
        "src/scanner.cc"
      ],
      "dependencies": ["tree_sitter_generate"],
      "cflags_c": [
        "-std=c99",
      ]
    }
  ]
}
