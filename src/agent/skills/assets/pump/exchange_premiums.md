---
name: PUMP Exchange Premiums Agent
version: 2.0
asset: PUMP
type: overlay
domain: exchange_premiums
requires: [base]
last_updated: 2026-01-16
sources:
  - skills/domains/exchange_premiums.md (v2.0 Framework)
  - voyager_reflex/components/analytics/exchange_insights.py
data_limitations:
  - Not listed on Coinbase (no US vs Asia premium)
  - No Hyperliquid spot market (perp only)
---

# PUMP Exchange Premiums Analysis v2.0

## Overview

PUMP (Pump.fun token) has the most limited exchange premium data of all supported tokens. It is **not listed on Coinbase** (no US vs Asia premium) and has **no Hyperliquid spot market** (perp only). Analysis focuses primarily on Binance and Bybit leverage sentiment. As a meme token, PUMP exhibits extreme volatility requiring specialized handling.

### Key Characteristics

- **No Coinbase:** US vs Asia premium unavailable
- **No HL Spot:** Only perp trading on Hyperliquid
- **High Volatility:** Meme token characteristics (3-5x BTC volatility)
- **Retail Heavy:** Dominated by retail traders
- **Limited Data:** Most constrained premium analysis
- **Liquidity Risk:** Thin order books, potential air pockets
- **Token Calibration:** 3.0x multiplier (meme token thresholds - widest calibration)

---

## Data Limitations

**US vs Asia Premium:** Not available. PUMP is not listed on Coinbase.

**Hyperliquid:** PUMP does not have a spot market on Hyperliquid. HL data shows perp vs CEX comparison only, not true perp/spot spread.

**Analysis Focus:** Binance and Bybit leverage sentiment only.

---

## Liquidity Vacuum Indicators (Critical for PUMP)

### Understanding Air Pockets

Meme tokens like PUMP are susceptible to "air pockets" - gaps in order book liquidity where price can flash crash:

**Oct 11, 2025 Reference:**
- ATOM crashed to $0.001 on Binance (order book evaporated)
- Similar risk exists for all low-liquidity tokens including PUMP

### Liquidity Vacuum Detection

**Indicators:**
1. Order book depth declining at multiple levels
2. Bid-ask spread widening rapidly
3. Large orders appear without counter-orders
4. Volume spikes with minimal price impact (hidden liquidity)

**Risk Assessment:**

| Depth Indicator | Risk Level | Action |
|-----------------|-----------|--------|
| Normal depth across levels | LOW | Standard trading |
| Thin depth at 1-2% from mid | MEDIUM | Reduce position size |
| Air pockets visible (no bids/asks) | HIGH | Exit or hedge immediately |
| Depth-Weighted Price diverging from Last | CRISIS | Use Depth-Weighted Price only |

### Depth-Weighted Price vs Last Price

During crashes, use **Depth-Weighted Price** instead of Last Price:

```
Depth-Weighted Price = Σ(Price_i × Depth_i) / Σ(Depth_i)

Where depth is aggregated across top 10 levels
```

**When to Use:**
- Arbitrage Index > 1.10 for PUMP
- Last Price deviating > 5% from depth-weighted
- Volume spike with price discontinuity

---

## PUMP Arbitrage Index (Extreme Ranges)

PUMP has the widest arbitrage bands of all covered assets:

| Arbitrage Index | PUMP-Specific Interpretation |
|-----------------|----------------------------|
| 1.000 - 1.015 | Normal for PUMP |
| 1.015 - 1.040 | Mild stress - elevated volatility |
| 1.040 - 1.080 | Moderate stress - retail FOMO/panic |
| 1.080 - 1.150 | High stress - flash crash risk |
| > 1.150 | Crisis - liquidity vacuum possible |

**Historical PUMP Index Values:**
- Normal trading: 1.008-1.020
- Meme cycle peak: 1.040-1.060
- Crash events: 1.100+ (brief spikes)

---

## PUMP-Specific Thresholds

### Leverage Spread Thresholds (Binance/Bybit Primary)

