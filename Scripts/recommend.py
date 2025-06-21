from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col
from transform import transform_data
from session import get_spark_session

def recommend_movies():
    spark = get_spark_session("ALS Recommendations")
    transformed = transform_data()
    ratings_cleaned = transformed["ratings_cleaned"]

    # 🚨 ALS requires integers for user_id and movie_id
    als_data = ratings_cleaned.select(
        col("user_id").cast("integer"),
        col("movie_id").cast("integer"),
        col("rating").cast("float")
    )

    # 🔧 Build ALS Model
    als = ALS(
        userCol="user_id",
        itemCol="movie_id",
        ratingCol="rating",
        nonnegative=True,
        implicitPrefs=False,
        coldStartStrategy="drop",  # drop NaN predicted ratings
        maxIter=10,
        regParam=0.1,
        rank=10,
        seed=42
    )

    model = als.fit(als_data)

    # 🧪 (Optional) Evaluate model performance
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    predictions = model.transform(als_data)
    rmse = evaluator.evaluate(predictions)
    print(f"✅ ALS model trained. RMSE: {rmse:.4f}")

    # 🎯 Generate top 5 movie recommendations per user
    user_recs = model.recommendForAllUsers(5)

    # 🔄 Flatten the nested recommendations structure
    from pyspark.sql.functions import explode
    recommendations_df = user_recs.withColumn("rec", explode("recommendations")) \
        .select(
            col("user_id"),
            col("rec.movie_id"),
            col("rec.rating").alias("predicted_rating")
        )

    return recommendations_df

if __name__ == "__main__":
    recommendations_df = recommend_movies()
    print("🎯 ALS-based recommendations:")
    recommendations_df.show(10)
