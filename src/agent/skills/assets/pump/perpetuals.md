---
name: PUMP Perpetuals Agent
version: 3.0
asset: PUMP
type: overlay
domain: perpetuals
requires: [base]
last_updated: 2025-01-15
sources:
  - templates/report_prompts.py (DERIVATIVES_MICROSTRUCTURE_FRAMEWORK)
  - skills/domains/perpetuals.md (v3.0 Framework)
---

# PUMP Perpetuals Analysis v3.0

## Overview

PUMP (pump.fun token) perpetuals are highly speculative instruments tied to the meme coin launch platform. Analysis must heavily incorporate platform metrics and meme cycle positioning.

### Key Characteristics

- **Platform Revenue Token:** Value tied to Pump.fun fee generation
- **Meme Cycle Dependency:** Revenue highly correlated with meme market sentiment
- **Very High Volatility:** Extreme swings common, 10-20% daily moves
- **Limited Liquidity:** Thin order books, high slippage
- **No Options Market:** Cannot use GEX signals
- **Social Sentiment Driven:** Twitter/social activity is primary indicator

### Trading Venues

| Exchange | Type | Notes |
|----------|------|-------|
| Hyperliquid | DEX | Primary PUMP perps venue |
| Binance | CEX | If listed |
| Bybit | CEX | If listed |

*Note: PUMP perps availability may be limited - check current listings*

---

## PUMP Regime Detection

### Volatility Regime

PUMP exhibits the highest volatility of any tracked asset.

| Vol Percentile (30d) | Classification | PUMP-Specific Note |
|----------------------|----------------|---------------------|
| > 80th | HIGH_VOL | Expect 15-30% daily swings |
| 20th - 80th | NORMAL_VOL | 8-15% daily range typical |
| < 20th | LOW_VOL | Unusual - breakout imminent |

### Meme Cycle Regime

| Regime | Pump.fun Metrics | PUMP Price | Trading Approach |
|--------|------------------|------------|------------------|
| MEME_MANIA | Record launches, high revenue | Explosive up | Ride momentum, trail tight |
| MEME_COOLING | Declining launches, falling revenue | Bearish | Defensive/short |
| MEME_TROUGH | Very low activity | Bottoming | Accumulate if fundamentals hold |
| MEME_RECOVERY | Activity picking up | Early bullish | Position early |

---

## PUMP-Specific Signal Thresholds

### ELR (Estimated Leverage Ratio)

**ELR = Open Interest / Market Cap**

PUMP can sustain very high ELR due to speculative nature but is extremely risky.

| ELR | Classification | PUMP-Specific Implication |
|-----|----------------|---------------------------|
| < 6% | LOW | Room for leverage (relatively) |
| 6-10% | MODERATE | Elevated but manageable |
| 10-15% | HIGH | Cascade risk very high |
| > 15% | EXTREME | Imminent violent move |

*Note: PUMP has much higher natural ELR than majors due to speculative nature*

### Funding Rate Thresholds

PUMP funding can reach extreme levels rarely seen in other assets.

| Funding (8h) | Z-Score | Classification | PUMP-Specific Signal |
|--------------|---------|----------------|----------------------|
| > 0.20% | > 3.0 | EXTREME_GREED | Squeeze imminent |
| 0.10-0.20% | 2.0-3.0 | ELEVATED_GREED | Very unsustainable |
| 0.04-0.10% | 1.0-2.0 | BULLISH | Strong meme demand |
| -0.04 to 0.04% | -1.0-1.0 | NEUTRAL | Balanced |
| -0.10 to -0.04% | -2.0 to -1.0 | BEARISH | Potential long setup |
| < -0.10% | < -2.0 | EXTREME_FEAR | Strong long if platform holds |

### Long/Short Ratio Thresholds

PUMP attracts the most extreme retail speculation.

| Global L/S | Classification | Contrarian Signal |
|------------|----------------|-------------------|
| > 5.0 | EXTREME_LONG_CROWDING | Maximum short signal |
| 3.0-5.0 | HEAVY_LONG_BIAS | Strong short signal |
| 1.8-3.0 | NORMAL_LONG_BIAS | Moderate short signal |
| 0.8-1.8 | BALANCED | No contrarian signal |
| 0.4-0.8 | SHORT_BIAS | Moderate long signal |
| < 0.4 | EXTREME_SHORT_CROWDING | Maximum long signal |

### OI Thresholds

| OI Level | Classification | Implication |
|----------|----------------|-------------|
| > $200M | EXTREME | Dangerous leverage |
| $100-200M | ELEVATED | High risk |
| $50-100M | NORMAL | Moderate risk |
| < $50M | LOW | Quiet/capitulation |

---

## Platform Metrics - PRIMARY SIGNAL

PUMP analysis must center on Pump.fun platform performance.

### Daily Revenue Correlation

| Daily Revenue | Trend | PUMP Price Implication |
|---------------|-------|------------------------|
| > $3M | Rising | Strongly bullish |
| $1-3M | Stable | Neutral to bullish |
| $500K-1M | Declining | Bearish pressure |
| < $500K | Crashed | Capitulation zone |

