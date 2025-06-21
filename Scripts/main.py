from ingest import ingest_data
from transform import transform_data
from recommend import recommend_movies
from export import export_final_model

def run_pipeline():
    print("🚀 Step 1: Ingesting raw data from CSVs...")
    ingest_data()  # Called to ensure file presence and validation

    print("\n🧹 Step 2: Cleaning data and extracting features...")
    transform_data()

    print("\n🎯 Step 3: Generating movie recommendations...")
    recommend_movies()

    print("\n📤 Step 4: Exporting final dataset for dashboard or BI tools...")
    export_final_model()

    print("\n✅ Pipeline execution complete. All steps finished successfully.")

if __name__ == "__main__":
    run_pipeline()
