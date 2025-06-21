from pyspark.sql.functions import col, split, explode, trim, year, from_unixtime, avg
from pyspark.sql.types import IntegerType
from ingest import ingest_data
from session import get_spark_session

def transform_data():
    spark = get_spark_session("Data Transformation")
    data = ingest_data()

    users_df = data["users"]
    movies_df = data["movies"]
    ratings_df = data["ratings"]
    watch_history_df = data["watch_history"]
    search_logs_df = data["search_logs"]

    # 🧹 USERS CLEANING
    users_cleaned = users_df.dropDuplicates(["user_id"]).na.drop(subset=["user_id", "name", "age", "gender", "location"])

    # 🧹 MOVIES CLEANING
    movies_cleaned = movies_df.dropDuplicates(["movie_id"]).na.drop(subset=["movie_id", "title", "genre"])

    # ➕ Extract release year from title (if applicable)
    from pyspark.sql.functions import regexp_extract
    movies_cleaned = movies_cleaned.withColumn("release_year", regexp_extract(col("title"), r"\((\d{4})\)", 1).cast(IntegerType()))

    # ➕ Explode genres
    movies_cleaned = movies_cleaned.withColumn("genre", split(col("genre"), "\\|"))
    movies_exploded = movies_cleaned.withColumn("genre", explode(col("genre"))).withColumn("genre", trim(col("genre")))

    # ➕ Add primary genre
    movies_exploded = movies_exploded.withColumn("primary_genre", col("genre"))

    # 🧹 RATINGS CLEANING
    ratings_cleaned = ratings_df.dropDuplicates(["user_id", "movie_id"]).na.drop(subset=["user_id", "movie_id", "rating"])

    # ➕ Add readable timestamp column
    ratings_cleaned = ratings_cleaned.withColumn("timestamp", from_unixtime(col("timestamp")))

    # 🧮 Feature: User watch count
    user_watch_count_df = watch_history_df.groupBy("user_id").count().withColumnRenamed("count", "movies_watched")

    # 🧮 Feature: Average movie rating & rating deviation per user-movie
    avg_movie_rating_df = ratings_cleaned.groupBy("movie_id").agg(avg("rating").alias("avg_movie_rating"))
    rating_with_deviation_df = ratings_cleaned \
        .join(avg_movie_rating_df, on="movie_id", how="left") \
        .withColumn("rating_deviation", col("rating") - col("avg_movie_rating"))

    # Return all transformed outputs
    return {
        "users_cleaned": users_cleaned,
        "movies_exploded": movies_exploded,
        "ratings_cleaned": ratings_cleaned,
        "user_watch_count": user_watch_count_df,
        "rating_with_deviation": rating_with_deviation_df
    }

if __name__ == "__main__":
    transformed = transform_data()
    for name, df in transformed.items():
        print(f"✅ {name}")
        df.show(2)
