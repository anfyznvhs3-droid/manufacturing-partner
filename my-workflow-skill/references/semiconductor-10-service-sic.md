# SiC MOSFET solar-inverter power stage - field service and failure analysis

This power stage converts solar-side DC-link power through SiC MOSFET switching and sends it to the AC output/filter/grid interface. Inputs are DC voltage/current, gate command, voltage/current/temperature feedback, and interlock. Outputs are per-phase AC power, status/fault signals, and diagnostic logs. Permit operation only after approved DC-link range, current/temperature limits, cooling, insulation/grounding, grid conditions, precharge, and interlock requirements are met.

On overcurrent, overtemperature, DC-link abnormality, drive fault, or released interlock, inhibit gate drive and enter the defined safe stop. Preserve cutoff time, cause code, sensor/command values, and immediately preceding events; do not treat a power cycle as cause resolution. Under the approved procedure, verify zero voltage, discharge, and insulation before replacing only BOM-defined customer-replaceable units. Recheck wiring, fastening, and cooling, then verify no-load startup, limited-load increase, protection action, and logs against the reference procedure. For recurrence prevention, correlate the same fault code with time, irradiance, temperature, and maintenance history.

## Unknown specification and log fields

Rated voltage/current/frequency, protection threshold, stop behavior, replaceable-unit list, device ID/firmware, timestamp, DC/AC voltage/current, temperature, gate/interlock status, fault code, operating mode, and cooling/grid status.
