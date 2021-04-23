import vertica_python
import logging
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
import toml

secrets = toml.load('secrets.toml')

conn_info = {
    "host": secrets["vertica"]["host"],
    "port": secrets["vertica"]["port"],
    "user": secrets["vertica"]["user"],
    "password": secrets["vertica"]["password"],
    "database": secrets["vertica"]["database"],
    "log_level": logging.INFO,
}

with vertica_python.connect(**conn_info) as connection:
    cur = connection.cursor()
    cur.execute("""select * from ETL_Admin.auditing_metadata order by 1""")
    rows = cur.fetchall()

    table = Table(title="Lag")

    table.add_column("Table")
    table.add_column("Status")
    table.add_column("SLA")
    table.add_column("Expected")
    table.add_column("Latest")
    table.add_column("Gaps")
    table.add_column("Note")

    for row in rows:
        table_name_wow = row[0]
        date_column = row[1]
        day_late = row[2]
        min_row = row[3]
        check_missing = row[4]
        notes = row[5]

        cur.execute(
            """SELECT
                DATE("""+date_column+""") AS day
                , COUNT(*) AS num_rows
            FROM """+table_name_wow+"""
            WHERE DATE("""+date_column+""") BETWEEN (DATE(NOW()) - 90) AND DATE(NOW())
            GROUP BY DATE("""+date_column+""")
            ORDER BY DATE("""+date_column+""")"""
        )
        rows = cur.fetchall()
        days_complete_data = [row[0].strftime("%Y-%m-%d") for row in rows if int(row[1]) >= min_row]
        if len(days_complete_data) > 0:
            latest_day = days_complete_data[-1]
        else:
            latest_day = None
        cutoff_day = (datetime.now().date() - timedelta(days=day_late))

        days_expected = [(cutoff_day - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(90-day_late)]

        days_missing = sorted(list(set(days_expected) - set(days_complete_data)))

        cutoff_day = cutoff_day.strftime("%Y-%m-%d")

        if not True:
            days_missing = []
        if latest_day is None:
            status = "EMPTY?"
        elif latest_day < cutoff_day and len(days_missing) == 0:
            status = "LATE"
        elif latest_day >= cutoff_day and len(days_missing) > 0:
            status = "GAPS"
        elif latest_day < cutoff_day and len(days_missing) > 0:
            status = "LATE+GAPS"
        else:
            status = "OK"

        missing_str = str(days_missing)

        table.add_row(table_name_wow,
        status,
        str(day_late),
        cutoff_day,
        latest_day,
        missing_str,
        notes
        )

    console = Console()
    console.print(table)


