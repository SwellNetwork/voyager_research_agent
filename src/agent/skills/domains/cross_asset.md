---
name: Cross-Asset Correlation & Capital Flow Framework
version: 1.0
type: domain
domain: cross_asset
applicable_assets: [BTC, ETH, ALL]
last_updated: 2026-01-18
sources:
  - Benjamin Cowen Crypto Risk Memo Q1 2026
  - Into The Cryptoverse Research
---

# Cross-Asset Correlation & Capital Flow Framework v1.0

## Overview

This framework analyzes cross-asset correlations to understand what type of capital is flowing through markets. Crypto's correlation with equities and other risk assets reveals whether markets are in a risk-on expansion or defensive contraction phase.

**Key Principle:** Correlation breakdowns signal capital segmentation, not broad risk-on behavior. When crypto decorrelates from equities while metals rally, capital is flowing to inflation-hedging assets rather than speculative risk assets.

---

## Module 1: Correlation Regime Framework

### 1.1 BTC-Equity Correlation Classification

| 90-Day Correlation | Classification | Market Interpretation |
|-------------------|----------------|----------------------|
| > 0.7 | STRONG_POSITIVE | Risk-on, liquidity-driven |
| 0.4 - 0.7 | MODERATE_POSITIVE | Normal bull market |
| 0.1 - 0.4 | WEAK_POSITIVE | Transition / uncertainty |
| -0.1 - 0.1 | UNCORRELATED | Decoupled, crypto-specific drivers |
| -0.4 - -0.1 | WEAK_NEGATIVE | Mild defensive behavior |
| < -0.4 | STRONG_NEGATIVE | Flight to safety (rare) |

### 1.2 Historical Correlation Patterns

| Period | BTC-SPX Correlation | Context |
|--------|---------------------|---------|
| 2020-2021 Bull | 0.6 - 0.8 | Liquidity-driven, risk-on |
| 2022 Bear | 0.7 - 0.9 | Correlated selloff |
| Late 2023-2024 | 0.3 - 0.5 | ETF-driven normalization |
| 2025 (current) | 0.0 - 0.3 | Decoupling, capital segmentation |

### 1.3 Correlation Regime Transitions

| Transition | Signal | Implication |
|------------|--------|-------------|
| Rising correlation | Crypto joining risk-on | Bullish (if equities rising) |
| Falling correlation | Crypto decoupling | Watch for crypto-specific drivers |
| Correlation flip (pos to neg) | Rare, major regime shift | Flight to safety dynamics |

---

## Module 2: Capital Flow Segmentation

### 2.1 Capital Type Classification

| Capital Type | Characteristics | Flows Into |
|--------------|-----------------|------------|
| **Speculative** | Risk-seeking, leverage-enabled, convex payoff | Crypto, meme stocks, high-beta tech |
| **Defensive** | Risk-averse, preservation-focused | Gold, bonds, utilities, cash |
| **Inflation-Hedging** | Real-asset focused, scarcity narrative | Gold, silver, copper, commodities |
| **Growth** | Earnings/innovation focused | Tech stocks, growth equities |
| **Institutional Passive** | Allocation-driven, systematic | ETFs, index funds |

### 2.2 Capital Flow Detection Matrix

| Signal | Speculative | Defensive | Inflation-Hedging |
|--------|-------------|-----------|-------------------|
| Crypto breadth | Expanding | Contracting | N/A |
| BTC dominance | Falling | Rising | Stable (BTC only) |
| Gold performance | Lagging | Leading | Leading |
| VIX level | Low | Elevated | Moderate |
| Risk assets | Outperforming | Underperforming | Mixed |

### 2.3 Current Capital Flow Assessment (Q1 2026)

Per Benjamin Cowen analysis:
- Speculative liquidity: **CONSTRAINED**
- Defensive capital: **ACTIVE** (flowing to gold, bonds)
- Inflation-hedging: **DOMINANT** (metals outperforming)
- Crypto-supportive capital: **ABSENT**

---

## Module 3: Metals Context

### 3.1 Gold Strength as Defensive Rotation Signal

