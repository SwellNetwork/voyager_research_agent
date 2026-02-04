---
name: XRP Perpetuals Agent
version: 3.0
asset: XRP
type: overlay
domain: perpetuals
requires: [base]
last_updated: 2025-01-15
sources:
  - templates/report_prompts.py (DERIVATIVES_MICROSTRUCTURE_FRAMEWORK)
  - skills/domains/perpetuals.md (v3.0 Framework)
---

# XRP Perpetuals Analysis v3.0

## Overview

XRP perpetuals are unique due to heavy retail participation, event-driven volatility, and lower correlation to broader crypto market.

### Key Characteristics

- **Retail-Dominated:** Very high retail speculation, extreme L/S swings
- **Event-Driven:** SEC litigation, partnership news drive major moves
- **Lower BTC Correlation:** Often moves independently of BTC
- **Violent Squeezes:** Frequent and aggressive short/long squeezes
- **No Options Market:** Cannot use GEX signals
- **Ripple Influence:** Company actions affect token supply

### Trading Venues

| Exchange | Type | Notes |
|----------|------|-------|
| Binance | CEX | Largest XRP perps volume |
| Bybit | CEX | Active leverage trading |
| OKX | CEX | Strong XRP derivatives |
| Hyperliquid | DEX | XRP perps available |
| Kraken | CEX | XRP-friendly jurisdiction |

---

## XRP Regime Detection

### Volatility Regime

XRP exhibits burst volatility - long periods of calm followed by explosive moves.

| Vol Percentile (30d) | Classification | XRP-Specific Note |
|----------------------|----------------|-------------------|
| > 80th | HIGH_VOL | Expect 8-15% daily swings |
| 20th - 80th | NORMAL_VOL | 3-6% daily range typical |
| < 20th | LOW_VOL | Coiled spring - breakout imminent |

### Event-Driven Regime

| Regime | Driver | Trading Approach |
|--------|--------|------------------|
| NEWS_DRIVEN | Legal/Partnership update | React quickly, trail stops |
| SQUEEZE_SETUP | Extreme positioning | Wait for trigger, trade squeeze |
| ACCUMULATION | Quiet period, stable price | Range trade or wait |
| CATCH_UP | BTC rallying, XRP lagging | Anticipate violent catch-up |

---

## XRP-Specific Signal Thresholds

### ELR (Estimated Leverage Ratio)

**ELR = Open Interest / Market Cap**

XRP can sustain surprisingly high ELR due to retail conviction.

| ELR | Classification | XRP-Specific Implication |
|-----|----------------|--------------------------|
| < 2.5% | LOW | Room for leverage to build |
| 2.5-4% | MODERATE | Healthy leverage levels |
| 4-6% | HIGH | Elevated squeeze/cascade risk |
| > 6% | EXTREME | Violent move incoming (either direction) |

*Note: At ~$150B market cap, 6% ELR = $9B OI*

### Funding Rate Thresholds

XRP funding exhibits extreme swings due to retail sentiment.

| Funding (8h) | Z-Score | Classification | XRP-Specific Signal |
|--------------|---------|----------------|---------------------|
| > 0.12% | > 3.0 | EXTREME_GREED | Long squeeze imminent |
| 0.05-0.12% | 2.0-3.0 | ELEVATED_GREED | High squeeze risk |
| 0.02-0.05% | 1.0-2.0 | BULLISH | Strong retail demand |
| -0.02 to 0.02% | -1.0-1.0 | NEUTRAL | Balanced |
| -0.05 to -0.02% | -2.0 to -1.0 | BEARISH | Short squeeze building |
| < -0.05% | < -2.0 | EXTREME_FEAR | Short squeeze imminent |

### Long/Short Ratio Thresholds

XRP L/S ratios swing more wildly than any other major - extreme levels are common.