PUMP has extreme volatility, requiring very wide thresholds.

| Spread | Classification | PUMP Signal |
|--------|----------------|-------------|
| > 0.20% | EXTREME_BULLISH | Longs extremely crowded - cascade imminent |
| 0.10% to 0.20% | HIGH_BULLISH | Very elevated long bias |
| 0.04% to 0.10% | MODERATE_BULLISH | Elevated bullish positioning |
| -0.04% to 0.04% | NEUTRAL | Balanced market |
| -0.10% to -0.04% | MODERATE_BEARISH | Elevated bearish positioning |
| -0.20% to -0.10% | HIGH_BEARISH | Very elevated short bias |
| < -0.20% | EXTREME_BEARISH | Shorts extremely crowded |

### Hyperliquid Premium (Perp-Only)

Since PUMP has no HL spot, HL data represents perp price vs CEX average.

| HL Premium | Classification | Interpretation |
|------------|----------------|----------------|
| > 0.15% | HL_PERP_PREMIUM | HL perp above CEX - DeFi FOMO |
| -0.15% to 0.15% | HL_ALIGNED | HL perp tracking CEX |
| < -0.15% | HL_PERP_DISCOUNT | HL perp below CEX - DeFi bearish |

---

## Funding Rate Anchor (PUMP-Specific)

### The 0.01% Anchor with Meme-Coin Adjustment

PUMP funding rates have faster mean reversion and extreme deviations:

| PUMP Funding Rate | Signal | Context |
|-------------------|--------|---------|
| > 0.15% | EXTREME_BULLISH | Retail FOMO - cascade imminent |
| 0.06% to 0.15% | ELEVATED_BULLISH | Strong speculative demand |
| 0.01% to 0.06% | AT/ABOVE ANCHOR | Normal for meme tokens |
| 0.00% to 0.01% | MILD_BEARISH | Caution |
| < 0.00% | EXTREME_BEARISH | Capitulation |

### PUMP Funding Volatility Half-Life

**PUMP Half-Life:** 1-2 days (fastest among all assets)

Meme token funding spikes decay rapidly, creating fast mean-reversion opportunities.

---

## Dynamic Z-Score Thresholds (PUMP)

### Rolling Z-Score Application

For PUMP, use 14-day rolling window (shorter due to faster cycles):

| Z-Score (14d) | Signal | Action |
|---------------|--------|--------|
| > 1.2 | Extreme bullish | High conviction contrarian short setup |
| 0.6 to 1.2 | Strong bullish | Take profits on longs |
| 0.2 to 0.6 | Mild bullish | Normal long bias |
| -0.2 to 0.2 | Neutral | No directional bias |
| -0.6 to -0.2 | Mild bearish | Normal short bias |
| -1.2 to -0.6 | Strong bearish | Cover shorts gradually |
| < -1.2 | Extreme bearish | High conviction contrarian long setup |

**Note:** PUMP thresholds are ~50% tighter than BTC due to extreme volatility.

### Multi-Factor Signal Application (PUMP)

**PUMP uses 3.0x threshold multiplier** (meme token calibration - widest).

| OI Change | Funding | Price | PUMP Interpretation |
|-----------|---------|-------|---------------------|
| Rising | > 0.09% (3x BTC) | Rising | Meme cycle acceleration - caution |
| Rising | > 0.15% | Rising | **EXTREME OVERHEATED** - imminent cascade |
| Rising | Negative | Rising | Short squeeze - can be violent (50%+ moves) |
| Falling | Negative | Falling | Meme cycle capitulation |
| Falling | Stabilizing | Flat | Dead cat or real bottom - check social |

**Threshold Calibration Table (PUMP):**
| BTC Baseline | PUMP Threshold | Calculation |
|--------------|----------------|-------------|
| Extreme leverage: 0.05% | 0.15% | 0.05% × 3.0 |
| Elevated leverage: 0.03% | 0.09% | 0.03% × 3.0 |
| Extreme funding: 0.05% | 0.15% | 0.05% × 3.0 |
| Crisis Arb Index: 1.015 | 1.045 | (1.015 - 1) × 3.0 + 1 |

