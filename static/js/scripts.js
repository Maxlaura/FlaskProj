/*!
    * Start Bootstrap - SB Admin v6.0.1 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
(function ($) {
    "use strict";

    // Add active state to sidbar nav links
    let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function () {
        if (this.href === path) {
            $(this).addClass("active");
        }
    });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function (e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });

    $("form[name='userForm']").validate({
        // Specify validation rules
        rules: {
            name: "required",
            surname: "required",
            email: {
                required: true,
                email: true
            },
            country: "required",
            city: "required",
            address: "required",
            phone: {
                required: true,
                matches: "[0-9]+",
                minlength:10,
                maxlength:10
            }
        },
        // Specify validation error messages
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            email: "Please enter a valid email address",
            country: "Please select your country",
            city: "Please enter a valid city",
            address: "Please enter a correct address",
            phone: "Please enter a correct phone number"
        },
        submitHandler: function (form) {
            form.submit();
        }
    });

    $("form[name='appointmentForm']").validate({
        // Specify validation rules
        rules: {
            date: "required",
            hour: "required",
            cause: "required",
            description: "required"
        },
        // Specify validation error messages
        messages: {
            date: "Please enter the date",
            hour: "Please enter hours",
            cause: "Please enter a cause",
            description: "Please enter a description"
        },
        submitHandler: function (form) {
            form.submit();
        }
    });

})(jQuery);
