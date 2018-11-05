(function($) {
  $('.js-share-twitter-link').click(function(e) {
    e.preventDefault();
    var href = $(this).attr('href');
    window.open(href, "Twitter", "height=285,width=550,resizable=1");
  });
  $('.js-share-facebook-link').click(function(e) {
    e.preventDefault();
    var href = $(this).attr('href');
    window.open(href, "Facebook", "height=269,width=550,resizable=1");
  });
})(jQuery);
