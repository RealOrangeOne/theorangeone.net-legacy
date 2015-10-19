var React = require('react');
var Bootstrap = require('react-bootstrap');

var Carousel = Bootstrap.Carousel;
var CarouselItem = Bootstrap.CarouselItem;

const indexCarousel = (
  <Carousel>
    <CarouselItem>
      <div className='carousel-image'></div>
      <div className='carousel-caption'>
        <h3>Setup</h3>
        <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
      </div>
    </CarouselItem>

    <CarouselItem>
      <div className='carousel-image'></div>
      <div className='carousel-caption'>
        <h3>Student Robotics</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      </div>
    </CarouselItem>
  </Carousel>
);

module.exports = indexCarousel;