---
name: ETH Perpetuals Agent
version: 3.0
asset: ETH
type: overlay
domain: perpetuals
requires: [base]
last_updated: 2025-01-15
sources:
  - templates/report_prompts.py (DERIVATIVES_MICROSTRUCTURE_FRAMEWORK)
  - skills/domains/perpetuals.md (v3.0 Framework)
---

# ETH Perpetuals Analysis v3.0

## Overview

ETH perpetuals are the second most liquid crypto derivative after BTC, with unique characteristics:
- **Higher Volatility:** Typically 1.3-1.5x BTC volatility
- **Beta to BTC:** Often moves 1.2-1.5x BTC moves
- **DeFi Correlation:** Network activity impacts price
- **Options Market:** Deep Deribit liquidity enables GEX analysis

### Key Venues

| Exchange | Type | Notes |
|----------|------|-------|
| Binance | CEX | Largest ETH perps volume |
| Bybit | CEX | Active leverage trading |
| OKX | CEX | Strong derivatives suite |
| dYdX | DEX | ETH-focused orderbook |
| Hyperliquid | DEX | Growing ETH volume |
| Deribit | Options | Primary ETH options venue |

### ETH-Specific Characteristics

- **Higher Volatility:** 1.3-1.5x BTC - adjust position sizing
- **DeFi Reflexivity:** Network congestion/fees affect sentiment
- **Staking Dynamics:** Validator exits can create pressure
- **L2 Correlation:** L2 activity impacts ETH value accrual
- **Options Liquidity:** Second to BTC on Deribit

---

## ETH Regime Detection

### Volatility Regime (EGARCH)

ETH exhibits leverage effect - use EGARCH model for volatility forecasting.

| Vol Percentile (30d) | Classification | ETH-Specific Note |
|----------------------|----------------|-------------------|
| > 80th | HIGH_VOL | Expect 4-7% daily swings |
| 20th - 80th | NORMAL_VOL | 2-4% daily range typical |
| < 20th | LOW_VOL | Compression - vol expansion imminent |

### GEX Regime (ETH-Specific)

ETH options market is deep but less liquid than BTC - signals are reliable but with wider bands.

| GEX State | Price Behavior | Trading Approach |
|-----------|----------------|------------------|
| POSITIVE_GEX | Dampened moves, range-bound | Fade extremes, sell vol |
| NEGATIVE_GEX | Momentum amplified | Trade breakouts, trail stops |

**Key ETH GEX Levels:**
- Round numbers ($2000, $2500, $3000, $4000, $5000)
- Strike concentrations often at $500 intervals
- Quarterly expiry has strongest gamma effects

---

## ETH-Specific Signal Thresholds

### ELR (Estimated Leverage Ratio)

**ELR = Open Interest / Market Cap**

| ELR | Classification | ETH-Specific Implication |
|-----|----------------|--------------------------|
| < 2% | LOW | Room for leverage to build |
| 2-3.5% | MODERATE | Healthy leverage levels |
| 3.5-5% | HIGH | Elevated cascade risk |
| > 5% | EXTREME | Cascade likely on 4-6% move |

*Note: At ~$400B market cap, 5% ELR = $20B OI*

### Funding Rate Thresholds

ETH funding rates are more volatile than BTC due to higher retail participation.

| Funding (8h) | Z-Score | Classification | ETH-Specific Signal |
|--------------|---------|----------------|---------------------|
| > 0.10% | > 3.0 | EXTREME_GREED | Very high squeeze risk |
| 0.05-0.10% | 2.0-3.0 | ELEVATED_GREED | Unsustainable, fade setup |
| 0.02-0.05% | 1.0-2.0 | BULLISH | Bull market sustainable |
| 0.01-0.02% | 0.5-1.0 | NORMAL_BULLISH | Trend continuation |
| -0.01 to 0.01% | -0.5-0.5 | NEUTRAL | Balanced |
| -0.02 to -0.01% | -1.0 to -0.5 | NORMAL_BEARISH | Downtrend continuation |
| -0.05 to -0.02% | -2.0 to -1.0 | ELEVATED_FEAR | Short squeeze setup |
| < -0.05% | < -2.0 | EXTREME_FEAR | Strong long setup |

### ETH vs BTC Funding Spread

