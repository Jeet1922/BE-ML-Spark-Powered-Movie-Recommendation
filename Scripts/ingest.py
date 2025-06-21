from session import get_spark_session

def ingest_data():
    spark = get_spark_session("Data Ingestion")

    # Define file paths
    base_path = "/content"
    users_path = f"{base_path}/users.csv"
    movies_path = f"{base_path}/movies.csv"
    ratings_path = f"{base_path}/ratings.csv"
    watch_history_path = f"{base_path}/watch_history.csv"
    search_logs_path = f"{base_path}/search_logs.csv"

    # Read CSV files
    users_df = spark.read.csv(users_path, header=True, inferSchema=True)
    movies_df = spark.read.csv(movies_path, header=True, inferSchema=True)
    ratings_df = spark.read.csv(ratings_path, header=True, inferSchema=True)
    watch_history_df = spark.read.csv(watch_history_path, header=True, inferSchema=True)
    search_logs_df = spark.read.csv(search_logs_path, header=True, inferSchema=True)

    return {
        "users": users_df,
        "movies": movies_df,
        "ratings": ratings_df,
        "watch_history": watch_history_df,
        "search_logs": search_logs_df
    }

if __name__ == "__main__":
    data = ingest_data()
    for name, df in data.items():
        print(f"📄 {name}")
        df.show(2)
