---
name: HYPE Research Overlay
version: 2.0
asset: HYPE
type: research_overlay
domain: research
last_updated: 2025-01-27
sources:
  - hype/base.md
  - hype_investment domain skill
  - Claude Equity Research framework
---

# HYPE Research Focus

## Primary Narrative: Fee-to-Buyback Protocol Economics

Hyperliquid represents a new model for protocol value accrual:
- **~97-99% of fees** flow directly to token buybacks (vs traditional dividends)
- **Market-leading DEX** with ~60%+ of DEX perp volume
- **Expanding ecosystem** via HIP-3 permissionless markets
- **Unique valuation model** - quasi-equity with perpetual buyback

### Key Investment Thesis Points

1. **Revenue Quality**: Real trading fees, not incentivized volume
2. **Capital Return**: Nearly all fees returned to holders via buybacks
3. **Growth Vector**: HIP-3 ecosystem expansion, CEX market share gains
4. **Valuation Support**: FDV/Revenue multiple vs traditional exchange peers

---

## Section-Specific Guidance

### Executive Summary Emphasis

Lead with:
1. **Trading volume** (daily, monthly, growth rate)
2. **Fee revenue** and annualized run rate
3. **Buyback metrics** (AF balance, daily rate, cumulative)
4. **Valuation multiples** (FDV/Revenue, FCF Yield)
5. **Market position** (DEX share, competitor comparison)

### Valuation Priority Metrics

**Tier 1 (Must Include):**

| Metric | Formula | Bullish | Neutral | Bearish |
|--------|---------|---------|---------|---------|
| FDV/Revenue | FDV / Ann. Fees | < 50x | 50-100x | > 150x |
| MC/Revenue | MC / Ann. Fees | < 30x | 30-50x | > 75x |
| FCF Yield | Ann. Fees / FDV | > 2% | 1-2% | < 1% |
| Volume Growth MoM | (Vol_t / Vol_t-1) - 1 | > 20% | 0-20% | Declining |
| Market Share (DEX) | HL Vol / Total DEX Vol | > 60% | 50-60% | < 50% |

**Tier 2 (Context):**

| Metric | Description | Watch For |
|--------|-------------|-----------|
| Vol/OI Ratio | Volume / Open Interest | < 15x = organic |
| Daily Buybacks | HYPE purchased | Consistency |
| AF Balance | USDC in fund | Growing reserve |
| User Growth | DAU trend | Sustained adoption |
| HIP-3 Share | HIP-3 % of total | Ecosystem growth |

**HYPE-Specific Metrics:**
- Daily/monthly perp volume
- Daily/monthly spot volume
- Fee revenue by product (perps, spot, HIP-3)
- Assistance Fund balance and buyback rate
- Circulating supply and buyback impact

---

## Assistance Fund Analysis Framework

### CRITICAL: AF is NOT Insurance

**The Assistance Fund is a buyback-and-burn mechanism, NOT an insurance fund.**

| Fund | Purpose | What It Holds |
|------|---------|---------------|
| **Assistance Fund (AF)** | Buyback & Burn | HYPE (burned/sidelined) |
| **HLP Vault** | Liquidation backstop | USDC |
| **Insurance Fund** | Bad debt coverage | USDC |

### Understanding the AF Mechanism

The Assistance Fund is HYPE's primary value accrual mechanism:

```
Trading Fees (USDC) -> AF (~99%) -> HYPE Buybacks -> Burned/Sidelined -> Permanent Supply Reduction
```

**There is NO 10/90 split.** The AF IS the buyback mechanism. ~99% of net fees flow to AF.

### AF Analysis Checklist

| Metric | What to Report | Why It Matters |
|--------|----------------|----------------|
| HYPE Balance | HYPE burned/sidelined in AF | Supply removed |
| Daily Buyback | HYPE purchased & burned | Deflation rate |
| Buyback/Fee Ratio | Buyback $ / Fee $ | Efficiency |
| Cumulative Total | All-time HYPE burned | Total deflation |

### Comparison Framework

| Metric | HYPE AF | Stock Buybacks | Dividends |
|--------|---------|----------------|-----------|
| % of Revenue | ~99% | 20-50% | 20-40% |
| Frequency | Continuous | Quarterly | Quarterly |
| Tax Efficiency | Capital gains | Capital gains | Income |
| Transparency | Real-time | Quarterly | Announced |
| Flexibility | Algorithmic | Board decision | Board decision |
| **Insurance Role** | **NONE** | N/A | N/A |

---

## Platform Metrics Analysis

