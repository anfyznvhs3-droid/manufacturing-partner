# Six-axis IMU vibration-monitoring module - standard engineer

## Confirmed information

The module uses a six-axis IMU to monitor industrial-equipment vibration. It acquires three-axis acceleration and three-axis angular-rate data for vibration change, impact, and orientation analysis. Confirm the supplied data fields and analysis functions in the specification.

## Estimated function and I/O

Inputs are acceleration and angular-rate sensing; the module requires power and a wired or wireless communications connection. Outputs may include raw sensor data, timestamps, status codes, and threshold-exceedance alarms sent to a PLC, gateway, or monitoring application.

## Estimated limits and fault response

Mounting stiffness and orientation, cable noise, sensor-range exceedance, temperature, humidity, dust, and electromagnetic interference can affect measurement reliability. On sensor or communication fault, output an error state rather than silently treating the last good value as current. Provide alerting and reconnection/restart behavior where specified.

## Estimated verification and missing fields

Compare amplitude, frequency, and directional response with a reference vibration source or instrument. Test communication loss/recovery and power restoration. Confirm power and communications method, sample/transmit period, measurement range and accuracy, alarm criterion, storage period, mounting method, environmental rating, certifications, and fault-safety policy.
