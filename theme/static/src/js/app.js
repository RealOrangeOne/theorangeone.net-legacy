import './creative';

$('.image').each(function () {
  const ele = $(this);
  ele.css('background-image', 'url(' + ele.data('image') + ')');
});
