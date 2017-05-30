"""
  Copyright (C) 2016-2017 {Sabrina Amrouche} <{as_amrouche@esi.dz}>

  This file is subject to the terms and conditions defined in
  file 'LICENSE.txt', which is part of this source code package.
"""

from multiprocessing import Queue
from time import sleep,time
import glob
import os
import re
from datetime import datetime, date
from PyQt4.QtCore import QThread, SIGNAL
from PyQt4.QtCore import QTimer,QTime
import xlrd
import numpy as np
from sklearn.utils import shuffle
from sklearn.externals import joblib



"""
RaceSVM

Real time features extraction from Excel files, text raw data and prediction using an SVM pre built model. 
Data describes fast races read every 1/5 of a seconds.
Data loading and prediction are done in parallel using two separate threads.
"""

#Global algo

"""
1. Predictive model built/trained on excel files
2. Live prediction from LV1 file: extract features and feed them to model
3. Read on evening R files and retrain model.
4. Go to 2

GUI 
""" 
"""
1- Paths
	Path to learning workbook represents the directory of excel files on the top of which
	the model is first built. All the excel files in this directory will be part of building
	the predictive model.


	Path to prediction information file, represents the path+filename where the application stores 
	prediction details (id, name, BACK, probability..) under the name B1

	Path to training files (R files), Each evening the application will read these files and train
	the model on them.

2- Evening training triggered at the time indicated in the box.

3- Model live prediction
Start the live prediction from live file, reads the file every 1/5 sec and extract features
predict on model and writes to prediction files.
Stop button stops live prediction, the last predictions are still being written to disk.

4- Logs box
All messages from the application are written to the log screen as well as inside the log file.
The logs screen helps monitor the running of the application


5- Accuracy chart
After retraining model on evening, computes and plots the accuracy reached 
on the new recorded data.

"""

#A boolean reflecting the state of the model (true if learning, false if stopped by user)
stop=False

# ***************Parallel computing funcs ******************

#Reads file every 1/5 sec and puts features into a queue
class ReadLiveThread(QThread):
    def __init__(self, q,live_file,get_stop,upd):
        QThread.__init__(self)
        self.queue = q
        self.file=live_file
        self.get_stop=get_stop
        self.upd=upd
    def __del__(self):
        self.wait()
    def run(self):
    	features=[]
    	names=[]
    	while not get_stop():

            if os.stat(self.file).st_size != 0:
                
                f,names,N,row=Lv1tofeatures(self.file)
                
                self.queue.put([f,names,N,row])
        	self.upd.processEvents() 
                sleep(0.2)
 
            else:
                 
                 sleep(1)
                 
                 print "no data"

#Reads from a queue and makes predictions        
class PredictThread(QThread):
    def __init__(self, q,pred_proba,get_stop,upd):
        QThread.__init__(self)
        self.queue = q
        self.file=pred_proba
        self.get_stop=get_stop
        self.upd=upd
    def __del__(self):
        self.wait()
    def run(self):
    	clf=joblib.load('model/SVM/SVM_model.pkl')   	
    	while self.queue.empty():
            sleep(1)
        print "computing features.."
    	while not get_stop():
                        print "size", self.queue.qsize()
			s=self.queue.get()
			features=s[0]
			names=s[1]
			N=s[2]
			row=s[3]
			print "computing probabilities.."
			computeProba(features,names,self.file,clf,self,N,row)


# ***************************** Loading, parsing funcs *********************************
			

#Extracts features from an excel sheet 
def sheet2features(sheet,runner,Nbr=8,EndValues=[0,1000]):
	features=[]
	target=[]
	for h in runner:
		r=3
		inf=h*Nbr	
		while r < sheet.nrows:
				price=sheet.row(r)[inf+2].value
				#If the race is not over
				if price not in EndValues: 
					features.append([i.value for i in sheet.row(r)[inf+2:inf+5]])
					target.append(0 if sheet.row(r)[inf+6].value==-2 else 1)
				r+=1
	return features,target
  


#Loads all excel files in a directory	used for offline testing
def load_data(files):
	features=[]
	target=[]
	for f in files[:2]:
		workbook = xlrd.open_workbook(f)
		sheets=workbook.sheet_names()[1:]
		for sheet_name in  sheets:
			sheet= workbook.sheet_by_name(sheet_name)
			if sheet.nrows >0:
				num_horses=(sheet.ncols+1)/8
				x,y=sheet2features(sheet,[j for j in range(num_horses)])
				x,y=shuffle(x,y)
				features= features+x
				target=target+y
		
	return features,target
#Reads and transforms R files to features for LIVE PREDICTION
def Lv1tofeatures(filename):
	features=[]
	names=[]
	num_horse=0
	lines = [line.rstrip('\n') for line in open(filename,'r')]
    	if len([l.strip().split(",") for l in lines]) >0:
		row=[l.strip().split(",") for l in lines][-1]
		if len(row)>0:
			row=row[0]
	else:
		print "File format error : ->",row
	if len(lines)>1:
                       
            line=[l.strip().split(",")[1:] for l in lines]
            line=[line[-1]]
            
     

            for word in line[0]:
                   name=re.sub("[^\sa-zA-Z]+", "", word)
                   if name:
                         names.append(name)
            num_horse= len(names)         
            
            for j,l in zip(line,range(len(line))):
                    for i in range(3,6*num_horse+3,6):
                            if len(j[i:i+3])==3:
					for s in j[i:i+3]:
						if not isinstance(s,float) and not isinstance(s,int):
							print "Error of format in file at line:",l
                        		features.append(j[i:i+3])
                   
                        
            return features,names,num_horse,row
        else:
            return features,names,num_horse,row