| Gold vs BTC Performance | Classification | Interpretation |
|------------------------|----------------|----------------|
| Gold >> BTC (+20%+ spread) | DEFENSIVE_ROTATION | Capital fleeing speculation |
| Gold > BTC (10-20% spread) | MILD_DEFENSIVE | Risk appetite waning |
| Gold ≈ BTC (±10%) | NEUTRAL | Balanced flows |
| BTC > Gold (10-20% spread) | RISK_SEEKING | Speculation preferred |
| BTC >> Gold (+20%+ spread) | SPECULATIVE_DOMINANCE | Full risk-on |

### 3.2 Metals Correlation Matrix

| Asset Pair | High Correlation (>0.7) | Interpretation |
|------------|------------------------|----------------|
| Gold-Silver | Precious metals trade together | Safe haven flows |
| Gold-SPY | Risk-on/off aligned | Macro-driven |
| Gold-DXY | Inverse (-0.5 to -0.8 typical) | Dollar hedge |
| BTC-Gold | Variable (0.1-0.5 historically) | Inflation narrative alignment |

### 3.3 "Bitcoin as Digital Gold" Assessment

| Condition | BTC Behaving as Gold? | Evidence |
|-----------|----------------------|----------|
| BTC-Gold correlation > 0.5 | Yes | Moving together |
| BTC outperforms in inflation | Partially | Mixed historical evidence |
| BTC holds value in risk-off | No | Still correlates with risk assets |
| BTC benefits from dollar weakness | Yes (typically) | Inverse DXY correlation |

---

## Module 4: Late-Cycle Correlation Patterns

### 4.1 2019 Analog Pattern

| Observation | 2019 | 2025 |
|-------------|------|------|
| Equities | Stabilized, later rallied | Resilient |
| Crypto | Continued digestion | Post-peak digestion |
| Correlation | Broke down | Breaking down |
| Metals | Stable | Outperforming |

**Key Insight:** Correlation breakdowns often occur when crypto transitions from late-cycle distribution to prolonged consolidation.

### 4.2 Why Crypto Decouples in Late Cycle

1. **Different Liquidity Needs:** Crypto requires speculative excess; equities supported by earnings/buybacks
2. **Participation Collapse:** Crypto losing marginal buyers while equity flows continue
3. **Institutional Reallocation:** Moving from high-beta to quality
4. **Risk Appetite Exhaustion:** Crypto first to lose buyers when risk appetite wanes

### 4.3 Signal: Equities Rally but Crypto Lags

| Condition | Interpretation |
|-----------|----------------|
| SPX new high + BTC range-bound | Crypto in distribution, not participating in risk-on |
| SPX steady + BTC falling | Crypto-specific weakness, not macro-driven |
| SPX rally + BTC dominance rising | Defensive rotation within crypto |

---

## Module 5: Scenario Templates

### 5.1 CORRELATION_BREAKDOWN Detection

| Condition | Check | Status |
|-----------|-------|--------|
| 90-day BTC-SPX correlation | < 0.3 | [ ] |
| Equities | Stable or rising | [ ] |
| Crypto | Underperforming | [ ] |
| Gold | Outperforming crypto | [ ] |

**Require 3+ conditions for CORRELATION_BREAKDOWN**

**Interpretation:** Capital is segmented. Liquidity in system but not flowing to crypto. Different cycle phase.

### 5.2 DEFENSIVE_ROTATION Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Gold performance | > BTC by 15%+ (90d) | [ ] |
| VIX | Elevated (> 20) | [ ] |
| BTC dominance | Rising | [ ] |
| Crypto breadth | Declining | [ ] |
| Bond yields | Falling | [ ] |

**Require 4+ conditions for DEFENSIVE_ROTATION**

**Interpretation:** Capital fleeing risk assets for safety. Crypto particularly vulnerable.

### 5.3 CAPITAL_SEGMENTATION Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Equities | Resilient | [ ] |
| Metals | Outperforming | [ ] |
| Crypto | Underperforming | [ ] |
| Correlation | Broken (< 0.3) | [ ] |
| Speculative metrics | Muted | [ ] |

**Require 4+ conditions for CAPITAL_SEGMENTATION**

**Interpretation:** Different capital types flowing to different assets. Crypto requires speculative capital which is currently scarce.

### 5.4 RISK_ON_CONVERGENCE Detection (Bullish)

| Condition | Check | Status |
|-----------|-------|--------|
| BTC-SPX correlation | Rising (> 0.5) | [ ] |
| Equities | Making new highs | [ ] |
| Crypto | Participating in rally | [ ] |
| Crypto breadth | Improving | [ ] |
| VIX | Low (< 18) | [ ] |

