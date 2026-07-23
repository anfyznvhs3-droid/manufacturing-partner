# GOAL 6 audit: Arduino UNO R4 WiFi

## Normalized product record

Arduino UNO R4 WiFi is a public development board, not an industrial end product. It combines an RA4M1 main MCU with an ESP32-S3 wireless MCU; their 5 V and 3.3 V domains are translated at the board boundary. It exposes programmable digital/analog and serial interfaces, supports wireless connectivity, and includes a 12x8 LED matrix. The evidence fact pack is the only allowed input for later recursive rounds unless a specific question requires returning to the source PDF.

## Fact audit

| Required field | Status | Evidence | Review result |
| --- | --- | --- | --- |
| Product/configuration | stated | Datasheet pp. 2, 9-10 | Main and wireless MCUs are identified. |
| Intended function | stated | Datasheet pp. 6, 12-14 | Development-board capability is stated; end-product use is not. |
| I/O/interface boundary | stated | Datasheet pp. 6, 12, 14, 18+ | I/O and bus availability are stated; connected load/system is unknown. |
| Operating limits | stated | Datasheet pp. 8, 16 | Supply, temperature, GPIO, and domain constraints are stated. |
| Fault response | missing | Datasheet has recovery information, not a defined industrial safe state | Do not infer a safety function or restart policy. |
| Verification conditions | missing | Declarations and cautions exist; no application test protocol/results | Require configuration-specific method, criterion, result, and record. |
| Standards basis | needs-fact-confirmation | Regulatory declarations are stated; IEC/ISO applicability is not | Select standard/edition from application scope, not from board name. |
| Unknown specification fields | stated by review | Evidence fact pack | The required unanswered fields are enumerated. |

## Standards basis

- Document-review baseline: ISO 9001:2015/Amd 1:2024, ISO 10013:2021, ISO 19011:2026.
- Product-source declarations: EU Directive 2014/53/EU, FCC Part 15, RoHS, and REACH references listed by the vendor.
- Conditional only: IEC 62443 if a connected industrial-control system is in scope; IEC 61508 if a safety function is claimed; IEC 60068 for environmental testing; IEC 61340 for ESD control; IEC 61131 for PLC integration. No conformity to any of these is claimed here.

## Fact-confirmation queue

1. Name the target end product, board revision, attached shield/peripheral, firmware revision, antenna/enclosure, and target market.
2. Define whether the board implements a safety function; if yes, provide the hazard analysis, safe state, and restart authority.
3. Select the applicable standard/edition and document the scope match.
4. Provide a test protocol with object/configuration, condition, method, acceptance criterion, result, instrument/reference, performer/date, and record ID.

## Metrics and decision

- Source extraction baseline: 15,837 `cl100k_base` tokens from 46 PDF pages. The cited fact pack is 447 tokens, a 97.2% reduction for later rounds; see `source-metrics.json`. This is a tokenizer comparison, not a production-model billing estimate.
- Critical source facts evidenced: 4 of 7 required product fields; 57.1%.
- Unsupported claims in this audit: 0.
- Critical ambiguities: 3 (end-product configuration, safety/fault role, verification/standards basis).
- Weighted quality score: 55.5/100 (57.1% fact coverage, 100% traceability of stated claims, 0% actionability for the unresolved application fields, three critical ambiguities). This score measures document-review readiness only.
- Gate decision: `needs-fact-confirmation`; a score cannot elevate this to `ready`.

## Comparison with GOAL 4 synthetic portfolio

The synthetic portfolio had zero attached primary-evidence sources and zero declared standards bases across ten documents. This audit has a preserved vendor primary source and full traceability for its stated claims, but it still fails the same application-level gates: end-product configuration, safety role, test evidence, and selected standard/edition are not established. The recursive method therefore improves evidence efficiency, not the right to claim conformity.

## Learning update

Add no product-specific terminology because the datasheet provides none requiring local interpretation. Retain the general rule: a vendor compliance declaration does not prove end-product conformity after a change in configuration, antenna, enclosure, market, or intended use.
