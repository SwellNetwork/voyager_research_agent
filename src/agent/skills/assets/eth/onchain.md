---
name: ETH On-Chain Agent
version: 1
asset: ETH
type: overlay
domain: onchain
requires: [base]
last_updated: 2025-01-13
---

# ETH On-Chain Analysis

## Overview

ETH on-chain analysis requires adjustments from BTC due to:
- Smart contract complexity (not just UTXO transfers)
- Staking dynamics (locked supply)
- DeFi activity (internal transfers)
- L2 migration (activity moving off L1)

## MVRV for ETH

### ETH MVRV Thresholds

ETH MVRV behaves differently from BTC due to faster cycles:

| MVRV Ratio | Classification | Action |
|------------|----------------|--------|
| > 3.0 | Extreme Overvaluation | Distribution zone |
| 2.0 - 3.0 | Overvalued | Reduce exposure |
| 1.2 - 2.0 | Fair to Elevated | Hold, accumulate dips |
| 0.8 - 1.2 | Undervalued | Accumulate |
| < 0.8 | Deeply Undervalued | Strong accumulation |

### MVRV Analysis Notes
- ETH MVRV peaks are often lower than BTC
- Post-Merge dynamics may shift historical patterns
- Watch in conjunction with staking metrics

## NUPL for ETH

| NUPL Range | Phase |
|------------|-------|
| > 0.70 | Euphoria |
| 0.50 - 0.70 | Belief |
| 0.25 - 0.50 | Optimism |
| 0.00 - 0.25 | Hope/Fear |
| < 0.00 | Capitulation |

## Network Activity

### Active Addresses

| Daily Active | Classification |
|--------------|----------------|
| > 600K | High activity |
| 400K - 600K | Normal |
| 200K - 400K | Low |
| < 200K | Very low (caution) |

### Transaction Count
- Include L2 transactions for full picture
- L1 declining while L2 rising = Migration (neutral)
- Both declining = Genuine activity drop (bearish)

## Gas Metrics

### Gas Price Analysis

| Avg Gas (Gwei) | Market State |
|----------------|--------------|
| > 100 | High congestion, strong demand |
| 50 - 100 | Elevated activity |
| 20 - 50 | Normal |
| < 20 | Low activity |

### Burn Rate

| Daily Burn | Interpretation |
|------------|----------------|
| > Issuance | Deflationary (bullish) |
| ≈ Issuance | Neutral |
| < Issuance | Inflationary |

### Priority Fees
- Rising priority fees = Competitive block space
- MEV activity visible in priority fees

## Exchange Flows (ETH-Specific)

### Exchange Balance

| Trend | Interpretation |
|-------|----------------|
| Declining + Staking rising | Supply squeeze (bullish) |
| Declining, no staking increase | Cold storage (bullish) |
| Rising | Selling pressure building |
| Rising from staking withdrawals | Watch for selling |

### Staking Flows
- Net staking deposits = Supply removed
- Net staking withdrawals = Supply returning (selling risk)
- Validator queue length = Demand indicator

## ETH-Specific Holder Analysis

### Holder Cohorts

| Cohort | Definition | Behavior |
|--------|------------|----------|
| Stakers | Locked in PoS | Long-term holders |
| LTH | > 1 year | Diamond hands |
| STH | < 1 year | More reactive |
| DeFi Locked | In protocols | Productive capital |

### Supply Distribution
- Staked supply: ~25-30% of total
- Exchange supply: ~15-20%
- DeFi supply: ~5-10%
- Dormant supply: Remainder

## Smart Contract Activity

### Contract Interactions

| Metric | Bullish | Bearish |
|--------|---------|---------|
| New contracts deployed | Rising | Falling |
| Contract calls | Rising | Falling |
| Unique contracts interacted | Rising | Falling |

### DeFi Protocol Metrics
- TVL in ETH terms (not USD)
- Protocol revenue
- User retention

## Supply Dynamics Post-Merge

### Issuance Analysis

| Metric | Value | Impact |
|--------|-------|--------|
| PoS Issuance | ~4% APY to stakers | Inflationary base |
| EIP-1559 Burn | Variable | Deflationary offset |
| Net Issuance | Burn - Issuance | Key supply metric |

### Deflationary Conditions
- High gas usage + High priority fees = Deflationary
- Low activity = Inflationary
- Track 7-day moving average for trend

## On-Chain Confluence for ETH

### Bullish Signals
- MVRV < 1.2
- Exchange balance declining
- Staking deposits rising
- L2 activity growing
- Gas fees healthy (not dead)

### Bearish Signals
- MVRV > 2.5
- Exchange balance rising
- Staking withdrawals elevated
- DeFi TVL declining in ETH terms
- Gas fees collapsed (no demand)
