# CLI based DWH auditing


## Notes

```sql
SELECT
    DATE(sales_date) AS day
    , COUNT(*) AS num_rows
FROM CA_ODS.ods_crf_fct_pos_header
WHERE DATE(sales_date) BETWEEN (DATE(NOW()) - 90) AND DATE(NOW())
GROUP BY DATE(sales_date)
ORDER BY DATE(sales_date)
```

```sql
create table ETL_Admin.auditing_metadata (
	table_name varchar(1000),
	date_column varchar(1000),
	days_late int,
	min_rows int,
	check_missing boolean,
	notes varchar(1000)
);

INSERT INTO ETL_Admin.auditing_metadata
(table_name, date_column, days_late, min_rows, check_missing, notes)
VALUES('ca_ods.ods_vox_lyl_fct_transaction', 'transaction_time', 3, 1000, true, 'vox transactions');
INSERT INTO ETL_Admin.auditing_metadata
(table_name, date_column, days_late, min_rows, check_missing, notes)
VALUES('CA_ODS.ods_crf_fct_pos_item', 'sales_date', 3, 100000, true, 'c4 transactions');
```
