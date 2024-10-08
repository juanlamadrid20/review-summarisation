# Databricks notebook source
"""Global Variables"""

# Configurable
################################################################
# Data Globals (All Notebooks)

CATALOG_NAME = "juan_dev"  # Unity Catalog Name
SCHEMA_NAME = "sol_acc_review_summarisation"  # Schema Name

# UC Options (All Notebooks)
USE_UC = True  # Use Unity Catalog?
USE_VOLUMES = True  # Use Volumes?

# Sampling Parameters (0.2-explore-prep)
TOP_BOOK_COUNT = 1000  # How many popular books to take ?
TOP_BOOK_SAMPLING_FRACTION = 0.01  # Sample further ? (None = no sampling)


# Auto Generated
################################################################

# Paths (All Notebooks)
if USE_VOLUMES:
    MAIN_STORAGE_PATH = f"/Volumes/{CATALOG_NAME}/{SCHEMA_NAME}"
    MAIN_DATA_PATH = MAIN_STORAGE_PATH
else:
    MAIN_STORAGE_PATH = f"/dbfs/{CATALOG_NAME}"
    MAIN_DATA_PATH = f"/{CATALOG_NAME}"

# Disable Volumes if not using Unity Catalog
USE_VOLUMES = False if not USE_UC else USE_VOLUMES


spark.sql(f"use catalog {CATALOG_NAME}");
spark.sql(f"use schema {SCHEMA_NAME}");


# COMMAND ----------

# MAGIC %sql
# MAGIC select current_catalog(), current_schema()
