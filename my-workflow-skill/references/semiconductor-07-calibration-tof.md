# ToF distance-sensor module - calibration and metrology engineer

The module calculates distance between a reference plane and a target using time of flight. The controller inputs power, trigger, and measurement settings such as cycle, integration condition, and calibration coefficient. The module outputs distance, quality, status flags, and diagnostics through a digital interface. For targets with different reflectance, record distance bias/repeatability together with target reflectance, incidence angle, measurement-plane tilt, and optical-axis alignment.

Limit use to the target-distance, target-reflectance, ambient-temperature, ambient-light, and contamination conditions stated in the product specification. Strong ambient light, multipath reflection, transparent/glossy surfaces, and optical-axis misalignment can reduce signal-to-noise ratio and increase uncertainty; mark the measurement excluded or remeasure according to the approved procedure.

On receive saturation, emitter/receiver fault, internal communications error, or calibration-data integrity fault, output an invalid state and fault code instead of presenting a normal distance. Change to the configured safe behavior.

Verify using traceable reference distance and reflectance standards after controlling alignment, thermal stabilization, and ambient light. Independently assess bias, repeatability, and uncertainty by distance; compare to reference equipment and verify failure flags. The calibration criterion is the applicable specification's distance range, reflectance, alignment tolerance, ambient light, and uncertainty limit.