| ETH - BTC Spread | Signal | Interpretation |
|------------------|--------|----------------|
| > 0.03% | ETH_EUPHORIA | Risk-on, altcoin season indicator |
| 0.01-0.03% | ETH_PREFERENCE | Moderate alt preference |
| -0.01 to 0.01% | BALANCED | Normal correlation |
| -0.03 to -0.01% | BTC_PREFERENCE | Risk-off rotation |
| < -0.03% | BTC_DOMINANCE | Flight to quality |

### Long/Short Ratio Thresholds

| Global L/S | Classification | Contrarian Signal |
|------------|----------------|-------------------|
| > 2.8 | EXTREME_LONG_CROWDING | Strong short signal |
| 2.0-2.8 | HEAVY_LONG_BIAS | Moderate short signal |
| 1.2-2.0 | NORMAL_LONG_BIAS | Neutral |
| 0.8-1.2 | BALANCED | No contrarian signal |
| 0.5-0.8 | SHORT_BIAS | Moderate long signal |
| < 0.5 | EXTREME_SHORT_CROWDING | Strong long signal |

### OI Thresholds (Aggregate)

| OI Level | Classification | Implication |
|----------|----------------|-------------|
| > $15B | EXTREME | High cascade risk |
| $10-15B | ELEVATED | Above-average leverage |
| $5-10B | NORMAL | Healthy market |
| < $5B | LOW | Capitulation or quiet |

---

## ETH Options Signals

### 25-Delta Risk Reversal

| Skew | Classification | ETH-Specific Behavior |
|------|----------------|----------------------|
| > 10% | VERY_BULLISH | Strong call buying - euphoria |
| 5-10% | BULLISH | Upside demand elevated |
| -3% to 5% | NEUTRAL | Normal market |
| -8% to -3% | BEARISH | Put protection bid |
| < -8% | VERY_BEARISH | Crash hedging active |

*Note: ETH skew tends to be more extreme than BTC*

### IV Percentile

| IV Percentile | Signal | ETH-Specific Action |
|---------------|--------|---------------------|
| > 85% | SELL_VOL | ETH vol mean-reverts faster than BTC |
| 70-85% | ELEVATED | Reduce long gamma |
| 30-70% | NORMAL | Balanced approach |
| 15-30% | DEPRESSED | Good entry for long vol |
| < 15% | BUY_VOL | Strong vol buying opportunity |

### ETH/BTC Implied Vol Ratio

| ETH IV / BTC IV | Signal | Interpretation |
|-----------------|--------|----------------|
| > 1.5 | ETH_VOL_PREMIUM | ETH expected to outperform/underperform |
| 1.2-1.5 | NORMAL_PREMIUM | Standard ETH beta |
| 1.0-1.2 | COMPRESSED | Unusual - watch for breakout |
| < 1.0 | INVERTED | Very rare - structural shift |

---

## ETH/BTC Ratio Trading

### Ratio Analysis

| ETH/BTC Ratio | Classification | Trade Bias |
|---------------|----------------|------------|
| > 0.055 | ETH_OUTPERFORMING | Consider short ratio |
| 0.045-0.055 | NEUTRAL_ZONE | No clear bias |
| 0.035-0.045 | ETH_UNDERPERFORMING | Consider long ratio |
| < 0.035 | EXTREME_UNDERPERFORMANCE | Strong long ratio |

### Ratio Trading Signals

| Signal | Conditions | Action |
|--------|------------|--------|
| LONG_RATIO | ETH/BTC < 0.04 + ETH funding < BTC funding | Long ETH, Short BTC |
| SHORT_RATIO | ETH/BTC > 0.055 + ETH funding >> BTC funding | Short ETH, Long BTC |
| RATIO_SQUEEZE | ETH L/S extreme + ETH/BTC at range boundary | Trade direction of squeeze |

---

## ETH On-Chain Integration

### Exchange Flows

| ETH Flow | Signal | Lead Time |
|----------|--------|-----------|
| > 100K ETH outflow (24h) | STRONG_ACCUMULATION | 24-48h bullish |
| 30-100K ETH outflow | MILD_ACCUMULATION | Gradual bullish |
| 30-100K ETH inflow | MILD_DISTRIBUTION | Gradual bearish |
| > 100K ETH inflow (24h) | STRONG_DISTRIBUTION | 24-48h bearish |

### MVRV Interpretation

