{
  "targets": [
    {
      "target_name": "reg",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
      ],
      "sources": [ "binding/reg.cc" ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "AdditionalOptions": [
            "/std:c++17"
          ],
          "ExceptionHandling": 1
        },
      }
    }
  ]
}
