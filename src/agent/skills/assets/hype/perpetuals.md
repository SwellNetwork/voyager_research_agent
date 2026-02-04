---
name: HYPE Perpetuals Agent
version: 3.0
asset: HYPE
type: overlay
domain: perpetuals
requires: [base]
last_updated: 2025-01-15
sources:
  - templates/report_prompts.py (DERIVATIVES_MICROSTRUCTURE_FRAMEWORK)
  - skills/domains/perpetuals.md (v3.0 Framework)
---

# HYPE Perpetuals Analysis v3.0

## Overview

HYPE is unique as both a tradeable asset AND the native token of Hyperliquid - a perpetual exchange. This creates powerful reflexive dynamics.

### Reflexivity Loop

```
Platform Volume Up → More Fees → HYPE Buybacks → Price Up
      ↑                                              ↓
      └──── Higher TVL ← More Staking ← Higher APY ←─┘
```

### Key Characteristics

- **DEX-Native Token:** HYPE is native to Hyperliquid exchange
- **Fee Capture:** 97% of trading fees go to HYPE buyback/burn
- **HLP Vault:** Unique liquidity provider vault with visible positions
- **On-Chain Transparency:** All positions visible on-chain
- **No CEX Top Trader Data:** Must rely on on-chain analysis

### Trading Venues

| Venue | Type | Notes |
|-------|------|-------|
| Hyperliquid | DEX | Native platform, highest liquidity |
| Binance | CEX | Large volume after listing |
| Bybit | CEX | Active trading |
| OKX | CEX | Growing volume |

---

## HYPE Regime Detection

### Volatility Regime

HYPE exhibits higher volatility than majors due to lower liquidity and reflexivity.

| Vol Percentile (30d) | Classification | HYPE-Specific Note |
|----------------------|----------------|---------------------|
| > 80th | HIGH_VOL | Expect 8-15% daily swings |
| 20th - 80th | NORMAL_VOL | 4-8% daily range typical |
| < 20th | LOW_VOL | Unusual calm - expect breakout |

### Platform Correlation Regime

| Regime | Platform Metrics | Price Action | Trading Approach |
|--------|------------------|--------------|------------------|
| BULL_REFLEXIVITY | Volume + TVL rising | Price rising | Ride trend |
| BEAR_REFLEXIVITY | Volume + TVL falling | Price falling | Stay defensive |
| DIVERGENCE_UP | Volume rising | Price flat/down | Accumulate |
| DIVERGENCE_DOWN | Volume falling | Price rising | Distribution - fade |

---

## HYPE-Specific Signal Thresholds

### ELR (Estimated Leverage Ratio)

**ELR = Open Interest / Market Cap**

HYPE has higher natural ELR due to reflexive trading (traders trade the platform they use).

| ELR | Classification | HYPE-Specific Implication |
|-----|----------------|---------------------------|
| < 4% | LOW | Room for leverage to build |
| 4-7% | MODERATE | Healthy leverage levels |
| 7-10% | HIGH | Elevated cascade risk |
| > 10% | EXTREME | Cascade likely on 5-8% move |

*Note: HYPE tolerates higher ELR due to loyal trader base*

### Funding Rate Thresholds

HYPE funding can be extremely volatile due to lower liquidity and narrative-driven trading.

| Funding (8h) | Z-Score | Classification | HYPE-Specific Signal |
|--------------|---------|----------------|----------------------|
| > 0.15% | > 3.0 | EXTREME_GREED | Very high squeeze risk |
| 0.08-0.15% | 2.0-3.0 | ELEVATED_GREED | Unsustainable |
| 0.03-0.08% | 1.0-2.0 | BULLISH | Strong demand |
| -0.03 to 0.03% | -1.0-1.0 | NEUTRAL | Balanced |
| -0.08 to -0.03% | -2.0 to -1.0 | BEARISH | Potential long setup |
| < -0.08% | < -2.0 | EXTREME_FEAR | Strong long opportunity |

### Long/Short Ratio Thresholds

HYPE attracts retail speculators - L/S extremes are more common.

| Global L/S | Classification | Contrarian Signal |
|------------|----------------|-------------------|
| > 4.0 | EXTREME_LONG_CROWDING | Strong short signal |
| 2.5-4.0 | HEAVY_LONG_BIAS | Moderate short signal |
| 1.5-2.5 | NORMAL_LONG_BIAS | Neutral |
| 0.8-1.5 | BALANCED | No contrarian signal |
| 0.4-0.8 | SHORT_BIAS | Moderate long signal |
| < 0.4 | EXTREME_SHORT_CROWDING | Strong long signal |

### OI Thresholds

| OI Level | Classification | Implication |
|----------|----------------|-------------|
| > $400M | EXTREME | High cascade risk for altcoin |
| $200-400M | ELEVATED | Above-average leverage |
| $100-200M | NORMAL | Healthy market |
| < $100M | LOW | Low interest/quiet market |

---

## HLP Vault Analysis - UNIQUE SIGNAL

The HLP (Hyperliquidity Provider) vault is unique to Hyperliquid. Its positions are visible ON-CHAIN - this is alpha unavailable elsewhere.

