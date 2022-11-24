#SAME DATA ANALYSİS WİTH LESS CODE WE CAN SAY İTS OPTİMİZED ONE
import pandas as pd
import numpy as np
import panel as pn
pn.extension('tabulator')
from  panel.interact import interact 
pn.extension()
import hvplot.pandas
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
import matplotlib.pyplot as plt 
%matplotlib inline
from pandas_datareader import data
import datetime as dt
dataset =pd.read_csv("Weekly_Datas_Uruguay.csv")

deneme = pn.widgets.DiscreteSlider(name='Discrete Slider', options=['2021-02-27', '2021-03-06', '2021-03-13', '2021-03-20',
               '2021-03-27', '2021-04-03', '2021-04-10', '2021-04-17',
               '2021-04-24', '2021-05-01', '2021-05-08', '2021-05-15',
               '2021-05-22', '2021-05-29', '2021-06-05', '2021-06-12',
               '2021-06-19', '2021-06-26', '2021-07-03', '2021-07-10',
               '2021-07-17', '2021-07-24', '2021-07-31', '2021-08-07',
               '2021-08-14', '2021-08-21', '2021-08-28', '2021-09-04',
               '2021-09-11', '2021-09-18', '2021-09-25', '2021-10-02',
               '2021-10-09', '2021-10-16', '2021-10-23', '2021-10-30',
               '2021-11-06', '2021-11-13', '2021-11-20', '2021-11-27',
               '2021-12-04', '2021-12-11', '2021-12-18', '2021-12-25',
               '2022-01-01', '2022-01-08', '2022-01-15', '2022-01-22',
               '2022-01-29', '2022-02-05', '2022-02-12', '2022-02-19',
               '2022-02-26', '2022-03-05', '2022-03-12', '2022-03-19',
               '2022-03-26'])
#--------------------------------------------------------------------------------------------------------------------------------------
#its isnt working cause when i trying to equalize the values beetwen table weeks values and datatime range slider ones 
#it doesnt work cause this function only support milisecond value for the step as you can see in the code and output will be like this
#27 Feb 2021 00:00:00 .. 29 May 2021 00:00:00 and on weeks data i cannot add the 00:00:00 on the week values 
deneme2 = pn.widgets.DatetimeRangeSlider(
    name='Datetime Range Slider',
    start=dt.date(2021,2,27), end=dt.date(2022,3,26),
    step=604800000
)
deneme2
###------------------------------------------------------------------------------------------------------------------------------------------
 #DATA PİPELİNE
  dataset.head()
idf = dataset.interactive()
pipeline=(
idf[
    idf.Weeks == deneme
]
    .sort_values(by= 'İndex')
    .reset_index(drop=True)
)
#------------------------------------
plot =dataset.hvplot.bar( x = "Weeks",y="Weekly_Rate",tittle = "Weekly Rate Of Vaccine Rates Uruguay",
                     stacked = True ,root =90 , width= 800,frame_width = 1500,rot = 80,color = "red" )
plot

frame_width = 4500, rot =80
###------------------------------------------------------------------------------------------------------------------------------------------
#scatter_plot  = pipeline.hvplot(x = "Weeks",y = "Weekly_Rate",size = 60,
#                                kind ='', legend = False , height = 500,width =500)
#scatter_plot
bar_plot = pipeline.hvplot (kind = "bar",
                            x ='Weeks',
                            y= 'Weekly_Rate',
                            title = "Weekly Rate Of Vaccine Rates Uruguay",
                            color = "green",
                            
                            
                              )
bar_plot
