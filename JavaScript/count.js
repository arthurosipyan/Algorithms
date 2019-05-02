// Q: Given a string as a parameter, find the count for each alphabet character.
// - Do we consider captial and lowercase to be the same counted alphabet character? Yes. (Interviewer can say no)

function count(str){
  str = str.toLowerCase();
  str = str.replace('/[^a-zA-Z0-9]/', '');
  var obj = {};
  
  for (var i = 0; i < str.length; i++) {
    obj[str[i]] = obj[str[i]] ? ++obj[str[i]] : 1;
  }
  return obj;
