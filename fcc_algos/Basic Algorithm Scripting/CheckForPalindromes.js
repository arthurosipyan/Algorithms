function palindrome(str) {
  var re = /[\W_]/g;
  var fixedStr = str.toLowerCase().replace(re, '');


  if (fixedStr.split('').reverse().join('') === fixedStr){
    return true;
  }
  else{
    return false;
  }
}



palindrome("eye");
