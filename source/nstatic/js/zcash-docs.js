window.onscroll = function(ev) {
  var docHeight = jQuery('.wy-nav-content-wrap').innerHeight();
  if ( (window.innerHeight + Math.ceil(window.pageYOffset)) >= docHeight - 128 ) {
      jQuery('.rst-versions').addClass('shift-up');
    } else {
      jQuery('.rst-versions').removeClass('shift-up');
    }
};
