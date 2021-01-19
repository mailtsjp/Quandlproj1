import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import quandl
from matplotlib.font_manager import FontProperties

print ("Defining instruments ...")

#print plt.style.available

plt.style.use('ggplot')

fig=plt.figure()
ax1=fig.add_subplot(111)

debtarray = []

# Countries ISO codes: https://s3.amazonaws.com/quandl-static-content/API+Descriptions/WHO/ccodes.txt
debtarray.append("ODA/USA_GGXWDN_NGDP")
debtarray.append("ODA/JPN_GGXWDN_NGDP")
debtarray.append("ODA/ITA_GGXWDN_NGDP")
debtarray.append("ODA/FRA_GGXWDN_NGDP")
debtarray.append("ODA/ESP_GGXWDN_NGDP")
debtarray.append("ODA/GBR_GGXWDN_NGDP")
debtarray.append("ODA/GRC_GGXWDN_NGDP")
debtarray.append("ODA/IRL_GGXWDN_NGDP")
debtarray.append("ODA/DEU_GGXWDN_NGDP")
debtarray.append("ODA/CHE_GGXWDN_NGDP")
debtarray.append("ODA/CAN_GGXWDN_NGDP")
debtarray.append("ODA/BEL_GGXWDN_NGDP")
#debtarray.append("ODA/NOR_GGXWDN_NGDP")
debtarray.append("ODA/SWE_GGXWDN_NGDP")
debtarray.append("ODA/DEN_GGXWDN_NGDP")

print ("Retrieving data ...")

series = quandl.get(debtarray,authtoken="shAvzzwDvkzzDq93Kzyy",trim_start="2000-01-01", trim_end="2016-11-01",collapse="annual")

print ("Plotting ...")

# https://www.quandl.com/collections/economics/net-debt-as-share-of-gdp-oda-by-country

for i in range(len(debtarray)):
    try:
        dateaxis = series.reset_index()['Date']
        plt.plot(dateaxis, series.ix[:,i], label=debtarray[i][4:-12], marker='.')
        ax1.annotate(debtarray[i][4:-12], xy=(dateaxis[i], series.ix[:,i][i]), rotation=0)
    except Exception as e:
        print ("error at ") + debtarray[i]
        pass

plt.xlabel("Year")
plt.ylabel("% of GDP")

myFont = FontProperties()
myFont.set_size('xx-small')

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0., numpoints = 1)
legend = ax1.legend(bbox_to_anchor=(0, 0, 1, 1), loc=0, ncol=1,
           prop = myFont,fancybox=True,shadow=False,title='Debt as % of GDP')
plt.setp(legend.get_title(),fontsize='xx-small')
plt.show()