**Critical:** These thresholds appear wide but are necessary for meme token volatility. A 0.15% funding rate on PUMP is equivalent in significance to 0.05% on BTC.

### Market Efficiency Context (PUMP)

**PUMP-Specific Efficiency Notes:**
- 11% annual efficiency improvement applies LESS to meme tokens
- Social sentiment dominates price discovery
- DEX often leads CEX for meme tokens (retail originated)
- Efficiency can completely break down during hype cycles

**PUMP Arbitrage Dynamics:**
| Market State | Typical Spread | Arbitrage Window |
|--------------|---------------|------------------|
| Normal | 0.3-1.0% | Minutes to hours |
| Hype cycle | 1-5% | May persist hours |
| Panic/crash | 5-20% | Can persist until stabilization |
| Air pocket | >20% | No convergence (liquidity vacuum) |

**Research Application:**
- Academic efficiency improvements (Crépellière et al.) apply minimally
- Treat PUMP as "efficiency-resistant" asset
- Social sentiment signals may outweigh premium signals

---

## Meme Token Premium Dynamics

PUMP premiums behave differently from major tokens due to meme token characteristics.

### Key Differences

| Factor | PUMP vs Majors |
|--------|----------------|
| Volatility | 3-5x higher than BTC/ETH |
| Spread Duration | Signals mean-revert faster (hours vs days) |
| Retail Dominance | Higher retail participation |
| News Sensitivity | Reacts to social media trends |
| Liquidity | Lower, wider bid-ask spreads |
| Air Pocket Risk | Significant |

### Premium Interpretation Adjustments

- Use wider thresholds (shown above)
- Expect faster mean reversion (1-2 day half-life)
- Combine with social sentiment if available
- Reduce position sizes due to volatility
- Monitor order book depth continuously

---

## Stablecoin De-peg Correlation

Meme tokens like PUMP are highly sensitive to stablecoin health:

### De-peg Impact on PUMP

| Stablecoin | De-peg Threshold | PUMP Impact |
|------------|-----------------|-------------|
| USDT | > 0.5% | Moderate selling pressure |
| USDC | > 0.3% | Significant selling |
| USDe | > 1.0% | **Cascade risk** (Oct 11 reference) |
| DAI | > 0.5% | Moderate concern |

**Oct 11, 2025 Reference:**
- USDe de-pegged to $0.65 on Binance
- Meme tokens collapsed faster than majors
- Collateral liquidations created selling cascade

### Stablecoin Monitoring Protocol

```
IF any major stablecoin de-peg > 1%:
  → Immediately reduce PUMP exposure
  → Switch to Depth-Weighted Price
  → Monitor for cascade liquidations
```

---

## Crisis Scenario Patterns

### PUMP as "Canary in the Coal Mine"

Meme tokens often signal systemic stress before majors:

**Early Warning Signs:**
1. PUMP Arbitrage Index rising while BTC stable
2. PUMP leverage extreme while BTC leverage moderate
3. PUMP funding rates spiking disproportionately
4. PUMP order book depth declining

**Signal Interpretation:**
```
IF PUMP shows stress signals AND BTC stable:
  → Retail leverage building in risky assets
  → May precede broader market correction
  → Consider reducing overall portfolio risk
```

### Cross-Venue Divergence During Panic

During Oct 11, 2025, some altcoins showed >20% spreads between exchanges:

**PUMP Crisis Protocol:**
- If Arbitrage Index > 1.10, switch to isolated venue logic
- Each exchange treated as closed system
- Don't assume convergence (may not happen quickly)
- Use limit orders only (no market orders)

---

## PUMP Scenario Templates

### PUMP_RETAIL_FOMO

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| Binance Leverage | > 0.15% |
| Bybit Leverage | > 0.15% |
| Duration | > 1 hour |
| Z-Score (14d) | > 0.8 |

**Signal:** Extreme retail FOMO. Very high probability of liquidation cascade. Avoid longs or consider short.

