---
name: Regime Transition & View Change Framework
version: 1.0
type: domain
domain: regime_transitions
applicable_assets: [BTC, ETH, ALL]
last_updated: 2026-01-18
sources:
  - Benjamin Cowen Crypto Risk Memo Q1 2026
  - Into The Cryptoverse Research
---

# Regime Transition & "What Would Change This View" Framework v1.0

## Overview

This framework defines the conditions required for a regime transition from Risk-Off (capital preservation) to Risk-On (capital deployment). The assessment is conditional rather than permanent - specific converging signals would materially change the outlook.

**Key Principle:** A more constructive outlook requires evidence that the market has transitioned from late-cycle distribution into a new accumulation phase. Four key factors must align.

---

## Module 1: The Four Required Factors

### 1.1 Factor Summary

| Factor | Current Status (Q1 2026) | Required for Transition |
|--------|-------------------------|-------------------------|
| **Participation Reset** | Narrow, declining | Broadening materially |
| **On-Chain Reset** | Distribution | Accumulation |
| **Volatility Expansion** | Compressed, fragile | Constructive expansion |
| **Liquidity Shift** | Restrictive | Crisis-level expansion |

### 1.2 Conviction Levels

| Factors Present | Signal | Conviction |
|-----------------|--------|------------|
| 0-1 of 4 | RISK_OFF | HIGH conviction bearish |
| 2 of 4 | TRANSITIONAL | MODERATE, tactical opportunities |
| 3 of 4 | IMPROVING | MODERATE bullish bias |
| 4 of 4 | RISK_ON | HIGH conviction bullish |

---

## Module 2: Participation Reset Signals

### 2.1 Required Evidence

For participation to reset, we need to see:

| Signal | Threshold | Current Status |
|--------|-----------|----------------|
| ADI improvement | Rising for 4+ weeks | Declining |
| Altcoin breadth | > 50% above 200 DMA | < 35% |
| Social engagement | Rising to > 0.5 Social Risk | < 0.3 |
| BTC dominance | Declining from peak | Rising/elevated |
| New participant growth | Exchange signups increasing | Muted |

### 2.2 Participation Reset Checklist

| Condition | Check | Status |
|-----------|-------|--------|
| ADI positive slope sustained | 4+ weeks | [ ] |
| % assets above 200 DMA | > 50% | [ ] |
| Social Risk Index | > 0.4 and rising | [ ] |
| BTC dominance | < 55% and falling | [ ] |
| Small-cap participation | Active | [ ] |
| Multi-sector participation | 3+ sectors rising | [ ] |

**Require 4+ conditions for PARTICIPATION_RESET confirmed**

### 2.3 What Would Trigger Participation Reset

- New narrative catalyst (regulatory clarity, major adoption)
- Altcoin-specific innovation cycle
- Retail FOMO return (social metrics spike)
- Institutional broadening beyond BTC

---

## Module 3: On-Chain Reset Signals

### 3.1 Required Evidence

For on-chain dynamics to reset, we need:

| Signal | Threshold | Current Status |
|--------|-----------|----------------|
| Supply at loss | > 20% of supply | Low (< 15%) |
| LTH behavior | Accumulating | Distributing |
| Capitulation event | SOPR < 0.95 sustained | Not present |
| Weak hand exhaustion | STH supply declining | Elevated |
| MVRV Z-Score | < 0 (deep value) | Elevated |

### 3.2 On-Chain Reset Checklist

| Condition | Check | Status |
|-----------|-------|--------|
| Supply at loss | > 20% | [ ] |
| LTH Net Position Change | Positive (accumulating) | [ ] |
| SOPR | < 0.98 sustained | [ ] |
| Realized price test | Price near/below realized | [ ] |
| STH capitulation | STH supply declining sharply | [ ] |

**Require 4+ conditions for ON_CHAIN_RESET confirmed**

### 3.3 What Would Trigger On-Chain Reset

- Deep correction (-40% or more from ATH)
- Extended time at lower prices (6+ months)
- Capitulation event with SOPR < 0.95
- Long-term holders shifting to accumulation

---

## Module 4: Volatility Transition Signals

### 4.1 Required Evidence

For volatility to transition constructively:

| Signal | Threshold | Current Status |
|--------|-----------|----------------|
| Vol expansion | Rising from compression | Compressed |
| Direction | Upward with rising vol | N/A |
| Breakout character | Strong, impulsive | N/A |
| Price discovery | New range establishment | Stuck in old range |

