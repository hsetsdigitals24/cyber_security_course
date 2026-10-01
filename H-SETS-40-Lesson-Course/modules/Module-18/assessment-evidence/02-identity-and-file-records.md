# Synthetic identity and file records

These are simplified event summaries, not native Windows event exports. A successful logon does not establish who physically used a credential. An allowed read is not proof that content left the organisation.

| Record | UTC time | Source | Observation |
|---|---|---|---|
| I01 | 10:01:02 | FILE-02 authentication | svc-stock network logon succeeded from ADMIN-03 |
| I02 | 10:04:10 | FILE-02 authentication | buyer07 network logon succeeded from BUY-WS-07 |
| F01 | 10:04:14 | FILE-02 file audit | buyer07 read Purchasing/Current/orders.csv; allowed |
| F02 | 10:09:05 | FILE-02 file audit | buyer07 read Finance/Archive/q2.csv; denied |
| F03 | 10:09:07 | FILE-02 file audit | buyer07 read Finance/Archive/vendors.csv; denied |
| F04 | 10:09:10 | FILE-02 file audit | buyer07 read Finance/Archive/bank-changes.csv; denied |
| I03 | 10:10:02 | Directory change summary | No buyer07 membership changes found in supplied interval |
| F05 | 10:13:09 | FILE-02 file audit | buyer07 read Purchasing/Current/orders.csv; allowed |
| I04 | 10:14:00 | Directory authentication summary | No failed buyer07 sign-ins in supplied interval |

The audit selection is restricted to these accounts and paths. No file contents or hashes of accessed files are supplied. Negative observations apply only to this selection and interval.
