---
name: HYPE Valuation Sensitivity Model
version: 1.0
asset: HYPE
type: research_overlay
domain: valuation
requires: [base]
last_updated: 2025-01-28
source: Cantor "Path to $5bn" Framework
---

# HYPE Valuation Sensitivity Model

## The "Share Capture" Valuation Model

Traditional crypto token valuation applies a simple multiple to fees. HYPE requires a more sophisticated model because its supply dynamics are **inversely correlated with revenue growth**.

### Core Formula

```
Price Target = (Global_Vol * Market_Share * Take_Rate * Multiple) / Effective_Float
```

Where:
- **Global_Vol**: Total addressable derivatives market ($200B+ daily)
- **Market_Share**: HYPE's capture of global volume (currently ~1-2%)
- **Take_Rate**: Average fee per dollar traded (~3.5 bps)
- **Multiple**: Earnings/Revenue multiple (varies by growth scenario)
- **Effective_Float**: Adjusted circulating supply (see "Cantor Adjusted" Supply below)

### The Double-Compounding Effect

**Key Insight**: Unlike traditional assets where revenue growth is neutral to supply, HYPE's Future_Supply *decreases* as Revenue *increases*.

```
More Volume → More Fees → More Buybacks/Burns → Less Supply → Higher Price per Token
     ↓                                              ↑
     └──────────────────────────────────────────────┘
```

This creates **double-compounding**: Revenue grows the numerator while burns shrink the denominator.

---

## 10-Year Sensitivity Matrix (Cantor Framework)

### Market Share Scenarios

| Scenario | Global Share | DEX Share | Annual Volume | Est. Annual Fees |
|----------|--------------|-----------|---------------|------------------|
| **Current** | ~1% | ~60% | ~$400B | ~$1.4B |
| **Base (5%)** | 5% | 70% | ~$3.6T | ~$12.6B |
| **Growth (10%)** | 10% | 80% | ~$7.3T | ~$25.5B |
| **Blue Sky (17%)** | 17% | 90% | ~$12.4T | ~$43.4B |

*Assumes: Global derivatives market grows to $200B daily by 2030, take rate of 3.5 bps*

### Price Target Sensitivity Table

| Market Share | Annual Fees | Implied Burn Rate | 5-Year Supply | Price Target (50x) |
|--------------|-------------|-------------------|---------------|-------------------|
| 1% (Current) | $1.4B | ~56M HYPE/yr | ~720M | $97 |
| 5% (Base) | $12.6B | ~500M HYPE/yr | ~500M | $1,260 |
| 10% (Growth) | $25.5B | ~1B HYPE/yr | ~350M | $3,643 |
| 17% (Blue Sky) | $43.4B | ~1.7B HYPE/yr | ~200M | $10,850 |

*Price targets assume 50x multiple on fees / effective float. Burn rate calculated at $25 avg acquisition price.*

### Key Assumptions

1. **Take Rate Stability**: 3.5 bps maintained (competitive pressure could lower)
2. **Burn Execution**: AF continues 99% fee-to-burn policy
3. **No Major Unlocks**: Core contributor unlocks absorbed by buybacks
4. **Market Growth**: Crypto derivatives TAM expands with adoption

---

## Deflationary Velocity Check

Use this framework to validate whether current price reflects the "Deflationary Supercycle" thesis.

### Annualized Burn Rate Formula

```
Annualized_Burn_Rate = (Monthly_Buybacks * 12) / Circulating_Supply
```

### Burn Rate Interpretation Table

| Annualized Burn Rate | Interpretation | Price Implication |
|---------------------|----------------|-------------------|
| < 2% | Slow deflation | Price follows revenue multiples only |
| 2-5% | Moderate deflation | 10-20% premium to revenue multiple |
| 5-10% | Aggressive deflation | 30-50% premium justified |
| 10-15% | Hyperdeflationary | Scarcity premium kicks in |
| > 15% | Supercycle territory | Supply shock potential |

### Validation Check

**Question**: Is current price justified by burn rate alone?

```
If (Burn_Rate > 5%) AND (FDV/Rev < 100x):
    → Undervalued relative to deflationary mechanics

If (Burn_Rate < 3%) AND (FDV/Rev > 150x):
    → Overvalued - revenue growth must accelerate
```

