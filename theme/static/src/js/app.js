import './creative';

$('.image').each(function () {
  const ele = $(this);
  console.log('ITTERATING', ele.data('image'));
  ele.css('background-image', 'url(' + ele.data('image') + ')');
});