**Require 4+ conditions for RISK_ON_CONVERGENCE**

**Interpretation:** Broad risk-on. Speculative liquidity returning. Bullish for crypto.

---

## Module 6: Cross-Asset Trading Signals

### 6.1 Gold Leading = Crypto Lagging

| Gold Trend | BTC Trend | Signal |
|------------|-----------|--------|
| Gold +20% (90d) | BTC flat | DEFENSIVE_ROTATION_ACTIVE |
| Gold +15% | BTC -10% | SPECULATIVE_CAPITAL_ABSENT |
| Gold flat | BTC +20% | RISK_APPETITE_RETURNING |
| Gold -10% | BTC +30% | SPECULATION_DOMINANCE |

### 6.2 Equity-Crypto Divergence

| SPX Trend | BTC Trend | Interpretation |
|-----------|-----------|----------------|
| New highs | Lagging | Crypto in different cycle phase |
| Correcting | Outperforming | Rare, crypto-specific catalyst |
| Rallying | Rallying | Risk-on convergence (bullish) |
| Selling off | Selling off | Risk-off (correlated weakness) |

### 6.3 Dollar Impact

| DXY Trend | BTC Impact | Confidence |
|-----------|------------|------------|
| DXY rising | BTC headwind | HIGH |
| DXY falling | BTC tailwind | MODERATE |
| DXY stable | Neutral | N/A |

---

## Module 7: Data Sources

### 7.1 Required Tables

| Table | Metrics Used |
|-------|-------------|
| `macro_asset_correlations` | Rolling correlations |
| `btc_lead_lag_results` | Lead-lag relationships |
| `macro_data` | Gold, SPY, DXY, VIX |
| `price_history` | BTC, ETH prices |

### 7.2 Key Calculations

```sql
-- 90-day rolling correlation
SELECT
  CORR(btc_return, spx_return) OVER (
    ORDER BY date
    ROWS BETWEEN 89 PRECEDING AND CURRENT ROW
  ) AS btc_spx_correlation_90d
FROM daily_returns;

-- Relative performance
SELECT
  (btc_price / btc_price_90d_ago - 1) -
  (gold_price / gold_price_90d_ago - 1) AS btc_vs_gold_90d
FROM macro_data;
```

---

## Module 8: Output Format Examples

### Standard Cross-Asset Analysis

```
**Cross-Asset Correlation Analysis**

**Correlation Regime:** DECOUPLED
- BTC-SPX 90d Correlation: 0.18 (weak)
- BTC-Gold 90d Correlation: 0.32 (weak positive)
- Trend: Decorrelating from equities

**Capital Flow Assessment:**
- Speculative Liquidity: CONSTRAINED
- Defensive Capital: ACTIVE (gold +18% 90d)
- Inflation-Hedging: DOMINANT
- Crypto-Supportive: ABSENT

**Relative Performance (90d):**
- Gold: +18%
- SPX: +8%
- BTC: -5%
- ETH: -12%
- Classification: DEFENSIVE_ROTATION

**Interpretation:**
Capital is present in the financial system but flowing to:
- Inflation-hedging assets (gold, metals)
- Quality equities (earnings-supported)
NOT to speculative digital assets.

This is classic late-cycle capital segmentation:
- Equities supported by buybacks/earnings
- Crypto requires speculative excess (currently absent)
- 2019 analog: Equities recovered while crypto digested

**Key Insight:**
Crypto not being "left behind" by bull market elsewhere.
It's in a different part of its cycle. Liquidity type mismatch.

**Watch For:**
- Correlation re-convergence (risk-on return)
- Gold underperformance (speculation returning)
- Crypto breadth improvement
```

### Alert-Style Output

```
**CROSS-ASSET ALERT: Capital Segmentation Active**

90-day BTC-SPX correlation collapsed to 0.18
Gold outperforming BTC by +23% over 90 days

This signals:
- Different capital types flowing to different assets
- Speculative liquidity (crypto's fuel) is ABSENT
- Defensive/inflation-hedging capital DOMINANT

Equities can rally while crypto digests because:
- Equities: Earnings + buybacks support
- Crypto: Needs speculative excess

Pattern matches 2019:
- Equities stabilized/rallied H2 2019
- Crypto continued digestion until 2020

Don't expect crypto to "catch up" automatically.
Wait for speculative liquidity return signals.
```
