$(window).scroll(function() {
		
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('menu-shrink');
    } else {
      $('#header').removeClass('menu-shrink');
    }
  });
  
  $('a').on('click', function(e){
      var anchor = $(this);
      $('html, body').stop().animate({
          scrollTop: $(anchor.attr('href')).offset().top - 50
      }, 1500);
      e.preventDefault();
  });
      

$(function() {
    "use strict";
    
    var body = $('body'),
        slider = $('.slider'),
        sliderUl = slider.find('> ul'),
        sliderOlLi = slider.find('> ol li'),
        sliderCtrl = slider.find('> .controll .fa'),
        sliderTime = 500,
        sliderWait = 4000,
        autoRun;

    sliderUl.append('<li>' + sliderUl.find('> li').first().html() + '</li>');
    sliderUl.prepend('<li>' + sliderUl.find('> li').last().prev().html() + '</li>');

    function resetDimension() {
        slider.height(sliderUl.height());
        sliderUl.find('> li').width(slider.width());
        sliderUl.width(sliderUl.find('> li').width() * sliderUl.find('> li').length);
    }
    resetDimension();

    $(window).on('resize', function() {
        resetDimension();
    });

    function runSlider() {
        if (sliderUl.find('> li').hasClass('slider-active')) {
            sliderUl.animate({
                left: -sliderUl.find('> li').width() * $('.slider-active').index()
            }, sliderTime);
            sliderOlLi.eq($('.slider-active').index() - 1).addClass('pointer-active').siblings('li').removeClass('pointer-active');
        }
    }
    runSlider();

    sliderCtrl.on('click', function() {
        $(this).addClass('active').siblings().removeClass('active');
        
        if ($(this).hasClass('fa-chevron-left')) {
            if ($('.slider-active').prev().is(':first-of-type')) {
                $('.slider-active').prev().addClass('slider-active').siblings('li').removeClass('slider-active');
                sliderUl.css('left', -sliderUl.find('> li').width() * (sliderUl.find('> li').length - 1));
                sliderUl.find('> li').last().prev().addClass('slider-active').siblings('li').removeClass('slider-active');
            } else {
                $('.slider-active').prev().addClass('slider-active').siblings('li').removeClass('slider-active');
            }
        }
        if ($(this).hasClass('fa-chevron-right')) {
            if ($('.slider-active').next().is(':last-of-type')) {
                $('.slider-active').next().addClass('slider-active').siblings('li').removeClass('slider-active');
                sliderUl.css('left', 0);
                sliderUl.find('> li').first().next().addClass('slider-active').siblings('li').removeClass('slider-active');
            } else {
                $('.slider-active').next().addClass('slider-active').siblings('li').removeClass('slider-active');
            }
        }
        runSlider();
    });

    function autoRunSlider() {
        if (body.css('direction') === 'ltr') {
            autoRun = setInterval(function() {
                sliderCtrl.last().click();
            }, sliderWait);
        } else if (body.css('direction') === 'rtl') {
            autoRun = setInterval(function() {
                sliderCtrl.first().click();
            }, sliderWait);
        }
    }
    autoRunSlider();

    sliderCtrl.on('mouseenter', function() {
        clearInterval(autoRun);
    });
    sliderCtrl.on('mouseleave', function() {
        autoRunSlider();
    });
    
    sliderOlLi.on('mouseenter', function() {
        clearInterval(autoRun);
    });
    sliderOlLi.on('mouseleave', function() {
        autoRunSlider();
    });
    
    
    sliderOlLi.on('click', function() {
        
        $(this).addClass('pointer-active').siblings().removeClass('pointer-active');
        
            sliderUl.animate({
                left: -sliderUl.find('> li').width() * ($('.pointer-active').index() + 1)
            }, sliderTime);
        
       sliderUl.find('> li').eq($('.pointer-active').index() + 1).addClass('slider-active').siblings('li').removeClass('slider-active');
        
    });
});

// Em An
// 4-2017

// https://www.facebook.com/groups/ElzeroWebSchool/permalink/1273846386077756/


$(document).ready(function() {
    $("#sidebarCollapse").on("click", function() {
      $("#sidebar").addClass("active");
    });
  
    $("#sidebarCollapseX").on("click", function() {
      $("#sidebar").removeClass("active");
    });
  
    $("#sidebarCollapse").on("click", function() {
      if ($("#sidebar").hasClass("active")) {
        $(".overlay").addClass("visible");
        console.log("it's working!");
      }
    });
  
    $("#sidebarCollapseX").on("click", function() {
      $(".overlay").removeClass("visible");
    });
  });
  // TOASTS 
 

  // jQuery MixItUp
	$('.product_item').mixItUp();

    