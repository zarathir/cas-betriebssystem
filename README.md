# cas-betriebssystem

## Aufgaben 2023-04-18

- 07_Koordiantion und Synchronisation
- Interrupthandler in der CPU
- ping-pong programmieren mit Threads (1 Thread sendet `ping`, der andere antwortet mit `pong`)

## Notizen Prüfung

Verständnis:

- Wie funktioniert was?
  - Interrupts
  - Was ist ein Prozess/Thread
  - Wie funktioniert IPC
- Wie funktioniert virt. Speicher
- mehrere Akteure und Ressourcen
  - Probleme?
    - Daten gehen verloren/kaputt...
    - Races
      - Lösung:
        - Mutex, Semaphore
    - Buffer
      - shared data
      - sync: Mutex, Semaphore, Monitor, usw.
    - Polling
      - wie macht man das?
        - condition variablen
          - wait(condition)
          - signal(condition)
