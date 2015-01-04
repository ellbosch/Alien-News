$(function() {

	function resize_columns() {
		// set widths
		var window_width = $(window).width();
		if (window_width >= 1200) {
			article_width = window_width - 500;
			$("#posts_list_div .scroll-container").width(500);
			$("#article_div").width(article_width);
		} else if (window_width >= 970) {
			posts_width = window_width - 700;
			$("#posts_list_div .scroll-container").width(posts_width);
			$("#article_div").width(700);
		} else if (window_width > 670) {
			article_width = window_width - 270;
			$("#posts_list_div .scroll-container").width(270);
			$("#article_div").width(article_width);

			$("#article_div").show();
		} else {
			$("#posts_list_div .scroll-container").width("100%");
			$("#article_div").width("100%");
		}

		// set heights
		height = $(window).height() - 50;
		$("#posts_list_div .scroll-container").height(height);
		$("#article_div .scroll-container").height(height);
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

	// back button handling when window width is less than 670px
	$("#go-back-to-posts").on('click', function() {
		$("#article_div").toggle("slide", { direction: 'right' });
	})

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
