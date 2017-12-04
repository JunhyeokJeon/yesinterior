$(function(){
    var lastScrollTop = 0, delta = 15;
    $(window).scroll(function(event){
        var st = $(this).scrollTop();

        if(Math.abs(lastScrollTop-st) <= delta)
          return;

        if((st > lastScrollTop) && (lastScrollTop > 0)){
          $(".none_header").css({"top": "-110px"});
        } else {
          $(".none_header").css({"top": "0px", "display": "block"});
        }
        lastScrollTop = st;
        if(lastScrollTop == 0) {
          $(".none_header").css({"top": "-110px"});
        }
    });
});
