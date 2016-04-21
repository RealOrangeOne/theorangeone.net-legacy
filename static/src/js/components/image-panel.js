export default function renderImagePanels() {
  $('.image-panel').each(function () {
    const element = $(this);
    if (!element.data('image')) {  // if it doesnt have an image, ignore it.
      return;
    }

    element.css('background-image', 'url("' + element.data('image') + '")');

    let height;
    switch (element.data('size').toLowerCase()) {
      case 'small':
        height = '30';
        break;
      default:
      case 'medium':
        height = '60';
        break;
      case 'large':
        height = '100';
    }
    element.css('background-image', `${height}vh`);
  });
}
