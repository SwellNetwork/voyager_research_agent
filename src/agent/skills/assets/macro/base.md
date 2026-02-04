---
name: MACRO Analysis Agent
version: 1
asset: MACRO
type: base
last_updated: 2025-01-13
sources:
  - templates/report_prompts.py
  - FRED economic data frameworks
---

# Macro Analysis Framework

## Overview

Cross-asset macroeconomic analysis framework for understanding how traditional finance conditions impact cryptocurrency markets. This framework applies to all crypto assets but is particularly important for BTC due to its correlation with macro factors.

## Primary Macro Indicators

| Indicator | Description | Crypto Impact |
|-----------|-------------|---------------|
| **DXY (Dollar Index)** | US Dollar strength vs basket | Inverse correlation with crypto |
| **Fed Funds Rate** | Federal Reserve target rate | Higher rates = lower risk appetite |
| **10Y Treasury Yield** | Long-term rate expectations | Competes with crypto yield |
| **M2 Money Supply** | Global liquidity proxy | Strong correlation with BTC |
| **VIX** | Equity volatility index | Risk-off indicator |
| **SPY/QQQ** | US equity indices | Risk appetite correlation |
| **Gold** | Traditional safe haven | Alternative to BTC |

## Macro Regime Classification

### Liquidity Regime Framework

| Liquidity Condition | DXY | M2 Growth | Fed Policy | Crypto Implication |
|--------------------|-----|-----------|------------|-------------------|
| **Abundant** | Falling | >6% | Easing | Strongly Bullish |
| **Normal** | Stable | 3-6% | Neutral | Neutral |
| **Tight** | Rising | <3% | Tightening | Bearish |
| **Crisis** | Spiking | Negative | Emergency | Initially bearish, then bullish |

### Rate Environment Framework

| Fed Funds Rate | 10Y Yield | Yield Curve | Crypto Impact |
|----------------|-----------|-------------|---------------|
| Rising | Rising | Steepening | Risk-off, bearish crypto |
| Rising | Falling | Flattening | Mixed, volatility up |
| Falling | Falling | Bull flattening | Risk-on, bullish crypto |
| Falling | Rising | Bear steepening | Uncertainty, volatile |

### Dollar Strength Framework

| DXY Level | Trend | Implication |
|-----------|-------|-------------|
| > 110 | Rising | Strong headwind for crypto |
| 105-110 | Stable | Mild headwind |
| 100-105 | Stable | Neutral |
| 95-100 | Falling | Tailwind for crypto |
| < 95 | Falling | Strong tailwind |

## Key Thresholds

### Dollar (DXY)
- **Strong Headwind**: DXY > 107
- **Neutral**: DXY 100-107
- **Tailwind**: DXY < 100
- **Major Resistance**: 110
- **Major Support**: 95

### Interest Rates
- **Restrictive**: Fed Funds > 4.5%
- **Neutral**: Fed Funds 2.5-4.5%
- **Accommodative**: Fed Funds < 2.5%
- **10Y Yield High**: > 4.5% (competes with crypto)
- **10Y Yield Low**: < 3% (favorable for crypto)

### Global Liquidity
- **M2 Growth Bullish**: > 5% YoY
- **M2 Growth Bearish**: < 2% YoY
- **Balance Sheet Expansion**: Fed assets growing
- **QT Pressure**: Fed assets shrinking > $60B/month

### Risk Indicators
- **VIX Elevated**: > 25 (risk-off)
- **VIX Extreme**: > 35 (capitulation/opportunity)
- **VIX Low**: < 15 (complacency)

## Correlation Framework

### BTC-Macro Correlations to Monitor

| Asset | Normal Correlation | Notes |
|-------|-------------------|-------|
| **SPY** | 0.3-0.6 | Higher during risk-off |
| **QQQ** | 0.4-0.7 | Tech correlation |
| **Gold** | 0.1-0.3 | Decoupling possible |
| **DXY** | -0.3 to -0.6 | Inverse relationship |
| **10Y Yield** | -0.2 to -0.4 | Rate sensitivity |

### Correlation Regime Changes

| Condition | BTC-SPY Correlation | Interpretation |
|-----------|---------------------|----------------|
| Risk-On Rally | 0.5-0.8 | BTC = levered beta |
| Risk-Off Crash | 0.7-0.9 | Everything sells together |
| Crypto Decoupling | < 0.3 | Idiosyncratic crypto drivers |
| Flight to Safety | Negative | BTC as hedge (rare) |

## Economic Calendar Framework

### High-Impact Events

| Event | Frequency | Expected Impact |
|-------|-----------|-----------------|
| **FOMC Decision** | 8x/year | Major volatility |
| **CPI Release** | Monthly | Direction-setting |
| **NFP Jobs Report** | Monthly | Risk sentiment |
| **GDP Release** | Quarterly | Macro narrative |
| **PCE Inflation** | Monthly | Fed's preferred measure |

### Event Positioning Guide

| Event | Pre-Event | Post-Event (Dovish) | Post-Event (Hawkish) |
|-------|-----------|---------------------|---------------------|
| FOMC | Reduce size | Rally, buy dips | Sell rallies |
| CPI | Reduce size | Risk-on | Risk-off |
| NFP | Reduce size | Depends on read | Depends on read |

## Global Macro Factors

### International Considerations

| Factor | Impact on Crypto |
|--------|-----------------|
| **China Stimulus** | Liquidity injection, bullish |
| **ECB Policy** | Euro weakness = DXY strength |
| **BOJ Policy** | Yen carry trade impacts |
| **Emerging Market Stress** | Risk-off, initially bearish |
| **Geopolitical Risk** | Volatility, safe haven flows |

### Global Liquidity Proxy

Track the sum of major central bank balance sheets:
- Federal Reserve
- ECB
- BOJ
- PBOC

**Rule of Thumb**: Global liquidity rising = bullish crypto backdrop

## Crypto-Specific Macro Factors

### Stablecoin Supply

| Metric | Bullish | Neutral | Bearish |
|--------|---------|---------|---------|
| USDT Market Cap | Rising | Stable | Falling |
| USDC Market Cap | Rising | Stable | Falling |
| Total Stablecoin Supply | ATH | Stable | Declining |

### ETF Flows (BTC/ETH)

| Flow Pattern | Implication |
|--------------|-------------|
| Sustained Inflows > $500M/day | Strong institutional demand |
| Steady Inflows $100-500M/day | Healthy accumulation |
| Mixed Flows | Neutral, watch trend |
| Sustained Outflows | Institutional distribution |

## Macro Regime Playbook

### Risk-On Environment
- DXY falling or stable low
- Fed dovish or cutting
- VIX < 20
- Equities in uptrend
- **Crypto Strategy**: Long, increase position size

### Risk-Off Environment
- DXY rising sharply
- Fed hawkish or hiking
- VIX > 25
- Equities falling
- **Crypto Strategy**: Reduce exposure, hedge

### Uncertainty/Transition
- Mixed signals across indicators
- Fed pivoting
- Economic data conflicting
- **Crypto Strategy**: Reduce size, wait for clarity

## Analysis Template

When conducting macro analysis, address:

1. **Current Regime**: Liquidity abundant/tight, rates rising/falling
2. **Dollar Outlook**: DXY trend and key levels
3. **Fed Expectations**: What's priced in vs likely outcome
4. **Risk Appetite**: VIX, equity trends, credit spreads
5. **Global Context**: Major central bank divergence
6. **Crypto-Specific**: ETF flows, stablecoin supply
7. **Calendar Risks**: Upcoming events that could shift narrative
8. **Correlation Watch**: Is crypto trading with or against macro?
