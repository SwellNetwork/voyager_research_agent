---
name: BTC Perpetuals Agent
version: 3.0
asset: BTC
type: overlay
domain: perpetuals
requires: [base]
last_updated: 2025-01-15
sources:
  - templates/report_prompts.py (DERIVATIVES_MICROSTRUCTURE_FRAMEWORK)
  - skills/domains/perpetuals.md (v3.0 Framework)
---

# BTC Perpetuals Analysis v3.0

## Overview

Bitcoin perpetuals are the most liquid crypto derivative globally. BTC is the benchmark asset and leads altcoin moves.

### Key Venues

| Exchange | Type | Notes |
|----------|------|-------|
| Binance | CEX | Largest volume, regulatory concerns |
| Bybit | CEX | High leverage, active retail base |
| OKX | CEX | Strong Asia flow |
| CME | Regulated | Institutional, cash-settled |
| Hyperliquid | DEX | Growing decentralized volume |
| dYdX | DEX | Orderbook-based perps |

### BTC-Specific Characteristics

- **Most Liquid:** Tightest spreads, deepest order books
- **Benchmark Asset:** Leads altcoin moves
- **Institutional Hedging:** CME used for basis trades
- **Funding Arbitrage:** Primary target for arb strategies
- **Options Market:** Deep Deribit liquidity enables GEX analysis

---

## BTC Regime Detection

### Volatility Regime (GARCH-TGARCH)

BTC exhibits asymmetric volatility - negative shocks increase vol more than positive shocks.

| Vol Percentile (30d) | Classification | BTC-Specific Note |
|----------------------|----------------|-------------------|
| > 80th | HIGH_VOL | Expect 3-5% daily swings |
| 20th - 80th | NORMAL_VOL | 1-3% daily range typical |
| < 20th | LOW_VOL | Compression precedes expansion |

### GEX Regime (BTC-Specific)

BTC has the deepest options market - GEX signals are highly reliable.

| GEX State | Price Behavior | Trading Approach |
|-----------|----------------|------------------|
| POSITIVE_GEX | Pins to strikes, dampened moves | Fade extremes, range trade |
| NEGATIVE_GEX | Momentum amplified | Trade breakouts, follow trends |

**Key BTC GEX Levels:**
- Watch for gamma flip near round numbers ($90K, $100K, $110K)
- Max gamma strike often acts as weekly magnet
- Quarterly expiry dates have strongest pin effects

---

## BTC-Specific Signal Thresholds

### ELR (Estimated Leverage Ratio)

**ELR = Open Interest / Market Cap**

| ELR | Classification | BTC-Specific Implication |
|-----|----------------|--------------------------|
| < 1.5% | LOW | Room for leverage to build |
| 1.5-2.5% | MODERATE | Healthy leverage levels |
| 2.5-4% | HIGH | Elevated cascade risk |
| > 4% | EXTREME | Cascade likely on 3-5% move |

*Note: At ~$1.5T market cap, 4% ELR = $60B OI (historically extreme)*

### Funding Rate Thresholds

BTC funding rates historically mean-revert more slowly than altcoins due to structural long bias.

| Funding (8h) | Z-Score | Classification | BTC-Specific Signal |
|--------------|---------|----------------|---------------------|
| > 0.08% | > 3.0 | EXTREME_GREED | Cycle tops form here |
| 0.04-0.08% | 2.0-3.0 | ELEVATED_GREED | Sustainable in strong bull runs |
| 0.02-0.04% | 1.0-2.0 | BULLISH | Healthy bull market range |
| 0.01-0.02% | 0.5-1.0 | NORMAL_BULLISH | Trend continuation likely |
| -0.01 to 0.01% | -0.5-0.5 | NEUTRAL | Balanced, low crowding |
| -0.02 to -0.01% | -1.0 to -0.5 | NORMAL_BEARISH | Healthy downtrend |
| -0.04 to -0.02% | -2.0 to -1.0 | ELEVATED_FEAR | Short squeeze building |
| < -0.04% | < -2.0 | EXTREME_FEAR | Historically excellent long entries |

### Long/Short Ratio Thresholds

BTC L/S behaves differently due to structural long bias from holders.

| Global L/S | Classification | Contrarian Signal |
|------------|----------------|-------------------|
| > 3.0 | EXTREME_LONG_CROWDING | Strong short signal |
| 2.0-3.0 | HEAVY_LONG_BIAS | Moderate short signal |
| 1.2-2.0 | NORMAL_LONG_BIAS | Neutral to slight bearish |
| 0.8-1.2 | BALANCED | No contrarian signal |
| 0.5-0.8 | SHORT_BIAS | Moderate long signal |
| < 0.5 | EXTREME_SHORT_CROWDING | Strong long signal |

