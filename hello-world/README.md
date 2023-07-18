# PDF Summary Demo Application

This demo application deploys a simple hello world application on Seaplane. It
takes a name (string) and returns a string `hello world <NAME>`.

To deploy follow these steps. We assume you have Seaplane installed on your
machine. You can do so by running `pip3 install seaplane`

- Open `main.py` and replace the Seaplane API key placeholders with your keys.
- Run `seaplane deploy` in the main `hello-world` directory.
- Set your Seaplane API key as an environment variable `export
  SEAPLANE_KEY="<YOUR-SEAPLANE-API-KEY>"`
- Execute the test script by running `python3 test.py POST <YOUR-NAME>`. This
  creates a `POST` request to the application you just deployed.
- Let a couple of seconds go by to allow for processing and then run `python3
  test.py GET <YOUR-REQUEST-ID>` to return the processed string.
