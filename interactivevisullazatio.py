import pandas as pd
import numpy as np
import hvplot.pandas
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
import panel as pn
pn.extension('tabulator')
pn.extension('plotly')
pn.extension('tabulator')
from  panel.interact import interact 
pn.extension()

dataset = pd.read_csv(("finaldataset.csv"),low_memory = False)
pip show panel bokeh holoviews pandas

date_slider = pn.widgets.DateSlider(name='Date Slider', start=dt.date(2021,2,22), end=dt.date(2022, 3, 29))
date_slider

select = pn.widgets.Select(name='Seçiniz', options=['Africa', 'Asia', 'Europe','North America','Ocenia','South America'],value = ("Asia"))
select

checkbutton_group = pn.widgets.CheckButtonGroup(name='Check Button Group', options=['Asia','Europe' ,'Africa' ,'South America', 'North America' ,'Ocenia'])

checkbutton_group
discrete_slider2 = pn.widgets.DiscreteSlider(name = "Tarih",options = ['2021-06-30','2021-07-01'])

idf = dataset.interactive()

idf2 = dataset.interactive()

pipeline1 =  (
    idf[
        (select == idf.continent)&
        (idf.date == discrete_slider2)
        
        ]
    .groupby(["date",'continent',"country"])["daily_vaccinations"].sum()
    
    
    
)
pipeline1

pipeline3 =  (
    idf[
        (idf.date == discrete_slider2)
        
        
        ]
    .groupby(["date",'continent'])["daily_vaccinations"].sum()
)
pipeline3


scatter_plot2  = pipeline1.hvplot.scatter(x = "continent",by = "continent",y= "daily_vaccinations",datashade = True,dynspread = True , hover = True,
                                 height = 500,width =500,alpha = 200,rot =100)
scatter_plot2

 bar_plot = pipeline1.hvplot (kind = "scatter",
                            x =['continent',"country"],
                            y= 'daily_vaccinations',
                            title = "World Vaccine Rates",
                            stacked = False,
                              dynamic = False
                              )
bar_plot

bar  = pipeline3.hvplot(kind = "bar",x = "continent",y = "daily_vaccinations",
                                 width = 600,height = 600,rot = 90,size = 150,colorbar= True,
                                 c= 'daily_vaccinations',cmap = 'Wistia'
                                )

bar


template = pn.template.FastListTemplate(
    title = "Dünya Pandemi Verileri",
    sidebar =[ pn.pane.Markdown("Pandemi"),
              pn.pane.Markdown("----DÜNYA PANDEMİ VERİLERİNİN DİNAMİK ANALİZİ---"),
              pn.pane.PNG('abc.png',sizing_mode = 'scale_both'),
              pn.pane.Markdown('Ayarlar'),
              discrete_slider2,select],
    main = [pn.Row(pn.Column(bar.panel(width = 700),margin = (0.25)),
            pn.Row(pn.Column(scatter_plot.panel(width=500),margin = (0.25))))],
    accent_base_color = '#88d8b0',
    header_background = "#88d8b0"
)

template.servable();
template.config
