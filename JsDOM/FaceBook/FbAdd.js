  /*
  ------------------------------------
  ixakblt - ibrahim AKBULUT
  ------------------------------------
  Web Site :ixakblt
  ------------------------------------
  All Sites : @ixakblt
  ------------------------------------
  */

  let i = 0;
  do {
    task(i);
    i++;
  } while (i < 200);

  function task(i) {
    setTimeout(function () {
      document.getElementsByClassName("addButton _4jy3 _517h _51sy")[i].click();
    }, 1200 * i);
  }