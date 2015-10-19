var is_navbar_attached = false;
function position_navbar() {
    if ($(window).width() < 862) {  // @screen-sm
        $('.navbar-icon').removeClass('ion-ios-arrow-up').addClass('ion-ios-arrow-down');
        return;
    }
    if ($(window).scrollTop() > $('#navbar-anchor').offset().top) {
        if(!is_navbar_attached) {attach_navbar(); is_navbar_attached = true;}
    } else if (is_navbar_attached) {
        detach_navbar();
        is_navbar_attached = false;
    }
    $('.dropdown-menu').each(function(){
        direction = ($(this).height() + 10 < $('nav').offset().top - $(window).scrollTop()) ? 'up' : 'down';
        flip_dropdowns($(this), direction);
    });
}


function detach_navbar() {
    $('#navbar-container').removeClass('stick-top').addClass('align');
    $('.dropdown-menu').removeClass('dropdown').addClass('dropup');
}


function set_page_sizes() {
    win_height = $(window).height();
    win_width = $(window).width();
    $('.page-height').each(function() {
        $(this).height(win_height);
    });
    $('.page-width').each(function() {
        $(this).width(win_width);
    });
}


function attach_navbar() {
    $('#navbar-container').removeClass('align').addClass('stick-top');
    $('.dropdown-menu').removeClass('dropup').addClass('dropdown');
}


function flip_dropdowns(obj, direction) {
    if (obj.hasClass('drop'+direction)){ return; }
    reverse = direction == 'up' ? 'down' : 'up';
    obj.removeClass('drop' + reverse).addClass('drop' + direction);
    obj.prev().children().removeClass('ion-ios-arrow-' + reverse).addClass('ion-ios-arrow-' + direction);
}


function space_navbar() { //This really should be CSS!
    if ($(window).width() < 862) {return;}  // @screen-sm
    nav_width = $('#navigation').outerWidth(true);
    full_width = $('nav > .container-fluid').outerWidth(true) - $('.home-button').outerWidth(true);
    margin = (full_width - nav_width) / 2;
    $('#navigation').css('margin-left', margin);
}


function checkDomain(url) {
  if ( url.indexOf('//') === 0 ) { url = location.protocol + url; }
  return url.toLowerCase().replace(/([a-z])?:\/\//,'$1').split('/')[0];
}


function isExternal(url) {
  return ( ( url.indexOf(':') > -1 || url.indexOf('//') > -1 ) && checkDomain(location.href) !== checkDomain(url) );
}


function is_on_screen(elm) {
    var vpH = $(window).height(), // Viewport Height
        st = $(window).scrollTop(), // Scroll Top
        y = $(elm).offset().top,
        elementHeight = $(elm).height();
    return ((y < (vpH + st)) && (y > (st - elementHeight)));
}


function navTo(url){
    location.href=url;
}
