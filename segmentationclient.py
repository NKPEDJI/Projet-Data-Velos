#pip install pyspark

from pyspark.sql import SparkSession

# Initialisez une session Spark
spark = SparkSession.builder.appName("segmentation-clientele").getOrCreate()

# Chemin vers les fichiers Excel
chemin_bikes = r"\\wsl.localhost\Ubuntu-20.04\home\flore\ProjetDataVelos\files\bikes.csv"
chemin_bikeshops = r"\\wsl.localhost\Ubuntu-20.04\home\flore\ProjetDataVelos\files\bikeshops.csv"
chemin_orders = r"\\wsl.localhost\Ubuntu-20.04\home\flore\ProjetDataVelos\files\orders.csv"

# Lisez les données à partir d'un fichier CSV
df_bikes = spark.read.csv(chemin_bikes, header=True, inferSchema=True)
df_bikeshops = spark.read_excel(chemin_bikeshops, header=True, inferSchema=True)
df_orders = spark.read_excel(chemin_orders, header=True, inferSchema=True)




# Afficher les premières lignes des DataFrames pour vérifier
print("Contenu du fichier bikes.xlsx :")
print(df_bikes.head())

print("\nContenu du fichier bikeshops.xlsx :")
print(df_bikeshops.head())

print("\nContenu du fichier orders.xlsx :")
print(df_order.head())
