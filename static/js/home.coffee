'use strict'
$ ->
	$('#panel').enhanceWithin().panel()

	setInterval ->
		$.get '/api/', (result)->
			console.log(result)
			data = {
				labels : ["二氧化碳","有害气体","烟雾"],
				datasets : [
					{
						fillColor : "rgba(148,235,225,0.5)",
						strokeColor : "rgba(148,235,225,1)",
						data : [result.co2, result.harmful*10, result.smoke]
					}
				]
			}
			console.log((result.co2 - 1400)/1400.0)
			score = 60 - ((result.co2 - 1400)/1400 * 18) - ((result.harmful-90)/90 * 18) - ((result.smoke - 2800)/2800 * 18)
			$('p.center.score').text(Math.floor(score))
			console.log(score)
			new Chart(document.querySelector('#stat').getContext('2d')).Bar(data)
	, 10000