### Volume Analysis

| Timeframe | What to Report | Benchmark |
|-----------|----------------|-----------|
| 24h Volume | Current activity | Compare to 7d avg |
| 7d Volume | Short-term trend | MoM change |
| 30d Volume | Medium-term trend | vs competitors |
| Perp/Spot Split | Product mix | Perps dominate |

### Market Share Tracking

| Comparison | Calculation | Target |
|------------|-------------|--------|
| DEX Perp Share | HL / (HL + dYdX + GMX + Others) | > 60% |
| Total Perp Share | HL / (All CEX + DEX Perps) | > 2% |
| Growth Trajectory | MoM share change | Increasing |

### Trading Quality Indicators

| Metric | Healthy Range | Red Flag |
|--------|---------------|----------|
| Vol/OI Ratio | 5-15x | > 25x (wash trading) |
| Organic Score | > 70% | < 50% |
| Spread Quality | < 0.05% | > 0.1% |

---

## HIP-3 Ecosystem Analysis

### What to Track

| Metric | Description | Growth Signal |
|--------|-------------|---------------|
| HIP-3 Volume | Trading on HIP-3 markets | > 10% of total |
| Deployer Count | Unique market creators | Growing |
| Top Markets | Highest volume assets | Diversifying |
| Fee Share | HIP-3 contribution to fees | Increasing |

### HIP-3 Bull Case

- Permissionless innovation drives new markets
- Revenue share attracts deployers
- Network effects compound
- New asset classes (stocks, commodities)

---

## HIP-3 Business Line Audit ("Exchange of Exchanges")

HYPE is transitioning from "Perp DEX" to infrastructure for *other* exchanges (Felix, Unit, Ventuals). This represents a fundamental shift in business model and warrants separate valuation treatment.

### The "Exchange of Exchanges" Model

Traditional DEX: `Users → Platform → Fees`

HIP-3 Model: `Users → Partner Exchanges → Platform → Shared Fees`

| Layer | Example | Value Capture |
|-------|---------|---------------|
| Infrastructure | Hyperliquid L1 | Base layer fees + security |
| Partner Exchanges | Felix, Unit, Ventuals | 50% of fees (deployer share) |
| End Users | Traders | Trading experience |

### Revenue Model

| Mechanism | Description | Impact |
|-----------|-------------|--------|
| **Deployer Stakes** | 500k HYPE staked to launch a market | Reduces Float |
| **Fee Split** | Deployers ~50% / Protocol ~50% | Direct buyback flow |
| **Growth Mode** | >90% fee reduction to bootstrap liquidity | Strategic user acquisition |

### Fee Economics Deep Dive

```
HIP-3 Partner Volume ($100M example)
        ↓
    Gross Fees (~3.5 bps = $35,000)
        ↓
    ┌─────────────────────────────────┐
    │  Deployer Share: ~50% ($17,500)  │  → Partner retention
    │  Protocol Share: ~50% ($17,500)  │  → AF → Buyback/Burn
    └─────────────────────────────────┘
```

**Growth Mode Exception**: During bootstrapping, deployers may receive >90% of fees to attract liquidity. This is a strategic investment in network growth.

### Valuation Impact

Every successful HIP-3 partner creates **two value streams**:

1. **Direct Burn**: 50% of partner volume fees flow to HYPE buyback/burn
2. **Supply Lock**: 500k HYPE removed from float per major partner

### Supply Lock Math

| Partners | HYPE Staked | % of Float Locked |
|----------|-------------|-------------------|
| 10 | 5M HYPE | ~1.5% |
| 50 | 25M HYPE | ~7.5% |
| 100 | 50M HYPE | ~15% |
| 200 | 100M HYPE | ~30% |

*Assumes ~333M circulating float*

### Key Metric: HIP-3 Volume Share

| HIP-3 % of Total Volume | Valuation Implication |
|-------------------------|----------------------|
| < 10% | "Feature" - minor ecosystem add-on |
| 10-20% | "Product Line" - material revenue contributor |
| > 20% | "Platform" - re-rate from DEX Token to Financial Infrastructure Layer |

### Platform Re-Rating Thesis

If HIP-3 exceeds 20% of total volume, HYPE should be compared to:

| Comp | Model | Multiple |
|------|-------|----------|
| NYSE/ICE | Exchange infrastructure | 15-20x Revenue |
| CME | Derivatives infrastructure | 20-25x Revenue |
| Coinbase | Crypto exchange | 10-15x Revenue |
| **HYPE (current)** | DEX token | 50-80x Revenue |
| **HYPE (platform)** | Infrastructure layer | 80-120x Revenue |

