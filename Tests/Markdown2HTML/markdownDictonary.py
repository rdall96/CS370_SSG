#!/usr/bin/python

#----------------------------------------------------------------------
# Markdown Dictonary
# Author: Ricky Dall'Armellina
# Date: 09/3/2018
#
# Description: Python dictonary for reference Markdown to HTML
# Reference: https://www.markdowntutorial.com/
#----------------------------------------------------------------------

#import statement for main in same folder:
	#import markdownDictonary as Markdown 
#access dictonary like this
	#Markdown.dictonary.get('').get(''))

dictonary = {
	
	'#': {
		'openTag': '<h1>',
		'closeTag': "</h1>"
	},
	
	'##': {
		'openTag': '<h2>',
		'closeTag': '</h2>'
	},
	
	'###': {
		'openTag': '<h3>',
		'closeTag': '</h3>'
	},
	
	'####': {
		'openTag': '<h4>',
		'closeTag': '</h4>'
	},
	
	'#####': {
		'openTag': '<h5>',
		'closeTag': '</h5>'
	},
	
	'**': {
		'openTag': '<b>',
		'closeTag': '</b>'
	},
	
	'_': {
		'openTag': '<i>',
		'closeTag': '</i>'
	},
	
	'~~': {
		'openTag': '<s>',
		'closeTag': '</s>'
	},
	
	'>': {
		'openTag': '<q>',
		'closeTag': '</q>'
	},
	
	'*': {
		'sectionTagOpen': '<ul>',
		'sectionTagClose': '</ul>',
		'openTag': '<li>',
		'closeTag': '</li>'
	},
	
	# FIXME: Add links and images
}


#	'': {
#		'openTag': '',
#		'closeTag': ''
#	},