---
name: SOL Perpetuals Agent
version: 3.0
asset: SOL
type: overlay
domain: perpetuals
requires: [base]
last_updated: 2025-01-15
sources:
  - templates/report_prompts.py (DERIVATIVES_MICROSTRUCTURE_FRAMEWORK)
  - skills/domains/perpetuals.md (v3.0 Framework)
---

# SOL Perpetuals Analysis v3.0

## Overview

Solana perpetuals are the third most liquid crypto derivative after BTC and ETH, with unique characteristics tied to ecosystem activity.

### Key Characteristics

- **High Beta to BTC/ETH:** Often moves 1.5-2x BTC moves
- **Ecosystem Correlation:** DEX volume, NFT activity, meme coins affect price
- **Retail Speculation:** High retail participation, especially during meme cycles
- **No Options Market:** Limited options data - cannot use GEX signals
- **Network Event Risk:** Historical outages create sudden volatility

### Trading Venues

| Exchange | Type | Notes |
|----------|------|-------|
| Binance | CEX | Largest SOL perps volume |
| Bybit | CEX | Active leverage trading |
| OKX | CEX | Strong derivatives suite |
| Hyperliquid | DEX | Growing SOL volume |
| dYdX | DEX | Orderbook-based perps |

---

## SOL Regime Detection

### Volatility Regime (CGARCH)

SOL exhibits both short-term and long-term volatility components - use CGARCH for forecasting.

| Vol Percentile (30d) | Classification | SOL-Specific Note |
|----------------------|----------------|-------------------|
| > 80th | HIGH_VOL | Expect 6-12% daily swings |
| 20th - 80th | NORMAL_VOL | 3-6% daily range typical |
| < 20th | LOW_VOL | Compression - breakout imminent |

### Ecosystem Activity Regime

| Regime | Ecosystem Metrics | Price Action | Trading Approach |
|--------|-------------------|--------------|------------------|
| MEME_MANIA | Pump.fun volume spiking | High vol, momentum | Trade momentum, tight stops |
| DeFi_GROWTH | DEX/TVL growing steadily | Bullish bias | Trend follow |
| QUIET_ACCUMULATION | Low activity, stable metrics | Range-bound | Mean reversion |
| RISK_OFF | Activity declining | Bearish bias | Defensive/short |

---

## SOL-Specific Signal Thresholds

### ELR (Estimated Leverage Ratio)

**ELR = Open Interest / Market Cap**

SOL has higher natural ELR due to retail speculation and meme correlation.

| ELR | Classification | SOL-Specific Implication |
|-----|----------------|--------------------------|
| < 3% | LOW | Room for leverage to build |
| 3-5% | MODERATE | Healthy leverage levels |
| 5-8% | HIGH | Elevated cascade risk |
| > 8% | EXTREME | Cascade likely on 5-7% move |

*Note: At ~$80B market cap, 8% ELR = $6.4B OI*

### Funding Rate Thresholds

SOL funding is more volatile than BTC/ETH due to higher retail participation.

| Funding (8h) | Z-Score | Classification | SOL-Specific Signal |
|--------------|---------|----------------|---------------------|
| > 0.12% | > 3.0 | EXTREME_GREED | Very high squeeze risk |
| 0.06-0.12% | 2.0-3.0 | ELEVATED_GREED | Unsustainable, fade setup |
| 0.02-0.06% | 1.0-2.0 | BULLISH | Strong demand |
| -0.02 to 0.02% | -1.0-1.0 | NEUTRAL | Balanced |
| -0.06 to -0.02% | -2.0 to -1.0 | BEARISH | Potential long setup |
| < -0.06% | < -2.0 | EXTREME_FEAR | Strong long opportunity |

### Long/Short Ratio Thresholds

SOL attracts heavy retail speculation - L/S extremes are common.

| Global L/S | Classification | Contrarian Signal |
|------------|----------------|-------------------|
| > 3.5 | EXTREME_LONG_CROWDING | Strong short signal |
| 2.2-3.5 | HEAVY_LONG_BIAS | Moderate short signal |
| 1.3-2.2 | NORMAL_LONG_BIAS | Neutral |
| 0.7-1.3 | BALANCED | No contrarian signal |
| 0.4-0.7 | SHORT_BIAS | Moderate long signal |
| < 0.4 | EXTREME_SHORT_CROWDING | Strong long signal |