---

## "Cantor Adjusted" Supply Definition

### Why CoinMarketCap Supply Is Wrong for HYPE

Standard supply metrics from aggregators don't capture HYPE's unique dynamics:

| Supply Metric | CoinMarketCap | Cantor Adjusted |
|---------------|---------------|-----------------|
| **What It Shows** | Raw token count | Actual tradeable float |
| **Includes Locked** | Yes | No |
| **Includes AF Holdings** | Yes | No |
| **Includes Burns** | Sometimes delayed | Real-time |

### Effective Float Calculation

```
Effective_Float = Minted_Supply
                  + Staking_Emissions
                  - Community_Grants (locked)
                  - Core_Contributor_Locked
                  - AF_Balance (HYPE)
                  - Cumulative_Burns
```

### Current Effective Float Estimate

| Component | Amount | Notes |
|-----------|--------|-------|
| Minted Supply | 1,000M | Max cap |
| Less: Unvested Team | (~238M) | Nov 2025 unlock starts |
| Less: Foundation Locked | (~106M) | Multi-year unlock |
| Less: AF HYPE Holdings | (~XXM) | Check current balance |
| Less: Cumulative Burns | (~XXM) | Check current total |
| Less: Staked & Locked | (~XXM) | Validator staking |
| **= Effective Float** | **~XXX M** | *Update with real-time data* |

### Why This Matters

Using raw 1B supply in valuation = **overestimating dilution by 40-60%**

Correct analysis uses Effective Float, which:
1. Excludes locked tokens that can't sell
2. Excludes AF holdings (permanently sidelined)
3. Accounts for actual tradeable supply

---

## Applying the Model: Worked Example

### Step 1: Gather Current Metrics

| Metric | Value | Source |
|--------|-------|--------|
| Daily Volume | $X.XB | Hyperliquid Stats |
| Monthly Fees | $XXM | On-chain |
| AF HYPE Balance | XXM | Contract |
| Cumulative Burns | XXM | Analytics |
| Current Price | $XX | Market |

### Step 2: Calculate Effective Float

```
Effective_Float = 1,000M - 238M - 106M - AF_HYPE - Burns - Staked
```

### Step 3: Run Sensitivity Scenarios

| Scenario | Market Share | Annual Fees | Multiple | Target FDV | Target Price |
|----------|--------------|-------------|----------|------------|--------------|
| Bear | 0.5% | $700M | 40x | $28B | $XX |
| Base | 2% | $2.8B | 60x | $168B | $XXX |
| Bull | 5% | $7B | 80x | $560B | $XXX |

### Step 4: Validate with Burn Rate

```
If Annual_Burn > 5% of Float:
    → Scarcity premium applies
    → Use higher end of multiple range
```

---

## Model Limitations

### What This Model Captures

- Market share expansion scenarios
- Deflationary supply mechanics
- Double-compounding effect

### What This Model Does NOT Capture

1. **Regulatory risk** - Could force KYC, limiting growth
2. **Competition response** - Binance/VC-backed DEXs fighting back
3. **Technical risk** - Smart contract exploits, oracle attacks
4. **Correlation risk** - Crypto bear market compresses all valuations
5. **Liquidity risk** - Large sells can't be absorbed at target prices

### Model Confidence Levels

| Scenario | Confidence | Key Assumption Risk |
|----------|------------|---------------------|
| Current (1%) | High | Volume stability |
| Base (5%) | Medium | DEX adoption curve |
| Growth (10%) | Low | CEX share capture |
| Blue Sky (17%) | Very Low | Market transformation |

---

## Integration with Research

When generating HYPE research reports, use this sensitivity model to:

1. **Frame price targets** in terms of market share scenarios
2. **Validate current valuation** against burn rate expectations
3. **Calculate Effective Float** rather than raw supply
4. **Project 5-10 year scenarios** for long-term positioning

### Key Questions the Model Answers

- "What market share does the current price imply?"
- "Is the burn rate sufficient to justify a scarcity premium?"
- "What's the price target if HYPE captures 5% of global derivatives?"
- "How does Effective Float change the valuation math?"
