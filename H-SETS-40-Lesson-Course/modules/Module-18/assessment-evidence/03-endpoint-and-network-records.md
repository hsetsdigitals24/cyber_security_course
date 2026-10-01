# Synthetic endpoint and network records

These records are authored summaries. They are not a PCAP and cannot be used to demonstrate Wireshark filtering or packet hash verification.

| Record | UTC time | Source | Observation |
|---|---|---|---|
| P01 | 10:03:50 | BUY-WS-07 process summary | explorer.exe launched stock-viewer.exe in buyer07 session; signature status not collected |
| P02 | 10:07:45 | BUY-WS-07 process summary | stock-viewer.exe opened a recent-paths configuration; contents unavailable |
| P03 | 10:08–10:12 | Collector health | Endpoint event collection unavailable; cause unknown |
| P04 | 10:12:03 | Collector health | Event collection resumed |
| N01 | 10:04:10–10:14:05 | Firewall flow summary | BUY-WS-07 to FILE-02 TCP 445 allowed; 92000 bytes sent, 410000 received |
| N02 | 10:06:00 | DNS summary | BUY-WS-07 requested updates.vendor.example; response 192.0.2.80 |
| N03 | 10:06:02–10:06:14 | Firewall flow summary | BUY-WS-07 to 192.0.2.80 TCP 443 allowed; 3200 bytes sent, 180000 received |
| N04 | 10:15:00 | Monitoring | Three denied Finance/Archive reads by buyer07 triggered rule FILE-DENIAL-BURST |

Network counters are from the workstation's direction. They include protocol traffic and do not identify transferred document contents. No decryption, packet payload or process-to-flow correlation is supplied. The domain and address are documentation-only placeholders; their appearance does not establish maliciousness. The supplied export has no other external flows, but export completeness outside its stated scope is unknown.
