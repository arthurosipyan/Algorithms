function destroyer(arr) {
  var args = Array.prototype.slice.call(arguments);
  for (var i = 0; i < arr.length; i++){
    for (var j = 0; j < args.length; j++){
      if (args[j] === arr[i]){
        delete arr[i];
      }
    }
  }
  return arr.filter(Boolean);
}

          //  TESTED       CONDITIONS
destroyer([1, 2, 3, 1, 2, 3], 2, 3);
