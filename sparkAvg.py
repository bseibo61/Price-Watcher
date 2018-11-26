from __future__ import print_function
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import Row
from pyspark.ml.feature import CountVectorizer
from operator import add
from pyspark.sql.window import Window
import pyspark.sql.functions as func

import pandas as pd

if __name__ == "__main__":
	
	spark = SparkSession\
		.builder\
		.appName("TfIdfExample")\
		.getOrCreate()

	sentenceData = spark.createDataFrame([
		(0.0, "Hi hello hi hi ifs"),
		(0.0, "I wish Java could hi hi hi")
	], ["label", "sentence"])

	sentenceData.show()

	sc = SparkContext.getOrCreate()

	#dirPath = "data/test/"

	#textFiles = sc.textFile(dirPath)
	
	spark.read.format("csv").option("header", "true").load("output/*.csv")
	df = spark.read.option("header","true").csv("output/*.csv")
	print("\nThe data frame is: ",df,"\n")
	df.show(n=500)
	#counts = textFiles.flatMap(lambda line: line.lower().split()).map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
#	print(counts.top(10, lambda t: t[1]))

#	outputs = counts.collect()
#	print(type(outputs))
#	df = counts.toDF()

#	w = Window.partitionBy(df['_2'])

#	datFrameTF = df.groupBy('_1', '_2').agg(func.count('*').alias('n_w'), func.sum(func.count('*')).over(w).alias('n_d'), (func.count('*')/func.sum(func.count('*')).over(w)).alias('tf')).orderBy('n_w', ascending=False).cache()

#	datFrameTF.show(truncate = 15)

	spark.stop()
