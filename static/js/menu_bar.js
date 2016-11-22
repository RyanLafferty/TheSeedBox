//http://stackoverflow.com/questions/17717025/how-to-active-nav-bar-in-bootstrap-with-jquery
$(function() {
   $("li").click(function() {
      // remove classes from all
      $("li").removeClass("active");
	  $("button").removeClass("active");
	  $('.navbar-toggle').click();
      // add class to the one we clicked
      $(this).addClass("active");
   });
});

$(function() {
   $("button").click(function() {
      // remove classes from all
      $("li").removeClass("active");
	  $("button").removeClass("active");
      // add class to the one we clicked
      $(this).addClass("active");
   });
});

