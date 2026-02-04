---
name: Volatility Regime & Fragility Detection Framework
version: 1.0
type: domain
domain: volatility_regime
applicable_assets: [BTC, ETH]
last_updated: 2026-01-18
sources:
  - Benjamin Cowen Crypto Risk Memo Q1 2026
  - Into The Cryptoverse Research
---

# Volatility Regime & Fragility Detection Framework v1.0

## Overview

This framework classifies volatility regimes and detects market fragility conditions. Sustained volatility compression following a multi-year advance reflects declining participation and risk appetite - historically preceding either sharp repricing or extended stagnation, not renewed bull markets.

**Key Principle:** Low volatility at cycle highs is not stability - it is fragility.

---

## Module 1: Volatility Regime Classification

### 1.1 By Historical Percentile

| Percentile | Classification | Market Interpretation |
|------------|----------------|----------------------|
| > 90th | EXTREME_HIGH | Capitulation / blow-off top |
| 70th - 90th | HIGH | Active trend, elevated risk |
| 30th - 70th | NORMAL | Healthy market conditions |
| 10th - 30th | LOW | Compression, watch for expansion |
| < 10th | EXTREME_LOW | Fragility warning, breakout imminent |

### 1.2 By Absolute Level (30-Day Realized Vol)

| 30-Day Vol | Classification | BTC-Specific Context |
|------------|----------------|---------------------|
| > 80% | EXTREME_HIGH | Crisis / capitulation event |
| 60% - 80% | HIGH | Active bear or blow-off top |
| 40% - 60% | ELEVATED | Normal bull market volatility |
| 25% - 40% | NORMAL | Consolidation / range |
| 15% - 25% | LOW | Compression phase |
| < 15% | EXTREME_LOW | Rare, breakout imminent |

### 1.3 By Timeframe (Multi-Scale Analysis)

| Timeframe | Use Case | Signal Reliability |
|-----------|----------|-------------------|
| 7-Day Vol | Short-term momentum | High noise, quick signals |
| 30-Day Vol | Medium-term regime | Primary indicator |
| 90-Day Vol | Trend regime | Macro context |
| 180-Day Vol | Cycle positioning | Historical comparison |

---

## Module 2: Compression-Expansion Cycle

### 2.1 Volatility Cycle Phases

| Phase | Characteristics | Duration | Next Phase |
|-------|-----------------|----------|------------|
| **COMPRESSION** | Declining vol, range-bound | 2-8 weeks | Expansion |
| **EXPANSION** | Rising vol, trending | 1-4 weeks | Peak |
| **PEAK** | Extreme vol, capitulation | Days | Mean reversion |
| **MEAN_REVERSION** | Vol normalizing | 2-4 weeks | Compression or Expansion |

### 2.2 Compression Detection

| Signal | Threshold | Interpretation |
|--------|-----------|----------------|
| 30-day vol < 90-day vol | > 25% lower | COMPRESSION_ACTIVE |
| Bollinger Band width | < 20th percentile | BANDS_SQUEEZE |
| Daily range (ATR) | Declining 2+ weeks | RANGE_NARROWING |
| IV vs RV | IV < RV | CHEAP_VOL (buy options) |

### 2.3 Expansion Trigger Signals

| Signal | Interpretation |
|--------|----------------|
| Band squeeze + directional break | Expansion beginning |
| Vol spike > 2x 20-day average | Expansion confirmed |
| Trend resumption after compression | Directional expansion |
| News catalyst | Event-driven expansion |

---

## Module 3: Late-Cycle Volatility Patterns

### 3.1 Fragility Detection

**Key Insight:** Low volatility at highs = fragility, not stability.

| Context | Low Vol Interpretation | Risk |
|---------|----------------------|------|
| Near ATH | FRAGILITY | High - susceptible to sharp repricing |
| Mid-range | CONSOLIDATION | Moderate - directional uncertainty |
| Near lows | CAPITULATION_EXHAUSTION | Lower - selling pressure exhausted |

### 3.2 Late-Cycle Vol Characteristics

