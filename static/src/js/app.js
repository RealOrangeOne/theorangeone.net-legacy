import './creative';
import ansi_up from 'ansi_up';


$('.image').each(function () {  // setup div-image hybrids
  const ele = $(this);
  if (ele.data('image')) {
    ele.css('background-image', 'url(' + ele.data('image') + ')');
  } else {
    ele.removeClass('image');
  }
});

$('.ansi-up').each(function () {
  const ele = $(this);
  ele.html(ansi_up.ansi_to_html(ele.html()));
});
