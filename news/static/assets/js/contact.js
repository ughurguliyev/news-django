$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "type the correct answer -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "Please enter your name",
                    minlength: "Your name must consist of at least 2 characters"
                },
                subject: {
                    required: "Please enter subject",
                    minlength: "Your subject must consist of at least 4 characters"
                },
                number: {
                    required: "Please enter your name",
                    minlength: "Your number must consist of at least 5 characters"
                },
                email: {
                    required: "Please enter your email"
                },
                message: {
                    required: "Please enter your message to us",
                    minlength: "Thats all? :)"
                }
            }
        })
    })
        
 })(jQuery)
})