| Global L/S | Classification | Contrarian Signal |
|------------|----------------|-------------------|
| > 3.5 | EXTREME_LONG_CROWDING | Strong squeeze short signal |
| 2.2-3.5 | HEAVY_LONG_BIAS | Moderate short signal |
| 1.2-2.2 | NORMAL_LONG_BIAS | Neutral |
| 0.7-1.2 | BALANCED | No contrarian signal |
| 0.4-0.7 | SHORT_BIAS | Moderate long signal |
| < 0.4 | EXTREME_SHORT_CROWDING | Strong squeeze long signal |

**CRITICAL:** XRP L/S extremes are the highest-conviction signal for this asset.

### OI Thresholds (Aggregate)

| OI Level | Classification | Implication |
|----------|----------------|-------------|
| > $3B | EXTREME | High squeeze/cascade risk |
| $1.5-3B | ELEVATED | Above-average leverage |
| $700M-1.5B | NORMAL | Healthy market |
| < $700M | LOW | Quiet market or capitulation |

---

## XRP Squeeze Dynamics - PRIMARY SIGNAL

XRP is the "squeeze coin" - positioning extremes are the most reliable signal.

### Squeeze Setup Detection

| Factor | Long Squeeze Risk | Short Squeeze Risk |
|--------|-------------------|-------------------|
| Global L/S | > 3.0 | < 0.5 |
| Funding | > 0.08% | < -0.04% |
| OI Trend | Rising | Rising |
| Price Action | At resistance | At support |
| News Catalyst | None imminent | None imminent |

### Squeeze Probability Score

| Score | Probability | Action |
|-------|-------------|--------|
| 5/5 factors | > 80% | Position for squeeze |
| 4/5 factors | 60-80% | Prepare, wait for trigger |
| 3/5 factors | 40-60% | Monitor closely |
| < 3 factors | < 40% | No squeeze setup |

### Historical Squeeze Behavior

| Squeeze Type | Typical Magnitude | Duration |
|--------------|-------------------|----------|
| Minor Squeeze | 5-10% | Hours |
| Major Squeeze | 15-30% | 1-2 days |
| Capitulation Squeeze | 30-50%+ | 2-5 days |

---

## Event-Driven Analysis

### Regulatory Catalysts

| Event Type | Expected Impact | Positioning |
|------------|-----------------|-------------|
| Favorable SEC Ruling | +20-50% | Pre-position long if L/S extreme short |
| Unfavorable SEC Ruling | -20-30% | Pre-position short if L/S extreme long |
| Settlement Announcement | Variable | Direction depends on terms |
| Appeal News | High volatility | Reduce size, trade reaction |

### Partnership/Adoption Catalysts

| Event Type | Expected Impact |
|------------|-----------------|
| Major Bank Partnership | +10-25% short-term |
| ODL Volume Milestone | +5-15% |
| New Corridor Launch | +3-8% |
| Ripple IPO Speculation | High volatility |

### Ripple Company Actions

| Action | XRP Impact |
|--------|------------|
| Escrow Release (monthly) | Mild selling pressure |
| Large XRP Sale | Bearish if significant |
| Treasury Update | Varies by messaging |

---

## CVD Signal Analysis

### Available CVD Data

| Data Source | Table | Update Frequency | Coverage |
|-------------|-------|------------------|----------|
| 5-Minute CVD | `cvd_aggregated` | Hourly | Binance, Bybit, OKX, Hyperliquid |
| Daily Summary | `cvd_daily_summary` | Daily @ 00:30 UTC | OHLC-style CVD metrics |
| Trading Signals | `cvd_signals` | Daily @ 00:30 UTC | Divergence detection |

**Note:** XRP now has full CVD coverage across all major exchanges.

### CVD Divergence Signals

The system detects 5 high-conviction divergence patterns:

