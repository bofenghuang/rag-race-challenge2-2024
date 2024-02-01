platform: Facebook
topic: Ad-Targeting-Dataset
subtopic: Table Schema Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Ad-Targeting-Dataset/Table Schema Documentation.md
url: https://developers.facebook.com/docs/ad-targeting-dataset/table-schema

## Delta table schema

The delta table lists ads that were reclassified as non-political (and therefore, removed from the table) since the last table publication. It is a single table to which we add data month to month.

| Column name | Type | Description | Sample value |
| --- | --- | --- | --- |
| `archive_id` | BigInt | Ad dataset archive ID that was reclassified and removed. | `2681789712070426` |
| `status` | string | Type of change being reported. | `updated`, `deleted` |
| `column_name` | string | Name of column affected by the change. Can also be empty. | `include_location`, `exclude` |
| `current_value` | string | Value after the change. Can also be empty. | `<address> Ecatepec de Morelos (+22 km), Estado de México (+40 km) State of Mexico` |
| `ds` | string | Date the ad no longer appeared in the dataset. | `2020-12-06` |
| `previous_value` | string | Value before the change. Can also be empty. | `Estado de México (+40 km) State of Mexico` |