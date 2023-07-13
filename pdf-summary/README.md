# PDF Summary Demo Application

This demo application deploys a PDF summary pipeline on Seaplane. It takes a PDF
URL as input and summarizes it using GPT-3. You can read more about it in [this
tutorial](https://developers.seaplane.io/tutorials/pdf-summary).

To deploy follow these steps. We assume you have Seaplane installed on your
machine. You can do so by running `pip3 install seaplane`

- Open `main.py` and replace the openAI and Seaplane API key placeholders with
  your keys.
- Head over to the Flight Deck and provision a new SQL database, copy over the
  connection parameters to the `sql_access` object in `database.py`.
- Log in to the database and create a new table using the following create
  statement.

```sql
CREATE TABLE pdf_summaries (
    url VARCHAR,
    prompt VARCHAR,
    summary VARCHAR
);
```

- Run `seaplane deploy` in the main `pdf-summary` directory.
- Replace the API key placeholder in `test.py` with your Seaplane API key and
  execute the script by running `python3 test.py` to run your first PDF summary
  inference request.
