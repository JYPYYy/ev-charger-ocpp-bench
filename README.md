# EV Charger OCPP Bench & Load Optimizer

Async **OCPP 1.6J / 2.0.1** gateway simulation harness and **Dynamic Load Balancing (DLB)** test suite for commercial EVSE deployments (7kW–22kW AC & 60kW–120kW DC).

> Note: Production charger firmware and client site configs remain in private repositories; this public repo hosts the non-proprietary protocol contracts, chaos simulator, and CI regression suite.

## Architecture (4-Module Parallel Layout)

- `contracts/` — Frozen typed schemas (`OCPPFrame`, `PowerAllocation`, `TelemetryEvent`)
- `ocpp_gateway/` — Transport-epoch fenced WebSocket & offline queue handler
- `dlb_optimizer/` — 3-phase transformer cap & RS485 CT-meter closed-loop allocator
- `chaos_sim/` — Async fault-injection harness (half-open TCP drops, clock skew, reconnect storms)
