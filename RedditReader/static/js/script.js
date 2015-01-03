$(function() {

	function resize_columns() {
		if ($(window).width() < 1200) {
			posts_width = $(window).width() - 700;
			$("#all_posts").width(posts_width);
			$("#article_div").width(700);
		} else {
			article_width = $(window).width() - 500;
			$("#all_posts").width(500);
			$("#article_div").width(article_width);
		}
		height = $(window).height() - 50;
		$("#posts_list_div .scroll-container").height(height);
		$("#article_div #article").height(height);
	}

	// function call that runs on page load
	resize_columns();


	/****************************************************
		EVENT HANDLERS
	****************************************************/

	// window resize events
	$(window).smartresize(function() {
		resize_columns();
	});

	// toggles sidebar
	$("#sidebar_button").click(function() {
		$("#sidebar").show("slide");
	});
	$("#close_button").click(function() {
		$("#sidebar").hide("slide");
	});


});


(function($,sr){

  // debouncing function from John Hann
  // http://unscriptable.com/index.php/2009/03/20/debouncing-javascript-methods/
  var debounce = function (func, threshold, execAsap) {
  	var timeout;

  	return function debounced () {
  		var obj = this, args = arguments;
  		function delayed () {
  			if (!execAsap)
  				func.apply(obj, args);
  			timeout = null;
  		};

  		if (timeout)
  			clearTimeout(timeout);
  		else if (execAsap)
  			func.apply(obj, args);

  		timeout = setTimeout(delayed, threshold || 100);
  	};
  }
  // smartresize 
  jQuery.fn[sr] = function(fn){  return fn ? this.bind('resize', debounce(fn)) : this.trigger(sr); };

})(jQuery,'smartresize');