### HIP-3 Partner Tracking

| Partner | Status | Stake | Volume | Notes |
|---------|--------|-------|--------|-------|
| Felix | Active | 500k HYPE | Track | HYPD partnership |
| Unit | Active | 500k HYPE | Track | Emerging |
| Ventuals | Active | 500k HYPE | Track | Emerging |
| Others | Various | Track | Track | Monitor deployer count |

### Analysis Questions

When analyzing HIP-3:
1. What % of total Hyperliquid volume comes from HIP-3 partners?
2. How many HYPE are locked in deployer stakes?
3. Are partners in "Growth Mode" or full fee-share?
4. What's the trend in new partner deployments?

---

## Competition Analysis Framework

### DEX Competitor Comparison

| Protocol | Volume | Vol/OI | Backing | Threat Level |
|----------|--------|--------|---------|--------------|
| Aster | Watch | High | Binance/CZ | Medium |
| Lighter | Watch | High | a16z | Medium |
| edgeX | Low | - | - | Low |
| dYdX | Moderate | Variable | VCs | Medium |
| GMX | Moderate | Low | Organic | Low |

### Volume Quality Assessment

**Organic Volume Indicators:**
- Consistent vol/OI ratio over time
- Diverse user base (many small traders)
- Stable post-TGE (no points farming)

**Wash Trading Indicators:**
- Vol/OI > 20-25x
- Volume spikes correlated with incentive events
- Few accounts driving majority of volume

### CEX Comparison

| Metric | HYPE | Binance | Bybit | Coinbase |
|--------|------|---------|-------|----------|
| Volume | ~$3-5B/day | ~$50B/day | ~$10B/day | ~$2B/day |
| Take Rate | 3.5bps | 5bps | 5.5bps | Higher |
| Fee to Holders | ~99% | Variable | Variable | Dividends |
| Regulation | No KYC | Mixed | Mixed | Full |

---

## Valuation Model Framework

### Base Valuation Model

```
Fair Value = Annual Fees * Multiple

Where Multiple depends on:
- Growth rate
- Market position
- Risk factors
```

### Scenario Analysis Template

| Scenario | Annual Fees | Multiple | Implied FDV | Price @ 1B Supply |
|----------|-------------|----------|-------------|-------------------|
| Bear | $500M | 40x | $20B | $20 |
| Base | $1B | 60x | $60B | $60 |
| Bull | $2B | 80x | $160B | $160 |
| Aggressive Bull | $5B | 100x | $500B | $500 |

### Key Assumptions by Scenario

**Bear Case:**
- Volume stagnates or declines
- Market share loss to competitors
- Regulatory pressure
- Higher unlocks create selling pressure

**Base Case:**
- 20% volume growth annually
- Maintain 60% DEX share
- Gradual CEX share gains
- Buybacks offset unlocks

**Bull Case:**
- 50%+ volume growth
- HIP-3 becomes significant
- CEX share reaches 5%+
- Institutional adoption

---

## Catalyst Analysis

### Near-Term Catalysts (0-3 months)

| Catalyst | Impact | Likelihood | Timing |
|----------|--------|------------|--------|
| Volume milestone | Medium | High | Ongoing |
| New HIP-3 markets | Medium | High | Monthly |
| CEX listings | High | Medium | TBD |
| Partnership announcements | Medium | Medium | TBD |

### Medium-Term Catalysts (3-12 months)

| Catalyst | Impact | Likelihood | Timing |
|----------|--------|------------|--------|
| Token unlocks | Negative | High | Nov 2025+ |
| Validator expansion | Medium | High | TBD |
| USDH launch | High | Medium | TBD |
| Institutional products | High | Medium | TBD |

### Long-Term Catalysts (1+ years)

| Catalyst | Impact | Likelihood |
|----------|--------|------------|
| Regulatory clarity | High | Medium |
| CEX 10% share | Very High | Low |
| HIP-3 ecosystem dominance | High | Medium |

---

## Risk Assessment Framework

### Risk Categories

**Regulatory Risk (High):**
- No-KYC model limits institutional adoption
- Derivatives exchange classification uncertain
- US access restrictions

**Competition Risk (Medium):**
- Aster (Binance-backed) growing
- Lighter (a16z-backed) emerging
- CEX feature improvements

**Technical Risk (Medium):**
- 21 validator centralization
- Smart contract vulnerabilities
- Oracle manipulation (JELLY incident)

