window.updateTitle = function (value) {
  document.title = value + ' | TheOrangeOne';
};

if ($('.header h1').length) {
  window.updateTitle($('.header h1').text());
}