### Token Launch Metrics

| Launches/Day | Signal | Interpretation |
|--------------|--------|----------------|
| > 15,000 | MEME_MANIA | Peak activity - potential top |
| 5,000-15,000 | HEALTHY | Good platform usage |
| 1,000-5,000 | DECLINING | Activity cooling |
| < 1,000 | CAPITULATION | Trough - potential bottom |

### Valuation Framework

**FDV/Revenue Multiple:**

| FDV / Annual Revenue | Classification | Signal |
|----------------------|----------------|--------|
| < 30x | UNDERVALUED | Strong accumulate |
| 30-50x | FAIR_VALUE | Hold |
| 50-100x | OVERVALUED | Take profits |
| > 100x | EXTREME_OVERVALUATION | Short or avoid |

---

## CVD Signal Analysis

### Available CVD Data

| Data Source | Table | Update Frequency | Coverage |
|-------------|-------|------------------|----------|
| 5-Minute CVD | `cvd_aggregated` | Hourly | Binance, Bybit, Hyperliquid |
| Daily Summary | `cvd_daily_summary` | Daily @ 00:30 UTC | OHLC-style CVD metrics |
| Trading Signals | `cvd_signals` | Daily @ 00:30 UTC | Divergence detection |

**Note:** PUMP CVD is now available via Hyperliquid native API + CEX listings (Binance, Bybit).

### CVD Divergence Signals

The system detects 5 high-conviction divergence patterns:

| Signal Type | Trigger Condition | Direction | Confidence |
|-------------|-------------------|-----------|------------|
| `DISTRIBUTION` | Price rising + Spot CVD falling | BEARISH | HIGH |
| `LEVERAGE_TRAP` | Price rising + Perp CVD >> Spot CVD (ratio > 2) | BEARISH | VERY_HIGH |
| `ABSORPTION` | Price stable/down + Perp CVD falling rapidly | BULLISH | MEDIUM |
| `BULLISH_DIVERGENCE` | Price makes lower low + CVD makes higher low | BULLISH | HIGH |
| `BEARISH_DIVERGENCE` | Price makes higher high + CVD makes lower high | BEARISH | HIGH |

### PUMP CVD vs Platform Revenue Priority

**Key Insight:** For PUMP, platform revenue remains the PRIMARY signal. CVD confirms/diverges.

| Platform Revenue | CVD Signal | Combined Interpretation |
|------------------|------------|------------------------|
| Rising | Rising CVD | Full confirmation - bullish |
| Rising | Falling CVD | Smart money selling into fundamentals |
| Falling | Rising CVD | Speculative buying - unsustainable |
| Falling | Falling CVD | Full confirmation - bearish |

### PUMP CVD Slope Thresholds

| 24h Slope | Signal | PUMP-Specific Interpretation |
|-----------|--------|------------------------------|
| > 0.8 | `STRONG_BUYING` | Meme cycle fuel - extreme caution at highs |
| 0.25 to 0.8 | `MILD_BUYING` | Gradual accumulation |
| -0.25 to 0.25 | `NEUTRAL` | Balanced - watch platform metrics |
| -0.8 to -0.25 | `MILD_SELLING` | Gradual distribution |
| < -0.8 | `STRONG_SELLING` | Aggressive selling - potential capitulation |

---

## PUMP Liquidation Dynamics

### Liquidation Characteristics

- Highest volatility = Fastest cascades
- Very low liquidity = Extreme wicks
- Platform metrics can change rapidly
- Social sentiment shifts can be instant

### Key Liquidation Levels

- Round numbers based on current price range
- Previous swing highs/lows
- FDV milestone levels

### Cascade Risk Assessment (PUMP-Specific)

| Factor | Weight | PUMP High Risk Threshold |
|--------|--------|--------------------------|
| ELR | 25 pts | > 12% (OI/MCap) |
| Funding | 25 pts | > 0.15% (8h) |
| L/S Extreme | 25 pts | > 4.0 or < 0.5 |
| Book Depth | 15 pts | < $5M within 2% |
| Platform Metrics | 10 pts | Revenue declining rapidly |

---

## PUMP Scenario Templates

