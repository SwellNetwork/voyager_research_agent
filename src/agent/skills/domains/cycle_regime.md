---
name: Market Cycle & Regime Detection Framework
version: 1.0
type: domain
domain: cycle_regime
applicable_assets: [BTC, ETH]
last_updated: 2026-01-18
sources:
  - Benjamin Cowen Crypto Risk Memo Q1 2026
  - Into The Cryptoverse Research
---

# Market Cycle & Regime Detection Framework v1.0

## Overview

This framework provides methodology for detecting Bitcoin's market cycle phase and regime status. The goal is to assess whether current conditions favor **capital preservation** or **capital deployment** based on cycle timing, drawdown dynamics, and behavioral signals.

**Key Principle:** Bitcoin cycles follow predictable timing patterns from bear-market lows. The October 2025 peak fits squarely within historical rhythm, indicating the cycle has transitioned from expansion to distribution.

---

## Module 1: Cycle Status Classification

### 1.1 Risk-On vs Risk-Off Regime

The primary regime classification determines overall market posture.

| Regime | Characteristics | Recommended Posture |
|--------|-----------------|---------------------|
| **RISK_ON** | Expanding liquidity, broadening participation, LTH accumulation | Capital deployment, trend-following |
| **RISK_OFF** | Restrictive liquidity, weak breadth, LTH distribution | Capital preservation, tactical positioning |
| **TRANSITIONAL** | Mixed signals, regime uncertainty | Reduced exposure, wait for confirmation |

### 1.2 Cycle Phase Detection

| Phase | Days from Cycle Low | Typical ROI | Current Interpretation |
|-------|---------------------|-------------|------------------------|
| Early Cycle | 0-365 | 2-5x | Maximum accumulation opportunity |
| Mid Cycle | 365-550 | 5-10x | Strong trend continuation |
| Late Cycle | 550-750 | 7-12x peak | Reduce exposure on strength |
| Post-Peak | 750+ | Declining | Capital preservation mode |

**Historical Cycle Durations:**
- Cycle 3 (2015-2018): ~1050 days to peak
- Cycle 4 (2018-2021): ~1050 days to peak
- Cycle 5 (2022-2025): ~900 days to peak (October 2025)

---

## Module 2: Apathy vs Euphoria Top Detection

### 2.1 Top Type Classification

Bitcoin cycle peaks occur via two distinct mechanisms with different implications.

| Top Type | Social Risk Index | Retail Participation | Speculative Breadth | Bear Duration |
|----------|-------------------|---------------------|---------------------|---------------|
| **EUPHORIA_TOP** | > 0.7 | Surging | Broad altcoin rally | 12+ months |
| **APATHY_TOP** | < 0.4 | Muted | Narrow, BTC-only | 6-9 months, choppy |

### 2.2 Social Risk Index Signals

The Social Risk Index combines content consumption, exchange activity, and social discourse.

| Social Risk Score | Classification | Market Implication |
|-------------------|----------------|-------------------|
| 0.8 - 1.0 | EXTREME_EUPHORIA | Cycle top imminent, maximum caution |
| 0.6 - 0.8 | ELEVATED_RISK | Late cycle, reduce on rallies |
| 0.4 - 0.6 | MODERATE_RISK | Mid-cycle, normal positioning |
| 0.2 - 0.4 | LOW_RISK | Early cycle or post-peak apathy |
| 0.0 - 0.2 | EXTREME_APATHY | Accumulation zone or apathy top |

### 2.3 2025 Cycle Characteristics (Apathy Top)

The 2025 peak exhibited classic apathy-top characteristics:

| Indicator | 2017/2021 (Euphoria) | 2019/2025 (Apathy) |
|-----------|---------------------|-------------------|
| Social engagement | Surging to ATH | Near historical lows |
| Retail inflows | Rapid expansion | Muted, institutional-only |
| Altcoin breadth | Broad participation | Narrow, BTC dominance rising |
| Speculative intensity | Extreme leverage | Moderate positioning |

**Key Insight:** Apathy tops produce choppier, countertrend-rally-prone declines rather than single capitulation events.

---

## Module 3: Cycle Timing from Lows

### 3.1 ROI from Cycle Bottom

Track return on investment from the cycle low to assess position in cycle.

| Days Since Low | Historical ROI Range | Cycle Position |
|----------------|---------------------|----------------|
| 100 | 1.5-2.5x | Early accumulation |
| 300 | 2-5x | Early-mid cycle |
| 500 | 4-8x | Mid-late cycle |
| 700 | 6-12x | Late cycle / peak zone |
| 900+ | Varies (often declining) | Post-peak |

### 3.2 Current Cycle Position Assessment

```
Current Days from Nov 2022 Low: ~790 days (as of Jan 2026)
Peak ROI (Oct 2025): ~7.9x
Current Status: POST_PEAK_DIGESTION
```

---

## Module 4: Post-Peak Drawdown Dynamics

### 4.1 Drawdown from Peak Comparison

| Days Since Peak | 2019 Drawdown | 2025 Drawdown (Expected) | Signal |
|-----------------|---------------|-------------------------|--------|
| 30 | -15% | Similar | Normal correction |
| 60 | -25% | Similar | Extended correction |
| 90 | -35% | Similar | Bear market confirmed |
| 120+ | -40 to -50% | Similar | Deep drawdown |

### 4.2 2019 Analog Overlay

The 2025 cycle closely mirrors 2019:
- Bitcoin peaked before QT ended
- Price continued weakening after tightening ended
- Apathy-driven peak with weak participation
- Narrow leadership, institutional-only flows

**Key Insight:** Bitcoin often leads liquidity cycles; liquidity responds to macro stress, not the other way around.

### 4.3 Rolling Returns Compression

