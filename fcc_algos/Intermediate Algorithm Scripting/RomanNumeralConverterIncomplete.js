function convertToRoman(num) {
  let romanNumerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  let romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  var result = '';
  for (var i = 0; i < romanValues.length; i++){
    while (romanValues[i] <= num){
      result += romanNumerals[i];
      num -= romanValues[i];
    }
  }
 return result;
}

convertToRoman(36);