### PUMP_SQUEEZE_SETUP

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| All Leverage Spreads | < -0.15% |
| Duration | > 30 minutes |
| Price | Near support |
| Funding | Negative |

**Signal:** Shorts crowded. Potential squeeze opportunity on support reclaim.

### PUMP_NEUTRAL_POSITIONING

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| All Leverage Spreads | Within ±0.04% |
| Duration | > 2 hours |

**Signal:** Rare neutral state. Market waiting for catalyst. Watch for breakout direction.

### PUMP_LIQUIDITY_WARNING

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| Arbitrage Index | > 1.06 |
| Order Book Depth | Declining |
| Bid-Ask Spread | Widening |

**Signal:** Liquidity deteriorating. Reduce position immediately or hedge.

### PUMP_STABLECOIN_CORRELATED_RISK

| Condition | PUMP-Specific Check |
|-----------|---------------------|
| Any Stablecoin | De-peg > 0.5% |
| PUMP Leverage | Any |

**Signal:** Systemic risk elevated. Reduce PUMP exposure regardless of premium signals.

---

## Risk Considerations

### Higher Risk Profile

| Risk Factor | PUMP Impact |
|-------------|-------------|
| Liquidity Risk | Very High - thin order books |
| Volatility Risk | Extreme - 10%+ daily moves common |
| Data Quality | Lowest confidence of all assets |
| Squeeze Risk | Elevated due to crowded positioning |
| Air Pocket Risk | Significant - can flash crash |
| Stablecoin Risk | High correlation to collateral health |

### Position Sizing Recommendations

- Use **25-50% of normal position size**
- Wider stops required (2-3x normal)
- Don't hold through extreme leverage readings
- Quick profit-taking on spikes
- Always monitor order book depth
- Consider reducing before known catalyst events

---

## Historical Premium Patterns

### Meme Cycle Phases

| Phase | Premium Behavior | Duration |
|-------|------------------|----------|
| Accumulation | Neutral to mild positive | Days-weeks |
| FOMO Rally | Extreme positive (> 0.15%) | Hours-days |
| Distribution | High positive with divergence | Hours |
| Capitulation | Extreme negative (< -0.15%) | Hours |

### Pattern Recognition

- PUMP cycles are faster than major tokens (days vs weeks)
- Peak leverage often precedes top by **2-6 hours**
- Capitulation leverage extreme marks bottom within **1-2 hours**
- Recovery can be violent (V-shaped) or prolonged

---

## Integration with Other Signals

### Premium + Order Book Depth

| Premium | Depth Status | Combined Signal |
|---------|-------------|-----------------|
| Positive | Deep book | Sustainable rally possible |
| Positive | Thin book | Fragile - reduce size |
| Negative | Deep book | Accumulation opportunity |
| Negative | Thin book | **Exit immediately** |

### Premium + Stablecoin Health

| Premium | Stablecoin Status | Combined Signal |
|---------|------------------|-----------------|
| Any | All pegged | Normal analysis applies |
| Any | Any de-peg > 0.5% | Reduce exposure regardless |
| Any | USDe de-peg > 1% | **Exit PUMP positions** |

---

## Data Quality Notes

PUMP premium data has significant limitations:

- **No Coinbase** - US vs Asia unavailable
- **No HL spot** - Perp-only on Hyperliquid
- Limited to Binance/Bybit leverage sentiment
- High volatility reduces signal reliability
- Lower liquidity increases noise
- Air pocket risk requires depth monitoring

**Confidence penalty: 30%** (most limited data coverage, highest volatility)

### Recommended Usage

- Use PUMP premium signals as **supplementary only**
- Combine with other indicators (funding, OI, social)
- Apply wider error margins to all thresholds
- Focus on extreme readings (> ±0.15%) only
- Always monitor order book depth
- Have exit plan before entering positions

### PUMP-Specific Data Checks

- Spreads > 1.5% indicate data issue (normal conditions)
- Spreads > 3% during crisis = potentially valid (verify depth)
- Arbitrage Index > 1.10 → use Depth-Weighted Price
- Last Price discontinuities > 3% → check for air pockets
- HL data less reliable due to perp-only market
