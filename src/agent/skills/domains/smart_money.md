---
name: Smart Money Tracking Framework
version: 1
type: domain
domain: smart_money
applicable_assets: [ALL]
last_updated: 2025-01-16
sources:
  - Hyperliquid API (top traders, positions, fills)
  - On-chain wallet tracking
---

# Smart Money Tracking Framework

## Overview

This framework provides methodology for analyzing "smart money" activity - the trading behavior of top performers, whales, and institutional players. Smart money tracking focuses on Hyperliquid's top traders, identified through their leaderboard performance and profit history.

## Data Sources

### Hyperliquid Leaderboard
- **hl_traders**: Master list of tracked traders with display names and notes
- **hl_trader_snapshots**: Daily snapshots of trader performance metrics
- **hl_trader_positions**: Current open positions by trader
- **hl_trader_fills**: Recent trades/fills by tracked traders

### Key Metrics Tracked
- Total PnL (all-time profit/loss)
- Daily/Weekly/Monthly PnL changes
- Open positions and direction
- Position sizing and leverage
- Entry/exit timing patterns

## Trader Classification

### By Performance Tier

| Tier | PnL Range | Characteristics |
|------|-----------|-----------------|
| Elite | >$10M | Consistently profitable, large size |
| Top Tier | $1M-$10M | Strong track record, meaningful signals |
| Rising | $100K-$1M | Emerging performers, watch for consistency |
| Tracked | <$100K | On watchlist, validating performance |

### By Trading Style

| Style | Indicators | Signal Value |
|-------|------------|--------------|
| Trend Follower | Large directional bets, holds through volatility | High for trend confirmation |
| Scalper | High frequency, small positions | Low (noise) |
| Swing Trader | Multi-day holds, size around key levels | High for level identification |
| Contrarian | Buys dips, sells rips, often early | Moderate (requires context) |

## Positioning Analysis

### Aggregate Smart Money Positioning

**Calculating Net Positioning:**
```
Net Position = Sum(Long USD) - Sum(Short USD)
Whale Bias = Net Position > 0 ? "LONG" : "SHORT"
Conviction = |Net Position| / Total Exposure
```

### Positioning Signals

| Positioning State | Signal | Confidence |
|-------------------|--------|------------|
| 70%+ net long | Strong bullish bias | High |
| 55-70% net long | Moderate bullish lean | Medium |
| 45-55% | Neutral/mixed | Low |
| 30-45% net long | Moderate bearish lean | Medium |
| <30% net long | Strong bearish bias | High |

### Position Changes (Most Important)

| Change Type | Timeframe | Significance |
|-------------|-----------|--------------|
| Rapid accumulation | 24h | Potential catalyst expected |
| Gradual accumulation | 7d | Trend formation |
| Position reduction | 24h | Profit-taking or risk-off |
| Position flip | Any | Major sentiment shift |

## Activity Patterns

### Recent Fills Analysis

**Key Metrics:**
- Net buy/sell volume (24h)
- Average fill size
- Number of traders active
- Time clustering of fills

### Activity Signals

| Pattern | Interpretation |
|---------|----------------|
| Large clustered buys | Coordinated accumulation |
| Large clustered sells | Coordinated distribution |
| High frequency small fills | Market making / noise |
| Single large fill | Whale conviction trade |
| Activity spike on dip | Dip buying = bullish |
| Activity spike on rally | Profit-taking = caution |

### Volume Concentration

| Concentration | Trading Implication |
|---------------|---------------------|
| >50% from top 3 traders | High conviction signal |
| Evenly distributed | Consensus forming |
| Single trader dominating | Whale manipulation risk |

## Trading Signals

### Bullish Smart Money Signals

1. **Strong Accumulation**
   - Net long positioning increasing
   - Multiple traders adding longs simultaneously
   - Accumulation during price weakness

2. **Whale Conviction**
   - Top performer initiating large long
   - Multiple elite traders aligned long
   - Position size above trader's average

3. **Dip Buying**
   - Smart money fills clustered on price drops
   - Increasing long exposure during pullbacks
   - Declining sell pressure from tracked traders

### Bearish Smart Money Signals

1. **Distribution Pattern**
   - Net positioning shifting short
   - Profit-taking after extended rally
   - Elite traders reducing exposure

2. **Whale Exit**
   - Top performers closing longs
   - Multiple tracked traders flipping short
   - Large single-trader exits

3. **Rally Selling**
   - Smart money fills clustered on price rallies
   - Increasing short exposure at highs
   - Declining buy pressure from tracked traders

### Caution Signals

1. **Mixed Positioning**
   - Equal long/short among smart money
   - Rapid position changes both directions
   - Low conviction sizing

2. **Divergence**
   - Smart money vs price divergence
   - Elite vs non-elite positioning difference
   - Single trader vs group divergence

## Cross-Reference Framework

### Smart Money + Other Indicators

| Combination | Signal Strength |
|-------------|-----------------|
| SM long + Negative funding | Very Strong Bullish |
| SM long + Positive funding | Moderate Bullish |
| SM short + Positive funding | Very Strong Bearish |
| SM short + Negative funding | Moderate Bearish |
| SM long + CVD bearish | Conflicting (SM leading?) |
| SM accumulating + ETF inflows | Strong Bullish |

### Confirmation Hierarchy

1. **Highest Value**: Smart money aligns with funding rate signal
2. **High Value**: Smart money aligns with CVD trend
3. **Moderate Value**: Smart money alone (no confirmation)
4. **Low Value**: Smart money contradicts other indicators

## Risk Considerations

### Limitations

1. **Survivorship Bias**: Leaderboard shows winners, losers removed
2. **Style Drift**: Past performance doesn't guarantee future
3. **Lag**: Position data may be delayed vs market
4. **Gaming**: Some traders may manipulate their public positions

### Position Size Guidelines

| Smart Money Signal Strength | Suggested Position Size |
|-----------------------------|------------------------|
| Strong consensus (>70%) | Full size |
| Moderate alignment (55-70%) | 50-75% size |
| Mixed signals | Reduced size or wait |
| Contradicting other signals | Small size or avoid |

### Timing Considerations

- Smart money data updates: Near real-time (fills) to hourly (positions)
- Best used for: Directional bias, not precise entries
- Combine with: Technical levels for entry timing
- Avoid: Chasing fills after large moves already occurred

## Interpretation Examples

### Example 1: Bullish Setup
```
Leaderboard: Top 10 traders +$500M total PnL
Positioning: 65% net long on BTC
Activity: $5M in buys vs $1M in sells (24h)
Context: Price at key support, funding neutral

Interpretation: Strong bullish bias from smart money.
Consider long positions with tight stops below support.
```

### Example 2: Bearish Setup
```
Leaderboard: Elite traders reducing BTC exposure
Positioning: Flipped from 60% long to 45% long in 48h
Activity: Large sells on price rallies
Context: Price at resistance, funding elevated

Interpretation: Smart money distributing.
Caution on longs, consider shorts on resistance rejection.
```

### Example 3: Neutral/Unclear
```
Leaderboard: Mixed performance among top traders
Positioning: 50/50 split
Activity: Low volume, no clear pattern
Context: Range-bound price action

Interpretation: No clear smart money signal.
Wait for positioning clarity before taking directional bets.
```

## Data Quality Notes

- **Reliability**: Hyperliquid data is highly reliable (on-chain verified)
- **Completeness**: Only tracks Hyperliquid traders (not all venues)
- **Timeliness**: Fills near real-time, positioning updates hourly
- **Coverage**: Primarily perpetual futures, not spot
