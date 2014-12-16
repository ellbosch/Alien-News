$(function() {
	var NAMESPACE = {
		article_width: $("#article_div").width()
	}

	function init() {
		resize_posts_div();
	}

	function resize_posts_div() {
		width = $(window).width() - NAMESPACE.article_width;
		$("#posts_list_div").css('width', width);
	}

	// window resize events
	$(window).smartresize(function() {
		resize_posts_div();
	});

	// toggles sidebar
	$("#sidebar_button").click(function() {
		$("#sidebar").show("slide");
	});
	$("#close_button").click(function() {
		$("#sidebar").hide("slide");
	});

	// // updates what article is viewed
	// $(".post").on('mousedown', function(){
	// 	$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
	// 	$.getJSON($SCRIPT_ROOT + '/article', {
	//         'url': $(this).attr("data-url");
	//     }, function(data) {
	//         console.log(data.result);
	//     });

	// 	// var url = $(this).attr("data-url");
	// 	// var get_url = "http://127.0.0.1:5000/article/" + url
		
	// 	// var xmlHttp = null;
	// 	// xmlHttp = new XMLHttpRequest();
	// 	// xmlHttp.open("GET", get_url, true);
	// 	// xmlHttp.send();
	// 	// console.log(xmlHttp.responseText);
	// 	// return xmlHttp.responseText;

	// });

	// function call that runs on page load
	init();

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
