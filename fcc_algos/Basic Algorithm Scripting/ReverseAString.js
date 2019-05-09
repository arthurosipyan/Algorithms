function reverseString(str) {
  var splitStr = str.split('');
  var reversedStr = splitStr.reverse();
  var newStr = reversedStr.join('');
  return newStr;
}

reverseString("hello");