| 365-Day ROI | Classification | Forward Outlook |
|-------------|----------------|-----------------|
| > 2.0x | STRONG_BULL | Expect mean reversion |
| 1.0 - 2.0x | MODERATE_BULL | Continued strength possible |
| 0.5 - 1.0x | WEAK / RANGE | Transition zone |
| < 0.5x | BEAR_MARKET | Accumulation opportunity emerging |

---

## Module 5: Cycle Regime Signals

### 5.1 Bull Market Confirmation Checklist

| Signal | Threshold | Weight |
|--------|-----------|--------|
| Days from cycle low | > 365 | 15% |
| ROI from low | > 3x | 20% |
| Social Risk Index | > 0.4 and rising | 15% |
| Advance-Decline Index | Rising | 20% |
| LTH Net Position Change | Accumulating | 15% |
| Fed Balance Sheet | Expanding | 15% |

**Bull Confirmation:** 4+ signals positive (weighted > 60%)

### 5.2 Bear Market / Risk-Off Checklist

| Signal | Threshold | Weight |
|--------|-----------|--------|
| Days since peak | > 30 | 15% |
| Drawdown from ATH | > -20% | 20% |
| Social Risk Index | < 0.4 and falling | 15% |
| Advance-Decline Index | Falling | 20% |
| LTH Net Position Change | Distributing | 15% |
| Fed Balance Sheet | Contracting or flat | 15% |

**Risk-Off Confirmation:** 4+ signals negative (weighted > 60%)

---

## Module 6: Scenario Templates

### 6.1 POST_PEAK_DIGESTION Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Price below cycle ATH | > -10% from peak | [ ] |
| Days since peak | > 60 days | [ ] |
| Social Risk Index | < 0.4 | [ ] |
| Advance-Decline falling | ADI trending down | [ ] |
| LTH distributing | Net selling > 0 | [ ] |

**Require 4+ conditions for HIGH conviction POST_PEAK regime**

**Interpretation:** Market in digestion phase similar to mid-2019. Rallies are tactical, not structural. Favor capital preservation.

### 6.2 CYCLE_LATE Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Days from cycle low | > 600 | [ ] |
| ROI from low | > 5x | [ ] |
| Price making new ATH | Within 30 days | [ ] |
| Funding rates elevated | > 0.03% avg | [ ] |

**Require 3+ conditions for LATE_CYCLE warning**

**Interpretation:** Reduce exposure on strength. Do not chase new highs.

### 6.3 APATHY_TOP Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Price at ATH | New high | [ ] |
| Social Risk Index | < 0.4 | [ ] |
| Retail participation | Below 2021 levels | [ ] |
| Altcoin breadth | Narrow / declining | [ ] |
| BTC dominance | Rising | [ ] |

**Require 4+ conditions for APATHY_TOP classification**

**Interpretation:** Peak driven by narrow capital pool, not expanding demand. Structurally fragile rally.

### 6.4 ACCUMULATION_ZONE Detection

| Condition | Check | Status |
|-----------|-------|--------|
| Drawdown from ATH | > -50% | [ ] |
| Days in bear | > 200 | [ ] |
| Social Risk Index | < 0.2 | [ ] |
| LTH accumulating | Net buying > 0 | [ ] |
| MVRV Z-Score | < 0 | [ ] |

**Require 4+ conditions for ACCUMULATION opportunity**

**Interpretation:** Deep value zone. Maximum accumulation for long-term holders.

---

## Module 7: Data Sources

### 7.1 Required Tables

| Table | Metrics Used |
|-------|-------------|
| `macro_regime_signals` | cycle_position, risk_signal, regime_status |
| `macro_calculated_metrics` | days_from_low, roi_from_low |
| `price_history` | ATH, drawdown calculations |
| `fear_greed_index` | social_risk_proxy |
| `glassnode_metrics` | LTH behavior, supply dynamics |

### 7.2 Key Metrics to Query

```sql
-- Cycle timing
SELECT days_since_cycle_low, roi_from_cycle_low
FROM macro_calculated_metrics
WHERE asset = 'BTC'
ORDER BY date DESC LIMIT 1;

-- Regime signal
SELECT cycle_phase, risk_regime, confidence
FROM macro_regime_signals
WHERE asset = 'BTC'
ORDER BY date DESC LIMIT 1;
```

---

## Module 8: Output Format Examples

### Standard Cycle Analysis

```
**Cycle Regime Analysis for BTC**

**Cycle Status:** RISK_OFF (Post-Peak Digestion)
- Days from cycle low: ~790 days
- Days since October 2025 peak: ~100 days
- Current drawdown: -15% from ATH

**Cycle Phase:** POST_PEAK
- ROI from Nov 2022 low: 6.8x (down from 7.9x peak)
- Historical analog: Mid-2019 (apathy top)

**Top Type Classification:** APATHY_TOP
- Social Risk Index: 0.28 (low participation)
- Retail engagement: Muted vs 2021 levels
- Speculative breadth: Narrow (BTC dominance rising)

**Forward Outlook:**
- Rallies are likely tactical, not structural
- Counter-trend moves expected (choppy, not single capitulation)
- Structural upside constrained until liquidity/participation reset

**Recommended Posture:** Capital preservation and tactical positioning
```

### Alert-Style Output

```
**CYCLE ALERT: POST_PEAK_DIGESTION Confirmed**

Bitcoin entered post-peak digestion phase ~100 days ago.
Pattern closely mirrors 2019 apathy-top dynamics.

Key Observations:
- Price: -15% from Oct 2025 ATH
- Social Risk: 0.28 (near historical lows)
- LTH Behavior: Distribution into strength

Action: Treat rallies as tactical opportunities, not new bull market.
Reference: 2019 drawdown lasted ~6 months with multiple countertrend rallies.
```
