function factorialize(n) {
  if (n > 0){
    return  n * factorialize(n-1);
  }
  else{
    return 1;
  }
}

factorialize(5);
