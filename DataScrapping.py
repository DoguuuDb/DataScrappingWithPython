import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


driverPath = r"C:\\chromedriver.exe"
browser=webdriver.Chrome(driverPath)


url = "https://www.worldometers.info/world-population/population-by-country/"
browser.get(url)
time.sleep(5)
browser.maximize_window()

#Scrape data from table
country=browser.find_elements(By.XPATH,'//*[@id="example2"]/tbody/tr/td[2]/a') #Country data
Population=browser.find_elements(By.XPATH,'//*[@id="example2"]/tbody/tr/td[3]') #Population data
Yearly_Change=browser.find_elements(By.XPATH,'//*[@id="example2"]/tbody/tr/td[4]') #Yearly Change data
Net_Change=browser.find_elements(By.XPATH,'//*[@id="example2"]/tbody/tr/td[5]') # Net Change data


#append table data to total_result
total_result=[]
for i in range(len(Yearly_Change)):
    #Create temp data
    temp_data={'Ülke':country[i].text,
               'Nüfus':Population[i].text,
               'Yıllık Değişim':Yearly_Change[i].text,
               'Net Değişim':Net_Change[i].text}
    total_result.append(temp_data) #Append Data --> total_result


#write data to excel with ExcelWriter
Excel_Url=r'D:/PythonProjects/PyautoGui/Data.xlsx'
df_data = pd.DataFrame(total_result)
with pd.ExcelWriter(Excel_Url) as writer:
    df_data.to_excel(writer,sheet_name='Sheet1',index=False)