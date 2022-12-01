"use strict";
exports.__esModule = true;
var fs = require("fs");
var result = fs.readFileSync('example.txt', 'utf8');
console.log(result);
var currentMax = 0;
