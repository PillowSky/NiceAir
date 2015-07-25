'use strict'
$ ->
	$('#panel').enhanceWithin().panel()

	data = {
		labels : ["二氧化碳","有害气体","烟雾"],
		datasets : [
			{
				fillColor : "rgba(148,235,225,0.5)",
				strokeColor : "rgba(148,235,225,1)",
				data : [65, 48, 32]
			}
		]
	}
	new Chart(document.querySelector('#stat').getContext('2d')).Bar(data);