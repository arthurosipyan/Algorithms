function getIndexToIns(arr, num) {

function compareNumbers(a, b) {
  return a - b;
}
  var newArr = arr.sort(compareNumbers);
  var result = 0;

  if (newArr.indexOf(num) === -1){
      result = 0;
    }
  for (var i = 0; i < newArr.length; i++){
    if (newArr[i] >= num){
      return i;
    }
  }
  return arr.length;
}

getIndexToIns([40, 60], 50);
