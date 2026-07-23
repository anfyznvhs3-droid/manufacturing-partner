# TFT LCD HMI module - tacit-knowledge-heavy writing

The 4.3-inch TFT LCD HMI module shows equipment status, work instructions, and alarms, and sends operator input to the controller. Use the existing equipment standard for screen structure and language. Connect signals according to the drawing pinout; when the controller is slow, follow the retry sequence normally used on the shop floor.

Keep temperature, supply voltage, communication cycle, and brightness within the product specification. After startup, cleaning, or replacement, do not operate the module until the responsible person sees the normally expected display. When the display, communications, or input fails, retain the last valid display or show an error screen; the upper-controller policy determines the safety decision. If required, remove power and wait the site-standard time before restarting.

Verify appearance/startup, screen changes, input response, controller communication, and display behavior through communication loss and recovery. For volume release, compare with a known-good unit and obtain the line leader's judgment.

## Tacit knowledge requiring explicit definition

- The applicable existing-standard document and revision.
- Retry sequence, count, and wait time.
- Normal display state and restart wait limit.
- Objective known-good comparison and release criteria.
- Priority between last valid display and error display.
