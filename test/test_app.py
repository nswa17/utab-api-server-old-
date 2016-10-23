# -*- coding: utf-8 -*-
import os
import sys
import cherrypy
from threading import Thread
import json

from subprocess import check_output

from unittest import TestCase
from nose.tools import eq_, ok_

API_VERSION = 'v0.1'
JSON_FOLDER = 'jsons'

path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, path)
from app import *

def send_data(path, api_version=API_VERSION, address='localhost', port=8080, json_file_name=None, errors=None, method='GET'):
	url = address+':'+str(port)+'/'+api_version+'/'+path
	if json_file_name is None:
		output = check_output("http "+method+" "+url, shell=True)
	else:
		output = check_output("http "+method+" "+url+" < "+JSON_FOLDER+'/'+json_file_name, shell=True)
	try:
		ret_val = json.loads(output.decode('utf-8'))
		return ret_val
	except:
		return output.decode('utf-8')

"""
class test1(TestCase):
	def setUp(self):
		th = threading.Thread(target=run, kwargs={"host":'localhost', "port":8080, "debug":True, "server":'cherrypy'})
		th.setDaemon(True)
		th.start()
		#th = threading.Thread(target=run, kwargs={"host":'localhost', "port":8080, "debug":True, "server":'cherrypy'})
		#th.setDaemon(True)
		#style = {"style_name": "ACADEMIC", "debater_num_per_team":4, "team_num":2, "score_weights":[1, 1, 1, 1], "replies":[], "num_of_replies":0}
		#t = Tournament(1, "testtournament", 4, style)

	def tearDown(self):
		pass

	def test_create_tournament_callback(self):
		with open('create_tournament_response.json') as data_file:    
			data = json.load(data_file)

		output = send_data('tournaments', json_file_name='create_tournament.json', method='POST')
		eq_(output, data)

	def test_xbit(self):
		pass
"""

if __name__ == '__main__':
		th = Thread(target=run, kwargs={"host":'localhost', "port":8080, "debug":True, "server":'cherrypy'})
		th.setDaemon(True)
		th.start()

		print(send_data('tournaments', json_file_name='create_tournament.json', method='POST'))
		print(send_data('testtournament/institutions/0', json_file_name='add_institution1.json', method='POST'))
		print(send_data('testtournament/institutions/1', json_file_name='add_institution2.json', method='POST'))
		print(send_data('testtournament/institutions/2', json_file_name='add_institution3.json', method='POST'))
		"""
		t3 = Thread(target=send_data, kwargs={'path':'testtournament/speakers/1', 'json_file_name':'add_debater1.json', 'method':'POST'})
		t4 = Thread(target=send_data, kwargs={'path':'testtournament/speakers/2', 'json_file_name':'add_debater2.json', 'method':'POST'})
		t5 = Thread(target=send_data, kwargs={'path':'testtournament/speakers/3', 'json_file_name':'add_debater3.json', 'method':'POST'})
		t6 = Thread(target=send_data, kwargs={'path':'testtournament/speakers/4', 'json_file_name':'add_debater4.json', 'method':'POST'})
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		"""
		print(send_data('testtournament/speakers/0', json_file_name='add_debater1.json', method='POST'))
		print(send_data('testtournament/speakers/1', json_file_name='add_debater2.json', method='POST'))
		print(send_data('testtournament/speakers/2', json_file_name='add_debater3.json', method='POST'))
		print(send_data('testtournament/speakers/3', json_file_name='add_debater4.json', method='POST'))
		

		print(send_data('testtournament/teams/0', json_file_name='add_team1.json', method='POST'))
		print(send_data('testtournament/teams/1', json_file_name='add_team2.json', method='POST'))
		print(send_data('testtournament/adjudicators/0', json_file_name='add_adjudicator1.json', method='POST'))
		print(send_data('testtournament/adjudicators/1', json_file_name='add_adjudicator2.json', method='POST'))
		print(send_data('testtournament/adjudicators/2', json_file_name='add_adjudicator3.json', method='POST'))
		print(send_data('testtournament/venues/0', json_file_name='add_venue1.json', method='POST'))
		print(send_data('testtournament', json_file_name='set_judge_criterion.json', method='PUT'))

		for round_num in range(1, 3):
			print(send_data('testtournament/'+str(round_num), json_file_name='send_round_config.json', method='PUT'))
			
			"""
			t3 = Thread(target=send_data, kwargs={'path':'testtournament/0/suggested_team_allocations', 'json_file_name':'get_suggested_team_allocations.json', 'method':'POST'})
			t4 = Thread(target=send_data, kwargs={'path':'testtournament/0/suggested_team_allocations', 'json_file_name':'get_suggested_team_allocations.json', 'method':'POST'})
			t5 = Thread(target=send_data, kwargs={'path':'testtournament/0/suggested_team_allocations', 'json_file_name':'get_suggested_team_allocations.json', 'method':'POST'})
			t3.start()
			t4.start()
			t5.start()	
			"""
			print(send_data(path='testtournament/'+str(round_num)+'/suggested_team_allocations', json_file_name='get_suggested_team_allocations.json', method='POST'))
			print(send_data(path='testtournament/'+str(round_num)+'/suggested_team_allocations/0', json_file_name='confirm_team_allocation.json', method='POST'))
			print(send_data(path='testtournament/'+str(round_num)+'/suggested_adjudicator_allocations'))
			print(send_data(path='testtournament/'+str(round_num)+'/suggested_adjudicator_allocations/0', json_file_name='confirm_adjudicator_allocation.json', method='POST'))
			print(send_data(path='testtournament/'+str(round_num)+'/suggested_venue_allocation'))
			print(send_data(path='testtournament/'+str(round_num)+'/suggested_venue_allocation', json_file_name='confirm_venue_allocation.json', method='POST'))

			print(send_data(path='testtournament/'+str(round_num)+'/results/speakers', json_file_name='send_speaker_result1.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num)+'/results/speakers', json_file_name='send_speaker_result2.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num)+'/results/speakers', json_file_name='send_speaker_result3.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num)+'/results/speakers', json_file_name='send_speaker_result4.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num)+'/results/adjudicators', json_file_name='send_adjudicator_result1.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num)+'/results/adjudicators', json_file_name='send_adjudicator_result2.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num)+'/results/adjudicators', json_file_name='send_adjudicator_result3.json', method='PUT'))
			print(send_data(path='testtournament/'+str(round_num), json_file_name='finish_round.json', method='POST'))
			print(send_data(path='testtournament/results/teams', json_file_name='finish_round.json'))
			print(send_data(path='testtournament/results/speakers', json_file_name='finish_round.json'))
			print(send_data(path='testtournament/results/adjudicators', json_file_name='finish_round.json'))


