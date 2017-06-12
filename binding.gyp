{
  "targets": [
    {
      "target_name": "addon",
      "cflags": ["-std=c++11" ,'-fexceptions' ,"-fPIC", "-fno-omit-frame-pointer" ],
      "sources": [
        "addon.cc",
        "DwarfWrapper.cc",
        "./src/DwarfReader.cpp",
        "./architecture/ArchBuilder.cpp",
        "./architecture/NamespaceRule.cpp",
        "./architecture/ClassRule.cpp",
        "./src/Context.cpp",
        "./include/DwarfHelper.cpp",
        "./src/Type.cpp",
        "./tag/TagMember.impl"
      ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1
        }
      },
      "conditions": [
        ["OS=='linux'", {
          "defines": [
            "_HAS_EXCEPTIONS=1"
          ]
        }]
      ],
      'cflags_cc': [ '-fexceptions', "-fpermissive" ],
      'include_dirs': [
        '/home/josef/dev/libdwarf-code/libdwarf',
        '/home/josef/dev/HiWi/DwarfLoader/3rdparty/json11',
        '/home/josef/dev/libelf-0.8.13/lib'
      ],
      'link_settings': {
        "libraries": [ "-ldwarf", "-lelf", "/home/josef/dev/HiWi/DwarfLoader/3rdparty/json11/libjson11.a" ]
      #  "ldflags": [
       #      "-Wl,-z,defs",
        #]
      }
      #"cflags": [ ]
     # "link_settings": {
      #  "ldflags": [
       #      "-Wl,-z,defs",
        #]
      #}
    }
  ]
}