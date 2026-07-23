# GOAL 7: training system profile and test matrix

## Declared training configuration

This is a fictitious training product, not a released design.

| Field | Declared value | Status |
| --- | --- | --- |
| Product | Indoor industrial condition-monitoring gateway | Training assumption |
| Target markets | Republic of Korea and EU | Training assumption; local legal review still required |
| Core board | Arduino UNO R4 WiFi, vendor datasheet ABX00087 | Public primary source |
| Enclosure/antenna | Vendor board with its onboard antenna inside a non-metallic protected enclosure; no antenna modification | Training assumption; drawing/BOM required |
| Inputs | Low-voltage sensors through an approved interface; exact sensor BOM is not yet fixed | Incomplete |
| Outputs | Local status indication and Wi-Fi telemetry only | Training assumption |
| Prohibited role | No actuator command, emergency stop, protective function, or personnel-safety decision | Training boundary |
| Environment | Indoor industrial equipment cabinet; normal ambient target 10-40 C | Training assumption; installation survey required |
| Fault behavior | On sensor/communications failure: do not issue a control command; mark data stale/invalid, retain an event record, and require an operator to investigate. | Proposed requirement; implementation evidence required |

## Standards applicability decision

| Reference | Decision | Rationale and evidence needed |
| --- | --- | --- |
| ISO 9001:2015/Amd 1:2024 | Apply as document/QMS baseline | Maintain revision, evidence, nonconformity, and improvement records; no certification is claimed. |
| ISO 10013:2021 | Apply as documented-information guidance | Control profile, BOM, firmware, test plan/report, and approvals. |
| ISO 19011:2026 | Apply as audit-method guidance | Separate criteria, evidence, findings, and conclusion. |
| IEC 61000-6-2:2016 | Candidate apply | Generic industrial EMC immunity only if no dedicated product/family standard governs the final product. Confirm final EUT, ports, installation, and market rules. |
| IEC 61000-6-4:2018 | Candidate apply | Generic industrial EMC emission only if no dedicated product/family standard governs the final product. Confirm final EUT, ports, installation, and market rules. |
| IEC 62443-4-2:2019 | Candidate apply | The Wi-Fi telemetry gateway may be an IACS component. First define asset role, zone/conduit, security-level target, account model, update method, and exposed interfaces. No compliance claim. |
| IEC 60068-2-2:2025 | Candidate apply | Use for dry-heat method selection after enclosure, temperature profile, duration, operating mode, and acceptance limits are approved. |
| IEC 61508 series | Not applicable by declared scope | No safety function or safety claim exists. Re-open immediately if the product controls equipment or contributes to risk reduction. |
| IEC 61131 series | Not applicable by declared scope | This is not a PLC product or PLC program. Re-open if PLC integration becomes a claimed product function. |

## Test matrix

| ID | Objective / reference | EUT configuration | Method and condition | Acceptance criterion | Evidence required | Status |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | Configuration control / ISO 10013 | Board, enclosure, sensor interface, firmware, power supply, cables | Review controlled BOM, revisions, source links, and change history | Every released artifact has ID, revision, owner, approval, and retention location | Controlled document register and change record | Planned |
| T02 | Industrial EMC immunity / IEC 61000-6-2:2016 if selected | Final assembled gateway, all normal cables/ports/PSU | Accredited-lab plan using the licensed standard and final market test plan | Criteria must be approved before test; no silent corruption, uncommanded output, or loss of fault indication | Lab report, setup photos, configuration/firmware ID, results | Not executed |
| T03 | Industrial EMC emissions / IEC 61000-6-4:2018 if selected | Same final EUT | Accredited-lab plan using the licensed standard and final market test plan | Applicable limits from selected standard/regulatory route | Lab report, setup photos, configuration/firmware ID, results | Not executed |
| T04 | Thermal operation / IEC 60068-2-2:2025 if selected | Final EUT in intended enclosure and normal telemetry load | Severity/duration only after site and product requirements are approved | No reset, unsafe output, unmarked stale data, or permanent degradation; numeric limits must be approved | Chamber log, telemetry log, pre/post functional record, report | Not executed |
| T05 | Security capability / IEC 62443-4-2:2019 if selected | Final firmware, credentials, Wi-Fi configuration, update path | Threat/risk scope then map selected component requirements to tests | No default production credential; interfaces, update path, and security event behavior must meet approved requirements | Asset/interface list, threat model, requirement mapping, test record | Not executed |
| T06 | Functional fault behavior | Final EUT with representative sensors and network loss injection | Disconnect sensor and network; restore each condition | No actuator output; stale/invalid state visible; event retained; recovery state recorded | Test procedure, logs, observation, result, performer/date | Not executed |
| T07 | Market-regulatory route | Final market-specific EUT | Confirm Korea/EU legal route, radio/EMC/safety labeling and test obligations | Approved market-entry decision before shipment | Regulatory review, declaration/certificates where required | Not started |

## DOC-READY v1 reassessment

The training specification now states product function, I/O boundary, operating environment, intended fault behavior, standards-selection logic, and a test matrix. The gate remains `needs-fact-confirmation` because the final enclosure/sensor/firmware/configuration is not fixed and T01-T07 have no completed evidence. This profile is not a market-conformity claim.

## Minimal remaining facts

1. Controlled BOM, enclosure drawing, cable/sensor list, power-supply specification, and firmware ID.
2. Approved standard selection with scope/market rationale and licensed clauses.
3. Approved numeric acceptance criteria and completed T01-T07 records.