### OI Thresholds (Aggregate)

| OI Level | Classification | Implication |
|----------|----------------|-------------|
| > $30B | EXTREME | High liquidation cascade risk |
| $20-30B | ELEVATED | Above-average leverage |
| $12-20B | NORMAL | Healthy market |
| < $12B | LOW | Capitulation or quiet market |

---

## BTC Options Signals

### 25-Delta Risk Reversal

| Skew | Classification | BTC-Specific Behavior |
|------|----------------|----------------------|
| > 8% | VERY_BULLISH | Strong call buying - FOMO phase |
| 4-8% | BULLISH | Upside demand elevated |
| -2% to 4% | NEUTRAL | Normal market |
| -6% to -2% | BEARISH | Put protection bid |
| < -6% | VERY_BEARISH | Crash hedging active |

### IV Percentile

| IV Percentile | Signal | BTC-Specific Action |
|---------------|--------|---------------------|
| > 85% | SELL_VOL | Consider selling strangles |
| 70-85% | ELEVATED | Reduce long gamma |
| 30-70% | NORMAL | Balanced approach |
| 15-30% | DEPRESSED | Cheap protection available |
| < 15% | BUY_VOL | Load up on options |

### Max Pain & CME Expiry

BTC max pain is significant due to:
- Large institutional OI on Deribit + CME
- Quarterly expiry concentrations
- Friday CME settlement creates gap risk

**BTC Expiry Calendar:**
- Deribit: Daily, Weekly, Monthly, Quarterly
- CME: Monthly (last Friday), Quarterly
- Watch for convergence to max pain in final 72 hours

---

## CME-Specific Dynamics

### CME Gap Analysis

| Gap Size | Fill Probability | Timeline |
|----------|------------------|----------|
| < 2% | ~60% | 1-3 days |
| 2-4% | ~70% | 1-2 weeks |
| > 4% | ~75% | 2-4 weeks |

**CME Gap Trading:**
- Gaps form Friday 5pm ET to Sunday 6pm ET
- Large gaps often coincide with liquidation events
- Fade gap fills when OI is elevated

### Basis Trade Flow

| CME Basis (Annualized) | Signal | Interpretation |
|------------------------|--------|----------------|
| > 15% | EXTREME_CONTANGO | Euphoria, carry trade attractive |
| 8-15% | HEALTHY_CONTANGO | Normal bull market |
| 3-8% | MILD_CONTANGO | Balanced |
| 0-3% | FLAT | Neutral |
| < 0% | BACKWARDATION | Extreme fear, unwinding pressure |

### COT Report Signals

| Positioning | Signal | Interpretation |
|-------------|--------|----------------|
| Asset Managers Net Long (Extreme) | BULLISH_CONSENSUS | Watch for reversal |
| Asset Managers Net Long (Normal) | BULLISH | Institutional support |
| Leveraged Funds Net Short (Extreme) | CONTRARIAN_BULLISH | Hedging overdone |
| Leveraged Funds Net Short (Normal) | BEARISH | Directional short bias |

---

## BTC On-Chain Integration

### Exchange Flows

| BTC Flow | Signal | Lead Time |
|----------|--------|-----------|
| > 10K BTC outflow (24h) | STRONG_ACCUMULATION | 24-48h bullish |
| 3-10K BTC outflow | MILD_ACCUMULATION | Gradual bullish |
| 3-10K BTC inflow | MILD_DISTRIBUTION | Gradual bearish |
| > 10K BTC inflow (24h) | STRONG_DISTRIBUTION | 24-48h bearish |

### MVRV Interpretation

| MVRV | BTC Cycle Position | Action |
|------|-------------------|--------|
| > 3.5 | CYCLE_TOP_ZONE | Take profits - historically marks tops |
| 2.5-3.5 | LATE_BULL | Reduce exposure |
| 1.5-2.5 | MID_CYCLE | Normal positioning |
| 1.0-1.5 | EARLY_BULL | Accumulate |
| 0.8-1.0 | ACCUMULATION_ZONE | Strong accumulation |
| < 0.8 | CAPITULATION | Maximum accumulation |

### SOPR Context

| SOPR | BTC-Specific Signal |
|------|---------------------|
| > 1.05 | Profit-taking at highs - distribution phase |
| 1.00-1.05 | Normal profit-taking in uptrend |
| 0.98-1.00 | Breakeven reset - often marks correction end |
| < 0.98 | Capitulation - often marks local bottom |

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

### BTC CVD Slope Thresholds

