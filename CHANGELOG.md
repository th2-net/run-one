1.2.7
-----

* Make `process` function return list of tuples of processing start and end times for each matrix file

1.2.6
-----

* Change event body format in `TH2EstoreHandler`

1.2.5
-----

* Fix class name for `store` action handler

1.2.4
-----

* Add ability to read CSV files with large size fields

1.2.3
-----

* Add handler for `store` actions which sends events to `th2-estore`

1.2.2
-----

* Change `SleepHandler` to take values in seconds

1.2.1
-----

* Use `UTF-8` encoding when working with files

1.2.0
-----

* Add ability to send events from action handlers via passing event router
* Refactor regeneration functions for ID-like and time-like fields to accept current action data

1.1.1
-----

* Add parameter `filename_pattern` to filter files when reading from directory
* Add try/catch around action processing method

1.1.0
-----

* Remove `pandas` usage

1.0.17
-----

* Add ability to save ID-like fields mapping

1.0.16
-----

* Make `generate_time` (default function for time-like fields regeneration) to return proper UTC time
* Fix possibility to pass custom function for regeneration of ID-like fields
* Add ability to work with directory of matrices

1.0.15
-----

* Fix filling `ignore_fields` for th2-check1 request
* Add proper ability to provide `fail_unexpected` for th2-check1 request

1.0.14
-----

* Change `key_fields` and `ignore_fields` parameters of `Th2ProcessorConfig` to be a mapping with message types as a keys

1.0.13
-----

* Fix building field filter for case when field is in `key_fields` and `nested_fields` in `TH2Check1handler`

1.0.12
-----

* Add parameter `ignore_fields` to set ignored fields in th2-check1 request
* Add parameter `fail_unexpected` to fail th2-check1 validation if any unexpected fields received

1.0.11
-----

* Fix `sleep` parameter in `processor_config` section
* Rework regeneration of time like fields

1.0.10
-----

* Rework package metadata for ability to install th2-related dependencies separately
* Add ability to provide root event name for `th2_processor`

1.0.9
-----

* Move to using `ast.literal_eval` for loading nested fields

1.0.7 & 1.0.8
-----

* Add backward compatibility for `pairwise` method

1.0.6
-----

* Change required Python version to 3.9

1.0.5
-----

* Add event types in `th2_processor`

1.0.4
-----

* Fix timestamp of test case EventID in `th2_processor`
* Ability to provide timeout for th2-act place methods

1.0.3
-----

* One more fix for `chain_id` logic in `TH2Check1Handler`

1.0.2
-----

* Fix `chain_id` logic in `TH2Check1Handler`
* Add new parameter `timetamp_shift` in `Th2ProcessorConfig` to shift event timestamps to the past 

1.0.1
-----

* Fix `on_action_change` method invocation in `th2_processor`