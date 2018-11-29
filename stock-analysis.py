from lxml import html  
import requests
from time import sleep
import json
import argparse
from collections import OrderedDict
from time import sleep

def parse(ticker):
	url = "http://finance.yahoo.com/quote/%s/key-statistics?p=%s"%(ticker,ticker)
	response = requests.get(url, verify=False)
	print ("Parsing %s"%(url))
	sleep(4)
	parser = html.fromstring(response.text)
	summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
	summary_data = OrderedDict()
	other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteKey-Statistics/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
	summary_json_response = requests.get(other_details_json_link)
	try:
		json_loaded_summary =  json.loads(summary_json_response.text)
		y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
		earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
		eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
		datelist = []
		for i in earnings_list['earningsDate']:
			datelist.append(i['fmt'])
		earnings_date = ' to '.join(datelist)
		for table_data in summary_table:
			raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
			raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
			table_key = ''.join(raw_table_key).strip()
			table_value = ''.join(raw_table_value).strip()
			summary_data.update({table_key:table_value})
		summary_data.update({'Return on Equity (TTM)':return_on_equity,'Operating Margin (TTM)':operating_margin,'Quarterly Earnings Growth (yoy)': quarterly_earnings_growth, 'ticker':ticker,'url':url})
		return summary_data
	except:
		print ("Failed to parse json response")
		return {"error":"Failed to parse json response"}
	
    url = "http://finance.yahoo.com/quote/%s/analysis?p=%s"%(ticker,ticker)
	response = requests.get(url, verify=False)
	print ("Parsing %s"%(url))
	sleep(4)
	parser = html.fromstring(response.text)
	summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
	summary_data = OrderedDict()
	other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteAnalysis/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
	summary_json_response = requests.get(other_details_json_link)
	try:
		json_loaded_summary =  json.loads(summary_json_response.text)
		y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
		earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
		eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
		datelist = []
		for i in earnings_list['earningsDate']:
			datelist.append(i['fmt'])
		earnings_date = ' to '.join(datelist)
		for table_data in summary_table:
			raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
			raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
			table_key = ''.join(raw_table_key).strip()
			table_value = ''.join(raw_table_value).strip()
			summary_data.update({table_key:table_value})
		summary_data.update({'Sales Growth (year/est)':sales_growth,'Surprise %': surprise, 'ticker':ticker,'url':url})
		return summary_data
	except:
		print ("Failed to parse json response")
		return {"error":"Failed to parse json response"}
	
	url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
	response = requests.get(url, verify=False)
	print ("Parsing %s"%(url))
	sleep(4)
	parser = html.fromstring(response.text)
	summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
	summary_data = OrderedDict()
	other_details_json_link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?formatted=true&lang=en-US&region=US&modules=summaryProfile%2CfinancialData%2CrecommendationTrend%2CupgradeDowngradeHistory%2Cearnings%2CdefaultKeyStatistics%2CcalendarEvents&corsDomain=finance.yahoo.com".format(ticker)
	summary_json_response = requests.get(other_details_json_link)
	try:
		json_loaded_summary =  json.loads(summary_json_response.text)
		y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
		earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
		eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
		datelist = []
		for i in earnings_list['earningsDate']:
			datelist.append(i['fmt'])
		earnings_date = ' to '.join(datelist)
		for table_data in summary_table:
			raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
			raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
			table_key = ''.join(raw_table_key).strip()
			table_value = ''.join(raw_table_value).strip()
			summary_data.update({table_key:table_value})
		summary_data.update({'PE Ratio (TTM)': pe_ratio, 'Beta (3y monthly)': beta, 'ticker':ticker,'url':url})
		return summary_data
	except:
		print ("Failed to parse json response")
		return {"error":"Failed to parse json response"}
if operating_margin > 15%
    print ("This stock's operating margin is good")
else:
    print ("This stock's operating margin isn't that good")
    
if return_on_equity > 18%
    print ("This stock's ROE,(Return On Equity) is good")
else:
    print ("This stock's ROE,(Return On Equity)is not good")

if quarterly_earnings_growth > 25%
    print ("This stock's Quarterly Earnings Growth is good")
else: 
    print ("This stock's Quarterly Earnings Growth is not good")
    
if sales_growth > 5.5%
    print ("This stock's sales growth is good")
else: 
    print ("This stock's sales growth is not good")

if suprise > 10%
    print ("This stock's earning suprise % is good")
else:
    print ("This stock's earning suprise % is not good")

if pe_ratio > 20, quarterly_earnings_growth < 15%
    print ("This stock is overvalued")

if pe_ratio > 20, quarterly_earnings_growth > 16%
    print ("This stock is at the correct price")

if pe_ratio < 15 
    print ("This stock may not be able to show high levels of growth")

if pe_ratio > 16
    print ("This stock may be able to show high levels of growth")

if beta < 1
    print ("This stock is less risky than the overall stock market but may have a lower return")

if beta > 1
    print("This stock is more risky than the overall stock market but may have the potential for higer returns")


if __name__=="__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('ticker',help = '')
	args = argparser.parse_args()
	ticker = args.ticker
	print ("Fetching data for %s"%(ticker))
	scraped_data = parse(ticker)
	print ("Writing data to output file")
	with open('%s-summary.json'%(ticker),'w') as fp:
		json.dump(scraped_data,fp,indent = 4)
