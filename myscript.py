# Ejemplo de script de Spark
#
# Cálculo numérico con 100000 números

from pyspark import SparkConf, SparkContext
from operator import add

def mult(num,factor=2):
    return num*factor

def main():
	conf = SparkConf()
	conf.set("spark.app.name", "Mi script Python")

	# Iniciamos el SparkContext
	sc = SparkContext(conf=conf)
	sc.setLogLevel("FATAL")

	rdd = sc.parallelize(range(100000)).cache()

	r = rdd.map(mult).reduce(lambda a,b:a+b)

	print("Resultado final = {0}".format(r))

	# Finalizamos el SparkContext
	sc.stop()

if __name__ == "__main__":
	main()
