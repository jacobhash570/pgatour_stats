from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from IPython.display import HTML


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    return browser

def scrape():
    browser=init_browser()
    stats_dict={}

    url = 'https://www.pgatour.com/stats.html'
    browser.visit(url)
    html = browser.html
    bsoup = bs(html,"html.parser") 

    results = bsoup.find_all("div", class_="module-statistics-overview-table clearfix")
    table_urls = []
    for div in results:
        link = div.find('div', class_= "clearfix")
        href = link.find('a')['href']   
        table_name = div.find('div', class_= "table-header")
        title = table_name.find('h3').text.strip('\n')    
        table_url = 'https://www.pgatour.com' + href
        table_urls.append({"title":title, "table_url":table_url})

    dataframes = []
    for url in table_urls:    
            facts_url = url['table_url']
            browser.visit(facts_url)
            facts_table = pd.read_html(facts_url, index_col=0)
            facts_df = facts_table[1]
            pd.set_option('colheader_justify', 'center')
            #facts_df.rename( columns={0 :'RANK THIs WEEK'}, inplace=True )
            fact_table = facts_df.to_html(col_space=2, justify='center', max_rows=6)
            title = url['title']
        #facts_df = facts_df.set_index("RANK THIS WEEK")
            dataframes.append({"title":title,"dataframes":fact_table})
        
            stats_dict={"dataframe":dataframes} 
    browser.quit()
    return stats_dict