var fnSetAntiForgeryToken = function(element, _pData) {
    var token = null;
    if (element != null && element.length > 0) {
        token = $(element).closest('form').find('[name=__RequestVerificationToken]').val();
    }
    else {
        token = $('[name=__RequestVerificationToken]').val();
    }

    var data = _pData;
    data["__RequestVerificationToken"] = token;
    return data;
}

var _parentcountriesList = "";

//function test() {
//    var requestData = {
//        sortBy: "country-z-a"
//    };
//    $.ajax({
//        url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries',
//        method: "POST",
//        data: fnSetAntiForgeryToken(this, requestData),
//        success: function (data) {
//            //$("#parentcountries").empty();
//            //$("#parentcountries").html(data);
//        }
//    })
//}


var closeInfoBar = function(element) {
    $(element).closest('.su-cookie').hide();
    return false;
}

jQuery(document).ready(function() {


    //custom input handler function
    //$('.alphaonly').on('keyup blur', function () {
    //    var node = $(this);
    //    node.val(node.val().replace(/[^a-z]/g, ''));
    //});






    $('#homebanner .sliderWrap').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: true
    });

    $('.testimonial-slider-wrap .sliderWrap').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: true
    });

    $('.cont-det-slider-wrap .sliderWrap').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: true
    });

    $('.category-slider-wrap .sliderWrap').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: true
    });

    $('#about--section--8 .board_slider').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: true
    });

    $('#sponsor--project .sponsor-slider').slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: false
    });
    
    $("#img-popUp .sliderWrap").slick({
        autoplay: true,
        autoplaySpeed: 8000,
        dots: false
    });



    // Award Submission


    $('#award-submission #others').click(function() {
        $('#award-submission #other-data').toggle();
    });


    $('.project-state #proj--ready').click(function() {
        $('.project-state #proj-data').show();
    });

    $('.project-state #proj-no-ready').click(function() {
        $('.project-state #proj-data').hide();
    });

    $('#award-submission #passportfile').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })


    $('#award-submission #mainAppDoc1').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })



    $('#award-submission #mainAppDoc2').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })


    $('#award-submission #tradelicense').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })


    $('#award-submission #endorsementletter').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })


    $('#award-submission #coreteamstructure').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })


    $('#award-submission #videolinks').on('change', function() {
        var fileName = $(this).val();
        var updatedName = fileName.replace("C:\\fakepath\\", "");
        $(this).next('.custom-file-label').html(updatedName);
    })








    // FAQ Accordian JS

    $('.qt_title').click(function() {
        $(this).toggleClass('active');
        $(this).siblings('.qt_content').slideToggle();
    });



    //Home hover effect

    $('#home--section--6 .wid').mouseover(function() {
        $('#home--section--6 .wid').addClass('hoverSibs');
        $(this).removeClass('hoverSibs');
    });

    $('#home--section--6 .wid').mouseout(function() {
        $('#home--section--6 .wid').removeClass('hoverSibs');
    });

    //About hover effect

    $('#about--section--7 .wid').mouseover(function() {
        $('#about--section--7 .wid').addClass('hoverSibs');
        $(this).removeClass('hoverSibs');
    });

    $('#about--section--7 .wid').mouseout(function() {
        $('#about--section--7 .wid').removeClass('hoverSibs');
    });


    if (navigator.userAgent.match(/iPad/i) != null) {
        $('.menu-wrap').find('li').on('click', function(e) {
            e.preventDefault();
            $(this).trigger('hover');
        });
    };

    $('.hamMenu').click(function() {
        $(this).toggleClass('active');
        $('header .menu ul').slideToggle();

        var width = $(window).width();
        var mobileScreen = 960;
        if (width > mobileScreen) {
            $('header .menu .submenu').hide();
        };
    });


    // Menu - submenu expansion

    $('.subExpand').click(function() {
        $(this).siblings('ul').slideToggle();
        $(this).toggleClass('active');
    });


    $('.search-input').on('blur', function() {
        $(this).removeClass('active');
    }).on('focus', function() {
        $(this).addClass('active');
    });

    $(window).scroll(function() {
        var topspace = $(this).scrollTop();
        if (topspace > 600) {
            $("#scrolltop").fadeIn();
        } else {
            $("#scrolltop").fadeOut();
        }
    });


    $('#scrolltop').click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });


    // Contact Form js


    $('#contact-form .form-group input, #contact-form .form-group textarea').focus(function() {
        console.log(this);
        $(this).removeAttr('placeholder');
    });

    //    Promise jQuery

    $('.promise-types .col-sm-6:first-child p a').click(function() {
        $('#promise-popup-business').show();
    });

    $('.promise-types .col-sm-6:last-child p a').click(function() {
        $('#promise-popup-individual').show();
    });

    $('#promise-popup-business .close').click(function() {
        $('#promise-popup-business').hide();
    });

    $('#promise-popup-individual .close').click(function() {
        $('#promise-popup-individual').hide();
    });


    $('#video-popUp .close').click(function() {
        $('#video-popUp').hide();
    });

    $('#img-popUp .close').click(function() {
        $(this).parent().hide();
    });



    // Email Match Validation - Registration Page

    function checkEmailMatch() {
        var email = $("#UserModel_EmailAddress").val();
        var confirmemail = $("#UserModel_ConfirmEmailAddress").val();
        $("#UserModel_ConfirmEmailAddress").siblings('small').remove();
        if (email != confirmemail) {
            $("#UserModel_ConfirmEmailAddress").addClass('is-invalid');
            $("#UserModel_ConfirmEmailAddress").parent().append('<small id="" class="form-text error">Please enter same email</small>');
        }
        else {
            $("#UserModel_ConfirmEmailAddress").removeClass('is-invalid');
        }

    }


    $("#UserModel_EmailAddress").keyup(function() {
        if ($("#UserModel_ConfirmEmailAddress").val() != "") {
            checkEmailMatch();
        }
    });

    $("#UserModel_ConfirmEmailAddress").keyup(checkEmailMatch);


    // Password Match Validation - Registration Page

    function checkPasswordMatch() {
        var password = $("#UserModel_Password").val();
        var confirmPassword = $("#UserModel_ConfirmPassword").val();
        $("#UserModel_ConfirmPassword").siblings('small').remove();

        if (password != confirmPassword) {
            $("#UserModel_ConfirmPassword").addClass('is-invalid');
            $("#UserModel_ConfirmPassword").parent().append('<small id="" class="form-text error">Your password do not match</small>');
        }
        else {
            $("#UserModel_ConfirmPassword").removeClass('is-invalid');
        }
    }

    $("#UserModel_Password").keyup(function() {
        if ($("#UserModel_ConfirmPassword").val() != "") {
            checkPasswordMatch();
        }
    });

    $("#UserModel_ConfirmPassword").keyup(checkPasswordMatch);



    // Popup Slider

    //$('#content--top .initiatives .initiative p.viewMore a.img-slideUp').click(function() {

    //    var popId = $(this).attr("href");
    //    console.log('h');
    //    $('#img-slideUp').show();
    //});


    var bullet = $('.ar-fix ul.slick-dots li'),
        bulWidth = 0;

    for (var i = 0; i < bullet.length; i++) {
        bulWidth += bullet[i].offsetWidth + 12;
        $('.ar-fix ul.slick-dots').css('width', bulWidth)
        }


    // Popup year of zayeed

    $('#content--top .initiatives .initiative p.viewMore a').click(function() {
        event.preventDefault();
        var popId = $(this).attr("href");
        console.log(popId);
        $('#img-popUp.' + popId).show();
    });

    // Country Ajax
    $(document).on('click', '#country-z-a', function() {

        var requestData = {
            sortBy: "country-z-a"
        };
        $.ajax({
            url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries',
            method: "POST",
            data: fnSetAntiForgeryToken(this, requestData),
            //headers: requestData ,
            success: function(data) {
                $("#parentcountries").empty();
                $("#parentcountries").html(data);
            },
            error: function (error) {
                $("#parentcountries").html(_parentcountriesList);
            }
        })
    });

    $(document).on('click', '#country-a-z', function() {
        var requestData = {
            sortBy: "country-a-z"
        };
        $.ajax({
            url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries',
            method: "POST",
            data: fnSetAntiForgeryToken(this, requestData),
            //headers: fnSetAntiForgeryToken(this, requestData),
            success: function(data) {
                $("#parentcountries").empty();
                $("#parentcountries").html(data);
            } ,error: function (error) {
                $("#parentcountries").html(_parentcountriesList);
            }
        })
    });

    $(document).on('click', '#solutions-a-z', function() {
        var requestData = {
            sortBy: "solutions-a-z"
        };
        $.ajax({
            url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries',
            method: "POST",
            data: fnSetAntiForgeryToken(this, requestData),
            success: function(data) {
                $("#parentcountries").empty();
                $("#parentcountries").html(data);
            }, error: function (error) {
                $("#parentcountries").html(_parentcountriesList);
            }
        })
    });

    $(document).on('click', '#solutions-z-a', function() {
        var requestData = {
            sortBy: "solutions-z-a"
        };
        $.ajax({
            url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries',
            method: "POST",
            data: fnSetAntiForgeryToken(this, requestData),
            success: function(data) {
                $("#parentcountries").empty();
                $("#parentcountries").html(data);
            }, error: function (error) {
                $("#parentcountries").html(_parentcountriesList);
            }
        })
    });

    $(document).on('click', '#lifes-a-z', function() {
        var requestData = {
            sortBy: "lifes-a-z"
        };
        $.ajax({
            url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries',
            method: "POST",
            data: fnSetAntiForgeryToken(this, requestData),
            success: function(data) {
                $("#parentcountries").empty();
                $("#parentcountries").html(data);
            }, error: function (error) {
                $("#parentcountries").html(_parentcountriesList);
            }
        })
    });

    $(document).on('click', '#lifes-z-a', function() {
        var requestData = {
            sortBy: "lifes-z-a"
        };
        $.ajax({
            url: '/api/sitecore/ListOfCountries/GetSortedListOfCountries?sortBy=lifes-z-a',
            method: "POST",
            data: fnSetAntiForgeryToken(this, requestData),
            success: function(data) {
                $("#parentcountries").empty();
                $("#parentcountries").html(data);
            }, error: function (error) {
                $("#parentcountries").html(_parentcountriesList);
            }
        })
    });




    //  Country List Sorting


    $(document).on('click', '.country-list .main_title span small', function() {
        // $('.country-list .main_title span small').removeClass('active');
        $(this).toggleClass('active');

        // $('#country_list_page .sortDropDown').slideToggle();
        $(this).parent().parent().siblings('.sortDropDown').slideToggle();

    });

    $(document).on('click', '.main_title .sortDropDown .field-wrap input', function () {
        _parentcountriesList = $("#parentcountries").html();
        $(this).parent().parent().parent().slideUp();
        $(this).parent().parent().parent().siblings('p').children().find('span small').toggleClass('active');
    });



    $("#resources .grid .resource .photos .res-in-inv").click(function() {
        $('#img-popUp').show();
        // alert('resource-inner img clicked');
    });


    $("#resources .grid .resource .videos .res-in-inv").click(function() {
        $('#video-popUp').show();
        // alert('resource-inner img clicked');
    });


        

     



    $('.userDiv').click(function() {
        if($(this).hasClass('logged')){
        $('.userDivDropDown').slideToggle();
        }
    });

    $('.userDivDropDown li a').click(function() {
        $('.userDivDropDown').slideToggle();
    });



    // Award Video popup

    var vid = document.getElementById("award_video");

    $('.about-award .video_wrap img').click(function() {
        $('.video_wrap video').show();
        vid.play();
    });






    //Global passport program - flip sliderWrap

    $('.flip-slider.global-pass-prog').flipster({
        style: 'carousel',
        style: 'flat',
        spacing: -0.25,
        nav: true,
        buttons: true,
    });

    //  $('.impact-in-country .flip-slider').flipster({
    //      style: 'carousel',
    //      style: 'flat',
    //         spacing: -0.25,
    //     nav: true,
    //        buttons: true,
    //  });

    //   $('.meet-winners .flip-slider').flipster({
    //      style: 'carousel',
    //      style: 'flat',
    //         spacing: -0.25,
    //     nav: true,
    //        buttons: true,
    //  });



    // Number Count Animation


    $('.acheived .data .nums .number.country').each(function() {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 2000,
            easing: 'swing',
            step: function(now) {
                $(this).text(Math.ceil(now));
            }
        });
    });



    $('.acheived .data .nums .number.solution').each(function() {
        var $this = $(this),
            countTo = $this.attr('data-count');

        $({
            countNum: $this.text()
        }).animate({
            countNum: countTo
        }, {
            duration: 2000,
            easing: 'swing',
            step: function() {
                $this.text(commaSeparateNumber(Math.floor(this.countNum)));
            },
            complete: function() {
                $this.text(commaSeparateNumber(this.countNum));
                //alert('finished');
            }
        });

    });

    $('.acheived .data .nums .number.lives').each(function() {
        var $this = $(this),
            countTo = $this.attr('data-count');

        $({
            countNum: $this.text()
        }).animate({
            countNum: countTo
        }, {
            duration: 2000,
            easing: 'swing',
            step: function() {
                $this.text(commaSeparateNumber(Math.floor(this.countNum)));
            },
            complete: function() {
                $this.text(commaSeparateNumber(this.countNum));
                //alert('finished');
            }
        });

    });

    function commaSeparateNumber(val) {
        while (/(\d+)(\d{3})/.test(val.toString())) {
            val = val.toString().replace(/(\d+)(\d{3})/, '$1' + ',' + '$2');
        }
        return val;
    }



    // Map Scripts

    $('.map .country').mouseenter(function() {
        $('.map .country .pin').removeClass('active');
        $('.map .country .popOut').slideUp();
        $(this).children().find('.pin').toggleClass('active');
        $(this).children().find('.popOut').slideToggle();
    });

    $('.map .country').mouseleave(function() {
        $('.map .country .pin').removeClass('active');
        $('.map .country .popOut').slideUp();
        $(this).children().find('.pin').remove('active');
        $(this).children().find('.popOut').slideUp();
    });



    $('.toggleWrap .mapView').click(function() {
        $('.toggleWrap .listView').toggleClass('active');
        $(this).toggleClass('active');

        $('.map-wrap .map').show();
        $('.map-wrap .country-list').hide();


    });
    $('.toggleWrap .listView').click(function() {
        $('.toggleWrap .mapView').toggleClass('active');
        $(this).toggleClass('active');

        $('.map-wrap .map').hide();
        $('.map-wrap .country-list').show();
    });


    //  Login Register Toggle

    $('#login-register .registerGo').click(function() {
        $('#login-register .login-container').slideUp();
        $('#login-register .register-container').slideDown();
    });

    $('#login-register .loginGo').click(function() {
        $('#login-register .login-container').slideDown();
        $('#login-register .register-container').slideUp();
    });



    // Filter JS



    filterSelection("all")

    function filterSelection(c) {
        var x, i;
        x = document.getElementsByClassName("resource");

        if (c == "all") c = "";
        for (i = 0; i < x.length; i++) {
            removeClass(x[i], "show");
            if (x[i].className.indexOf(c) > -1) addClass(x[i], "show");
        }
    }

    // Show filtered elements
    function addClass(element, name) {
        var i, arr1, arr2;
        arr1 = element.className.split(" ");
        arr2 = name.split(" ");
        for (i = 0; i < arr2.length; i++) {
            if (arr1.indexOf(arr2[i]) == -1) {
                element.className += " " + arr2[i];
            }
        }
    }

    // Hide elements that are not selected
    function removeClass(element, name) {
        var i, arr1, arr2;
        arr1 = element.className.split(" ");
        arr2 = name.split(" ");
        for (i = 0; i < arr2.length; i++) {
            while (arr1.indexOf(arr2[i]) > -1) {
                arr1.splice(arr1.indexOf(arr2[i]), 1);
            }
        }
        element.className = arr1.join(" ");
    }

    // Add active class to the current control button (highlight it)

    $('#filter .btn').click(function() {
        $('#filter .btn').removeClass('active');
        $(this).addClass('active');
    });


    $('#resources nav .nav-tabs a').click(function() {
        $('#resources #filter li').removeClass('active');
        $('#resources #filter li.all-button').addClass('active');

        filterSelection('all');

    });







    $('#resources #filter li.all-button').click(function() {
        filterSelection('all');
    });

    $('#resources #filter li.cat1-button').click(function() {
        filterSelection('cat1');
    });

    $('#resources #filter li.cat2-button').click(function() {
        filterSelection('cat2');
    });

    $('#resources #filter li.cat3-button').click(function() {
        filterSelection('cat3');
    });

    $('#resources #filter li.cat4-button').click(function() {
        filterSelection('cat4');
    });





    // Donation - Real Time Amount Display
    $('#customAmount').on("keyup", function() {
        // alert(inputBox.value);
        var _amount = $(this).val();
        $('.custom-amount-disp span big').text(_amount);
        $('#otherAmount').val(_amount);
    });


    // Donation - Custom Amount JS


    $('.one-time-donate-box .form-radio input').click(function() {
        $(".form-group.custom-amount-field").hide();
        $(".form-group.custom-amount-field input").removeAttr("required");
    });

    $('#otherAmount').click(function() {
        $(".form-group.custom-amount-field input").attr("required", "required");
        var realVal = document.getElementById("otherAmount").value;
        $(".form-group.custom-amount-field").show();

    });



    // why water animation

    $('.why-water-icon img').addClass("hidden").viewportChecker({
        classToAdd: 'visible  animated slideInDown',
        repeat: true,
    });




    // Custom Select box

    //$('.custom-select').select2(); // select2 js is not included
    var finalWidth = parseInt($(".masterWrap").width() * 0.8);
    var finalHeight = parseInt($(".masterWrap").height() * 0.25);
    finalHeight = parseInt((finalWidth * 9) / 16);


    function SliderHeightSetter() {
        finalWidth = parseInt($(".masterWrap").width() * 0.8);
        finalHeight = parseInt($(".masterWrap").height() * 0.25);
        finalHeight = parseInt((finalWidth * 9) / 16);
    }

    setTimeout(function () {
        SliderHeightSetter();
        UtubeVideoResponsive();
        ImageItemResponsive();
        $(window).trigger("resize");
    }, 1000);

    $(window).on("resize", function () {
        SliderHeightSetter();
        UtubeVideoResponsive();
        ImageItemResponsive();
        //$(window).trigger("resize");
    })

    
    function UtubeVideoResponsive() {
        if ($(".utube") != undefined && $(".utube").length > 0) {
            $(".utube").css("width", parseInt(finalWidth) + "px");
            $(".utube").css("height", parseInt(finalHeight) + "px");
        }
    }


    function ImageItemResponsive() {
        if ($(".imageItem") != undefined && $(".imageItem").length > 0) {
            $(".imageItem").each(function (i, o) {
                var img = $("img")[0];
                var pic_real_width = $(o)[0].naturalHeight;
                var pic_real_height = $(o)[0].naturalWidth;

                console.log("pic_real_width :" + pic_real_width)
                console.log("pic_real_height :" + pic_real_height)
                //$(o).attr("src", $(img).attr("src"))
                //    .load(function () {
                //        pic_real_width = this.width;   // Note: $(this).width() will not
                //        pic_real_height = this.height; // work for in memory images.
                //    });

                $(o).css("max-height", parseInt(finalHeight + 5) + "px");
                $(o).css("height", parseInt(finalHeight) + "px");
                $(o).css("min-height", parseInt(finalHeight) + "px");

                var _finalWidth = ((finalHeight * pic_real_height) / pic_real_width);

                $(o).css("max-width", parseInt(_finalWidth + 5) + "px");
                $(o).css("width", parseInt(_finalWidth) + "px");
                $(o).css("min-width", parseInt(_finalWidth) + "px");
            });

        }
        
    }

    $("._navlink").click(function () {
      var  IS_IPAD = navigator.userAgent.match(/iPad/i) != null;
      var  IS_IPHONE = (navigator.userAgent.match(/iPhone/i) != null) || (navigator.userAgent.match(/iPod/i) != null);
        if (IS_IPAD || IS_IPHONE) {
            var _url = $(this).attr("href");
            var _target = $(this).attr("target");
            if (_target != "_blank") {
                window.location = _url;
            } else {
                window.open(_url, '_blank');
            }

        }

    })

});