### PUMP LOCAL_TOP

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| Price | At resistance or new high |
| CVD Signal | `DISTRIBUTION` or `BEARISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | 24h slope < -0.5 (selling pressure) |
| Funding | > 0.12% (8h) |
| Global L/S | > 4.0 |
| OI Change | > 20% in 24h |
| Platform Revenue | Flat or declining |
| Social Sentiment | Peak euphoria |
| Meme Launches | Record high (exhaustion) |

**4+ conditions = HIGH conviction SHORT**

### PUMP SHORT_SQUEEZE

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| Price | At major support |
| Funding | < -0.08% (8h) |
| Global L/S | < 0.5 |
| OI | Rising into support |
| Platform Revenue | Stable or rising |
| Meme Cycle | Not in full crash mode |

**4+ conditions = HIGH conviction LONG on reclaim**

### PUMP PLATFORM_DIVERGENCE

| Condition | Check |
|-----------|-------|
| Platform Revenue | Rising |
| Token Launches | Increasing |
| PUMP Price | Flat or falling |
| Funding | Neutral or negative |

**Platform fundamentals leading price = Accumulate**

### PUMP MEME_CYCLE_TOP

| Condition | Check |
|-----------|-------|
| Launches/Day | Record high (> 15K) |
| Social Sentiment | Maximum euphoria |
| Funding | Extreme positive |
| L/S | Extreme long |
| Revenue | Peaking |

**All conditions = Meme cycle top - aggressive short**

### PUMP CAPITULATION_BOTTOM

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| OI Change | > -35% in 24h |
| Funding | Deeply negative |
| L/S | Extreme short (< 0.4) |
| CVD Signal | `ABSORPTION` or `BULLISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | Stabilizing (slope returning toward 0 from negative) |
| Platform Revenue | Stabilizing (not zero) |
| Social | Maximum despair |

**4+ conditions = HIGH conviction LONG (if platform survives)**

---

## Trading Considerations

### Entry Timing

| Setup | Best PUMP Entry |
|-------|-----------------|
| Long | Extreme short crowding + Platform metrics stable + Meme cycle bottoming |
| Short | Extreme long crowding + Platform metrics declining + Meme cycle peaking |

### Position Sizing (PUMP)

- PUMP has extreme volatility (3-5x BTC)
- Maximum recommended leverage: 1-2x only
- Account for massive wicks and low liquidity
- Reduce size 50% when ELR > 10%
- Never size larger than you can afford to lose

### Risk Management - CRITICAL

| Risk | Mitigation |
|------|------------|
| Extreme wicks | Use limit orders, wide stops |
| Platform failure | Size for total loss possibility |
| Liquidity gaps | Avoid large market orders |
| Social pump/dump | Don't chase, wait for setup |

### Exit Signals

- L/S normalizing from extreme = Move exhausted
- Platform metrics diverging from price = Warning
- Social sentiment flipping = Trend change
- Funding flipping = Sentiment shift

---

## Meme Cycle Positioning

### Cycle Phase Detection

| Phase | Platform Metrics | Social Sentiment | Action |
|-------|------------------|------------------|--------|
| Early Cycle | Revenue rising | Growing interest | Accumulate |
| Peak Mania | Record everything | Maximum FOMO | Take profits |
| Crash | Revenue collapsing | Panic | Stay out / short |
| Trough | Minimal activity | Despair | Watch for stabilization |

### Cycle Duration

Historical meme cycles last 2-8 weeks:
- Early phase: 1-2 weeks
- Mania phase: 1-2 weeks
- Crash phase: 1-3 weeks
- Trough: Variable

---

## Social Sentiment Analysis

### Primary Indicators

| Indicator | Bullish | Bearish |
|-----------|---------|---------|
| Twitter mentions | Rising from low | Falling from high |
| Influencer posts | Increasing coverage | Abandoning topic |
| New user growth | Accelerating | Decelerating |
| Meme quality | Fresh narratives | Stale recycling |

### Sentiment vs Price

| Sentiment | Price | Signal |
|-----------|-------|--------|
| Euphoric | Rising | Late stage - cautious |
| Optimistic | Rising | Healthy trend |
| Fearful | Falling | Normal correction |
| Despair | Falling | Potential bottom |
| Apathetic | Flat | Accumulation zone |

---

## Data Quality Notes

PUMP has improved data availability:
- **No options market:** N/A
- **Good CVD data:** Now available via Hyperliquid + CEX listings
- **No traditional on-chain:** N/A
- **Platform metrics:** Primary data source (most important)
- **Social data:** Critical secondary source

### CVD Data Coverage
| Exchange | Spot CVD | Perp CVD | Update Frequency |
|----------|----------|----------|------------------|
| Binance | ✅ | ✅ | Hourly (5-min buckets) |
| Bybit | ✅ | ✅ | Hourly (5-min buckets) |
| Hyperliquid | - | ✅ | Hourly (5-min buckets) |

### Other Data Availability

| Data Point | Availability | Source |
|------------|--------------|--------|
| Funding Rate | Good | Hyperliquid + CEXs |
| Global L/S | Limited | If available |
| Top Trader L/S | None | N/A |
| OI | Good | Hyperliquid + CEXs |
| CVD Signals | ✅ Good | `cvd_signals` table - auto-detected |
| Platform Revenue | Excellent | Pump.fun API |
| Token Launches | Excellent | Pump.fun API |
| Social Sentiment | Good | Twitter/Discord |

**Confidence penalty: 30%** (lowest liquidity, limited L/S data, but improved CVD)

---

## Key PUMP Trading Rules

1. **Platform First:** Platform metrics are the primary signal
2. **Size Small:** Never oversize - wicks are brutal
3. **Respect the Cycle:** Don't fight meme cycle phases
4. **Social Matters:** Monitor Twitter/social actively
5. **Exit Discipline:** Take profits in mania, cut losses fast
6. **Survival First:** This is the highest risk asset - preserve capital
