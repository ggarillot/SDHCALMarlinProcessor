#!/usr/bin/env python


import os
import sys
from os import path
import time

sys.path.insert(0 , '/home/garillot/SDHCALMarlinProcessor/script')

import EfficiencyProcessor


if __name__ == '__main__' :

	if len(sys.argv) < 2 :
		sys.exit('Error : too few arguments')

	runNumber = sys.argv[1]

	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Oct2015/163'
	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Oct2015/214'
	#dir = '/home/garillot/files/DATA/TRIVENT/electrons'
	#dir = '/home/garillot/files/DATA/TRIVENT'
	#dir = '/home/garillot/files/DATA/TRIVENT/H2Sept2017'
	#dir = '/home/garillot/files/DATA/TRIVENT/SPS_Apr2015'
	#dir = '/home/garillot/files/DATA/TRIVENT/thrScan'
	dir = '/home/garillot/files/DATA/TRIVENT/SPS_Sept2018'
	
	print ('Searching files in ' + dir)

	#list files
	fileList = []

	for fileName in os.listdir(dir) :
		if runNumber in fileName :
			fileList.append(dir + '/' + fileName)


	thr = '320-233-288'
	runList = [743847,743848,743849,743850,743851,743853]
	fileList = []
	for run in runList :
		fileList.append(dir + '/TDHCAL_' + str(run) + '.slcio')


	#fileList = [ inputFilePath ]
	print 'Filelist : '
	print fileList


	os.environ["MARLIN"] = '/home/garillot/ilcsoft/v01-19-05/Marlin/v01-15-02'
	os.environ["PATH"] = os.environ["MARLIN"] + '/bin:' + os.environ["PATH"]
	os.environ["MARLIN_DLL"] = '/home/garillot/SDHCALMarlinProcessor/lib/libsdhcalMarlin.so'


	a = EfficiencyProcessor.Params()
	a.collectionName = 'SDHCAL_HIT'

	if len(sys.argv) > 2 :
		a.geometry = sys.argv[2]

	a.outputFileName = 'Eff_' + runNumber + '.root'
	a.outputFileName = 'Eff_' + thr + '.root'

	EfficiencyProcessor.launch(a , fileList)


#	outputDir = '/home/garillot/files/MultiplicityMap/DATA/H2Sept2017'
	outputDir = dir.replace('DATA/TRIVENT' , 'MultiplicityMap/DATA')

	os.system('mkdir -p ' + outputDir)
	os.system('mv ' + a.outputFileName + ' ' + outputDir + '/' + a.outputFileName)
