# PMIC power-management module - thermal and power-integrity engineer

The PMIC converts and distributes external input power to multiple system power rails and monitors rail startup order and stable state. Inputs are rated DC power, enable/disable control, and where needed power-good interaction; outputs are load rails plus status/fault signals.

On startup, allow a following rail only after the preceding rail is valid to reduce reverse current and partial startup. During rapid load change, manage voltage droop and transient oscillation within the control response. Review layout and thermal path so the module and neighboring components remain within system temperature limits. Guarantee operation only when input voltage, per-rail current, ambient/junction temperature, and start/stop conditions are within datasheet and system budgets.

On overcurrent, short circuit, overtemperature, undervoltage, or sequence fault, limit or disable the affected rail and update status. Retry, latch-off, and automatic-recovery policies follow the implementation specification; inspect load and input conditions before clearing the fault.

Verify rail voltage, ripple, sequence, and power-good timing at minimum/maximum input and static/dynamic loads. At worst-case thermal conditions, verify temperature stability, protection, and recovery.

## Unknown specification fields

Input range, rail count/rating, sequence/power-good timing, load-transient conditions, thermal limit/path, protection threshold/recovery policy, and permitted ripple.
