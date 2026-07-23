# Evidence fact pack: Arduino UNO R4 WiFi

## Source identity

- Product: Arduino UNO R4 WiFi.
- Source: vendor datasheet `ABX00087`, observed modification date 2026-07-17; SHA-256 in `source-manifest.json`.
- Evidence locator: datasheet pages 2, 8-16, 21-24; public product page.

## Stated facts

- Configuration: RA4M1 is the main MCU; ESP32-S3-MINI-1-N8 is the secondary wireless MCU. The two MCU domains are 5 V and 3.3 V respectively and communicate through a level translator.
- Function: development board with programmable I/O, USB-C power/programming/serial use, a 12x8 LED matrix, and Wi-Fi/Bluetooth connectivity.
- Interfaces: 14 digital I/O, 6 analog channels, UART, SPI, two I2C buses, and CAN that requires an external transceiver.
- Limits: VIN/DC jack 6-24 V; USB input 4.8-5.5 V; operating temperature -40 to 85 C. Do not exceed 5 V at USB-C. RA4M1 GPIO is limited to 8 mA; power higher-current devices separately.
- Compliance declarations in the vendor datasheet: EU Radio Equipment Directive 2014/53/EU, FCC Part 15, EU RoHS references, REACH references, and radio-operation cautions. These are vendor declarations, not a test record for a new system using the board.

## Not established by the source

- The end-product configuration, country of sale, antenna/enclosure changes, and industrial environment.
- Functional-safety role, hazard analysis, defined safe state, restart authority, or fault-response timing.
- Test method, acceptance criterion, result, instrument, performer/date, and record ID for the intended application.
- Selection and scope match of an international standard for the intended application.

## DOC-READY v1 result

`needs-fact-confirmation`. The vendor board data is well evidenced, but it cannot establish readiness or conformity of an unspecified industrial end product.
