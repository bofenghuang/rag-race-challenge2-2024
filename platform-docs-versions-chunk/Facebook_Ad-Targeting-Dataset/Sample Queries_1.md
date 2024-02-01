platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Sample Queries
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Sample Queries.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/sample-queries

# Sample queries

Once you import our query module, you can use it to query the dataset using your own custom SQL queries. The code sample below shows importing the query module; specifying the database, table, and API table; defining a SQL query; and assigning the query to a variable (`sql`).

RPython

    library(fbrir)
    athena = AthenaFacade$new()
    
    database <- "fbri_prod_atp"
    table <- "ad_targeting_dataset_siep_aug_2020"
    api_table <- "ad_archive_api"
    
    # Define your own SQL query and assign to variable 'sql' 
    sql <- sprintf("SELECT * FROM %s.%s LIMIT 5", database, table)
    athena$QueryAthena(sql)

    from fbri.private.sql.query import execute
    
    database = "fbri_prod_atp"
    table = "ad_targeting_dataset_siep_aug_2020"
    api_table = "ad_archive_api"
    
    # Define your own SQL query and assign to variable 'sql' 
    sql = f"SELECT * FROM {database}.{table} LIMIT 5"
    
    execute(sql)

The dataframe result from the R example would look similar to this (blurred intentionally):

  
  

The dataframe result from the Python example would look similar to this (blurred intentionally):

  
  

The sample queries in the rest of this section demonstrate the types of queries you can perform against the dataset. For each example, we show the SQL first followed by a tabbed codeblock with Python and R so you can see how the SQL is used to define the `sql` variable. To try out a sample query, copy the R or Python from the codeblock and paste it into your Jupyter notebook cell. Then run the code.

Dataframe results screenshots have been blurred intentionally. They are intended only to show the output format you can expect.