function bouncer(arr) {
  //var falsy = [false, null, 0, "", undefined, NaN];
function falsy(check){
  switch(check){
    case false:
      return false;
    case null:
      return null;
    case 0:
      return 0;
    case "":
      return "";
    case undefined:
      return undefined;
    case NaN:
      return NaN;
    default:
      return check;
  }
}

  return arr.filter(falsy);
}

bouncer([7, "ate", "", false, 9]);
