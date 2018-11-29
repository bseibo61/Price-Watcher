from __future__ import print_function
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import Row
from pyspark.ml.feature import CountVectorizer
from operator import add
from pyspark.sql.window import Window
from os import listdir
from os.path import isfile, join
import pyspark.sql.functions as func
import json

import pandas as pd

if __name__ == "__main__":
	
	spark = SparkSession\
		.builder\
		.appName("TfIdfExample")\
		.getOrCreate()

	sc = SparkContext.getOrCreate()
	
	inputPath = "output"
	filelist = [f for f in listdir(inputPath) if isfile(join(inputPath,f))]
	print("\n Input files are",filelist,"\n")
	
	d = dict.fromkeys(filelist)

	for f in filelist:
	
		print("\n INPUT FILE DATE IS:",f,"\n")		

		spark.read.format("csv").option("header", "true").load("output/"+f)
		df = spark.read.option("header","true").csv("output/"+f)
		print("\nThe data frame is: ",df,"\n")
	
		df.createOrReplaceTempView("table")
		tickers = {"AMD": (0,0), "TLRY": (0,0), "MU": (0,0), "BABA": (0,0), "IQ": (0,0), "JD": (0,0), "TCEHY": (0,0), "APRN": (0,0)}
		for ticker in tickers:
			sqlDfBear = spark.sql("SELECT COUNT(*) FROM table WHERE sent='Bearish' AND ticker='"+ticker+"'")
			countListBear = sqlDfBear.select("*").collect()[0].asDict()
			print("\n Info:",ticker,countListBear["count(1)"],"\n")

			sqlDfBull = spark.sql("SELECT COUNT(*) FROM table WHERE sent='Bullish' AND ticker='"+ticker+"'")
			countListBull = sqlDfBull.select("*").collect()[0].asDict()

			tickers[ticker] = (countListBear["count(1)"], countListBull["count(1)"])

		print("\n date dict:",tickers,"\n")
		d[f] = tickers

	print(d)

	with open('result.json','w') as fp:
		json.dump(d,fp)
	
	spark.stop()
