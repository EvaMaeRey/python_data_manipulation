1 + 1

life = pd.DataFrame(
{"states": ["NY", "CO", "IL", "MI"],
  "region": ["New England", "Mountain", "Midwest", "Midwest"],
"life_exp": [76, 77, 76, 20]
})

life

import pandas as pd



import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
plt.style.use('seaborn')

total_cases = pd.read_csv("https://covid.ourworldindata.org/data/total_cases.csv", index_col='date')  
total_cases[["France", "Italy"]].tail(3)  
cases100_France = total_cases.query("France > 100")["France"]  
days100_France = np.arange(len(cases100_France))  
cases100_Italy = total_cases.query("Italy > 100")["Italy"]  
days100_Italy = np.arange(len(cases100_Italy))
#Plot by Alonso Silva
fig, ax = plt.subplots(figsize = (10,7))  
plt.plot(days100_France, cases100_France,  
    label='France', linewidth = 2, marker='o')  
plt.plot(days100_Italy, cases100_Italy,  
    label='Italy',  linewidth = 2, marker='o')  
plt.plot(np.array([14, 15, 16, 17]),  
    np.array([6604, 7730, 9134, 10995]),  
    label='France (ESRI)', linewidth=2, marker='o')  
plt.axvline(9, color='green', linestyle='dashed')  
plt.annotate('Italy closes schools  \n and universities  -> ',  
    (3.5, 5000.0), color='green', fontsize='x-large')  
plt.axvline(13, color='green', linestyle='dashed')  
plt.annotate('Italy\n lockdown -> ',  
    (9.3, 8000.0), color='green', fontsize='x-large'  )  
plt.axvline(14, color='blue', linestyle='dashed')  
plt.annotate('<-  France closes schools\n       and universities',  
    (14.4, 3000), color='blue', fontsize='x-large')  
plt.axvline(15, color='darkred', linestyle='dashed')  
plt.annotate('<-  France lockdown', (15.2, 700),  
    color='darkred', fontsize='x-large')  
ax. set_title('COVID-19: Number of known cases vs number of days since 100 cases',  
    fontsize='x-large')  
ax.set_xlabel('number of days since 100 cases',  
    fontsize='x-large')  
ax.set_ylabel('number of known cases', fontsize = 'x-large')  
plt.legend(fontsize = 'x-large')  
plt.yscale("log"); plt.show() 
