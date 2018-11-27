jQuery(document).ready(function($) {
	'use strict';

	$('#contact-form').submit(function(e) {
			e.preventDefault();
			var $form = $(this),
				$messageSuccess = $('#contactSuccess'),
				$messageError = $('#contactError'),
				$submitButton = $(this.submitButton);

        $submitButton.button('loading');


			// Ajax Submit
			$.ajax({
				type: 'POST',
				url: $form.attr('action'),
				data: {
					name: $form.find('#id_name').val(),
					email: $form.find('#id_email').val(),
					subject: $form.find('#id_subject').val(),
					message: $form.find('#id_message').val(),
					recaptcha: $form.attr("data-sitekey"),
					csrfmiddlewaretoken: $form.attr("data-csrf-token")
				},
				dataType: 'json',
				complete: function(data) {
					console.log(data);
					if (typeof data.responseJSON === 'object') {
						if ('success' in data.responseJSON ){

							$messageSuccess.removeClass('hidden');
							$messageError.addClass('hidden');

							// Reset Form
							$form.find('.controled')
								.val('')
								.blur()
								.parent()
								.removeClass('has-success')
								.removeClass('has-error')
								.find('label.error')
								.remove();

              $form.find('.controled').removeClass('error');

 							if (($messageSuccess.offset().top - 80) < $(window).scrollTop()) {
								$('html, body').animate({
									scrollTop: $messageSuccess.offset().top - 80
								}, 300);
							}

							$submitButton.button('reset');

              $('.controled').keyup(function(){
                $messageSuccess.addClass('hidden');
              });

							return;

						}
					}

					$messageError.removeClass('hidden');
					$messageSuccess.addClass('hidden');

          // Reset Form
							$form.find('.controled')
								.val('')
								.blur()
								.parent()
								.removeClass('has-success')
								.removeClass('has-error')
								.find('label.error')
								.remove();

					if (($messageError.offset().top - 80) < $(window).scrollTop()) {
						$('html, body').animate({
							scrollTop: $messageError.offset().top - 80
						}, 300);
					}

					$form.find('.has-success').removeClass('has-success');

					$submitButton.button('reset');

          $('.controled').keyup(function(){
            $messageError.addClass('hidden');
          });

				}
			});
		});
});
