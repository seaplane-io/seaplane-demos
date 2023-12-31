from seaplane import task

# you can get this information from the flightdeck
sql_access = {
    "username": "<YOUR-USER-NAME>",
    "password": "<YOUR-PASSWORD>",
    "database": "<YOUR-DB-NAME>",
    "port": 5432,
}


@task(type="sql", id="pdf-summary-db", sql=sql_access)
def database(data, sql):
    # get the summary from the response
    summary = data["choices"][0]["message"]["content"]

    # insert into SQL DB
    sql.insert(
        """ INSERT INTO pdf_summaries
                        (url, prompt, summary)
                        VALUES
                        (%s,%s,%s)
                    """,
        [data["url"], data["prompt"], summary],
    )
