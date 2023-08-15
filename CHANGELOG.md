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