### OI Thresholds (Aggregate)

| OI Level | Classification | Implication |
|----------|----------------|-------------|
| > $5B | EXTREME | High cascade risk |
| $3-5B | ELEVATED | Above-average leverage |
| $1.5-3B | NORMAL | Healthy market |
| < $1.5B | LOW | Capitulation or quiet |

---

## Ecosystem Correlation Signals

### DEX Volume Correlation

| DEX Volume Trend | Price Trend | Signal | Action |
|------------------|-------------|--------|--------|
| Rising | Rising | HEALTHY_RALLY | Ride trend |
| Rising | Flat | BULLISH_DIVERGENCE | Accumulate |
| Falling | Rising | WARNING | Distribution likely |
| Falling | Falling | BEAR_MARKET | Defensive |

### Meme Coin Activity (Pump.fun)

| Pump.fun Activity | SOL Impact | Signal |
|-------------------|------------|--------|
| Volume spiking | Bullish | Network usage = demand |
| Launches > 10K/day | Very bullish | Meme mania in progress |
| Activity declining | Bearish | Risk-off rotation |
| Very quiet | Neutral | Wait for catalyst |

### TVL Dynamics

| TVL Trend | Signal | Interpretation |
|-----------|--------|----------------|
| Rising > 10% MoM | CAPITAL_INFLOW | Bullish for ecosystem |
| Stable | NEUTRAL | Mature phase |
| Falling > 10% MoM | CAPITAL_OUTFLOW | Bearish pressure |

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

### SOL CVD Slope Thresholds

| 24h Slope | Signal | SOL-Specific Interpretation |
|-----------|--------|----------------------------|
| > 0.6 | `STRONG_BUYING` | Strong accumulation - meme season fuel |
| 0.15 to 0.6 | `MILD_BUYING` | Gradual buying pressure |
| -0.15 to 0.15 | `NEUTRAL` | Balanced flow - range-bound |
| -0.6 to -0.15 | `MILD_SELLING` | Gradual distribution |
| < -0.6 | `STRONG_SELLING` | Aggressive distribution - ecosystem cooling |

### SOL CVD vs Ecosystem Correlation

**Key Insight:** SOL CVD often leads ecosystem metrics (DEX volume, TVL) by 12-24 hours.

| Scenario | SOL CVD | Ecosystem Activity | Interpretation |
|----------|---------|-------------------|----------------|
| Leading Indicator | Rising | Flat | Accumulation before activity spike |
| Confirmation | Rising | Rising | Healthy ecosystem rally |
| Distribution Warning | Falling | Rising | Smart money exiting meme cycle top |
| Capitulation | Falling | Falling | Risk-off - wait for stabilization |

---

## SOL Liquidation Dynamics

### Liquidation Characteristics

- Higher volatility than BTC/ETH = faster cascades
- Retail-heavy = more aggressive leverage usage
- Ecosystem events (outages) can trigger cascades
- Meme cycle correlation creates additional volatility

### Key Liquidation Levels

- Round numbers: $100, $125, $150, $175, $200, $250
- Previous cycle ATH: ~$260 zone
- FTX-era support levels
- Meme cycle highs/lows

### Cascade Risk Assessment (SOL-Specific)

| Factor | Weight | SOL High Risk Threshold |
|--------|--------|-------------------------|
| ELR | 30 pts | > 6% (OI/MCap) |
| Funding | 25 pts | > 0.08% (8h) |
| Book Depth | 25 pts | < $30M within 2% |
| Price Near Liq Zone | 20 pts | < 3% from cluster |
| Meme Correlation | +10 pts | Pump.fun volume spiking |

---

## SOL Scenario Templates

### SOL LOCAL_TOP

