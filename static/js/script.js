// some scripts

// jquery ready start
$(document).ready(function() {
	// jQuery code


    /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE, 
    For sliders, interactions and other

    */ ///////////////////////////////////////
    

	//////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name='+ check_attr_name +']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if




    
}); 


setTimeout(function() {
    const alerts = document.querySelectorAll('.alert-message');
    alerts.forEach(function(alert) {
        alert.style.transition = "opacity 0.6s ease";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 6000); // Remove after fade completes
    });
}, 3000);

// jquery end
//timeout for message 
// setTimeout(function() {
//     $('#alert-message').fadeOut('slow');
// }, 3000); // <-- time in milliseconds


// $(document).ready(function() {
//     // Select by class to catch all messages
//     setTimeout(function() {
//         $(".alert-message").fadeTo(500, 0).slideUp(500, function(){
//             $(this).remove(); // Removes the element from the page entirely
//         });
//     }, 3000); 
// });



