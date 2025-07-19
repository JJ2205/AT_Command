\# Assignment 3: Command Variants \& Help



\## Objective



To explore various AT command syntax variants and understand how commands respond when used with:

\- `AT+CMD=?` → Test command

\- `AT+CMD?` → Read current setting

\- `AT+CMD=<value>` → Set new value





\## AT Command Syntax Types



| Syntax Variant     | Format           | Description                                      |

|--------------------|------------------|--------------------------------------------------|

| Test Command       | `AT+CMD=?`       | Lists supported values or options                |

| Read Command       | `AT+CMD?`        | Displays current setting                         |

| Set Command        | `AT+CMD=<val>`   | Changes value or mode (if supported)             |

| Execute Command    | `AT+CMD`         | Performs an action directly without parameters   |



\## Help-style Documentation (Manual Output)



Since the emulator does not auto-display help or list all supported commands, each command was tested manually and results documented below.



\## Grouped Commands by Syntax Type



\### Group 1: Supports Test, Read, and Set



\*\*Command: `AT+CMGF` (SMS Format)\*\*


AT+CMGF=? → +CMGF: (0,1)

AT+CMGF? → +CMGF: 0

AT+CMGF=1 → OK



\*\*Command: `AT+CLIP` (Caller ID Presentation)\*\*



AT+CLIP=? → +CLIP: (0,1)

AT+CLIP? → +CLIP: 0

AT+CLIP=1 → OK





\### Group 2: Supports Read and Set only



\*\*Command: `AT+CREG` (Network Registration Status)\*\*



AT+CREG? → +CREG: 0,1

AT+CREG=2 → OK



\### Group 3: Read-only



\*\*Command: `AT+CPIN?` (SIM Status)\*\*

AT+CPIN? → +CPIN: "READY"





\### Group 4: Execute-only



\*\*Command: `ATZ` (Reset the module)\*\*



AT → OK





\### Group 5: Execute, but Test and Set give ERROR



\*\*Command: `AT+CGMI` (Manufacturer Identification)\*\*



AT+CGMI → CELER

AT+CGMI? → ERROR

AT+CGMI=? → ERROR





\## Summary Table



| Command     | Test `=?` | Read `?` | Set `=val` | Execute |

|-------------|------------|-----------|-------------|----------|

| `AT+CMGF`   | Yes        | Yes       | Yes         | No       |

| `AT+CLIP`   | Yes        | Yes       | Yes         | No       |

| `AT+CREG`   | No         | Yes       | Yes         | No       |

| `AT+CPIN?`  | No         | Yes       | No          | No       |

| `AT+CGMI`   | No         | No        | No          | Yes      |

| `ATZ`       | No         | No        | No          | Yes      |

| `AT`        | No         | No        | No          | Yes      |



\## Notes



\- The emulator may return `ERROR` for unsupported syntax types.

\- Not all commands support all variants.

\- Manual testing was necessary due to lack of built-in command help listing.









