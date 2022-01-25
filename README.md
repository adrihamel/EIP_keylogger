# EIP_keylogger

Proof of concept of a keylogger for cibersecurity educational purposes only, <a href="https://eiposgrados.com/programas/master-en-ciberseguridad/">@eiposgrados</a>.

# Requirements
Pynput utilitie is required.
```
pip install pynput
```
# Options
When starting the script, six options will appear:
```
+============= MENU =============+
|1. recordKey (CTRL+ESC to back) |
|2. readLogs                     |
|3. readCredentials              |
|4. delete credentials.txt       |
|5. delete keylog.txt            |
|6. Exit                         |
+================================+

```
<b>recordKey:</b> It will start a listener to intercept keys pressed.

<b>readLogs:</b> It will display the logs of keys pressed.

<b>readCredentials:</b> It will show the passwords obtained after detecting a domain (<i>.eiposgrados.edu.es</i>).

<b>delete credentials.txt:</b> Delete the credentials.txt file if it exists.

<b>delete keylog.txt:</b> Delete the keylog.txt file if it exists.

<b>Exit:</b> Exit the script.
