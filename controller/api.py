# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-
import json
from datetime import datetime, timedelta
from tornado.gen import coroutine, Return
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError

class APIHandler(RequestHandler):
	def initialize(self):
		self.client = AsyncHTTPClient()

	@coroutine
	def get(self):
		url = 'http://dev.machtalk.net/callAjax'
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie': 'Hm_lvt_a107a146f265a17619df50a3ffa2807a=1437708104,1437791351; JSESSIONID=81A83F35687A8B61B98B305908A65A5F; navselected=service; Hm_lpvt_a107a146f265a17619df50a3ffa2807a=1437791475; username=andysol; pwd=9f10fb4e1dd60c207421cb566bf1d8cf; autologon=1',
		}
		body1 = r'reqContext={"data":{"params":"{\"pageSize\":10000,\"start\":\"' + (datetime.now() - timedelta(hours=1)).isoformat() + r'\",\"end\":\"' + datetime.now().isoformat() + r'\"}"},"url":"/v1.0/device/4d1dab2993b6429b9c9c88c0097cb805/1/1/datapoints","headers":{},"method":"POST"}'
		body2 = r'reqContext={"data":{"params":"{\"pageSize\":10000,\"start\":\"' + (datetime.now() - timedelta(hours=1)).isoformat() + r'\",\"end\":\"' + datetime.now().isoformat() + r'\"}"},"url":"/v1.0/device/4d1dab2993b6429b9c9c88c0097cb805/2/1/datapoints","headers":{},"method":"POST"}'
		body3 = r'reqContext={"data":{"params":"{\"pageSize\":10000,\"start\":\"' + (datetime.now() - timedelta(hours=1)).isoformat() + r'\",\"end\":\"' + datetime.now().isoformat() + r'\"}"},"url":"/v1.0/device/4d1dab2993b6429b9c9c88c0097cb805/3/1/datapoints","headers":{},"method":"POST"}'

		try:
			batchRequest = []
			batchRequest.append(HTTPRequest(url, method='POST', headers=headers, body=body1))
			batchRequest.append(HTTPRequest(url, method='POST', headers=headers, body=body2))
			batchRequest.append(HTTPRequest(url, method='POST', headers=headers, body=body3))
			batchResponse = yield [self.client.fetch(req) for req in batchRequest]
			
			response = {
				'co2': json.loads(batchResponse[0].body)['data'][0]['value'],
				'harmful': json.loads(batchResponse[1].body)['data'][0]['value'],
				'smoke': json.loads(batchResponse[2].body)['data'][0]['value'],
			}
			self.write(response)
		except HTTPError as e:
			self.write(e)