### HLP TVL Signals

| TVL Change (24h) | Signal | Interpretation |
|------------------|--------|----------------|
| > +5% | STRONG_INFLOWS | LPs bullish on vault performance |
| +1-5% | MILD_INFLOWS | Gradual LP additions |
| -1 to +1% | STABLE | No conviction either way |
| -5 to -1% | MILD_OUTFLOWS | Some LP withdrawals |
| < -5% | STRONG_OUTFLOWS | Risk-off signal - LPs leaving |

### HLP Position Bias

| HLP Net Exposure | Interpretation | Signal |
|------------------|----------------|--------|
| NET_LONG | Vault has long bias | Counter-indicator - be cautious on longs |
| NEUTRAL | Balanced positions | No bias |
| NET_SHORT | Vault has short bias | Counter-indicator - be cautious on shorts |

*Note: HLP often takes the opposite side of retail - watch for divergence*

### HLP PnL Correlation

| Scenario | HLP PnL | Market Direction | Signal |
|----------|---------|------------------|--------|
| HLP Winning | Positive | Any | Market likely to continue |
| HLP Losing | Negative | Trending | Trend may be overextended |
| HLP Flat | Near zero | Choppy | Range-bound market |

---

## Platform Metrics Correlation

### Volume-Price Relationship

| Volume Trend | Price Trend | Interpretation | Action |
|--------------|-------------|----------------|--------|
| Rising | Rising | BULLISH_REFLEXIVITY | Ride trend |
| Rising | Flat | VALUE_NOT_RECOGNIZED | Accumulate |
| Falling | Rising | SPECULATION | Fade - not sustainable |
| Falling | Falling | BEARISH_REFLEXIVITY | Stay defensive |

### HYPE Buyback Analysis

**HYPE Tokenomics:**
- 97% of trading fees → HYPE buyback/burn
- ~333,000 HYPE burned monthly (~$9M at $27)
- Fixed 1B supply, ~395M circulating

| Daily Buyback | Signal | Implication |
|---------------|--------|-------------|
| > $500K | HIGH_ACTIVITY | Strong platform usage |
| $200-500K | NORMAL_ACTIVITY | Healthy volume |
| < $200K | LOW_ACTIVITY | Quiet period |

### Implied Deflation Rate

```
Annual Deflation = (Daily Buyback x 365) / (Price x Circulating Supply)
```

| Deflation Rate | Signal | Note |
|----------------|--------|------|
| > 5% | STRONG_DEFLATION | Aggressive buybacks |
| 2-5% | MODERATE_DEFLATION | Healthy tokenomics |
| < 2% | WEAK_DEFLATION | Low platform activity |

---

## CVD Signal Analysis

### Available CVD Data

| Data Source | Table | Update Frequency | Coverage |
|-------------|-------|------------------|----------|
| 5-Minute CVD | `cvd_aggregated` | Hourly | Binance, Bybit, Hyperliquid |
| Daily Summary | `cvd_daily_summary` | Daily @ 00:30 UTC | OHLC-style CVD metrics |
| Trading Signals | `cvd_signals` | Daily @ 00:30 UTC | Divergence detection |

**Note:** HYPE CVD is now available via Hyperliquid native API + CEX listings (Binance, Bybit).

### CVD Divergence Signals

The system detects 5 high-conviction divergence patterns:

| Signal Type | Trigger Condition | Direction | Confidence |
|-------------|-------------------|-----------|------------|
| `DISTRIBUTION` | Price rising + Spot CVD falling | BEARISH | HIGH |
| `LEVERAGE_TRAP` | Price rising + Perp CVD >> Spot CVD (ratio > 2) | BEARISH | VERY_HIGH |
| `ABSORPTION` | Price stable/down + Perp CVD falling rapidly | BULLISH | MEDIUM |
| `BULLISH_DIVERGENCE` | Price makes lower low + CVD makes higher low | BULLISH | HIGH |
| `BEARISH_DIVERGENCE` | Price makes higher high + CVD makes lower high | BEARISH | HIGH |

### HYPE CVD Slope Thresholds

| 24h Slope | Signal | HYPE-Specific Interpretation |
|-----------|--------|------------------------------|
| > 0.7 | `STRONG_BUYING` | Aggressive accumulation - platform bullish |
| 0.2 to 0.7 | `MILD_BUYING` | Gradual buying pressure |
| -0.2 to 0.2 | `NEUTRAL` | Balanced flow |
| -0.7 to -0.2 | `MILD_SELLING` | Gradual distribution |
| < -0.7 | `STRONG_SELLING` | Aggressive distribution - platform sentiment shift |

### HYPE CVD vs Platform Metrics

**Key Insight:** HYPE CVD often correlates with platform volume/buyback changes.

| Scenario | HYPE CVD | Platform Volume | Interpretation |
|----------|----------|-----------------|----------------|
| Reflexive Bull | Rising | Rising | Positive feedback loop active |
| Early Accumulation | Rising | Flat | Smart money front-running volume |
| Distribution | Falling | Rising | Insiders selling into activity |
| Capitulation | Falling | Falling | Full risk-off mode |

