from transform import transform_data
from recommend import recommend_movies
from session import get_spark_session

def export_final_model():
    spark = get_spark_session("Final Model Export")

    # 📦 Load transformed data and recommendations
    transformed = transform_data()
    recommendations_df = recommend_movies()

    users_df = transformed["users_cleaned"]
    movies_df = transformed["movies_cleaned"]
    user_watch_count_df = transformed["user_watch_count"]
    rating_with_deviation_df = transformed["rating_with_deviation"]

    # 🔗 Join all data
    final_df = recommendations_df \
        .join(users_df, on="user_id", how="left") \
        .join(movies_df, on="movie_id", how="left") \
        .join(user_watch_count_df, on="user_id", how="left") \
        .join(rating_with_deviation_df, on=["user_id", "movie_id"], how="left")

    # 🧾 Select & reorder columns
    export_df = final_df.select(
        "user_id", "name", "age", "gender", "location",
        "movie_id", "title", "genre", "release_year",
        "predicted_rating", "user_avg_rating", "rating_deviation", "movies_watched"
    )

    # 💾 Export as CSV
    export_path = "/content/export/final_recommendation_model.csv"
    export_df.write.csv(export_path, header=True, mode="overwrite")
    print(f"✅ Final data model exported to: {export_path}")

if __name__ == "__main__":
    export_final_model()
