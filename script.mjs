import { createRequire } from './module';
const require = createRequire(import.meta.url);
var mysql = require('mysql');

var con = mysql.createConnection({
  host: getenv('HOST'),
  user: getenv('USER'),
  password: getenv('PASSWORD'),
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
///  con.query("SELECT * FROM customers", function (err, result, fields) {
