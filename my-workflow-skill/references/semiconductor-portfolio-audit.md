# GOAL 4: semiconductor portfolio audit

## Corpus and token baseline

The corpus contains ten independently authored synthetic product descriptions spanning functional specification, tacit operating knowledge, FMEA, reliability, commissioning, calibration, thermal/power integrity, compliance, and field service. It is 15,126 characters, approximately 3,784 tokens using `ceil(characters / 4)`. This is a rough planning estimate, not a tokenizer measurement.

First-pass processing must read each document once, extract only the `DOC-READY` schema plus evidence excerpts, and pass that compact fact table to later rounds. Do not repeatedly send the entire 3,784-token corpus to each audit route.

## Decision results

All ten documents receive `needs-fact-confirmation`. They are intentionally synthetic training sources, contain no attached datasheet/test record, and were generated before the standards-basis field was added. None may be labeled conformant, production-ready, or safety-approved.

| ID | Product / route | Concrete strength | Failed or missing gate | Next fact-confirmation request |
| --- | --- | --- | --- | --- |
| 01 | Arduino motor controller / functional vocabulary | I/O, fault transition, test scenarios | 4 site terms; safe-state definition; standards basis | Define terms and approved safe-state behavior. |
| 02 | TFT LCD HMI / tacit knowledge | Identifies hidden operating conventions | Existing standard, retry procedure, normal display, wait limit, release rule are undefined | Supply revision-controlled HMI specification and objective criteria. |
| 03 | IMU / standard engineering | Separates confirmed from estimated statements | Model/configuration, measurement specification, standards basis | Supply datasheet and installation/test configuration. |
| 04 | IGBT inverter / FMEA | Separates mode, effect, detection, response | Protection thresholds, timing, and safety requirement absent | Supply protection matrix and applicable safety basis. |
| 05 | Industrial SSD / reliability | Connects integrity, life, and traceability | Endurance, retention, power-loss behavior, test acceptance absent | Supply device datasheet and approved endurance procedure. |
| 06 | PLC I/O / commissioning | Explicit installation sequence and safety boundary | Model behavior, safe state, grounding and interlock criteria absent | Supply model drawing, site grounding rule, and interlock test record. |
| 07 | ToF sensor / metrology | States uncertainty contributors and calibration artifacts | Exact range, reflectance, uncertainty, and traceability chain absent | Supply calibration procedure, reference instruments, and acceptance limits. |
| 08 | PMIC / thermal-power integrity | Identifies sequencing and protection phenomena | Rail configuration, limits, timing, and thermal budget absent | Supply schematic/configuration and power/thermal budget. |
| 09 | BLE module / compliance | Separates module evidence from end-product conformity | Country, antenna/enclosure, security policy, and selected standard absent | Supply market list, final configuration, and security/compliance plan. |
| 10 | SiC solar inverter / field service | Requires preservation of diagnostic evidence | Exact log schema, CRU list, stop policy, limits absent | Supply service procedure, log dictionary, and approved replacement list. |

## Quantitative outcome

| Metric | Result | Interpretation |
| --- | ---: | --- |
| Documents with attached primary evidence | 0 / 10 | All factual product claims need source confirmation. |
| Documents with a declared standards basis | 0 / 10 | The new baseline must be inserted in the next revision. |
| Documents with explicit unknown-field list | 10 / 10 | The generation prompt successfully preserved uncertainty. |
| Documents with a direct release/scrap/rework authorization | 0 / 10 | No unsafe operational authorization was generated. |
| Gate result | 10 `needs-fact-confirmation`, 0 `ready` | Correct outcome for synthetic, unsourced examples. |

The adversarial release test also passes: the Skill preserves the source request but blocks its release recommendation because affected-lot evidence and an approved disposition authority are absent.

## Adversarial findings

1. A phrase can sound operationally clear while still being unusable: `tight ramp`, `usual retry`, `normal display`, and `safe state` need a defined parameter or approved procedure.
2. A named test is not verifiable until it specifies configuration, condition, method, acceptance criterion, result, reference/instrument, performer/date, and record identifier.
3. A generic standard family is not a compliance basis. Record edition, scope match, applicable part, and a rationale for non-applicability.
4. Fault handling is incomplete when its stop state, restart authority, or evidence preservation rule is not explicit.

## Next recursive input

Use one real public datasheet or a deliberately fictional but fully specified product profile. Add its model/configuration, revision, selected standard/edition, acceptance criteria, and test records. Then rerun the audit and compare failed-gate count against this baseline.
