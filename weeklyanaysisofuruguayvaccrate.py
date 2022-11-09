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
dataset =pd.read_csv("country_vaccinations.csv")

# EXTRACT THE WEEK DATAS FROM DATASET 
weekly_uruguay = pd.date_range(start ="2/27/2021",end = "3/29/2022",freq ="7D")
sweekly_uruguay = pd.Series(weekly_uruguay)
sweekly2_uruguay = pd.DataFrame(sweekly_uruguay)
sweekly2_uruguay.head()
# EXTRACT THE SUM OF 7 DAYS  İN SAME ROW WİTH A FUNCTİON 
result =[]
def calculating_sumofnumbers_byweeks(i):
    x = 0
    y = 8
    i = 0
    for i in range (57):
        df3=df2["daily_vaccinations"].iloc[x:y].sum()
        x+=7
        y+=7
        print(df3)
        result.append(df3)
        print (result)  
# SELECTİNG ONLY THE COUNTRY  URUGUAY FROM DATASET 
df1 = dataset[["country","date","daily_vaccinations"]]
df2 = df1[df1["country"]=="Uruguay"]
#MAKİNG A DİSTRECETE SLİDER FOR WEEK DATES İTS SEPERATE FROM EACHOTHER 
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
#RENAMİNG COLUMN AND MAKİNG İT PERMANENT
sweeklyn2_uruguay.rename(columns={0:'Weekly_Rate'},inplace=True)  # changing empty column name
sweeklyn2_uruguay.index.name = "İndex" #setting index name 
sweekly2_uruguay.rename(columns={0:"Weeks"},inplace=True)
sweekly2_uruguay.index.name = "İndex"
sweeklyn2_uruguay.info
sweekly2_uruguay.head()
sweeklyn2_uruguay.head()
final_data=sweekly2_uruguay.merge(sweeklyn2_uruguay,how = "inner", on ="İndex")
#RENAMİNG COLUMN AND MAKİNG İT PERMANENT
idf = final_data.interactive()
final_data.head(58)
#MAKİNG A DATA PİPELİNE FOR THE SLİDER 
country = ["Uruguay"]
pipeline = (
    idf[
        (idf.Weeks<= deneme)
    ]
    .groupby(['Weeks','Weekly_Rate'])
)
#GRAPH 
#plot
scatter = hv.Scatter( data =final_data , kdims = "Weeks",vdims = "Weekly_Rate" )
scatter.opts(line_color = 'blue',width= 700)
#link
#deneme.jslink(scatter , value= 'glyph.Weeks')
#layout
pn.Row(scatter,deneme)
#OTHER VERSİON OF GRAPH
#select = pn.widgets.Select(name = "Week Select",options = deneme2)
def create_plot(symbol):
    return final_data[final_data["Weeks"]] == symbol.hvplot('Weeks')
#
#interact(create_plot,symbol= deneme)
interact(create_plot,symbol= deneme)
