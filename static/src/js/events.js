$(window).scroll(function() {
    position_navbar();
});


$(window).resize(function() {
    set_page_sizes();
    space_navbar();
});


$("#page-down").click(function() {
    $('html, body').animate({
        scrollTop: $("#navbar-anchor").offset().top
    }, 750);
});
