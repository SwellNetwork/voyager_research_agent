---
name: BTC Macro Agent
version: 1
asset: BTC
type: overlay
domain: macro
requires: [base]
last_updated: 2025-01-13
sources:
  - templates/report_prompts.py (MACRO_CORRELATION_FRAMEWORK)
---

# BTC Macro Analysis

## Overview

Bitcoin's correlation with traditional macro factors has evolved significantly since 2020. Understanding macro context is essential for BTC analysis, particularly:
- **Monetary Policy**: Fed rates, QE/QT, global liquidity
- **Dollar Dynamics**: DXY strength/weakness
- **Risk Sentiment**: VIX, equity correlation
- **Institutional Adoption**: ETF flows, treasury holdings

## Dollar Correlation (DXY)

### BTC-DXY Relationship

BTC typically exhibits inverse correlation with the US Dollar Index (DXY):

| DXY Trend | BTC Implication | Confidence |
|-----------|-----------------|------------|
| DXY breaking down | Bullish for BTC | High |
| DXY strengthening | Headwind for BTC | High |
| DXY range-bound | Other factors dominate | Medium |

### Key DXY Levels
- **DXY > 110**: Strong dollar, significant BTC headwind
- **DXY 100-110**: Moderate dollar strength
- **DXY 95-100**: Neutral zone
- **DXY < 95**: Weak dollar, tailwind for BTC

### Correlation Breakdown
- Correlation strengthens during macro stress
- Decoupling possible during crypto-specific catalysts
- Watch for divergence as leading indicator

## Interest Rate Environment

### Fed Policy Impact

| Rate Environment | BTC Implication |
|------------------|-----------------|
| Rate cuts (dovish pivot) | Strongly bullish |
| Rate pause | Neutral to bullish |
| Rate hikes | Bearish headwind |
| Emergency cuts | Volatility spike, then bullish |

### Real Rates
- Negative real rates (inflation > nominal rates): Bullish for BTC
- Positive real rates: Bearish, opportunity cost rises
- Watch TIPS yields as proxy

### Fed Balance Sheet
- QE (balance sheet expansion): Risk-on, bullish BTC
- QT (balance sheet contraction): Risk-off, bearish BTC
- Pivot signals often precede BTC rallies

## Global Liquidity

### M2 Money Supply

BTC often correlates with global M2 money supply growth:

| M2 Trend | BTC Implication |
|----------|-----------------|
| M2 accelerating | Bullish (with 3-6 month lag) |
| M2 flat | Neutral |
| M2 contracting | Bearish |

### Liquidity Indicators
- Global M2 aggregate (US + China + EU + Japan)
- Repo market stress (watch for dislocations)
- Credit spreads widening = Risk-off

## Equity Correlation

### BTC-SPX Correlation

| Correlation Level | Context |
|-------------------|---------|
| > 0.8 | High correlation, BTC as risk asset |
| 0.4 - 0.8 | Moderate correlation |
| 0 - 0.4 | Low correlation, crypto-specific drivers |
| < 0 | Negative correlation, safe haven behavior (rare) |

### Correlation Regime Changes
- 2020-2022: High correlation as institutions entered
- Correlation spikes during market stress (March 2020, 2022 bear)
- Decoupling during crypto-specific events

### Equity Index Signals
- SPX/QQQ breaking out: Risk-on, tailwind for BTC
- SPX/QQQ breaking down: Risk-off, headwind
- Divergence (BTC up, equities down): Watch closely

## VIX (Volatility Index)

### VIX-BTC Relationship

| VIX Level | Market Condition | BTC Implication |
|-----------|------------------|-----------------|
| > 40 | Panic | Short-term bearish, medium-term opportunity |
| 25 - 40 | Elevated fear | Cautious |
| 15 - 25 | Normal | Business as usual |
| < 15 | Complacency | Potential correction brewing |

### VIX Spike Analysis
- VIX spike + BTC dump = Correlated risk-off
- VIX elevated but BTC stable = Relative strength, bullish
- VIX collapsing + BTC flat = Risk appetite returning

## Treasury Yields

### Yield Curve Analysis

| Yield Curve | Interpretation |
|-------------|----------------|
| Steepening | Growth expectations, risk-on |
| Flattening | Growth concerns |
| Inversion | Recession warning |
| Dis-inversion | Recession imminent (historically) |

### 10-Year Yield
- Rising yields: Headwind for risk assets including BTC
- Falling yields: Tailwind, especially if Fed-driven
- Yield volatility: Watch MOVE index

## ETF Flow Analysis

### Daily Flow Interpretation

| Flow Type | Magnitude | Signal |
|-----------|-----------|--------|
| Strong inflow | > $500M/day | Institutional demand surge |
| Moderate inflow | $100-500M/day | Steady accumulation |
| Flat | -$100M to +$100M | Balanced/consolidation |
| Moderate outflow | -$100M to -$300M | Profit-taking |
| Strong outflow | < -$300M/day | Institutional selling |

### ETF vs Spot Premium
- Premium = Demand > Supply (bullish)
- Discount = Supply > Demand (caution)
- Arbitrage activity keeps premium/discount tight

### Cumulative Flow Analysis
- Rising cumulative: Sustained institutional demand
- Plateau: Demand exhaustion
- Declining: Institutional exit

## Macro Regime Framework

### Risk-On Regime
- Fed dovish, liquidity expanding
- DXY weakening
- Equities rallying
- VIX low
- **BTC Strategy**: Long with conviction

### Risk-Off Regime
- Fed hawkish, liquidity contracting
- DXY strengthening
- Equities selling off
- VIX elevated
- **BTC Strategy**: Reduce exposure, wait for stabilization

### Transition Regime
- Mixed signals
- Correlation breakdown
- **BTC Strategy**: Crypto-specific factors dominate, use on-chain

## Key Macro Dates to Watch

| Event | Typical Impact |
|-------|----------------|
| FOMC Meetings | High volatility, directional moves |
| CPI Release | Inflation expectations reset |
| NFP/Jobs | Risk sentiment shift |
| Quarterly Opex | Liquidation/positioning unwinds |
| ETF Rebalancing | Flow spikes |

## Macro Confluence Scoring

### Bullish Macro Setup
- Fed pivoting dovish
- DXY weakening
- M2 growth resuming
- VIX declining
- ETF inflows sustained

### Bearish Macro Setup
- Fed hawkish
- DXY strengthening
- M2 contracting
- VIX elevated
- ETF outflows

### Neutral/Mixed
- Conflicting signals across factors
- Focus on crypto-specific catalysts
- Tighter position sizing
