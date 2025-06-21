# 🎮 Movie Recommendation System (with Apache Spark & PySpark)

A real-world, production-ready movie recommendation pipeline built using **Apache Spark**, modularized into Python scripts for scalability and daily execution. This project processes large-scale user behavior data (watch history, ratings, search logs), performs feature engineering, and generates personalized movie recommendations for users.

---

## 🚀 Features

* 📅 **Ingestion** of raw data from CSVs (users, movies, ratings, watch history, search logs)
* 🧹 **Data cleaning** with handling of duplicates and nulls
* 🔍 **Feature engineering** including:

  * Primary genre extraction
  * User-level movie watch count
  * User average rating & rating deviation
* 🎯 **Recommendation generation** using collaborative filtering
* 📊 **Export** of enriched, recommendation-ready dataset for BI tools like Power BI
* 🔄 **Modular architecture** designed for automation and daily runs
* 🧪 **Notebook-friendly**: Includes full pipeline in Google Colab notebook for exploratory runs

---

## 📁 Project Structure

```bash
.
├── ingest.py          # Ingests raw CSV files using Spark
├── transform.py       # Cleans data and performs feature engineering
├── recommend.py       # Builds and applies the recommendation model
├── export.py          # Final export with selected columns for analysis
├── main.py            # Orchestrates all steps in order
├── session.py         # Manages Spark session
└── README.md
```

---

## 🛠 Requirements

* Python 3.7+
* Apache Spark with PySpark
* Google Colab (for notebook use)

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender-spark.git
cd movie-recommender-spark
```

### 2. Install Dependencies

If you're running locally (not Colab), install PySpark:

```bash
pip install pyspark
```

---

## 📊 Input Data Files

Place your input CSVs in the `/content/` directory (this is the path used in the scripts):

* `users.csv`
* `movies.csv`
* `ratings.csv`
* `watch_history.csv`
* `search_logs.csv`

If you're running on Google Colab, upload the files manually or mount Google Drive.

---

## ▶️ Running the Pipeline

### Option 1: Run Entire Pipeline via Script

```bash
python main.py
```

This will sequentially:

* Ingest data
* Clean and transform it
* Generate recommendations
* Export the final dataset to `/content/output/`

### Option 2: Explore in Google Colab

> 💡 This project was **originally developed in Google Colab**. If you wish to experiment in a notebook-style format, use the included notebook.

Open [`complete_project.ipynb`](complete_project.ipynb) in [Google Colab](https://colab.research.google.com/), and ensure all data is available in `/content/`.

---

## 📤 Output

After running the pipeline:

* Cleaned CSVs are saved to `/content/cleaned/`
* Engineered features are saved to `/content/features/`
* Final export is saved to `/content/output/final_recommendations.csv`

These files are ideal for use in tools like Power BI, Tableau, or any analytics engine.

---

## 🧠 Model Details

* **Collaborative Filtering** using Spark’s `ALS` (Alternating Least Squares)
* Predictions are merged with metadata for user interpretability
* Recommendation quality can be improved further with hyperparameter tuning or hybrid approaches

---

## 📌 Notes

* Paths are hardcoded for Colab (`/content/`). If running locally, update paths accordingly.
* For large-scale production deployment, you can integrate these scripts with Airflow or cron jobs.
* Spark session creation is modularized via `session.py` for reusability.

---

## ❤️ Contributing

Have ideas or suggestions? Pull requests are welcome!

---

# Apache Spark

This repository contains a complete setup to run Apache Spark in Google Colab, allowing you to explore distributed data processing, analytics, and transformations without needing a Spark cluster locally.

---

## 🚀 What is Apache Spark?

Apache Spark is an open-source, distributed computing system that provides an interface for programming entire clusters with implicit data parallelism and fault tolerance. Spark is designed to process large-scale data efficiently, both in batch and real-time environments.

---

## 🔥 Why Spark?

### ✅ Speed

Spark performs in-memory processing which makes it **up to 100x faster** than traditional systems like Hadoop MapReduce.

### ✅ Scalability

Spark is built to handle **terabytes to petabytes** of data across distributed clusters.

### ✅ Flexibility

Supports a wide variety of workloads:

* Batch Processing
* Interactive Queries (Spark SQL)
* Machine Learning (MLlib)
* Stream Processing (Spark Streaming)
* Graph Processing (GraphX)

### ✅ Unified Engine

A single platform for different types of big data workloads.

---

## 📚 Example Use Case: Netflix Recommendation System

Imagine Netflix wants to generate daily movie recommendations for millions of users based on watch history, search patterns, and user interactions.

**Data Size:**

* \~500 million users
* 10+ years of history
* Billions of events per day

### Why Spark Works:

* Distributes data and computation across multiple nodes
* Caches frequent queries in memory for fast retrieval
* Efficiently handles data joins, aggregations, and filtering at massive scale
* Real-time pipeline integration with tools like Kafka

> 💡 Traditional tools like Pandas or Excel fail beyond a few gigabytes of data. Spark is designed to thrive in this environment.

---

## 🧪 What's in This Project

This Google Colab-based setup includes:

* ✅ Java and PySpark installation
* ✅ Spark environment configuration
* ✅ Spark session creation
* ✅ Reading a CSV file with Spark
* ✅ Displaying and inspecting the DataFrame

---

## 📁 Sample Data

```csv
id,name,department,salary
1,Alice,Engineering,70000
2,Bob,Sales,50000
3,Charlie,HR,45000
4,David,Engineering,80000
5,Eva,Marketing,60000
```

You can modify or scale this data to simulate big data scenarios using Spark's `union()` operations.

---

## 🛠️ How to Run

1. Open the notebook in Google Colab.
2. Follow the steps: Install Java, install PySpark, set environment variables.
3. Create and initialize a Spark session.
4. Load and explore the CSV using Spark.

---

## 📌 When Should You Use Spark?

| Scenario                                  | Spark Needed?       |
| ----------------------------------------- | ------------------- |
| CSV with 1,000 rows                       | ❌ Pandas is enough  |
| 10 million+ rows from logs or sensors     | ✅ Yes               |
| Real-time fraud detection                 | ✅ Yes               |
| Joining huge datasets (e.g., sales + CRM) | ✅ Yes               |
| Exploratory data analysis on small data   | ❌ Use Pandas or SQL |

---

## 📎 Resources

* [Apache Spark Official Documentation](https://spark.apache.org/docs/latest/)
* [Spark SQL Guide](https://spark.apache.org/sql/)
* [PySpark API Reference](https://spark.apache.org/docs/latest/api/python/index.html)

---

## 🙌 Contribution

Feel free to fork, clone, and contribute to this notebook by adding new datasets, transformations, and visualizations.

---

## 📧 Contact

Created with ❤️ by \[Your Name]

If you found this helpful, ⭐ the repo and share it with fellow data enthusiasts!