| Condition | SOL-Specific Check |
|-----------|-------------------|
| Price | New ATH or major resistance |
| CVD Signal | `DISTRIBUTION` or `BEARISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | 24h slope < -0.3 (selling pressure) |
| Funding | > 0.08% (8h) |
| Global L/S | > 3.0 |
| OI Change | > 12% in 24h |
| Meme Activity | Peak mania (> 10K launches/day) |
| DEX Volume | Flat or declining |

**3+ conditions = HIGH conviction SHORT**

### SOL SHORT_SQUEEZE

| Condition | SOL-Specific Check |
|-----------|-------------------|
| Price | At major support |
| Funding | < -0.04% (8h) |
| OI | Rising into support |
| L/S | Falling rapidly (< 0.6) |
| Ecosystem | Activity holding or rising |
| BTC/ETH | Holding or rising |

**3+ conditions = HIGH conviction LONG on reclaim**

### SOL MEME_CYCLE_TOP

| Condition | Check |
|-----------|-------|
| Pump.fun | Record launches/volume |
| SOL Funding | Extreme positive |
| Social Sentiment | Peak euphoria |
| DEX Volume | Declining from peak |

**3+ conditions = Meme cycle topping - fade SOL**

### SOL CAPITULATION_BOTTOM

| Condition | SOL-Specific Check |
|-----------|-------------------|
| OI Change | > -25% in 24h |
| Funding | Negative and falling |
| L/S | Extreme short (< 0.5) |
| CVD Signal | `ABSORPTION` or `BULLISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | Stabilizing (slope returning toward 0 from negative) |
| Ecosystem | TVL stable (no panic) |
| Network | No technical issues |

**4+ conditions = VERY_HIGH conviction LONG**

### SOL NETWORK_EVENT

| Condition | Check |
|-----------|-------|
| Network Status | Degraded/Outage |
| OI | Elevated |
| Funding | Any level |

**Network event + High OI = Expect cascade - wait for resolution**

---

## Trading Considerations

### Entry Timing

| Setup | Best SOL Entry |
|-------|----------------|
| Long | Extreme negative funding + OI declining + ecosystem activity stable |
| Short | Extreme positive funding + OI at highs + meme cycle peaking |

### Position Sizing (SOL)

- SOL has higher volatility than BTC/ETH (1.5-2x)
- Maximum recommended leverage: 3-5x for swing trades
- Account for higher funding costs and wider spreads
- Reduce size 50% when ELR > 6%
- Reduce size during network instability

### SOL-Specific Catalysts

| Catalyst | Expected Impact |
|----------|-----------------|
| Network Upgrade | Volatility spike, direction varies |
| Network Outage | Bearish cascade risk |
| Major Airdrop | Short-term bullish |
| Meme Coin Launch | Bullish if successful |
| ETF Speculation | Directional based on news |
| Jupiter/Raydium News | Ecosystem sentiment |

### Exit Signals

- Funding flipping from extreme = Momentum exhausted
- Ecosystem metrics diverging from price = Warning
- Network degradation = Exit regardless of direction
- OI collapse without price follow-through = Deleveraging

---

## SOL vs BTC Correlation

### Beta Analysis

| Condition | SOL Beta | Trading Implication |
|-----------|----------|---------------------|
| BTC trending up | 1.3-1.8x | SOL outperforms |
| BTC trending down | 1.5-2.5x | SOL underperforms more |
| BTC ranging | Variable | SOL driven by ecosystem |

### Correlation Regime

| SOL/BTC Correlation | Market Phase | Approach |
|---------------------|--------------|----------|
| High (> 0.8) | Risk-on/off driven | Trade BTC direction |
| Medium (0.5-0.8) | Normal | Blend BTC + ecosystem |
| Low (< 0.5) | SOL-specific drivers | Focus on ecosystem |

---

## Data Quality Notes

SOL has good but not comprehensive data:
- **No options market:** Cannot calculate GEX or skew
- **Strong CVD data:** Full coverage from all major exchanges
- **Limited on-chain metrics:** No MVRV/SOPR like BTC/ETH
- **Strong ecosystem data:** DEX volume, TVL, meme metrics

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
| Global L/S | Good | Binance/Bybit/OKX |
| Top Trader L/S | Good | Binance/Bybit |
| OI | Good | Multiple CEXs + DEXs |
| CVD Signals | ✅ Good | `cvd_signals` table - auto-detected |
| Options/GEX | None | N/A |
| Ecosystem Metrics | Excellent | DefiLlama, Pump.fun |

**Confidence penalty: 10%** (no options data, limited on-chain)
