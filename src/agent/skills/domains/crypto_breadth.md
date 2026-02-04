---
name: Crypto Breadth & Market Internal Health Framework
version: 1.0
type: domain
domain: crypto_breadth
applicable_assets: [BTC, ALL]
last_updated: 2026-01-18
sources:
  - Benjamin Cowen Crypto Risk Memo Q1 2026
  - Into The Cryptoverse Research
---

# Crypto Breadth & Market Internal Health Framework v1.0

## Overview

This framework analyzes the internal health of crypto markets through breadth indicators, participation metrics, and dominance dynamics. The advance-decline index reveals whether rallies are broad-based or narrow, which is critical for assessing sustainability.

**Key Principle:** Breadth collapses not when price is high, but when marginal buyers are gone. When breadth fails, it indicates risk appetite exhaustion, not asset weakness.

---

## Module 1: Advance-Decline Index Analysis

### 1.1 ADI Interpretation

The Advance-Decline Index tracks how many crypto assets are rising vs falling.

| ADI Trend | Market Cap Trend | Signal | Interpretation |
|-----------|------------------|--------|----------------|
| Rising | Rising | HEALTHY_BULL | Broad participation, sustainable rally |
| Falling | Rising | DIVERGENCE | Narrow leadership, fragile rally |
| Rising | Falling | ACCUMULATION | Internal strength building |
| Falling | Falling | CONFIRMED_BEAR | Broad weakness, risk-off |

### 1.2 ADI Level Classification

| ADI Value (Cumulative) | Classification | Market State |
|------------------------|----------------|--------------|
| New highs | STRONG_BREADTH | Healthy bull market |
| Rising but below highs | IMPROVING | Recovery phase |
| Flat | NEUTRAL | Consolidation |
| Falling | WEAKENING | Distribution phase |
| New lows | COLLAPSE | Bear market / capitulation |

### 1.3 ADI Divergence Signals

| Divergence Type | Description | Historical Accuracy |
|-----------------|-------------|---------------------|
| **Bearish Divergence** | BTC new high + ADI declining | ~75% precedes correction |
| **Bullish Divergence** | BTC new low + ADI improving | ~70% precedes rally |
| **Confirmation** | BTC trend = ADI trend | Trend continuation |

---

## Module 2: Bitcoin Dominance Framework

### 2.1 Dominance Interpretation

| BTC Dominance | Classification | Market Interpretation |
|---------------|----------------|----------------------|
| > 65% | EXTREME_HIGH | Defensive posture, altcoin capitulation |
| 55% - 65% | ELEVATED | Risk-off, BTC preference |
| 45% - 55% | BALANCED | Healthy market, selective alts |
| 35% - 45% | LOW | Risk-on, altcoin season |
| < 35% | EXTREME_LOW | Altcoin euphoria, cycle top warning |

### 2.2 Dominance Trend Signals

| Dominance Trend | Price Trend | Signal |
|-----------------|-------------|--------|
| Rising | Rising | BTC leadership, healthy |
| Rising | Falling | Defensive rotation, bearish alts |
| Falling | Rising | Altcoin rotation, risk-on |
| Falling | Falling | BTC falling faster than alts (rare) |

### 2.3 2025 Dominance Pattern

Per Benjamin Cowen analysis:
- Dominance rose structurally as capital migrated away from altcoins
- Rising dominance = defensive posture (investors choosing most liquid asset)
- Post-October 2025 decline in dominance reflects BTC falling faster, NOT altcoin revival

**Key Insight:** Modest dominance decline after peak doesn't indicate altcoin revival - it reflects BTC falling faster than already-depressed alts. Same pattern observed 2019.

---

## Module 3: Participation Breadth Signals

### 3.1 Narrow Leadership Warning

| Indicator | Healthy Market | Narrow Leadership |
|-----------|----------------|-------------------|
| % of alts above 200 DMA | > 60% | < 40% |
| % of alts positive YTD | > 50% | < 30% |
| Top 10 vs rest performance gap | < 20% | > 40% |
| New highs count (30d) | > 100 | < 30 |

