

		$('.js-text').on('input', function () {
			$('.answer').empty();
		});

		$('.js-search').on('click', function (){
			var search_text = $('.js-text').val();
			
				$.get(URL + '&name' = search_text, function (data) {
					$('.answer').html(search_text + ' has ' + data + ' friends');
					// YOUR RESPONSE.
				});	


		})