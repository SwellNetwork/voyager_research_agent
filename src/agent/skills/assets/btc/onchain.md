---
name: BTC On-Chain Agent
version: 1
asset: BTC
type: overlay
domain: onchain
requires: [base]
last_updated: 2025-01-13
sources:
  - templates/report_prompts.py (ON_CHAIN_VALUATION_FRAMEWORK)
---

# BTC On-Chain Analysis

## Overview

Bitcoin has the richest on-chain dataset of any cryptocurrency, with 15+ years of transparent blockchain data. On-chain analysis for BTC focuses on:
- **Holder Behavior**: LTH/STH distribution, accumulation patterns
- **Network Valuation**: MVRV, NUPL, SOPR metrics
- **Supply Dynamics**: Exchange flows, miner behavior
- **Cycle Positioning**: Where are we in the 4-year halving cycle?

## MVRV Analysis (Deep Dive)

### MVRV Z-Score Interpretation

The MVRV Z-Score normalizes Market Value vs Realized Value to identify over/undervaluation relative to history.

| Z-Score | Historical Context | Trading Implication |
|---------|-------------------|---------------------|
| > 7.0 | 2011 peak only | Extreme bubble, immediate distribution |
| 5.0 - 7.0 | 2013, 2017 peaks | Major cycle top zone |
| 3.5 - 5.0 | Late 2017, Late 2021 | Distribution begins |
| 2.0 - 3.5 | Mid-bull runs | Elevated but sustainable |
| 0.5 - 2.0 | Most of bull markets | Healthy accumulation zone |
| 0.0 - 0.5 | Late bear markets | Strong buy zone |
| -0.5 - 0.0 | 2015, 2018, 2022 lows | Generational buying opportunity |
| < -0.5 | Extreme capitulation | Maximum opportunity (rare) |

### MVRV Trend Analysis
- **Rising MVRV + Rising Price**: Healthy bull market
- **Flat MVRV + Rising Price**: Late-stage speculation (caution)
- **Falling MVRV + Falling Price**: Bear market confirmation
- **Rising MVRV + Flat Price**: Accumulation in progress

## NUPL (Net Unrealized Profit/Loss)

NUPL measures the aggregate profit/loss of all BTC holders.

| NUPL Range | Phase | Description |
|------------|-------|-------------|
| > 0.75 | Euphoria | Extreme greed, distribution imminent |
| 0.50 - 0.75 | Belief | Strong conviction, bull market |
| 0.25 - 0.50 | Optimism | Healthy uptrend |
| 0.00 - 0.25 | Hope/Fear | Transition zone |
| -0.25 - 0.00 | Anxiety | Bear market, weak hands selling |
| < -0.25 | Capitulation | Maximum pain, cycle bottom zone |

### NUPL Trading Signals
- **NUPL crossing 0.5 from below**: Bull market confirmation
- **NUPL crossing 0.75**: Begin scaling out
- **NUPL crossing 0 from above**: Bear market beginning
- **NUPL < -0.25**: Aggressive accumulation zone

## SOPR (Spent Output Profit Ratio)

SOPR measures whether coins being moved are in profit or loss.

| SOPR Value | Interpretation |
|------------|----------------|
| > 1.05 | Profit-taking (healthy in uptrend) |
| 1.00 - 1.05 | Neutral |
| 0.95 - 1.00 | Loss-taking, capitulation in progress |
| < 0.95 | Heavy capitulation |

### SOPR Analysis for BTC

- **SOPR > 1 consistently**: Bull market, holders in profit
- **SOPR dips to 1.0 in uptrend**: "Reset" - healthy correction, often buying opportunity
- **SOPR < 1 consistently**: Bear market, holders underwater
- **SOPR spikes above 1 in downtrend**: Relief rally, likely to fade

### LTH-SOPR vs STH-SOPR
- **LTH-SOPR**: Long-term holder behavior (155+ days)
- **STH-SOPR**: Short-term holder behavior (<155 days)
- LTH-SOPR elevated + STH-SOPR low = Distribution to new buyers (late cycle)
- LTH-SOPR low + STH-SOPR capitulating = Cycle bottom

## Exchange Flow Analysis

### Exchange Balance Trends

| Trend | Interpretation |
|-------|----------------|
| Sustained outflows | Accumulation, bullish long-term |
| Sustained inflows | Preparation for selling, bearish |
| Large single deposit | Whale selling imminent (watch) |
| Large single withdrawal | OTC deal or cold storage (neutral-bullish) |

### Exchange Reserve Metrics
- **All-time low reserves**: Extreme supply squeeze potential
- **Reserves rising from lows**: Caution, selling pressure building
- **Stablecoin inflows + BTC outflows**: Dry powder ready to buy

### Whale Transaction Monitoring
- Transactions > 1000 BTC: Significant market impact
- Whale-to-exchange flows: Selling pressure
- Exchange-to-whale flows: Accumulation
- Whale-to-whale flows: OTC, minimal market impact

## Holder Cohort Analysis

### Long-Term Holders (LTH)
- Definition: Coins held > 155 days
- LTH accumulating = Bullish long-term
- LTH distributing = Late cycle warning

### Short-Term Holders (STH)
- Definition: Coins held < 155 days
- STH cost basis = Key support/resistance level
- STH in loss for extended period = Capitulation

### Entity-Adjusted Metrics
- Remove exchange movements and internal transfers
- Cleaner signal of actual holder behavior

## Miner Metrics

### Hash Ribbons
- 30-day MA crossing below 60-day MA = Miner capitulation
- Ribbon inversion often marks cycle bottoms
- Hash rate recovery = Network strength returning

### Miner Revenue/Outflows
- High miner outflows post-halving = Selling pressure (normal)
- Miner reserves depleting = Forced selling (bearish short-term)
- Miner accumulation = Confidence in higher prices

### Difficulty Adjustment
- Positive adjustment = Healthy competition, bullish
- Negative adjustment = Miner exit, short-term pressure
- Watch for correlation with price action

## Halving Cycle Context

### Historical Pattern

| Phase | Timing | Characteristics |
|-------|--------|-----------------|
| Post-Halving Consolidation | 0-6 months | Supply shock not yet felt |
| Acceleration | 6-12 months | Parabolic move begins |
| Euphoria | 12-18 months | Cycle peak formation |
| Distribution | 18-24 months | Smart money exits |
| Bear Market | 24-36 months | 70-80% drawdown |
| Accumulation | 36-48 months | Cycle bottom, LTH accumulate |

### Current Cycle Positioning
- Identify days since last halving
- Compare on-chain metrics to same phase in prior cycles
- Adjust for macro context (rates, liquidity)

## On-Chain Confluence Scoring

For high-conviction signals, look for multiple metrics aligning:

### Bullish Confluence (3+ signals)
- MVRV Z-Score < 1.0
- NUPL < 0.25
- SOPR reset to 1.0
- Exchange outflows sustained
- LTH accumulating

### Bearish Confluence (3+ signals)
- MVRV Z-Score > 3.0
- NUPL > 0.65
- SOPR elevated with price stalling
- Exchange inflows rising
- LTH distributing
