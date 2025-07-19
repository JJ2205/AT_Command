\# Assignment 2: Syntax \& Status Commands



Objective



To test and understand the functionality of standard 3GPP AT commands used for checking:



\- Signal quality

\- SIM card status

\- Network operator information



The following AT commands were manually tested using an AT emulator:



\- `AT+CSQ`

\- `AT+CPIN?`

\- `AT+COPS?`



---



&nbsp;Commands Overview



| Command      | Full Form                                | Description                               |

|--------------|-------------------------------------------|-------------------------------------------|

| `AT+CSQ`     | Signal Quality                            | Returns RSSI (signal strength) \& BER      |

| `AT+CPIN?`   | SIM Personal Identification Number status | Shows if SIM is ready or needs a PIN      |

| `AT+COPS?`   | Operator Selection Status                 | Returns current network registration info |



---



Sample Manual Output



AT+CSQ

+CSQ: 21,0

OK



AT+CPIN?

+CPIN: "READY"

OK



AT+COPS?

ERROR





---



\##  What is RSSI?



\*\*RSSI\*\* stands for \*\*Received Signal Strength Indicator\*\*.  

It gives a numeric value representing how strong the signal is.



\### 📏 RSSI Value Range (from `+CSQ: <rssi>,<ber>`)



| RSSI | Signal Strength | Approx. dBm     | Description         |

|------|------------------|------------------|----------------------|

| 0    | -113 dBm         | Very poor signal |

| 1    | -111 dBm         | Poor             |

| 10   | -93 dBm          | Average          |

| 20   | -73 dBm          | Good             |

| 31   | -51 dBm          | Excellent        |

| 99   | Not detectable   | N/A              |



\*\*Formula to convert RSSI to dBm\*\*:

RSSI (dBm) = -113 + (RSSI × 2)





➡️ Example:  

For `+CSQ: 21,0` → RSSI = 21  

→ dBm = -113 + (21 × 2) = \*\*-71 dBm\*\*  

→ This indicates \*\*good signal quality\*\*



---



&nbsp;SIM Status (`AT+CPIN?`)



\- `+CPIN: "READY"` → SIM is \*\*inserted\*\* and \*\*active\*\*

\- Other possible values:

&nbsp; - `"SIM PIN"` → SIM needs PIN

&nbsp; - `"SIM PUK"` → SIM locked

&nbsp; - `"NOT INSERTED"` → No SIM detected



---



&nbsp;Network Operator Status (`AT+COPS?`)



\- May return:



+COPS: 0,0,"OperatorName"

OK



\- In this case, the emulator responded with:

ERROR



This means the \*\*emulator does not support\*\* querying operator info — which is acceptable for simulated environments.



---



\## OVERVIEW



| Command     | Result                         |

|-------------|--------------------------------|

| `AT+CSQ`    | ✅ RSSI = 21 → -71 dBm (Good)   |

| `AT+CPIN?`  | ✅ SIM Status = READY           |

| `AT+COPS?`  | ❌ Not supported in emulator    |



