**Token Risk (Medium):**
- Core contributor unlocks (Nov 2025)
- Potential selling pressure
- Circulating supply increase

### Risk Quantification

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Regulatory crackdown | 20% | High | Geographic diversification |
| Competitor volume theft | 30% | Medium | Product innovation |
| Technical exploit | 10% | High | Audits, insurance fund |
| Unlock selling | 60% | Medium | Buyback absorption |

### Invalidation Levels

| Metric | Exit Trigger | Recovery Signal |
|--------|--------------|-----------------|
| Volume | -30% MoM sustained | +20% rebound |
| Market Share | < 40% DEX | > 50% recovery |
| FDV/Revenue | > 250x | < 150x |
| AF Activity | Stopped | Resumed |

---

## Investment Vehicles Analysis

### HYPD (Hyperion DeFi)

**What It Is:**
- Public company holding HYPE tokens
- Active yield strategy (staking, validator, HIP-3)
- OTC traded

**Analysis Framework:**

| Metric | How to Calculate | Interpretation |
|--------|------------------|----------------|
| mNAV | (HYPE Holdings * Price + Cash) / Shares | Fair value |
| Premium/Discount | (Stock Price - mNAV) / mNAV | Relative value |
| Yield Sources | Staking APR + Validator + HIP-3 | Income potential |

### PURR (Hyperliquid Strategies)

**What It Is:**
- Public company holding HYPE + cash
- Passive treasury strategy
- OTC traded

**Analysis Framework:**

| Metric | How to Calculate | Interpretation |
|--------|------------------|----------------|
| mNAV | (HYPE Holdings * Price + Cash) / Shares | Fair value |
| Premium/Discount | (Stock Price - mNAV) / mNAV | Relative value |
| Cash % | Cash / mNAV | Safety buffer |

### Comparison

| Factor | HYPD | PURR | Direct HYPE |
|--------|------|------|-------------|
| Liquidity | Low (OTC) | Low (OTC) | High (DEX/CEX) |
| Yield | Active | Passive | Buyback only |
| Premium/Discount | Variable | Variable | N/A |
| Tax Treatment | Equity | Equity | Crypto |

---

## Comparable Assets Table

| Asset | Comparison Basis | Key Metric | HYPE Advantage |
|-------|------------------|------------|----------------|
| dYdX | DEX perps | FDV/Rev | Better tokenomics |
| GMX | DEX perps | Yield | Higher growth |
| SNX | Derivatives | Revenue | Simpler model |
| COIN | Exchange | P/E | Higher growth |
| UNI | DEX (spot) | Volume | Derivatives exposure |

---

## Required Data Points Checklist

Before generating HYPE research report, ensure you have:

### Platform Metrics
- [ ] Daily perp volume
- [ ] Daily spot volume
- [ ] Open interest (total)
- [ ] Daily active users
- [ ] Net inflows/outflows

### Revenue & Buybacks
- [ ] Monthly fee revenue
- [ ] Annualized revenue
- [ ] AF balance (USDC)
- [ ] Daily buyback amount
- [ ] Cumulative buybacks

### Valuation
- [ ] Current HYPE price
- [ ] Market cap (circulating)
- [ ] Fully diluted valuation
- [ ] FDV/Revenue multiple
- [ ] MC/Revenue multiple
- [ ] FCF yield

### Competition
- [ ] DEX perp market share
- [ ] dYdX volume
- [ ] GMX volume
- [ ] Aster/Lighter volume (if available)
- [ ] Vol/OI comparisons

### Supply & Tokens
- [ ] Circulating supply
- [ ] Staking rate
- [ ] Next unlock date
- [ ] Unlock amount

### HIP-3
- [ ] HIP-3 volume
- [ ] HIP-3 % of total
- [ ] Number of deployers
- [ ] Top HIP-3 markets

---

## Chart Requirements

### Must-Have Charts

| Chart | Purpose | Priority |
|-------|---------|----------|
| hl_daily_volume_chart | Volume trend | High |
| hl_monthly_revenue_chart | Revenue trend | High |
| hl_af_balance_chart | Buyback capacity | High |
| hl_fdv_multiple_chart | Valuation | High |
| hl_competitor_volume_chart | Market position | High |

### Supporting Charts

| Chart | Purpose | Priority |
|-------|---------|----------|
| hl_cumulative_buyback_chart | Total buybacks | Medium |
| hip3_volume_chart | Ecosystem growth | Medium |
| hl_vol_oi_platform_chart | Trading quality | Medium |
| hl_daily_users_chart | Adoption | Medium |
| price_chart | Price action | Medium |
