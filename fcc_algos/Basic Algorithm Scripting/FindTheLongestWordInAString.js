function findLongestWord(str) {
  str = str.split(" ");
  var longest = str[0].length;
  for (var i = 1; i < str.length; i++){
      if (longest < str[i].length){
        longest = str[i].length;
      }
    }
  return longest;
}
            //    0    1     2    3    4     5    6    7   8
findLongestWord("The quick brown fox jumped over the lazy dog");
