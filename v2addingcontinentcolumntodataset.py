#IN THIS CODE ALGORİTHM GİVİNG TRUE VALUES OF THE CONTİNENTS V1 was have some issues but this version is fixed :)
import pandas as pd 
dataset = pd.read_csv("country_vaccinations.csv")
asya1 =['AFG','ARM','AZE','BHR','BGD','BTN','BRN','KHM','CHN','CXR','CCK','IOT','GEO','HKG','IND','IDN','IRN','IRQ','ISR','JPN','JOR','KAZ','KWT','KGZ','LAO','LBN','MAC','MYS','MDV','MNG','MMR','NPL','PRK','OMN','PAK','PSE','PHL','QAT','SAU','SGP','KOR','LKA','SYR','TWN','TJK','THA','TUR','TKM','ARE','UZB','VNM','YEM']
avrupa = ['ALB','AND','AUT','BLR','BEL','BIH','BGR','HRV','CYP','CZE','DNK','EST','FRO','FIN','FRA','DEU','GIB','GRC','HUN','ISL','IRL','IMN','ITA','XKX','LVA','LIE','LTU','LUX','MKD','MLT','MDA','MCO','MNE','NLD','NOR','POL','PRT','ROU','RUS','SMR','SRB','SVK','SVN','ESP','SWE','CHE','UKR','GBR','VAT','RSB','OWID_ENG']
guneyamerika = ['ARG','BOL','BRA','CHL','COL','ECU','FLK','GUF','GUF','GUY','PRY','PER','SUR','URY','VEN']
kuzeyamerika =  ['AIA','ATG','ABW','BHS','BRB','BLZ','BMU','BES','VGB','CAN','CYM','CRI','CUB','CUW','DMA','DOM','SLV','GRL','GRD','GLP','GTM','HTI','HND','JAM','MTQ','MEX','SPM','MSR','ANT','KNA','NIC','PAN','PRI','BES','BES','SXM','KNA','LCA','SPM','VCT','TTO','TCA','USA','VIR']
afrika = ['DZA','AGO','SHN','BEN','BWA','BFA','BDI','CMR','CPV','CAF','TCD','COM','COG','COD','DJI','EGY','GNQ','ERI','SWZ','ETH','GAB','GMB','GHA','GIN','GNB','CIV','KEN','LSO','LBR','LBY','MDG','MWI','MLI','MRT','MUS','MYT','MAR','MOZ','NAM','NER','NGA','STP','REU','RWA','STP','SEN','SYC','SLE','SOM','ZAF','SSD','SHN','SDN','SWZ','TZA','TGO','TUN','UGA','COD','ZMB','TZA','ZWE']
avusturalya = ['ASM','AUS','NZL','COK','TLS','FSM','FJI','PYF','GUM','KIR','MNP','MHL','UMI','NRU','NCL','NZL','NIU','NFK','PLW','PNG','MNP','WSM','SLB','TKL','TON','TUV','VUT','UMI','WLF']
sasya1 =pd.Series(asya1)
savrupa=pd.Series(avrupa)
sguneyamerika=pd.Series(guneyamerika)
skuzeyamerika=pd.Series(kuzeyamerika)
safrika=pd.Series(afrika)
savusturalya=pd.Series(avusturalya)
def GetContinent(iso_code):
    if sasya1.str.contains(iso_code).any():
        return 'Asia'
    elif savrupa.str.contains(iso_code).any():
        return 'Europe'
    elif sguneyamerika.str.contains(iso_code).any():
        return 'North America'
    elif skuzeyamerika.str.contains(iso_code).any():
        return 'South America'
    elif safrika.str.contains(iso_code).any():
        return 'Africa'
    elif savusturalya.str.contains(iso_code).any():
        return 'Ocenia'
dataset["continent"]=dataset["iso_code"].apply(GetContinent)


with pd.ExcelWriter("finaldataset.xlsx") as writer:
    dataset.to_excel(writer,sheet_name = "Sayfa1")
