---
name: ETF Flows Framework
version: 1
type: domain
domain: etf
applicable_assets: [BTC, ETH]
last_updated: 2025-01-13
sources:
  - SoSoValue ETF data
  - Farside Investors
---

# ETF Flow Analysis Framework

## Overview

This framework provides analysis methodology for spot Bitcoin and Ethereum ETF flows. ETF data represents institutional demand and is a key indicator for price direction.

## Institutional Flow Mechanics

### How ETF Flows Impact Price
1. **Net Inflows**: Issuers must purchase underlying asset to back new shares
2. **Net Outflows**: Issuers may sell underlying to meet redemptions
3. **Large sustained flows**: Direct supply/demand impact on spot markets

### Flow Timing
- ETF flows are reported with ~1 day delay
- Trading day flows announced after market close
- Weekend accumulation reflected in Monday flows

## Flow Classification

### Daily Flow Magnitude

| Flow Size | Classification | Significance |
|-----------|----------------|--------------|
| > $500M | Massive | Major institutional move, price impact expected |
| $200M - $500M | Large | Significant institutional interest |
| $50M - $200M | Moderate | Normal institutional activity |
| < $50M | Small | Retail or rebalancing activity |

### Flow Streak Analysis

| Streak Type | Duration | Implication |
|-------------|----------|-------------|
| Inflow streak | 5+ days | Strong institutional accumulation |
| Outflow streak | 5+ days | Institutional distribution |
| Alternating | N/A | Indecision, rotation |

## ETF-Specific Considerations

### GBTC Dynamics (BTC)
- GBTC had massive legacy holdings from Grayscale Trust
- Initial outflows were trust-to-ETF rotation, not net selling
- GBTC now in equilibrium, flows more meaningful
- Higher fee structure = eventual migration to cheaper ETFs

### Issuer Analysis

| Issuer | Characteristics |
|--------|-----------------|
| BlackRock (IBIT) | Largest AUM, institutional benchmark |
| Fidelity (FBTC) | Strong retail distribution |
| Grayscale (GBTC) | Legacy, higher fees, outflow bias |
| Bitwise | Crypto-native, smaller but growing |
| ARK/21Shares | Thematic investors |

### AUM Ranking Signals
- AUM concentration in top 2-3 = institutional preference
- AUM redistribution = fee competition effects
- Rapid AUM growth in new entrant = strong demand

## Flow Analysis Techniques

### Net Flow Trend
- 7-day moving average smooths noise
- 30-day cumulative shows trend
- Compare current vs historical average

### Flow vs Price Correlation
- Flows leading price = institutional front-running
- Flows lagging price = institutional following retail
- Divergence = potential reversal signal

### Cumulative Flow Analysis
- All-time cumulative = total institutional exposure
- Rate of change = acceleration/deceleration
- Plateaus = absorption periods

## Trading Signals

### Bullish ETF Signals
- Multi-day inflow streak accelerating
- Inflows during price weakness (accumulation)
- AUM making new ATH
- GBTC outflows slowing/reversing

### Bearish ETF Signals
- Multi-day outflow streak accelerating
- Outflows during price strength (distribution)
- AUM growth stalling
- Large single-day outflows

### Neutral/Caution Signals
- Choppy flows with no clear direction
- Small daily flows (< $50M)
- Offsetting flows between issuers

## NAV Premium/Discount

### Premium Analysis

| NAV Premium | Interpretation |
|-------------|----------------|
| > +2% | Strong demand, authorized participants can't create fast enough |
| +0.5% to +2% | Normal demand |
| -0.5% to +0.5% | Fair value, efficient market |
| -0.5% to -2% | Slight selling pressure |
| < -2% | Strong selling pressure, potential buying opportunity |

### Premium Trading
- Persistent premium = demand exceeds supply
- Premium collapse = demand exhaustion
- Discount = often a contrarian buy signal

## Cross-Market Integration

### ETF Flows vs Perpetual Futures
- ETF inflows + negative funding = strong bullish
- ETF outflows + positive funding = distribution
- Divergence between spot (ETF) and derivatives = tension

### ETF Flows vs On-Chain
- ETF inflows + exchange outflows = mega bullish (double accumulation)
- ETF outflows + exchange inflows = mega bearish (double distribution)

## Trading Considerations

### ETF-Informed Perps Trading

**Entry Timing**
- **Best Long Setup**: Strong inflow streak + price at support + neutral/negative funding
- **Best Short Setup**: Strong outflow streak + price at resistance + elevated funding

**Position Sizing**
- Scale position with flow magnitude
- Larger position on >$200M flow days
- Smaller position on choppy flow periods

### Risk Management
- ETF data is delayed - price may have already moved
- Single-day flows can be noisy
- Focus on 3-5 day trends, not individual days
- Monitor GBTC specifically for early warning

### Limitations
- Data delay means you're always trading on lagging info
- Issuers may pre-position before flow announcements
- Authorized participant activity can mask true demand
- Weekend flows are unknown until Monday
