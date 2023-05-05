import matplotlib.pyplot as plt
import numpy as np
import itertools

#bimodal
#no error
x = [4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16]
y = [0.7801340404242333, 0.7779191228990232, 0.7661710985344001, 0.7805168918614375, 0.8047362222532133, 0.8090382634028493, 0.8303109103645095, 0.8434726216149862, 0.8485005957528943, 0.8485043076089337, 0.8466250479227128, 0.8466250479227128, 0.8466250479227128]
y_porcentage=[]

for i in range(0, len(y)):
    y_porcentage.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage)
plt.plot(x,y_porcentage)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Bimodal Predictor Performance')
plt.show()

#with error
x = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = [0.7636072665414887, 0.7600942599327942, 0.7669797528858355, 0.7817608938997767, 0.7846550810801926, 0.791341724602553, 0.8007671876168241,0.8025022151826577, 0.8012576828791701, 0.8000062571287521, 0.8017423452248827, 0.8018627154135882, 0.8017338609825071]
y_porcentage_error=[]




for i in range(0, len(y)):
    y_porcentage_error.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage_error)
plt.plot(x,y_porcentage_error)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Bimodal Predictor Performance with error injection')
plt.show()


#both
#no error
x = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = [0.7801340404242333, 0.7779191228990232, 0.7661710985344001, 0.7805168918614375, 0.8047362222532133, 0.8090382634028493, 0.8303109103645095, 0.8434726216149862, 0.8485005957528943, 0.8485043076089337, 0.8466250479227128, 0.8466250479227128, 0.8466250479227128]
y_porcentage=[]

for i in range(0, len(y)):
    y_porcentage.append(round(y[i]*100,2))

#error
y = [0.7636072665414887, 0.7600942599327942, 0.7669797528858355, 0.7817608938997767, 0.7846550810801926, 0.791341724602553, 0.8007671876168241,0.8025022151826577, 0.8012576828791701, 0.8000062571287521, 0.8017423452248827, 0.8018627154135882, 0.8017338609825071]
y_porcentage_error=[]

for i in range(0, len(y)):
    y_porcentage_error.append(round(y[i]*100,2))



plt.scatter(x,y_porcentage)
plt.scatter(x,y_porcentage_error)
plt.plot(x,y_porcentage)
plt.plot(x,y_porcentage_error)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Bimodal Predictor Performance')
plt.legend(["no error", "with error"], loc ="lower right")
plt.show()





#gshare---------------------------------------------------------------------------------------------
#no error
x = [4, 5, 6, 7, 8, 9 ,10 ,11,12,13,14,15,16]
y = [0.72248,0.7142,0.6935,0.7052006814967688, 0.7142936682629415, 0.7275524180355903,0.7250877456254451, 0.7293431234420147, 0.7336902371292717, 0.7788, 0.7653, 0.778, 0.7988]
y_porcentage=[]

for i in range(0, len(y)):
    y_porcentage.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage)
plt.plot(x,y_porcentage)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Gshare Predictor Performance')
plt.show()

#with error
x = [4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16]
y = [0.7148987007973597, 0.7027036629125661, 0.6954178197724208,0.7023764893159526, 0.7115765896421188, 0.7251020627844541, 0.7333938189112702, 0.7424141593521009, 0.7545211732222463, 0.8009146013281021, 0.8011712496599674, 0.8012216248490733, 0.8023457869638555]
y_porcentage_error=[]

for i in range(0, len(y)):
    y_porcentage_error.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage_error)
plt.plot(x,y_porcentage_error)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Gshare Predictor Performance with error injection')
plt.show()


#both
x = [4, 5, 6, 7, 8, 9 ,10 ,11,12,13,14,15,16]
y = [0.72248,0.7142,0.6935,0.7052006814967688, 0.7142936682629415, 0.7275524180355903,0.7250877456254451, 0.7293431234420147, 0.7336902371292717, 0.7788, 0.7653, 0.778, 0.7988]
y_porcentage=[]

for i in range(0, len(y)):
    y_porcentage.append(round(y[i]*100,2))

y = [0.7148987007973597, 0.7027036629125661, 0.6954178197724208,0.7023764893159526, 0.7115765896421188, 0.7251020627844541, 0.7333938189112702, 0.7424141593521009, 0.7545211732222463, 0.8009146013281021, 0.8011712496599674, 0.8012216248490733, 0.8023457869638555]
y_porcentage_error=[]

for i in range(0, len(y)):
    y_porcentage_error.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage)
plt.scatter(x,y_porcentage_error)
plt.plot(x,y_porcentage)
plt.plot(x,y_porcentage_error)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Gshare Predictor Performance')
plt.legend(["no error", "with error"], loc ="lower right")
plt.show()





#tage--------------------------------------------------------------------------------------
#no error
x=[4,5,6,7,8,9,10,11,12,13,14,15,16]
y=[0.7524247575242475,0.7677,0.7575,0.7762,0.777922207779222,0.7894,0.792,0.7968,0.8278,0.8441,0.8577,0.8679,0.873012698730127]
y_porcentage=[]

