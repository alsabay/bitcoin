# bitcoin
Prerequisites:
MongoDB
Apache Spark
python3

okcoinMongo.py - pulls bitcoin ticker data from okcoin.com, stores in MongoDB at 5 sec intervals.
livegraph.py - plots bitcoin ticker data from MongoDB.
live-sparkgraph.py - runs as an apache spark process. Connects to MongoDB using the Stratio spark-mongodb package hosted at spark.packages.org

Instructions:
1. Start MongoD in a terminal
2. Start mongo console and type command "use okcoindb"
3. In a separate terminal, run "python okcoinMongo.py"
4. In another terminal, run "python livegraph.py"
5. To run apache spark version, from a terminal window type below:

$ spark-submit --conf "spark.mongodb.input.uri=mongodb://127.0.0.1/test.myCollection?readPreference=primaryPreferred"               --conf "spark.mongodb.output.uri=mongodb://127.0.0.1/test.myCollection"   --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 live-sparkgraph.py