---

## HYPE Liquidation Dynamics

### Liquidation Characteristics

- Higher volatility = Faster cascades
- Smaller market cap = Lower liquidity to absorb
- Reflexive dynamics can amplify moves
- Platform users may defend token price

### Key Liquidation Levels

- Round numbers: $20, $25, $30, $35, $40
- Previous highs/lows from consolidation
- Airdrop claim price zones

### Cascade Risk Assessment (HYPE-Specific)

| Factor | Weight | HYPE High Risk Threshold |
|--------|--------|--------------------------|
| ELR | 30 pts | > 8% (OI/MCap) |
| Funding | 25 pts | > 0.10% (8h) |
| Book Depth | 25 pts | < $15M within 2% |
| Price Near Liq Zone | 20 pts | < 3% from cluster |
| HLP Stressed | +10 pts | HLP PnL deeply negative |

---

## HYPE Scenario Templates

### HYPE LOCAL_TOP

| Condition | HYPE-Specific Check |
|-----------|---------------------|
| Price | New ATH or major resistance |
| CVD Signal | `DISTRIBUTION` or `BEARISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | 24h slope < -0.4 (selling pressure) |
| Funding | > 0.10% (8h) |
| Global L/S | > 3.5 |
| OI Change | > 15% in 24h |
| Platform Volume | Flat or declining |
| HLP Position | Net short (retail long) |

**3+ conditions = HIGH conviction SHORT**

### HYPE SHORT_SQUEEZE

| Condition | HYPE-Specific Check |
|-----------|---------------------|
| Price | At major support |
| Funding | < -0.05% (8h) |
| OI | Rising into support |
| L/S | Falling rapidly (< 0.6) |
| Platform Volume | Rising (bullish divergence) |
| HLP Position | Net long (retail short) |

**3+ conditions = HIGH conviction LONG on reclaim**

### HYPE PLATFORM_DIVERGENCE

| Condition | Check |
|-----------|-------|
| Platform Volume | Rising significantly |
| Price | Flat or falling |
| Funding | Neutral or negative |
| Buyback Rate | Increasing |

**Platform leading price = HIGH conviction LONG**

### HYPE CAPITULATION_BOTTOM

| Condition | HYPE-Specific Check |
|-----------|---------------------|
| OI Change | > -30% in 24h |
| Funding | Negative and falling |
| L/S | Extreme short (< 0.5) |
| CVD Signal | `ABSORPTION` or `BULLISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | Stabilizing (slope returning toward 0 from negative) |
| Platform Volume | Holding or rising |
| HLP TVL | Stable (confidence) |

**4+ conditions = VERY_HIGH conviction LONG**

---

## Trading Considerations

### Entry Timing

| Setup | Best HYPE Entry |
|-------|-----------------|
| Long | Extreme negative funding + Platform volume rising + L/S extreme short |
| Short | Extreme positive funding + Platform volume falling + L/S extreme long |

### Position Sizing (HYPE)

- HYPE has much higher volatility than majors (2-3x BTC)
- Maximum recommended leverage: 2-3x for swing trades
- Account for wider spreads and higher funding
- Reduce size 50% when ELR > 8%

### HYPE-Specific Catalysts

| Catalyst | Expected Impact |
|----------|-----------------|
| New Feature Launch | Bullish if successful |
| Volume Milestone | Reflexive bullish |
| CEX Listing | Short-term bullish |
| Competitor News | Varies by sentiment |
| Airdrop Unlock | Potential selling pressure |
| HLP Stress Event | Volatility spike |

### Exit Signals

- Funding flipping from extreme = Momentum exhausted
- Platform volume diverging from price = Warning sign
- HLP position flipping = Market structure change
- OI collapse without price follow-through = Deleveraging

---

## Data Quality Notes

HYPE has unique data characteristics:
- **No Binance Top Trader L/S:** Must rely on global L/S or on-chain HLP positions
- **Strong CVD data:** Now available via Hyperliquid + CEX listings
- **Excellent on-chain data:** HLP positions, staking, burns visible
- **Platform metrics:** Volume, TVL, buybacks are primary signals

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
| Global L/S | Partial | CEXs only |
| Top Trader L/S | Limited | No direct source |
| OI | Good | Hyperliquid + CEXs |
| HLP Positions | Excellent | On-chain |
| Platform Volume | Excellent | Hyperliquid API |
| CVD Signals | ✅ Good | `cvd_signals` table - auto-detected |

**Confidence penalty: 20%** (lower liquidity, limited top trader data)

---

## HYPE vs Platform Performance

Always analyze HYPE relative to platform performance:

| Scenario | HYPE Action | Note |
|----------|-------------|------|
| Platform growing, HYPE lagging | Accumulate | Market not pricing growth |
| Platform flat, HYPE pumping | Cautious | Speculation ahead of fundamentals |
| Platform declining, HYPE holding | Warning | May be distribution |
| Both declining | Defensive | Bear market dynamics |
| Both rising | Ride trend | Healthy reflexivity |