### 4.2 Constructive Volatility Checklist

| Condition | Check | Status |
|-----------|-------|--------|
| 30-day vol | Rising from < 20th percentile | [ ] |
| Price breakout | Above prior range high | [ ] |
| Breakout character | Strong volume, impulsive | [ ] |
| Participation | ADI rising with price | [ ] |

**Require 3+ conditions for CONSTRUCTIVE_VOL_EXPANSION**

### 4.3 What Would Trigger Constructive Vol

- New ATH breakout with strong volume
- Fundamental catalyst (ETF approval extension, adoption news)
- Risk-on environment returning broadly
- Correlation re-convergence with equities

### 4.4 Bearish Vol Expansion (Different Signal)

| Condition | Interpretation |
|-----------|----------------|
| Vol spike + price falling | Capitulation, potential bottom |
| Vol spike + no breadth improvement | More downside likely |
| Vol spike + participation surge | Potential trend change |

---

## Module 5: Liquidity Shift Signals

### 5.1 Required Evidence

For macro liquidity to become supportive:

| Signal | Threshold | Current Status |
|--------|-----------|----------------|
| Fed policy | Emergency easing | Slow expansion |
| M2 growth | > 5% YoY | < 4% |
| Real yields | Collapsing | Positive |
| Recession phase | Nonlinear (layoff acceleration) | Cooling, not breaking |

### 5.2 Liquidity Shift Checklist

| Condition | Check | Status |
|-----------|-------|--------|
| Emergency QE | Announced/imminent | [ ] |
| Real yields | < 1% and falling | [ ] |
| M2 growth | > 5% YoY | [ ] |
| Unemployment spike | > 0.5% in 3 months | [ ] |
| Financial stress | Credit spreads widening sharply | [ ] |

**Require 3+ conditions for LIQUIDITY_SHIFT confirmed**

### 5.3 What Would Trigger Liquidity Shift

- Recession entering nonlinear phase (layoff acceleration)
- Financial instability (bank failures, credit freeze)
- Emergency Fed intervention
- Real yield collapse (inflation spike OR growth collapse)

### 5.4 Important Nuance: Orderly Soft Landing

A recession is NOT strictly required for recovery:

> "If the labor market continues to cool in an orderly way, with unemployment stabilizing, wage growth moderating, and inflation easing, then monetary conditions could gradually become less restrictive without requiring crisis-level intervention."

This would produce a slower, more gradual recovery rather than explosive rally.

---

## Module 6: Scenario Templates

### 6.1 BULLISH_REGIME_CHANGE Detection

**Required: 4 of 4 factors present**

| Factor | Condition | Status |
|--------|-----------|--------|
| Participation Reset | ADI rising, breadth > 50%, social > 0.4 | [ ] |
| On-Chain Reset | Supply at loss > 20%, LTH accumulating | [ ] |
| Constructive Vol | Rising vol with upward price | [ ] |
| Liquidity Shift | Emergency easing OR real yields collapsing | [ ] |

**Conviction:** HIGH for sustained bull market if ALL 4 present

**Interpretation:** New accumulation phase confirmed. Shift from capital preservation to capital deployment.

### 6.2 TACTICAL_OPPORTUNITY Detection

**Required: 2 of 4 factors present**

| Factor | Condition | Status |
|--------|-----------|--------|
| Participation | Showing improvement signs | [ ] |
| On-Chain | Capitulation event | [ ] |
| Volatility | Constructive expansion | [ ] |
| Liquidity | Incrementally improving | [ ] |

**Conviction:** MODERATE for tactical rally

**Interpretation:** Conditions improving but not confirmed regime change. Rallies are tradeable but likely not sustainable.

### 6.3 SOFT_LANDING_RECOVERY Detection

**Alternative path without crisis:**

| Condition | Check | Status |
|-----------|-------|--------|
| Unemployment | Stabilizing (not collapsing) | [ ] |
| Inflation | Easing toward 2% | [ ] |
| Wage growth | Moderating | [ ] |
| Fed stance | Gradually less restrictive | [ ] |
| No emergency intervention | True | [ ] |

**Interpretation:** Gradual, slower recovery. Not explosive rally but durable base formation.

---

## Module 7: Current Assessment (Q1 2026)

### 7.1 Factor Status Check