| 24h Slope | Signal | BTC-Specific Interpretation |
|-----------|--------|----------------------------|
| > 0.5 | `STRONG_BUYING` | Institutional accumulation - trend continuation |
| 0.1 to 0.5 | `MILD_BUYING` | Gradual buying pressure |
| -0.1 to 0.1 | `NEUTRAL` | Balanced flow - range-bound |
| -0.5 to -0.1 | `MILD_SELLING` | Gradual distribution |
| < -0.5 | `STRONG_SELLING` | Aggressive distribution - reversal warning |

### Spot vs Perp CVD Divergence

**Key Insight:** Spot CVD reflects genuine demand; Perp CVD reflects leveraged speculation.

| Scenario | Spot CVD | Perp CVD | Interpretation |
|----------|----------|----------|----------------|
| Genuine Rally | Rising | Rising | Confirmed uptrend - buy dips |
| Leverage Trap | Flat/Down | Rising strongly | Fake rally - prepare to short |
| Distribution | Falling | Any | Smart money exiting - bearish |
| Accumulation | Rising | Flat/Down | Whales buying, retail short - bullish |

---

## BTC Liquidation Dynamics

### Historical Liquidation Clusters

Major BTC liquidation clusters form at:
- **Round Numbers:** $50K, $60K, $90K, $100K, $110K
- **Previous Range Highs/Lows:** Prior consolidation boundaries
- **CME Gap Fills:** Weekend gaps often get filled
- **ATH Zones:** Stop clusters above ATH

### Cascade Risk Assessment (BTC-Specific)

| Factor | Weight | BTC High Risk Threshold |
|--------|--------|-------------------------|
| ELR | 30 pts | > 3% (OI/MCap) |
| Funding | 25 pts | > 0.05% (8h) |
| Book Depth | 25 pts | < $100M within 2% |
| Price Near Liq Zone | 20 pts | < 2% from cluster |

---

## BTC Scenario Templates

### BTC LOCAL_TOP

| Condition | BTC-Specific Check |
|-----------|-------------------|
| Price | New ATH or major resistance |
| CVD Signal | `DISTRIBUTION` or `BEARISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | 24h slope < -0.3 (selling pressure) |
| Funding | > 0.05% (8h) |
| Global L/S | > 2.5 |
| OI Change | > 8% in 24h |
| MVRV | > 2.5 |

**3+ conditions = HIGH conviction SHORT**

### BTC SHORT_SQUEEZE

| Condition | BTC-Specific Check |
|-----------|-------------------|
| Price | At major support or range low |
| Funding | < -0.02% (8h) |
| OI | Rising into support |
| L/S | Falling rapidly (< 1.0) |
| CME Basis | Compressing or backwardated |

**3+ conditions = HIGH conviction LONG on reclaim**

### BTC CAPITULATION_BOTTOM

| Condition | BTC-Specific Check |
|-----------|-------------------|
| OI Change | > -20% in 24h |
| Funding | Negative and falling |
| SOPR | < 0.95 |
| Exchange Outflows | > 10K BTC |
| MVRV | < 1.0 |
| CVD Signal | `ABSORPTION` or `BULLISH_DIVERGENCE` in `cvd_signals` table |
| CVD Slope | Stabilizing (slope returning toward 0 from negative) |

**4+ conditions = VERY_HIGH conviction LONG**

---

## Trading Considerations

### Entry Timing

| Setup | Best BTC Entry |
|-------|----------------|
| Long | Extreme negative funding + OI declining + key support + MVRV < 1.5 |
| Short | Extreme positive funding + OI at ATH + key resistance + MVRV > 2.5 |

### Position Sizing (BTC)

- BTC has lower volatility than altcoins (typically 60-80% of alts)
- Maximum recommended leverage: 5-10x for swing trades
- Account for funding costs in multi-day positions
- Reduce size 50% when ELR > 3%

### Exit Signals

- Funding flipping from extreme to normal = Momentum exhausted
- OI divergence from price = Position unwind imminent
- CME gap fill completed = Take partial profits
- MVRV reaching cycle extreme = Scale out

---

## BTC Data Quality Notes

BTC has the most complete data availability:

### CVD Data Coverage
| Exchange | Spot CVD | Perp CVD | Update Frequency |
|----------|----------|----------|------------------|
| Binance | ✅ | ✅ | Hourly (5-min buckets) |
| Bybit | ✅ | ✅ | Hourly (5-min buckets) |
| OKX | ✅ | ✅ | Hourly (5-min buckets) |
| Hyperliquid | - | ✅ | Hourly (5-min buckets) |

### Other Data
- Deep options data (Deribit + CME) - GEX, skew, IV available
- Comprehensive on-chain metrics (MVRV, SOPR)
- Reliable L/S ratios across exchanges
- CVD divergence signals auto-detected in `cvd_signals` table

**Confidence penalty: 0%** (most liquid, best data)
