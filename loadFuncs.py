"""
  Copyright (C) 2016-2017 <{greyback7@gmail.com}>

  This file is subject to the terms and conditions defined in
  file 'LICENSE.txt', which is part of this source code package.
"""
import re

#Extracts features from an excel sheet 
def readSheet(sheet,runner,Nbr=8,EndValues=[0,1000]):
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
  
#Reads and transforms text files to features for LIVE PREDICTION
def readLive(filename):
	features=[]
	names=[]
	num_runners=0
  #Parse lines
	lines = [line.rstrip('\n') for line in open(filename,'r')]    
	if len(lines)>1:                     
            line=[l.strip().split(",")[1:] for l in lines]
            line=[line[-1]]
            #retreive runners names from first line
            for word in line[0]:
                   name=re.sub("[^\sa-zA-Z]+", "", word)
                   if name:
                         names.append(name)
            num_runners= len(names)
              
            for j in line:
                    for i in range(3,6*num_runners+3,6):                            
                            features.append(j[i:i+3])                 
            return features,names,num_runners
        else:
            return features,names,num_runners

#Read files for offline prediction
def readOffline(filename,EndValues=[0,1000]):
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