| MVRV | ETH Cycle Position | Action |
|------|-------------------|--------|
| > 3.0 | CYCLE_TOP_ZONE | Take profits |
| 2.0-3.0 | LATE_BULL | Reduce exposure |
| 1.3-2.0 | MID_CYCLE | Normal positioning |
| 1.0-1.3 | EARLY_BULL | Accumulate |
| 0.8-1.0 | ACCUMULATION_ZONE | Strong accumulation |
| < 0.8 | CAPITULATION | Maximum accumulation |

*Note: ETH MVRV thresholds are slightly lower than BTC*

### Staking Dynamics

| Signal | Condition | Implication |
|--------|-----------|-------------|
| STAKING_INFLOWS | Net positive validator deposits | Supply reduction, bullish |
| STAKING_OUTFLOWS | Net validator withdrawals | Supply expansion, bearish |
| QUEUE_BUILDUP | Large exit queue | Potential selling pressure |
| UNSTAKING_WAVE | Mass withdrawals | Watch for cascade |

---

## CVD Signal Analysis

### Available CVD Data

| Data Source | Table | Update Frequency | Coverage |
|-------------|-------|------------------|----------|
| 5-Minute CVD | `cvd_aggregated` | Hourly | Binance, Bybit, OKX, Hyperliquid |
| Daily Summary | `cvd_daily_summary` | Daily @ 00:30 UTC | OHLC-style CVD metrics |
| Trading Signals | `cvd_signals` | Daily @ 00:30 UTC | Divergence detection |

### CVD Divergence Signals

The system detects 5 high-conviction divergence patterns:

| Signal Type | Trigger Condition | Direction | Confidence |
|-------------|-------------------|-----------|------------|
| `DISTRIBUTION` | Price rising + Spot CVD falling | BEARISH | HIGH |
| `LEVERAGE_TRAP` | Price rising + Perp CVD >> Spot CVD (ratio > 2) | BEARISH | VERY_HIGH |
| `ABSORPTION` | Price stable/down + Perp CVD falling rapidly | BULLISH | MEDIUM |
| `BULLISH_DIVERGENCE` | Price makes lower low + CVD makes higher low | BULLISH | HIGH |
| `BEARISH_DIVERGENCE` | Price makes higher high + CVD makes lower high | BEARISH | HIGH |

### ETH CVD Slope Thresholds

| 24h Slope | Signal | ETH-Specific Interpretation |
|-----------|--------|----------------------------|
| > 0.5 | `STRONG_BUYING` | Institutional accumulation - often follows BTC |
| 0.1 to 0.5 | `MILD_BUYING` | Gradual buying pressure |
| -0.1 to 0.1 | `NEUTRAL` | Balanced flow - range-bound |
| -0.5 to -0.1 | `MILD_SELLING` | Gradual distribution |
| < -0.5 | `STRONG_SELLING` | Aggressive distribution - may lead BTC down |

### ETH CVD vs ETH/BTC Ratio

**Key Insight:** ETH CVD diverging from BTC CVD often precedes ETH/BTC ratio moves.

| Scenario | ETH CVD | BTC CVD | ETH/BTC Implication |
|----------|---------|---------|---------------------|
| ETH Relative Strength | Rising | Flat | ETH/BTC ratio expansion likely |
| ETH Relative Weakness | Flat | Rising | ETH/BTC ratio compression likely |
| Synchronized | Rising | Rising | Beta trade - follow BTC |
| Both Weak | Falling | Falling | Risk-off - reduce exposure |

---

## ETH Liquidation Dynamics

### Historical Liquidation Clusters

Major ETH liquidation clusters form at:
- **Round Numbers:** $2000, $2500, $3000, $3500, $4000
- **Previous Cycle ATH:** ~$4,800 zone
- **DeFi Liquidation Levels:** Aave/Compound thresholds
- **Ratio Extremes:** When ETH/BTC hits range boundaries

### DeFi Liquidation Amplification

ETH liquidations can compound via DeFi:
- Aave/Compound loan liquidations
- CDP (Maker) liquidations
- Liquid staking derivative depegs

| DeFi Risk | Signal | Action |
|-----------|--------|--------|
| HIGH | Large loans near liquidation + Falling price | Expect cascade amplification |
| MODERATE | Some concentration near levels | Monitor DeFi dashboards |
| LOW | Healthy collateral ratios | Normal liquidation risk |

