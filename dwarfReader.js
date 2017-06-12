var addon = require("./build/Release/addon");

var filename = process.argv[2];
//console.log(filename);

var dwarfReader = new addon.dwarf(filename);

console.log(dwarfReader.start());