#Reads files for offline prediction
#Reads records each evening from R1.txt and returns, ready for prediction, features
def readR(filename,EndValues=[0,1000]):
	features=[]
	target=[]
	names=[]
	lines = [line.rstrip('\n') for line in open(filename)]
	if lines:         
            #Extract winner name
            winner=lines[0].strip().split(",")[-1]
            winner=" ".join(winner.split())
            #Bypass first line
            lines=lines[1:]
            #Parse features
            line=[l.strip().split(",")[1:] for l in lines]
            #Learn num of horses
            for word in line[0]:
                   name=re.sub("[^\sa-zA-Z]+", "", word)
                   if name:
                         names.append(name)
            num_runners= len(names)
            
            #Build feature matrix each row 
            for j in line:
                    for i,n in zip(range(3,6*num_runners+3,6),range(0,6*num_runners,6)):
                            runnerName=j[n]
                            #Extract features
                            psa=[float(s) for s in j[i:i+3]]                                           
                            if psa[0] not in EndValues:
                                    if str(runnerName)==winner:
                                            target.append(1)
                                    else:
                                            target.append(0)				
                                    features.append(psa)
        return features,target            


# ********************Training, testing and prediction funcs ******************


# Offline test of the model
def test_model(model,X,y,p=0.7,NN=True):
	if NN==True:
		s=int(X.shape[1]*p)
		X_test = X[:,s:]
		y_test = y[s:]
		t2 = time()
		prediction = model(X_test)
		t3 = time()
		print 'Prediction time',t3-t2
		accuracy = np.mean((prediction > .5) == y_test)
		return accuracy
	else:
		s=int(len(X)*p)
		X_test = X[s:]
		y_test = y[s:]
		t2 = time()
		prediction = model.predict(X_test)
		t3 = time()
		print model.decision_function(X_test)
		print prediction[:100]
		print y_test
		print 'Prediction time',t3-t2
		accuracy = np.mean((prediction > .5) == y_test)
		print accuracy
		return accuracy




#Computes probabilities from predictions
def computeProba(f,names,pred_proba,clf,self,N,row):
	
        if len(f)>1:
		    clf=joblib.load('model/SVM/SVM_model.pkl')
		    prediction=clf.predict(f)
		    proba=clf.predict_proba(f)
		    prediction=list(prediction)
		    pred_runner=[prediction[i:i+N] for i in range(0,len(prediction),N)]
		    feature_runner=[f[i:i+N] for i in range(0,len(f),N)]
		    pred_runner=np.array(pred_runner)
		    if 1 in prediction:
		            print "prediction made"
		            for runners,pred_id in zip(pred_runner,range(len(pred_runner))):
		                    runners=np.array(runners)
		                    if 1 in runner:
		                            winners=list(np.where(runners==1)[0])
		                            print "writing predictions.."
		                            for y in winners: 
		                                print str(row)+','+str(names[y])+','+'BACK,'+str(round(proba[y][0],2))+','+str(feature_runner[pred_id][y][0])+'\n'
		                            with open(pred_proba, 'a') as b:
		                                for y in winners:
		                                    
		                                    b.write(str(row)+','+str(names[y])+','+'BACK,'+str(round(proba[y][0],2))+','+str(feature_runner[pred_id][y][0])+'\n')
		                                print "written"
                    else:
                    	print "no winner predicted for now"
                                

# Writes predictions to file  in the format
# id, name , "BACK", probability, price
def write_predictions(d,f,names,pred_proba,N):
	with open(pred_proba, 'a') as b:
		for i in d.keys():
			b.write(str(i)+','+str(names[i])+','+'BACK,'+str(d[i]/float(100))+','+str(f[-N+i][0])+'\n')

def live_prediction(self,live_file,pred_proba,get_stop,upd):

	q = Queue()
	self.read = ReadLiveThread(q,live_file,get_stop,upd)
	self.predict = PredictThread(q,pred_proba,get_stop,upd)
	self.connect(self.predict, SIGNAL("finished()"), self.over)
	
	self.read.start()
	self.predict.start()

def set_stop():
	global stop
	stop=True

def get_stop():
	return stop



# Offline training, predictions tests 
# From Excel files
def main(save=False):
	files= glob.glob("data/*/*/*.xlsm")
	features,target=load_data(files)
	#save matrix
	if save:
		features=np.save('features.npy',features)
		target=np.save('target.npy',target)

	features=np.load('features.npy')
	target=np.load('target.npy')[:5000]
	features=features[:5000]
	clf = joblib.load('model/SVM/SVM_model.pkl')
	test_model(clf,features,target,p=0.7,NN=False)
