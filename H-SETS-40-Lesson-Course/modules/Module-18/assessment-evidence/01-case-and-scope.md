# Case HSETS-IR-02: unexpected access to a purchasing share

All people, organisations, systems and records below are fictional. These files are authored synthetic evidence, not exports from a real incident. Do not contact addresses or attempt to recreate activity.

At 10:15 UTC on 14 September 2026, a monitoring rule alerted on repeated file-access denials from BUY-WS-07 at the fictional organisation Cedar Training Supplies. You are the junior analyst reviewing the interval 09:55–10:25 UTC. The purchasing team needs normal order processing to continue. No containment has yet been performed.

| Asset | Address | Function |
|---|---|---|
| BUY-WS-07 | 10.50.10.27 | Purchasing workstation; assigned user buyer07 |
| FILE-02 | 10.50.20.12 | Purchasing and restricted archive file server |
| ADMIN-03 | 10.50.10.8 | Approved administrator workstation |

`buyer07` may read Purchasing/Current but is not authorised for Finance/Archive. `svc-stock` is a scheduled inventory service account. Request CHG-214 approves a stock-agent update from ADMIN-03 during 10:00–10:20; it does not authorise a change to buyer07 or finance permissions. The monitoring export uses UTC. Retention covers only the stated interval. Endpoint telemetry is incomplete between 10:08 and 10:12 because collection stopped; the reason is not supplied.

Your authority is evidence review and recommendations only. Do not reset accounts, alter permissions, scan systems or contact external infrastructure. Recommend operational changes with an owner and validation plan.
