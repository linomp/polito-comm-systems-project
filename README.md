# polito-comm-systems-project

- [`DB`](./DB/) contains the `.sql` script to create the database and tables of the project (`plcs_db`).

- [`inventory-backend`](./inventory-backend/) contains the web service
    - Minimal commands to run the server (by default connects to our MySQL instance running on Digital Ocean):
        ```
         source venv/Scripts/activate
         pip install -r requirements.txt
         python -m uvicorn main:app --reload
        ```
         - (More details [here](./server_instructions.md))
     
    - To run the tests, in the `inventory-backend` directory, activate the virtual environment and run `pytest`:
        ```
        source venv/Scripts/activate
        pytest
        ```

- [`raspberry-pi-scripts`](./raspberry-pi-scripts/) contains scripts to run in the rpi, e.g. nfc tag reading.

## Overall architecture of the app
<img src="./architecture.png" width="80%">