### Cascade Risk Assessment (ETH-Specific)

| Factor | Weight | ETH High Risk Threshold |
|--------|--------|-------------------------|
| ELR | 30 pts | > 4% (OI/MCap) |
| Funding | 25 pts | > 0.06% (8h) |
| Book Depth | 25 pts | < $50M within 2% |
| Price Near Liq Zone | 20 pts | < 2% from cluster |
| DeFi Amplification | +10 pts | Large loans near liquidation |

---

## ETH Scenario Templates

### ETH LOCAL_TOP

| Condition | ETH-Specific Check |
|-----------|-------------------|
| Price | New ATH or major resistance |
| CVD Signal | `DISTRIBUTION` or `BEARISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | 24h slope < -0.3 (selling pressure) |
| Funding | > 0.06% (8h) |
| Global L/S | > 2.3 |
| ETH/BTC | At ratio highs (> 0.055) |
| OI Change | > 10% in 24h |

**3+ conditions = HIGH conviction SHORT**

### ETH SHORT_SQUEEZE

| Condition | ETH-Specific Check |
|-----------|-------------------|
| Price | At major support |
| Funding | < -0.03% (8h) |
| OI | Rising into support |
| L/S | Falling rapidly (< 0.9) |
| ETH/BTC | At ratio lows (< 0.04) |
| BTC | Holding or rising |

**3+ conditions = HIGH conviction LONG on reclaim**

### ETH RATIO_REVERSAL

| Condition | Check |
|-----------|-------|
| ETH/BTC | At extreme (< 0.035 or > 0.06) |
| ETH Funding | Diverging from BTC funding |
| ETH L/S | Opposite extreme to ratio |
| Network Activity | Diverging from price |

**3+ conditions = HIGH conviction RATIO trade**

### ETH CAPITULATION_BOTTOM

| Condition | ETH-Specific Check |
|-----------|-------------------|
| OI Change | > -25% in 24h |
| Funding | Negative and falling |
| MVRV | < 0.9 |
| Exchange Outflows | > 100K ETH |
| Staking | Net inflows (confidence) |
| CVD Signal | `ABSORPTION` or `BULLISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | Stabilizing (slope returning toward 0 from negative) |

**4+ conditions = VERY_HIGH conviction LONG**

---

## Trading Considerations

### Entry Timing

| Setup | Best ETH Entry |
|-------|----------------|
| Long | Extreme negative funding + OI declining + support + ETH/BTC at lows |
| Short | Extreme positive funding + OI at ATH + resistance + ETH/BTC at highs |

### Position Sizing (ETH)

- ETH has higher volatility than BTC (1.3-1.5x)
- Maximum recommended leverage: 3-5x for swing trades
- Account for higher funding costs
- Reduce size 50% when ELR > 4%

### ETH-Specific Catalysts

| Catalyst | Expected Impact |
|----------|-----------------|
| Major Protocol Upgrade | High vol, direction unclear |
| ETF Flow Announcement | Directional based on news |
| Large DeFi Exploit | Bearish, watch for cascade |
| Staking Rate Change | Supply dynamics shift |
| L2 Milestone | Bullish if positive |

### Exit Signals

- Funding flipping from extreme = Momentum exhausted
- ETH/BTC ratio reversal = Rotation starting
- OI divergence from price = Unwind imminent
- DeFi liquidation cascade = Exit regardless of direction

---

## ETH Data Quality Notes

ETH has strong data availability:

### CVD Data Coverage
| Exchange | Spot CVD | Perp CVD | Update Frequency |
|----------|----------|----------|------------------|
| Binance | ✅ | ✅ | Hourly (5-min buckets) |
| Bybit | ✅ | ✅ | Hourly (5-min buckets) |
| OKX | ✅ | ✅ | Hourly (5-min buckets) |
| Hyperliquid | - | ✅ | Hourly (5-min buckets) |

### Other Data
- Good options data (Deribit) - GEX, skew, IV available
- Comprehensive on-chain (MVRV, SOPR, staking)
- Reliable L/S ratios across exchanges
- DeFi liquidation monitoring available
- CVD divergence signals auto-detected in `cvd_signals` table

**Confidence penalty: 0%** (very liquid, excellent data)
