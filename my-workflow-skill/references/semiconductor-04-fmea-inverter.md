# IGBT power-module inverter - FMEA-focused engineer

- **Function:** Convert DC-link power, under a control signal, to variable-voltage and variable-frequency multiphase AC for the load.
- **I/O:** Inputs are DC link, PWM/enable, auxiliary power, current/temperature feedback. Outputs are phase AC plus operating/fault status.
- **Limits:** Keep voltage, phase current, switching conditions, junction/case temperature, cooling, insulation, short-circuit capability, and load characteristics within the approved specification.
- **Failure modes:** IGBT short/open, loss of gate drive, cooling-related overtemperature, current/voltage sensing error, and PWM/communications fault.
- **Effects:** Phase imbalance, torque loss, overcurrent/overvoltage, overheating, load stop, additional power-stage damage, and safety risk.
- **Detection:** Monitor phase current, DC-link voltage, temperature, gate-drive diagnostics, PWM/communications health, insulation, and continuity.
- **Fault response:** When the specified threshold and timing condition are met, inhibit PWM and retain/report the fault code. Output isolation, restart, and upstream interlock follow approved safety requirements.
- **Verification:** At rated and boundary loads, thermal/cooling boundaries, supply variation, and short/sensor/communications fault, verify detection, inhibit action, and status reporting against the specification.

## Specification fields to confirm

Rated and maximum voltage/current, transient capability, switching conditions, thermal resistance/cooling, insulation, protection thresholds/delays, fault-code/restart policy, and test criteria.
