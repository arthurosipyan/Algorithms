function repeatStringNumTimes(str, num) {
  var result = str;
  if (num < 0){
    return '';
  }
  for (var i = 1; i < num; i++){
    result += str;
  }
  return result;
}
repeatStringNumTimes("abc", 3);
