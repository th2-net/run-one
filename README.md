# run-one
Tool for parsing matrix files, extracting actions and processing them according to user defined logic

### How to setup environment and install dependencies
```bash
python -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry
$VENV_PATH/bin/poetry install
```

### Config example (using th2 processor)
```yaml
matrix_path: "matrix_case.csv" # path to matrix file
processed_actions: # which actions to process
  send: "TH2ActHandler"
  receive: "TH2Check1Handler"
  sleep: "SleepHandler"
  actSsh: "TH2ActSSHHandler"

field_mapping: # mapping for field renaming
  OrderQty: "OrderQty"
  TimeInForce: "TimeInForce"

nested_fields: ["NoPartyIDs", "OrderQtyData", "Parties", "Instrument"] # which fields to convert to collections

fields_to_drop: # which fields to remove
  ["PreviousID", "Protocol", "CaseName", "Seq"]

fields_to_extract: # which fields to extract and keep as additional information
  ["Action", "MessageType", "Time", "User", "ID", "ExecutionAlias", "Direction", "Description"]

regenerate_id_fields: ["ClOrdID", "OrigClOrdID"] # ID-like fields to regenerate

regenerate_time_fields: ["TransactTime"] # Time-like fields to regenerate

processor_config: # processor config in free form
  th2_configs: "th2_configs" # path to directory with th2 configs
  book: "test_book" # book name
  scope: "test_script" # scope name
  use_place_method: False # use th2 act place methods (True) or plain send (False)
  key_fields: ["Side", "ClOrdID", "OrigClOrdID"] # list of key fields for th2-check1 request
  sleep: 1 # delay between each action processing
```