| Observation | Bull Market | Late Cycle / Distribution |
|-------------|-------------|-------------------------|
| Vol trend | Elevated but controlled | Compressing at highs |
| Participation | Broad, rising activity | Narrow, declining activity |
| Rally character | Strong trends | Choppy, countertrend rallies |
| Correction character | V-shaped recoveries | Extended, grinding |

### 3.3 2025 Cycle Vol Pattern

Per Benjamin Cowen analysis:
- 180-day BTC volatility at ~1.87% (historically low)
- Compression following multi-year advance
- Declining participation and risk appetite
- Pattern precedes sharp repricing OR extended stagnation

---

## Module 4: Cross-Asset Volatility Comparison

### 4.1 BTC vs SPX Volatility Ratio

| Ratio (BTC Vol / VIX) | Classification | Interpretation |
|----------------------|----------------|----------------|
| > 5x | BTC_VOL_EXTREME | Crypto-specific stress |
| 3x - 5x | BTC_VOL_ELEVATED | Normal crypto premium |
| 2x - 3x | CONVERGING | Institutionalization effect |
| < 2x | BTC_VOL_LOW | Unusual - watch for expansion |

### 4.2 Volatility Correlation

| Correlation | Market State |
|-------------|--------------|
| BTC vol rising + VIX rising | Risk-off across assets |
| BTC vol rising + VIX stable | Crypto-specific event |
| BTC vol falling + VIX rising | Decoupling (rare) |
| BTC vol falling + VIX falling | Low vol everywhere |

### 4.3 Post-ETF Volatility Dynamics

| Metric | Pre-ETF (2023) | Post-ETF (2024-2025) |
|--------|----------------|----------------------|
| Average daily volatility | ~4.2% | ~1.8% |
| Weekend vol share | 28% | 16% |
| US session vol share | 25-30% | 38-57% |
| Institutional dampening | Limited | Significant |

---

## Module 5: Signal Templates

### 5.1 VOL_COMPRESSION_LATE_CYCLE Signal

**Trigger Conditions:**
- Price within 20% of cycle ATH
- 30-day vol < 25th percentile (historical)
- 30-day vol < 90-day vol by > 20%
- Participation declining (ADI falling)

**Signal Classification:**

| Conditions Met | Signal Strength |
|----------------|-----------------|
| 2 of 4 | EARLY_WARNING |
| 3 of 4 | MODERATE |
| 4 of 4 | STRONG |

**Interpretation:** Market vulnerable to sharp move. Low vol at highs = fragility.

### 5.2 FRAGILITY_WARNING Signal

**Trigger Conditions:**
- Price at or near ATH
- Realized vol < 20% annualized
- Social engagement muted vs price
- Breadth diverging from price

**Action:** Do not interpret low vol as stability. Reduce leverage, tighten stops.

### 5.3 CONSTRUCTIVE_VOL_EXPANSION Signal

**Trigger Conditions:**
- Price rising from support
- Vol expanding (30-day > 90-day)
- Breadth improving
- Volume increasing

**Interpretation:** Healthy regime transition. Vol expansion supporting price discovery.

### 5.4 CAPITULATION_VOL_SPIKE Signal

**Trigger Conditions:**
- 30-day vol > 90th percentile
- Price down > 20% in 30 days
- Extreme negative funding
- Exchange inflows spiking

**Interpretation:** Capitulation event. Watch for vol mean-reversion = potential bottom.

---

## Module 6: Scenario Templates

### 6.1 LATE_CYCLE_FRAGILITY Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Price | Within 15% of ATH | [ ] |
| 30-day vol | < 30th percentile | [ ] |
| Vol trend | Declining for > 4 weeks | [ ] |
| Participation | ADI falling | [ ] |
| Social engagement | < 50% of 2021 peak | [ ] |

**Require 4+ conditions for LATE_CYCLE_FRAGILITY**

**Interpretation:**
- Low vol is NOT stability at cycle highs
- Market susceptible to sharp repricing
- Expect either sharp correction OR extended stagnation
- NOT conducive to renewed bull market

### 6.2 HEALTHY_VOL_REGIME Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Vol | 30th - 70th percentile | [ ] |
| Vol trend | Stable or rising | [ ] |
| Participation | ADI stable or rising | [ ] |
| Corrections | V-shaped recoveries | [ ] |

