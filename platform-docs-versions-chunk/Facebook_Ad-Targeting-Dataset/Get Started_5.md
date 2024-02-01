platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Get Started
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Get Started.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/get-started


### Step 4: Create and run a SQL query

Enter the following code in the empty notebook cell to define a SQL query (`sql`) using variable substitution (`database` and `table`), and use the query module to execute the query:

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

Run the code. This should return a dataframe of your results, similar to those shown below (screenshots of dataframe results blurred intentionally).

The dataframe result from the R example would look similar to this (blurred intentionally):

  
  

The dataframe result from the Python example would look similar to this (blurred intentionally):

  
  

You can scroll within the dataframe to see additional table columns.