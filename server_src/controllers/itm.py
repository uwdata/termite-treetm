#!/usr/bin/env python

import os
import json

def index():
	identifier = {
		'server_type' : 'itm',
		'server_version' : '0.1',
		'server_handlers' : [
			'TermTopicMatrix',
			'TermIndex',
			'TopicIndex',
			'TermTopicConstraints'
		]
	}
	return json.dumps( identifier, encoding = 'utf-8', indent = 2 )

def GetTermTopicMatrix():
	filename = os.path.join( request.folder, 'data', 'term-topic-matrix.txt' )
	with open( filename ) as f:
		content = [ [ float(value) for value in line.split('\t') ] for line in f.read().decode( 'utf-8' ).splitlines() ]
	return content

def GerTermIndex():
	filename = os.path.join( request.folder, 'data', 'term-index.txt' )
	with open( filename ) as f:
		content = f.read().decode( 'utf-8' ).splitlines()
	return content

def GetTopicIndex():
	filename = os.path.join( request.folder, 'data', 'topic-index.txt' )
	with open( filename ) as f:
		content = f.read().decode( 'utf-8' ).splitlines()
	return content

def GetTermTopicConstraints():
	return []

def TermTopicMatrix():
	data = {
		'content_type' : 'TermTopicMatrix',
		'content_version' : '0.1',
		'content' : GetTermTopicMatrix()
	}
	return json.dumps( data, encoding = 'utf-8' )

def TermIndex():
	data = {
		'content_type' : 'TermIndex',
		'content_version' : '0.1',
		'content' : GerTermIndex()
	}
	return json.dumps( data, encoding = 'utf-8' )

def TopicIndex():
	data = {
		'content_type' : 'TopicIndex',
		'content_version' : '0.1',
		'content' : GetTopicIndex()
	}
	return json.dumps( data, encoding = 'utf-8' )

def TermTopicConstraints():
	data = {
		'content_type' : 'TermTopicConstraints',
		'content_version' : '0.1',
		'content' : GetTermTopicConstraints()
	}
	return json.dumps( data, encoding = 'utf-8' )