**Require 3+ conditions for HEALTHY_VOL_REGIME**

**Interpretation:** Normal market conditions. Trend strategies appropriate.

### 6.3 EXTREME_VOL_CAPITULATION Detection

| Condition | Check | Status |
|-----------|-------|--------|
| 30-day vol | > 80th percentile | [ ] |
| Drawdown | > 30% from local high | [ ] |
| Funding | Extremely negative | [ ] |
| Fear & Greed | < 20 | [ ] |

**Require 3+ conditions for CAPITULATION event**

**Interpretation:** Potential bottom forming. Watch for vol mean-reversion signal.

---

## Module 7: Volatility Regime Trading Implications

### 7.1 Strategy by Vol Regime

| Vol Regime | Appropriate Strategy | Position Sizing |
|------------|---------------------|-----------------|
| EXTREME_LOW | Long straddles, expect expansion | Reduced directional |
| LOW | Reduce leverage, expect expansion | Conservative |
| NORMAL | Trend-following, standard methods | Normal |
| HIGH | Mean-reversion, range trading | Reduced |
| EXTREME_HIGH | Fade extremes, accumulate dips | Very conservative |

### 7.2 Options Strategy by Vol Regime

| Vol Regime | Options Strategy |
|------------|------------------|
| EXTREME_LOW | Buy options (cheap vol) |
| LOW | Long gamma, long straddles |
| NORMAL | Balanced approach |
| HIGH | Sell premium (expensive vol) |
| EXTREME_HIGH | Short vol if IV > RV |

---

## Module 8: Data Sources

### 8.1 Required Tables

| Table | Metrics Used |
|-------|-------------|
| `price_history` | volatility_24h, volatility_7d, high, low, close |
| `options_snapshots` | implied_vol (BTC, ETH) |
| `macro_data` | VIX |
| `derived_volatility_metrics` | percentile rankings |

### 8.2 Key Calculations

```sql
-- 30-day realized volatility
SELECT
  STDDEV(LN(close / LAG(close) OVER (ORDER BY date))) * SQRT(365) * 100
  AS realized_vol_30d
FROM price_history
WHERE symbol = 'BTC'
  AND date > CURRENT_DATE - INTERVAL '30 days';

-- Vol percentile (1-year lookback)
SELECT
  PERCENT_RANK() OVER (ORDER BY vol_30d) AS vol_percentile
FROM volatility_history
WHERE date > CURRENT_DATE - INTERVAL '365 days';
```

---

## Module 9: Output Format Examples

### Standard Volatility Analysis

```
**Volatility Regime Analysis for BTC**

**Current Regime:** LOW_VOL_FRAGILITY
- 30-Day Realized Vol: 22% (annualized)
- Percentile (1Y): 18th percentile
- 180-Day Vol: 1.87%

**Compression Status:** ACTIVE
- 30-day vol < 90-day vol by 28%
- Bollinger Band width: 15th percentile
- Duration: 6 weeks

**Context Assessment:** LATE_CYCLE_FRAGILITY
- Price: Within 15% of ATH
- Participation: Declining (ADI falling)
- Social engagement: Muted

**Fragility Warning:**
Low volatility at cycle highs is NOT stability.
This environment historically precedes:
1. Sharp repricing (sudden correction)
2. Extended stagnation (grinding consolidation)
NOT renewed bull market.

**Cross-Asset Context:**
- BTC Vol / VIX ratio: 2.1x (converging)
- Institutionalization dampening crypto-specific vol
- Weekend trading at all-time low (16%)

**Recommendation:**
- Reduce leverage
- Expect vol expansion (direction uncertain)
- Do not interpret low vol as stability
```

### Alert-Style Output

```
**VOLATILITY ALERT: Late-Cycle Fragility Detected**

30-day realized vol at 18th percentile while price near ATH.
This is NOT stability - it is FRAGILITY.

Pattern matches:
- 2019 pre-H2-selloff compression
- 2021 Q2 pre-crash compression

Compression at highs + declining participation =
Sharp repricing OR extended stagnation ahead

Action: Reduce leverage, prepare for vol expansion.
Watch for: Vol spike > 2x average = regime transition
```