| Signal Type | Trigger Condition | Direction | Confidence |
|-------------|-------------------|-----------|------------|
| `DISTRIBUTION` | Price rising + Spot CVD falling | BEARISH | HIGH |
| `LEVERAGE_TRAP` | Price rising + Perp CVD >> Spot CVD (ratio > 2) | BEARISH | VERY_HIGH |
| `ABSORPTION` | Price stable/down + Perp CVD falling rapidly | BULLISH | MEDIUM |
| `BULLISH_DIVERGENCE` | Price makes lower low + CVD makes higher low | BULLISH | HIGH |
| `BEARISH_DIVERGENCE` | Price makes higher high + CVD makes lower high | BEARISH | HIGH |

### XRP CVD vs L/S Priority

**Key Insight:** For XRP, L/S ratios remain the PRIMARY signal. CVD is a confirming indicator.

| L/S Signal | CVD Confirmation | Combined Conviction |
|------------|------------------|---------------------|
| Extreme Long (L/S > 3.0) | `DISTRIBUTION` signal | VERY_HIGH (short) |
| Extreme Short (L/S < 0.5) | `ABSORPTION` signal | VERY_HIGH (long) |
| Extreme Long (L/S > 3.0) | No CVD divergence | HIGH (short) - L/S alone sufficient |
| Neutral L/S | CVD divergence | MEDIUM - wait for L/S confirmation |

### XRP CVD Slope Thresholds

| 24h Slope | Signal | XRP-Specific Interpretation |
|-----------|--------|----------------------------|
| > 0.6 | `STRONG_BUYING` | Catch-up rally fuel building |
| 0.15 to 0.6 | `MILD_BUYING` | Gradual accumulation |
| -0.15 to 0.15 | `NEUTRAL` | Balanced - watch L/S for direction |
| -0.6 to -0.15 | `MILD_SELLING` | Gradual distribution |
| < -0.6 | `STRONG_SELLING` | Aggressive selling - potential squeeze setup |

---

## XRP Liquidation Dynamics

### Liquidation Characteristics

- Very high leverage usage by retail
- Squeezes create rapid cascades
- Lower liquidity than BTC/ETH = bigger wicks
- Event-driven liquidations can be severe

### Key Liquidation Levels

- Round numbers: $0.50, $0.75, $1.00, $1.50, $2.00, $3.00
- Previous cycle ATH: ~$3.40 zone
- SEC lawsuit filing price levels
- Historical support/resistance clusters

### Cascade Risk Assessment (XRP-Specific)

| Factor | Weight | XRP High Risk Threshold |
|--------|--------|-------------------------|
| ELR | 30 pts | > 5% (OI/MCap) |
| Funding | 25 pts | > 0.08% (8h) |
| L/S Extreme | 30 pts | > 3.0 or < 0.5 |
| Book Depth | 15 pts | < $20M within 2% |

**Note:** L/S extreme is weighted higher for XRP than other assets.

---

## XRP Scenario Templates

### XRP LONG_SQUEEZE

| Condition | XRP-Specific Check |
|-----------|-------------------|
| Price | At resistance or new high |
| Funding | > 0.08% (8h) |
| Global L/S | > 3.0 |
| OI | Rising into resistance |
| No Bullish Catalyst | No positive news imminent |

**4+ conditions = HIGH conviction SHORT / fade longs**

### XRP SHORT_SQUEEZE

| Condition | XRP-Specific Check |
|-----------|-------------------|
| Price | At support |
| Funding | < -0.04% (8h) |
| Global L/S | < 0.6 |
| OI | Rising into support |
| No Bearish Catalyst | No negative news imminent |

**4+ conditions = HIGH conviction LONG on reclaim**

### XRP NEWS_PLAY

| Condition | Check |
|-----------|-------|
| Major News | Legal/Partnership pending |
| Positioning | Check L/S for crowding |
| Volatility | Compressed (< 20th percentile) |
| OI | Elevated (fuel for move) |

**Pre-position opposite to retail crowding before catalyst**

### XRP CATCH_UP_RALLY

| Condition | XRP-Specific Check |
|-----------|-------------------|
| BTC | Up > 10% this week |
| XRP | Flat or lagging |
| XRP Funding | Neutral or negative |
| XRP L/S | Neutral or short bias |

