import pandas as pd
from bs4 import BeautifulSoup
import requests
import time 
import datetime 
import smtplib
import numpy as np 
dataset = pd.read_csv("country_vaccinations.csv")
asya1 =['AFG','ARM','AZE','BHR','BGD','BTN','BRN','KHM','CHN',
                      'CXR','CCK','IOT','GEO','HKG','IND','IDN','IRN','IRQ','ISR','JPN','JOR',
                      'KAZ','KWT','KGZ','LAO','LBN','MAC','MYS','MDV','MNG','MMR','NPL','PRK',
                      'OMN','PAK','PSE','PHL','QAT','SAU','SGP','KOR','LKA','SYR','TWN','TJK',
                      'THA','TUR','TKM','ARE','UZB','VNM','YEM']
avrupa = ['ALB','AND','AUT','BLR','BEL','BIH','BGR','HRV','CYP','CZE','DNK','EST','FRO','FIN','FRA','DEU','GIB','GRC',
          'HUN','ISL','IRL','IMN','ITA','XKX','LVA','LIE','LTU','LUX','MKD','MLT','MDA','MCO','MNE','NLD','NOR','POL',
          'PRT','ROU','RUS','SMR','SRB','SVK','SVN','ESP','SWE','CHE','UKR','GBR','VAT','RSB','OWID_ENG']
guneyamerika = ['ARG','BOL','BRA','CHL','COL','ECU','FLK','GUF','GUF','GUY','PRY','PER','SUR','URY','VEN']
kuzeyamerika =  ['AIA','ATG','ABW','BHS','BRB','BLZ','BMU','BES','VGB','CAN','CYM','CRI','CUB','CUW','DMA','DOM','SLV',
                 'GRL','GRD','GLP','GTM','HTI','HND','JAM','MTQ','MEX','SPM','MSR','ANT','KNA','NIC','PAN','PRI','BES',
                 'BES','SXM','KNA','LCA','SPM','VCT','TTO','TCA','USA','VIR']
afrika = ['DZA','AGO','SHN','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG','COD','DJI','EGY','GNQ','ERI',
          'SWZ','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY','MDG','MWI','MLI','MRT','MUS','MYT',
          'MAR','MOZ','NAM','NER','NGA','STP','REU','RWA','STP','SEN','SYC','SLE','SOM','ZAF','SSD','SHN','SDN','SWZ',
          'TZA','TGO','TUN','UGA','COD','ZMB','TZA','ZWE']
avusturalya = ['ASM','AUS','NZL','COK','TLS','FSM','FJI','PYF','GUM','KIR','MNP','MHL','UMI','NRU','NCL','NZL','NIU',
               'NFK','PLW','PNG','MNP','WSM','SLB','TKL','TON','TUV','VUT','UMI','WLF']

#in first step i did web scraping with excel to acces world countries and their iso code for comparing  and adding value by their continent i extract each continent 
#countries iso code and assigning them to pyhton list
#here is my source web link = https://www.countrycallingcodes.com/iso-country-codes/

dataset.insert(loc = 3,column = 'continent',value = '') #adding new column calling continent
y =0
for i in dataset["iso_code"]:
    if i in asya1:
            dataset["continent"].iloc[y]="Asia"
            y+=1
    elif  i in avrupa:
            dataset["continent"].iloc[y]= 'Europe'
            y+=1
    elif i in guneyamerika:
            dataset["continent"].iloc[y]='South America'
            y+=1
    elif i in kuzeyamerika:
            dataset["continent"].iloc[y]='North America'
            y+=1
    elif i in afrika:
            dataset["continent"].iloc[y]='Africa'
            y+=1
    elif i in avusturalya:
            dataset["continent"].iloc[y]='Ocenia'
            y+=1
 
 #comparing values from dataset with the list and adding new values to the list 
  #---------
  #updating & saving the excel file for further analysis
  with pd.ExcelWriter("Updated_Dataset.xlsx") as writer:
    dataset.to_excel(writer,sheet_name = "Sayfa1")
