#!/usr/bin/env python

import os
import sys
from os import path
import time

import AnalysisProcessor


if __name__ == '__main__' :

	if len(sys.argv) < 2 :
		sys.exit('Error : too few arguments')


	runNumber = sys.argv[1]

	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Nov2012'
	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Oct2015/163'
	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Oct2015/214'
	#dir = '/home/garillot/files/DATA/TRIVENT/electrons'
	#dir = '/home/garillot/files/DATA/TRIVENT/thrScan'
	dir = '/home/garillot/files/DATA/TRIVENT/SPS_Sept2018'
	#dir = '/home/garillot/files/DATA/TRIVENT'
	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Apr2015'
	#dir = '/home/garillot/files/DATA/TRIVENT/test'

	print ('Searching files in ' + dir)

	#list files
	fileList = []

	for fileName in os.listdir(dir) :
		if runNumber in fileName :
			fileList.append(dir + '/' + fileName)

	print 'File List :'
	print fileList

	os.environ["MARLIN"] = '/home/garillot/ilcsoft/v01-19-05/Marlin/v01-15-02'
	os.environ["PATH"] = os.environ["MARLIN"] + '/bin:' + os.environ["PATH"]
	os.environ["MARLIN_DLL"] = '/home/garillot/SDHCALMarlinProcessor/lib/libsdhcalMarlin.so'

	a = AnalysisProcessor.Params()
	a.collectionName = 'SDHCAL_HIT'
	a.outputFileName = runNumber + '.root'
	a.runNumber = runNumber
	#a.maxRecordNumber = 5000

	AnalysisProcessor.launch(a , fileList)

  	#outputDir = '/home/garillot/files/DATA/Analysis/SPS_Oct2015/163Custom'
	outputDir = dir.replace('TRIVENT' , 'Analysis')

	os.system('mkdir -p '+ outputDir)
	os.system('mv ' + a.outputFileName + ' ' + outputDir)