| Factor | Status | Assessment |
|--------|--------|------------|
| Participation | Declining, narrow | NOT RESET |
| On-Chain | Distribution, LTH selling | NOT RESET |
| Volatility | Compressed at highs | NOT CONSTRUCTIVE |
| Liquidity | Restrictive but not crisis | NOT SHIFTED |

**Current Score: 0 of 4 factors present**
**Regime: RISK_OFF with HIGH conviction**

### 7.2 What Would Change This View

1. **Participation broadening** - ADI rising, social engagement returning
2. **On-chain reset** - Deep correction creating supply at loss, LTH accumulation
3. **Constructive vol expansion** - Breakout with participation, not fragility
4. **Liquidity catalyst** - Recession nonlinear phase OR emergency easing

Until these develop, rallies are **tactical rather than structural**.

---

## Module 8: Monitoring Framework

### 8.1 Key Metrics to Track Weekly

| Metric | Source | Transition Threshold |
|--------|--------|---------------------|
| ADI slope | Calculated | Positive for 4+ weeks |
| Social Risk Index | fear_greed_index, social | > 0.4 |
| LTH Net Position | glassnode_metrics | Positive |
| 30-day vol percentile | price_history | Rising from < 20th |
| Unemployment rate | fred_series | > 4.5% or rising sharply |
| Fed balance sheet | fred_series (WALCL) | QE announcement |

### 8.2 Early Warning Signals

| Signal | Interpretation | Action |
|--------|----------------|--------|
| ADI inflection | Participation may be bottoming | Watch for confirmation |
| Social spike | Engagement returning | Verify breadth follows |
| Vol breakout | Price discovery returning | Check direction and participation |
| Fed tone shift | Policy pivot possible | Monitor employment data |

### 8.3 Confirmation Requirements

Never act on single signal. Require:
- **Duration:** Signal sustained 2+ weeks minimum
- **Breadth:** Multiple confirming indicators
- **Volume:** Activity backing the move
- **Context:** Macro environment supportive

---

## Module 9: Output Format Examples

### Standard Regime Assessment

```
**Regime Transition Assessment**

**Current Regime:** RISK_OFF (Capital Preservation)
**Factor Score:** 0 of 4 factors present
**Conviction:** HIGH

**Factor Status:**

1. **Participation Reset:** NOT PRESENT
   - ADI: Declining for 8 weeks
   - Breadth: 34% above 200 DMA (needs > 50%)
   - Social Risk: 0.28 (needs > 0.4)
   - Status: NARROW LEADERSHIP CONTINUES

2. **On-Chain Reset:** NOT PRESENT
   - Supply at loss: 12% (needs > 20%)
   - LTH behavior: Distributing
   - SOPR: 1.02 (needs < 0.98)
   - Status: DISTRIBUTION CONTINUES

3. **Constructive Vol Expansion:** NOT PRESENT
   - 30-day vol: 18th percentile (compressed)
   - Character: Fragile, not constructive
   - Status: COMPRESSION AT HIGHS

4. **Liquidity Shift:** NOT PRESENT
   - Fed policy: Slow expansion (not crisis QE)
   - Real yields: Positive
   - Recession: Cooling but not nonlinear
   - Status: RESTRICTIVE CONDITIONS

**What Would Change This View:**

For HIGH conviction bullish shift, would need to see:
□ ADI rising 4+ weeks with breadth > 50%
□ Supply at loss > 20%, LTH accumulating
□ Vol expanding with constructive price action
□ Emergency easing OR real yield collapse

Current probability of regime shift: LOW
Tactical rallies possible but not structural.
Maintain capital preservation posture.
```

### Alert-Style Output

```
**REGIME WATCH: No Transition Signals Present**

Current score: 0/4 factors for bullish regime change

Monitor for these early signals:
- ADI inflection (currently declining)
- Social engagement spike
- Fed tone shift / employment weakness
- Deep correction triggering on-chain reset

Until 2+ factors present: Rallies are tactical, not structural.
Maintain defensive positioning.
```

### Transition Alert Example

```
**REGIME ALERT: Potential Transition Signal**

Factor change detected: Participation showing improvement
- ADI: Positive slope for 3 weeks (needs 4 for confirmation)
- Breadth: Rising to 42% (approaching 50% threshold)
- Social: 0.35 (improving but below 0.4)

Current Score: 0.5 of 4 (partial signal)
Conviction: LOW - unconfirmed

Action: Monitor for confirmation. Not yet actionable.
Require: 4th week of ADI improvement + breadth > 50%
```
