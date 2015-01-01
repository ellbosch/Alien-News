$(function() {
	var NAMESPACE = {
		article_width: $("#article_div").width()
	}

	function init() {
		resize_posts_div();
		resize_article_div();
	}

	function resize_posts_div() {
		width = $(window).width() - NAMESPACE.article_width;
		height = $(window).height() - 50;
		$("#posts_list_div").css('width', width);
		$("#posts_list_div #all_posts").height(height);
	}

	function resize_article_div() {
		height = $(window).height() - 50;
		$("#article_div #article").height(height);
	}

	// function call that runs on page load
	init();


	/****************************************************
		EVENT HANDLERS
	****************************************************/

	// window resize events
	$(window).smartresize(function() {
		init();
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