### 3.2 Capital Concentration Detection

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| BTC + ETH share of gains | < 60% | 60-80% | > 80% |
| Top 5 assets share | < 70% | 70-85% | > 85% |
| Small-cap participation | Active | Weak | Absent |

### 3.3 Sector Breadth Analysis

| Sector | Participation Status | Implication |
|--------|---------------------|-------------|
| Large-cap (BTC, ETH) | Only sector participating | Narrow, defensive |
| L1 Alternatives | Mixed | Selective risk-taking |
| DeFi | Weak | Risk appetite limited |
| Meme / Speculative | Absent | No retail FOMO |

---

## Module 4: Social Participation Composite

### 4.1 Price vs Engagement Divergence

| Price Trend | Engagement Trend | Signal | Classification |
|-------------|------------------|--------|----------------|
| ATH | ATH | CONFIRMED_EUPHORIA | Cycle top zone |
| ATH | Muted | APATHY_TOP | Fragile rally |
| Falling | Falling | CONFIRMED_BEAR | Risk-off |
| Falling | Rising | CAPITULATION_INTEREST | Bottom forming |

### 4.2 Social Risk Index Components

| Component | Weight | Data Source |
|-----------|--------|-------------|
| Content consumption | 25% | YouTube views, podcast downloads |
| Exchange activity | 25% | New signups, active users |
| Social discourse | 25% | Twitter/X engagement, Reddit activity |
| Search interest | 25% | Google Trends, Bing searches |

### 4.3 Social Participation Classification

| Social Risk Score | Classification | Market Phase |
|-------------------|----------------|--------------|
| 0.8 - 1.0 | EXTREME_EUPHORIA | Cycle top imminent |
| 0.6 - 0.8 | ELEVATED | Late bull, caution |
| 0.4 - 0.6 | MODERATE | Mid-cycle |
| 0.2 - 0.4 | LOW | Early cycle or apathy top |
| 0.0 - 0.2 | EXTREME_LOW | Accumulation zone |

---

## Module 5: Breadth-Based Trading Signals

### 5.1 BREADTH_DIVERGENCE Signal

**Trigger Conditions:**
- BTC making new local high (30-day)
- ADI declining over same period
- > 60% of top 100 altcoins underperforming BTC

**Signal Strength:**

| Divergence Duration | Signal Strength |
|--------------------|-----------------|
| < 2 weeks | EARLY_WARNING |
| 2-4 weeks | MODERATE |
| > 4 weeks | STRONG |

**Action:** Reduce altcoin exposure, consider BTC-only positioning.

### 5.2 NARROW_LEADERSHIP Signal

**Trigger Conditions:**
- BTC dominance > 58%
- ETH/BTC ratio declining
- ADI negative slope for > 2 weeks
- Social engagement < 50% of prior cycle peak

**Action:** Market in defensive posture. Capital concentrated in perceived safety.

### 5.3 PARTICIPATION_COLLAPSE Signal

**Trigger Conditions:**
- ADI making new lows
- < 30% of assets above 200 DMA
- Social Risk Index < 0.3
- Trading volume declining vs 30-day average

**Action:** Bear market confirmed. Capital preservation priority.

### 5.4 BREADTH_EXPANSION Signal (Bullish)

**Trigger Conditions:**
- ADI rising from lows
- % of assets above 200 DMA increasing
- BTC dominance declining from peak
- Small-cap participation returning

**Action:** Risk appetite returning. Consider selective altcoin exposure.

---

## Module 6: Scenario Templates

### 6.1 LATE_CYCLE_NARROW_BREADTH Detection

| Condition | Check | Status |
|-----------|-------|--------|
| BTC near ATH | Within 10% | [ ] |
| ADI divergence | Declining vs price | [ ] |
| BTC dominance | > 55% and rising | [ ] |
| Social engagement | < 40% of 2021 levels | [ ] |
| Altcoin performance | Lagging BTC by > 30% | [ ] |

**Require 4+ conditions for LATE_CYCLE_NARROW_BREADTH**

**Interpretation:** Classic late-cycle pattern. Rally driven by narrow capital pool. Structurally fragile.

### 6.2 HEALTHY_BULL_BREADTH Detection