**XRP often has violent catch-up rallies when lagging BTC**

### XRP CAPITULATION_BOTTOM

| Condition | XRP-Specific Check |
|-----------|-------------------|
| OI Change | > -25% in 24h |
| Funding | Negative and falling |
| L/S | Extreme short (< 0.5) |
| CVD Signal | `ABSORPTION` or `BULLISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | Stabilizing (slope returning toward 0 from negative) |
| Price | At major historical support |
| No Adverse News | Selling not news-driven |

**4+ conditions = VERY_HIGH conviction LONG**

---

## Trading Considerations

### Entry Timing

| Setup | Best XRP Entry |
|-------|----------------|
| Long | Extreme short crowding + No adverse news + Support level |
| Short | Extreme long crowding + No bullish news + Resistance level |

### Position Sizing (XRP)

- XRP can move 15-30% in squeeze events
- Maximum recommended leverage: 2-3x for swing trades
- Account for violent wicks and low liquidity periods
- Reduce size 50% when ELR > 5%
- Always have stop loss - XRP wicks can be brutal

### XRP-Specific Risk Management

| Risk | Mitigation |
|------|------------|
| News bomb | Smaller size before known events |
| Squeeze wick | Wider stops than other assets |
| Low liquidity | Avoid large market orders |
| Ripple action | Monitor company announcements |

### Exit Signals

- L/S normalizing from extreme = Squeeze exhausted
- OI dropping rapidly = Deleveraging complete
- Major news announced = Re-evaluate thesis
- Funding flipping = Sentiment shift

---

## XRP vs BTC Correlation

### Correlation Regime

| Correlation | Market Phase | Approach |
|-------------|--------------|----------|
| High (> 0.7) | Risk-on/off driven | Trade with BTC |
| Medium (0.4-0.7) | Mixed drivers | Blend analysis |
| Low (< 0.4) | XRP-specific drivers | Focus on L/S + news |

### Catch-Up Dynamics

XRP often lags BTC in early rallies, then has violent catch-up:

| BTC Move | XRP Typical Behavior |
|----------|---------------------|
| +20% over 2 weeks | XRP +5-10%, then +30% catch-up |
| -20% over 2 weeks | XRP -25-30%, faster |
| Range-bound | XRP independent, L/S driven |

---

## Data Quality Notes

XRP has improved data availability:
- **No options market:** Cannot calculate GEX or skew
- **Strong CVD data:** Now available from all major exchanges
- **No on-chain metrics:** No MVRV/SOPR available
- **Excellent L/S data:** Primary signal source (highest conviction)

### CVD Data Coverage
| Exchange | Spot CVD | Perp CVD | Update Frequency |
|----------|----------|----------|------------------|
| Binance | ✅ | ✅ | Hourly (5-min buckets) |
| Bybit | ✅ | ✅ | Hourly (5-min buckets) |
| OKX | ✅ | ✅ | Hourly (5-min buckets) |
| Hyperliquid | - | ✅ | Hourly (5-min buckets) |

### Other Data Availability

| Data Point | Availability | Source |
|------------|--------------|--------|
| Funding Rate | Good | Multiple CEXs |
| Global L/S | Excellent | Binance/Bybit/OKX |
| Top Trader L/S | Good | Binance/Bybit |
| OI | Good | Multiple CEXs |
| CVD Signals | ✅ Good | `cvd_signals` table - auto-detected |
| Options/GEX | None | N/A |
| News/Events | Critical | SEC filings, Ripple announcements |

**Confidence penalty: 10%** (no options, but excellent L/S and good CVD)

---

## Key XRP Trading Rules

1. **L/S is King:** XRP L/S extremes are the highest-conviction signal
2. **Respect the Squeeze:** Position early, trail stops during squeeze
3. **News Trumps Technicals:** Major legal/partnership news overrides all signals
4. **Wicks are Normal:** Use wider stops, smaller size
5. **Catch-Up Happens:** Don't fade when XRP finally moves to catch BTC
