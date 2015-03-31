$(document).ready(function() {
    /* Creation of additional elements
    ================================================== */
    $('.section').wrapInner('<article class="contents"></article>');
    $('.section').append('<div class="half-pattern left"><div class="rotate"></div></div><div class="half-pattern right"><div class="rotate"></div></div>');
    $('.next-section').wrapInner('<span></span>');
    $('h2,h3').wrapInner('<div class="headline"></div>');
    $('.headline').append('<div class="pattern-left"><span class="icon-polygon"></span></div><div class="pattern-right"><span class="icon-polygon"></span></div>');
    $('.grid .item div.wow').wrapInner('<div class="rotate-left"></div>').wrapInner('<div class="rotate-right"></div>').wrapInner('<div class="filter-item"></div>');
    $('.vertical-separator').wrapInner('<span></span>');
    $('.vertical-separator').each(function(i) {
        var height = $(this).parents(".row").height();
        $('span', this).css('height', height - 50);
    });
    $('.entry-meta-details span').append('<div class="line-decoration hidden-xs"></div>');
    $('.progress-bar').each(function(i) {
        var value = $(this).data('value');
        $('span', this).css('width', value+'%');
    });

    /* Up arrow when scrolling
    ================================================== */
    var offset = 220;
    var duration = 500;
    $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
            $('.back-to-top').fadeIn(duration);
        } else {
            $('.back-to-top').fadeOut(duration);
        }
    });

    $('.back-to-top').on( "click", function(event) {
        event.preventDefault();
        $('html, body').animate({scrollTop: 0}, duration);
        return false;
    });

    /* initialize shuffle plugin (jquery.shuffle.min.js)
    ================================================== */
    var $grid = $('.grid');

    $grid.shuffle({
        itemSelector: '.item' // the selector for the items in the grid
    });

    $('.filter a').on( "click", function(event) {

        event.preventDefault();
        $('.filter a').removeClass('active');
        $(this).addClass('active');
        var groupName = $(this).attr('data-group');
        $grid.shuffle('shuffle', groupName);

    });

    /* Decorative line in the blog post
    ================================================== */
    $(window).load(function() {
        $('.entry-meta-details').each(function(i) {
            var width = $(this).width();
            var width_details = $('span', this).width();
            var width_comments = $('.entry-comments').width();
            $('.line-decoration', this).css('width', width - width_details - width_comments - 10);
        });
    });


    /* WOW plugin triggers animation.css on scroll
    ================================================== */
    new WOW({
        boxClass: 'wow', // animated element css class (default is wow)
        offset: 0, // distance to the element when triggering the animation (default is 0)
        mobile: false // trigger animations on mobile devices (true is default)
    }).init();

    $("#home-slider").owlCarousel({
        slideSpeed : 300,
        paginationSpeed : 400,
        pagination: true,
        singleItem: true,
        autoPlay: 3000,
        stopOnHover: true,
        mouseDrag: true,
    })

    $("#events").owlCarousel({
        slideSpeed : 300,
        paginationSpeed : 400,
        pagination: true,
        singleItem: true,
        autoPlay: 10000,
        stopOnHover: true,
        mouseDrag: true,
    });

});
