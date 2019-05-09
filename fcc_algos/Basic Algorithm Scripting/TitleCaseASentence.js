function titleCase(str) {
  return str.toLowerCase().replace(/(^|\s)\S/g, (L) => L.toUpperCase());
}
        //--0--1---2-----3---4---
titleCase("I'm a little tea pot");