| Condition | Check | Status |
|-----------|-------|--------|
| ADI rising | Positive slope | [ ] |
| BTC dominance | Stable or declining | [ ] |
| % above 200 DMA | > 50% | [ ] |
| Social engagement | Rising | [ ] |
| Multi-sector participation | Yes | [ ] |

**Require 4+ conditions for HEALTHY_BULL confirmation**

**Interpretation:** Broad-based rally with expanding participation. Trend likely sustainable.

### 6.3 BEAR_MARKET_BREADTH Detection

| Condition | Check | Status |
|-----------|-------|--------|
| ADI making new lows | Yes | [ ] |
| BTC dominance | > 60% | [ ] |
| % above 200 DMA | < 30% | [ ] |
| Social engagement | < 0.2 | [ ] |
| Capital fleeing alts | Yes | [ ] |

**Require 4+ conditions for BEAR_MARKET confirmation**

**Interpretation:** Broad weakness. Capital preservation mode. Await breadth improvement for accumulation.

---

## Module 7: Historical Context

### 7.1 2025 Cycle Breadth Characteristics

Per Benjamin Cowen memo:

| Observation | Status |
|-------------|--------|
| Bitcoin reached new ATH | Yes |
| Majority of alts participated | No |
| ADI trend during rally | Declining |
| Social engagement | Near historical lows |
| Capital concentration | Extreme (BTC + top 5 only) |

**Conclusion:** Classic divergence between index-level price and market internals = late-cycle signal.

### 7.2 2019 Comparison

| Metric | 2019 | 2025 |
|--------|------|------|
| BTC rally from low | +200% | +690% |
| Altcoin participation | Weak | Weak |
| Dominance trend | Rising | Rising |
| ADI vs price | Diverging | Diverging |
| Rally durability | Failed (H2 selloff) | Similar pattern |

---

## Module 8: Data Sources

### 8.1 Required Tables

| Table | Metrics Used |
|-------|-------------|
| `macro_data` | btc_dominance, total_market_cap |
| `fear_greed_index` | sentiment proxy |
| `social_sentiment` | engagement metrics |
| `price_history` | individual asset performance |

### 8.2 Calculated Metrics

| Metric | Calculation |
|--------|-------------|
| ADI | Sum of daily advances minus declines |
| % Above 200 DMA | Count of assets > 200-day moving average / total |
| Dominance | BTC market cap / total crypto market cap |
| Participation Rate | % of top 100 with positive returns over period |

---

## Module 9: Output Format Examples

### Standard Breadth Analysis

```
**Crypto Breadth Analysis**

**Advance-Decline Index:** DIVERGING (Bearish)
- ADI Trend: Declining for 8 weeks
- BTC Price Trend: Making new highs
- Divergence Signal: STRONG (> 4 weeks)

**Bitcoin Dominance:** ELEVATED (58.7%)
- Trend: Rising structurally
- Interpretation: Defensive rotation, capital fleeing alts
- Sector: Only large-caps participating

**Participation Metrics:**
- % Above 200 DMA: 34% (Warning)
- Top 5 Share of Gains: 82% (Critical)
- Small-cap Participation: Absent

**Social Participation:** LOW (0.31)
- Price at ATH but engagement muted
- Pattern: Classic apathy top structure
- Retail FOMO: Absent

**Breadth Signal:** LATE_CYCLE_NARROW_BREADTH
- Rally driven by narrow capital pool (institutional only)
- Structural fragility - few marginal buyers
- Similar to mid-2019 pattern

**Recommendation:**
Market internals indicate risk-off posture beneath surface strength.
Reduce altcoin exposure. BTC relatively safer but still constrained.
```

### Alert-Style Output

```
**BREADTH ALERT: Narrow Leadership Detected**

BTC making new highs but internals deteriorating:
- ADI: Declining for 8+ weeks (STRONG divergence)
- Participation: Only 34% of assets above 200 DMA
- Concentration: Top 5 assets = 82% of gains
- Social Engagement: 31% of 2021 peak

This is NOT a healthy bull market.
Capital has concentrated in perceived "safe" assets.
Rallies are structurally fragile without expanding participation.

Watch for: Breadth improvement (ADI inflection, participation expanding)
Until then: Capital preservation, minimal altcoin exposure
```