for i in range(0, len(y)):
    y_porcentage.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage)
plt.plot(x,y_porcentage)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Tage Predictor Performance')
plt.show()

#with error
x=[4,5,6,7,8,9,10,11,12,13,14,15,16]
y=[0.8061247575242475, 0.8313, 0.7752, 0.8035, 0.8422222077792221, 0.831, 0.8310000000000001, 0.864, 0.8622, 0.9190999999999999, 0.9118, 0.8964, 0.912912698730127]
y_porcentage_error=[]

for i in range(0, len(y)):
    y_porcentage_error.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage_error)
plt.plot(x,y_porcentage_error)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Tage Predictor Performance with error injection')
plt.show()


#both
x = [4, 5, 6, 7, 8, 9 ,10 ,11,12,13,14,15,16]
y=[0.7524247575242475,0.7677,0.7575,0.7762,0.777922207779222,0.7894,0.792,0.7968,0.8278,0.8441,0.8577,0.8679,0.873012698730127]
y_porcentage=[]

for i in range(0, len(y)):
    y_porcentage.append(round(y[i]*100,2))

y=[0.8061247575242475, 0.8313, 0.7752, 0.8035, 0.8422222077792221, 0.831, 0.8310000000000001, 0.864, 0.8622, 0.9190999999999999, 0.9118, 0.8964, 0.912912698730127]
y_porcentage_error=[]

for i in range(0, len(y)):
    y_porcentage_error.append(round(y[i]*100,2))

plt.scatter(x,y_porcentage)
plt.scatter(x,y_porcentage_error)
plt.plot(x,y_porcentage)
plt.plot(x,y_porcentage_error)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Tage Predictor Performance')
plt.legend(["no error", "with error"], loc ="lower right")
plt.show()



#Mix all 3 -----------------------------------------------------------------------------------------------

x = [4, 5, 6, 7, 8, 9 ,10 ,11,12,13,14,15,16]
bimodal_no=[0.7801340404242333, 0.7779191228990232, 0.7661710985344001, 0.7805168918614375, 0.8047362222532133, 0.8090382634028493, 0.8303109103645095, 0.8434726216149862, 0.8485005957528943, 0.8485043076089337, 0.8466250479227128, 0.8466250479227128, 0.8466250479227128]
gshare_no=[0.72248,0.7142,0.6935,0.7052006814967688, 0.7142936682629415, 0.7275524180355903,0.7250877456254451, 0.7293431234420147, 0.7336902371292717, 0.7788, 0.7653, 0.778, 0.7988]
tage_no=[0.7524247575242475,0.7677,0.7575,0.7762,0.777922207779222,0.7894,0.792,0.7968,0.8278,0.8441,0.8577,0.8679,0.873012698730127]


for i in range(0, len(bimodal_no)):
    bimodal_no[i]=(round(bimodal_no[i]*100,2))
    gshare_no[i]=(round(gshare_no[i]*100,2))
    tage_no[i]=(round(tage_no[i]*100,2))



plt.scatter(x,bimodal_no)
plt.scatter(x,gshare_no)
plt.scatter(x,tage_no)
plt.plot(x,bimodal_no)
plt.plot(x,gshare_no)
plt.plot(x,tage_no)
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')
plt.title('Predictors Performance')
plt.legend(["bimodal", "gshare","tage"], loc ="lower right")
plt.show()





#bars no error
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [0.7801340404242333, 0.8047362222532133, 0.8466250479227128]
ECE = [0.72248, 0.7142936682629415,0.7988]
CSE = [0.7524247575242475, 0.7677, 0.7575]
 
# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, IT, color ='rosybrown', width = barWidth,
        edgecolor ='grey', label ='bimodal')
plt.bar(br2, ECE, color ='darkgoldenrod', width = barWidth,
        edgecolor ='grey', label ='gshare')
plt.bar(br3, CSE, color ='darkred', width = barWidth,
        edgecolor ='grey', label ='tage')
 
# Adding Xticks
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy (%)')

plt.xticks([r + barWidth for r in range(len(IT))],
        ['4', '8', '16'])
 
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()



#bar with error
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [0.7636072665414887,0.7846550810801926,0.8017338609825071]
ECE = [0.7148987007973597,0.7115765896421188,0.8023457869638555]
CSE = [0.8061247575242475, 0.8422222077792221, 0.912912698730127]
 
# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, IT, color ='rosybrown', width = barWidth,
        edgecolor ='grey', label ='bimodal')
plt.bar(br2, ECE, color ='darkgoldenrod', width = barWidth,
        edgecolor ='grey', label ='gshare')
plt.bar(br3, CSE, color ='darkred', width = barWidth,
        edgecolor ='grey', label ='tage')
 
# Adding Xticks
plt.xlabel('Pattern History table size (bits)')
plt.ylabel('Conditional Branch Prediction Accuracy with error injection (%)')

plt.xticks([r + barWidth for r in range(len(IT))],
        ['4', '8', '16'])
 
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()