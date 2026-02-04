---
name: HYPE Base Agent
version: 3.0
asset: HYPE
type: base
last_updated: 2025-01-27
sources:
  - Hyperliquid documentation & whitepaper
  - Hyperliquid Stats Dashboard
  - ASXN Analytics
  - DefiLlama
---

# HYPE Analysis Framework

## Asset Narrative

**Hyperliquid (HYPE)**: The dominant perpetual DEX with ~60%+ DEX perp market share, unique fee-to-buyback model, and expanding ecosystem via HIP-3.

HYPE is the native token of Hyperliquid, a decentralized perpetual futures exchange with:
- **Market Dominance**: #1 DEX by perps trading volume, ~60%+ DEX market share
- **Unique Economics**: ~97-99% of fees flow to Assistance Fund for HYPE buybacks
- **Platform Growth**: Expanding from perps into spot, HIP-3 permissionless markets
- **Product Innovation**: CEX-like orderbook UX on proprietary L1 (HyperBFT)
- **Founder**: Jeff Yan (ex-Citadel, Harvard Math)
- **TGE**: November 2024

### The Economic Flywheel

The investment thesis relies on a self-reinforcing loop that creates **double-compounding value accrual**:

```
┌─────────────────────────────────────────────────────────────┐
│  1. Hyperion/Partners STAKE HYPE to launch markets (HIP-3)  │
│                          ↓                                   │
│  2. Clients TRADE on new markets (Felix, Unit, etc.)        │
│                          ↓                                   │
│  3. FEES generated from trading activity                    │
│                          ↓                                   │
│  4. Fees used to BUYBACK and BURN HYPE                      │
│                          ↓                                   │
│  5. SUPPLY DECREASES while Staking Demand INCREASES         │
│                          ↓                                   │
│  6. PRICE APPRECIATION attracts more builders/liquidity     │
│                          ↓                                   │
│  └──────────────────────────→ (back to step 1)              │
└─────────────────────────────────────────────────────────────┘
```

**Key Insight**: Unlike traditional exchanges where volume growth dilutes existing holders (more shares issued for acquisitions, employee comp), HYPE's model compounds value:

| Traditional Exchange | HYPE Model |
|---------------------|------------|
| More volume → More revenue | More volume → More revenue |
| Revenue → Dividends + Buybacks (20-50%) | Revenue → Buybacks (97-99%) |
| Growth funded by dilution | Growth funded by fee retention |
| Supply increases over time | Supply decreases over time |

**The Compounding Math**:
- More volume → More fees → More burns → **Higher price**
- Higher price → More staking demand → **Less float**
- Less float + Higher demand → **Accelerated price appreciation**

This flywheel is **anti-fragile**: market volatility (which increases trading volume) actually strengthens the mechanism.

---

## L1 Architecture & Technical Stack

### Why "Purpose-Built" Matters

Unlike **general-purpose blockchains** (Ethereum, Solana, Arbitrum) that must handle diverse workloads (DeFi, NFTs, gaming, social), Hyperliquid is a **single-purpose L1** built exclusively for one thing: **high-frequency trading**.

| Chain Type | Examples | Optimization | Trade-off |
|------------|----------|--------------|-----------|
| General-Purpose | Ethereum, Solana | Flexibility | Bloated, slower |
| App-Specific | Hyperliquid, dYdX v4 | Speed for one use case | Limited functionality |

**The Hyperliquid Advantage**: Every design decision optimizes for orderbook trading:
- No smart contract execution bloat on the critical path
- Consensus tuned for order throughput, not general compute
- State model designed for position/margin tracking
- Native orderbook at the protocol level (not a dApp)

### The Three-Layer Stack

```
┌─────────────────────────────────────────────────┐
│                   HyperEVM                       │
│    (EVM-compatible smart contracts, DeFi)       │
├─────────────────────────────────────────────────┤
│                   HyperCore                      │
│    (Native orderbook, matching engine)          │
├─────────────────────────────────────────────────┤
│                   HyperBFT                       │
│    (Consensus layer, validator network)         │
└─────────────────────────────────────────────────┘
```

#### 1. HyperBFT (Consensus Layer)

**What it is**: Modified Tendermint/HotStuff BFT consensus optimized for trading workloads.

| Specification | Value | Comparison |
|---------------|-------|------------|
| Block Time | ~200ms | Ethereum: 12s, Solana: 400ms |
| Finality | Single-slot (~200ms) | Ethereum: ~15min probabilistic |
| Validator Set | 21 active | Tendermint-style dPoS |
| Throughput Target | 200,000 orders/second | NASDAQ: ~1M orders/sec |

**Key Innovation**: Unlike general BFT that batches diverse transactions, HyperBFT is tuned specifically for order flow:
- Order placement/cancellation are first-class citizens
- Optimized state transitions for position updates
- Parallelized order matching within blocks

#### 2. HyperCore (Trading Engine)

**What it is**: The native perpetual futures trading engine built directly into the L1 (not a smart contract).

| Feature | Description |
|---------|-------------|
| Orderbook | Fully on-chain limit orderbook (not AMM) |
| Matching | Price-time priority matching (like CEX) |
| Margin | Cross-margin and isolated margin |
| Liquidations | Protocol-level liquidation engine |
| Oracle | Proprietary price feeds + fallbacks |

**Why Native Matters**:
- No EVM gas overhead for trades
- Deterministic execution (no MEV extraction on orders)
- Matching engine runs at consensus speed, not smart contract speed

#### 3. HyperEVM (Smart Contract Layer)

**What it is**: EVM-compatible execution environment for DeFi applications that interact with HyperCore.

| Feature | Description |
|---------|-------------|
| Compatibility | Full EVM equivalence |
| Use Cases | Vaults, structured products, integrations |
| Separation | Runs parallel to HyperCore, not blocking it |

**Design Philosophy**: Keep the trading engine (HyperCore) fast by offloading complex logic to HyperEVM. Trading itself doesn't touch EVM.

### Performance Benchmarks

| Metric | Hyperliquid | Binance (CEX) | dYdX v4 | Solana DEXs |
|--------|-------------|---------------|---------|-------------|
| Order Throughput | 200K/sec (target) | 1M+/sec | 10K/sec | Variable |
| Latency (order→confirm) | ~200ms | ~10ms | ~1-2s | ~400ms |
| Finality | Instant | Centralized | Instant | Probabilistic |
| Custody | Self-custody | Exchange-held | Self-custody | Self-custody |

**Key Insight**: Hyperliquid is ~10-20x slower than Binance on raw latency, but:
1. Self-custody (you hold your funds)
2. No counterparty risk
3. Transparent execution (no front-running by exchange)
4. Fast enough for 99% of traders (HFT excluded)

---

## Perpetual Futures: Why They Dominate Crypto

### Perps vs Traditional Futures

| Feature | Perpetual Futures | Traditional Futures |
|---------|-------------------|---------------------|
| Expiry | Never expires | Monthly/quarterly expiry |
| Settlement | Continuous (funding) | At expiry |
| Roll Cost | None | Must roll positions |
| Capital Efficiency | Higher | Lower (roll management) |
| Price Tracking | Funding rate mechanism | Basis convergence |

### Why Perps Are the "Winning Product"

1. **No Expiry Management**: Traditional futures require rolling positions before expiry. Perps eliminate this operational burden.

2. **Capital Efficiency**: No need to manage multiple expiry contracts. One position, one margin requirement.

3. **Funding Rate Mechanism**: Instead of expiry settlement, perps use periodic funding payments:
   - When perp price > spot: Longs pay shorts (incentivizes selling)
   - When perp price < spot: Shorts pay longs (incentivizes buying)
   - This keeps perp price anchored to spot

4. **Simpler Mental Model**: Traders think in terms of one price, not a term structure.

### Market Structure Implication

| Market | 24h Volume (approx) | Primary Product |
|--------|---------------------|-----------------|
| Crypto Derivatives | $100-200B | ~90% Perps |
| Traditional Futures | $5T+ | Dated expiries |

**Crypto chose perps** because:
- 24/7 markets (no daily settlement)
- Retail-dominated (simpler product)
- High leverage demand (perps allow 50-125x)
- No physical delivery complexity

---

## Organic Volume vs "Point Tourists"

### The Points Farming Problem

Many DEX protocols bootstrap volume through **points programs**:
1. Trade volume → earn points
2. Points → expected airdrop allocation
3. Result: Artificial volume inflation

**"Point Tourists"** are users who:
- Farm volume purely for airdrop rewards
- Provide no long-term value
- Leave immediately after TGE (Token Generation Event)
- Often use wash trading (self-trades)

### How to Detect Inflated Volume

| Metric | Organic Volume | Points-Farmed Volume |
|--------|----------------|----------------------|
| Vol/OI Ratio | 5-15x daily | 25-100x+ daily |
| User Retention | Stable post-TGE | Cliff after airdrop |
| Trade Sizes | Varied, realistic | Round numbers, pattern |
| Time Distribution | 24/7 activity | Spikes around snapshots |

**Vol/OI Ratio Explained**:
- **Volume**: Total $ traded in a day
- **Open Interest (OI)**: Total $ of outstanding positions
- **Ratio**: How many times the average position "turns over"

| Vol/OI Ratio | Interpretation |
|--------------|----------------|
| 5-10x | Very organic, position-focused |
| 10-15x | Normal active trading |
| 15-25x | Elevated speculation |
| 25-50x | Likely incentivized |
| 50x+ | Almost certainly wash trading |

### Why Hyperliquid's Volume is "Stickier"

1. **Post-TGE Proof**: Volume remained high AFTER the airdrop (November 2024), unlike competitors where volume cratered.

2. **No Ongoing Points**: Hyperliquid discontinued points farming after TGE. Current volume is organic utility.

3. **Product Quality**: Users stay because of:
   - Best liquidity (tightest spreads)
   - Fastest execution
   - Most pairs available
   - Familiar CEX-like UX

4. **Network Effects**: Liquidity begets liquidity. Market makers concentrate where volume is.

### Competitor Volume Quality Comparison

| Protocol | Backing | Vol/OI (approx) | Assessment |
|----------|---------|-----------------|------------|
| Hyperliquid | Organic | 8-12x | Highly organic |
| dYdX | VCs | 10-20x | Mixed |
| GMX | Organic | 5-8x | Very organic |
| Aster | Binance/CZ | 30-50x+ | Points-inflated |
| Lighter | a16z | 40-60x+ | Points-inflated |

**Key Insight**: When Aster/Lighter TGEs happen, expect their volume to collapse as point tourists exit. This is a potential catalyst for Hyperliquid market share gains.

---

## Self-Custody & The FTX Lesson

### The CEX Counterparty Risk Problem

When you deposit funds to a centralized exchange (CEX):

```
Your Funds → CEX Wallet → CEX Controls Everything
                ↓
        You have an IOU, not actual crypto
```

**What can go wrong**:
1. **Insolvency**: Exchange loses funds (FTX, Mt. Gox)
2. **Fraud**: Exchange misappropriates funds (FTX)
3. **Hacks**: Hot wallet compromised (many examples)
4. **Regulatory Seizure**: Funds frozen by authorities
5. **Withdrawal Restrictions**: "Temporary" pauses during stress

### The FTX Catastrophe (November 2022)

| What Happened | Impact |
|---------------|--------|
| Customer deposits used for proprietary trading | $8B+ shortfall |
| Commingled funds with Alameda Research | Complete loss of segregation |
| Fake accounting | Hid insolvency for months |
| Withdrawal halt | Users couldn't exit |
| **Result** | ~$10B customer losses |

**The Lesson**: "Not your keys, not your crypto" isn't just a slogan—it's risk management.

### How DEX Self-Custody Works

On Hyperliquid (and other DEXs):

```
Your Funds → Your Wallet → Smart Contract (Escrow)
                              ↓
                    You retain private key control
                    Protocol can't unilaterally move funds
                    Withdrawal is permissionless
```

| Aspect | CEX (Binance, Coinbase) | DEX (Hyperliquid) |
|--------|-------------------------|-------------------|
| Custody | Exchange holds funds | You hold funds |
| Withdrawal | Permission required | Permissionless |
| Counterparty Risk | Exchange solvency | Smart contract risk |
| Transparency | Trust their books | On-chain verifiable |
| Regulatory Risk | Can be frozen | Harder to freeze |

### Why This Drives CEX→DEX Migration

Post-FTX, sophisticated traders learned:
1. **Don't trust centralized entities with large sums**
2. **Prefer verifiable, on-chain custody**
3. **Accept slightly worse execution for safety**

**The Trade-off**:
- CEX: Faster, cheaper, but counterparty risk
- DEX: Slightly slower, but self-custody

As DEX UX improves (Hyperliquid leading here), the trade-off becomes less painful, accelerating migration.

### Hyperliquid's Security Model

| Layer | Protection |
|-------|------------|
| Consensus | 21 validators (BFT majority required) |
| Funds | User-controlled wallets on L1 |
| Margin | Smart contract escrow (audited) |
| Liquidations | Protocol-level (no human intervention) |
| Insurance | HLP (Hyperliquidity Provider) vault |

**Remaining Risks**:
- Smart contract bugs (mitigated by audits)
- Oracle manipulation (JELLY incident lesson)
- Validator collusion (21 validators = centralization risk)
- Bridge risk (if funds bridged from other chains)

---

## Primary Metrics

| Metric | Description | Why It Matters |
|--------|-------------|----------------|
| **Daily Volume** | Platform trading volume | Primary revenue driver |
| **Fee Revenue** | Trading fees generated | Protocol income |
| **AF Balance** | Assistance Fund USDC | Buyback capacity |
| **Daily Buybacks** | HYPE purchased by AF | Supply reduction |
| **Cumulative Buybacks** | Total HYPE bought back | Deflation metric |
| **FDV/Revenue** | Valuation multiple | Relative value vs peers |
| **MC/Revenue** | Market cap multiple | Current holder value |
| **FCF Yield** | Fees / FDV | Cash flow return |
| **Vol/OI Ratio** | Volume vs Open Interest | Trading quality indicator |
| **Active Users** | Daily unique traders | Platform adoption |

---

## Tokenomics & Supply

### Token Distribution

| Category | Allocation | Notes |
|----------|------------|-------|
| Genesis (Community) | 31% | Airdrop recipients |
| Core Contributors | 23.8% | Team + early contributors |
| Foundation | 10.6% | Hyperliquid Foundation |
| Community Rewards | 38.888% | Future distribution |
| **Max Supply** | 1B HYPE | Hard cap |
| **Circulating** | ~333M | ~33% of max |

### Vesting Schedule

- **Core Contributors**: 1-year cliff, then linear over 2 years
- **Unlock Start**: November 2025
- **Impact**: Watch for selling pressure at unlock milestones

### Supply Dynamics

- Buybacks permanently remove HYPE from circulation (burned/sidelined)
- AF-purchased HYPE is NOT held as reserves - it's removed from supply
- Staking locks supply

---

## Assistance Fund (AF) - The Deflationary Engine

### CRITICAL: AF vs Insurance Fund

**The Assistance Fund is NOT an insurance fund.** It does not backstop bad debt or cover liquidations.

| Fund | Purpose | Holds |
|------|---------|-------|
| **Assistance Fund (AF)** | Fee sink → Buyback & Burn | HYPE (burned/sidelined) |
| **HLP Vault** | Market making + Liquidation backstop | USDC |
| **Insurance Fund** | Bad debt coverage | USDC |

The AF is purely a **value-accrual mechanism** that converts fees to HYPE and removes them from circulation.

### How It Works

```
Trading Fees (USDC)
        ↓
   ~99% to AF (no 10/90 split exists)
        ↓
  Continuous HYPE Buybacks
        ↓
  HYPE Burned/Sidelined
        ↓
  Permanent Supply Reduction
```

1. Trading fees collected in USDC
2. ~99% of net protocol fees flow to Assistance Fund (excluding referral/builder fees)
3. AF automatically buys HYPE on the open market
4. **Purchased HYPE is burned/sidelined** (permanently removed from circulation)
5. The AF does NOT hold HYPE as "reserves" to pay claims - it's a deflationary burn mechanism

### Key Metrics

| Metric | What to Track |
|--------|---------------|
| AF Balance (USDC) | Buyback capacity |
| Daily Buyback ($) | Current activity |
| Cumulative Buybacks | Total removed from circulation |
| Buyback/Volume Ratio | Efficiency metric |
| % of Supply Repurchased | Deflation rate |

### "Shareholder Yield on Steroids"

Traditional stock buybacks:
- Companies allocate 20-50% of free cash flow
- Executed quarterly, opportunistically
- Disclosed after the fact

HYPE buybacks:
- ~97-99% of ALL revenue → buybacks
- Continuous, algorithmic execution
- Real-time on-chain transparency

| Metric | HYPE AF | Apple Buybacks | S&P 500 Avg |
|--------|---------|----------------|-------------|
| % of Revenue | ~97-99% | ~25% | ~15-20% |
| Frequency | Continuous | Quarterly | Quarterly |
| Transparency | Real-time | Quarterly filing | Quarterly filing |

### Supply Impact Modeling

If Hyperliquid generates $1B annual fees:
- ~$970M-$990M → HYPE buybacks
- At $25 HYPE price → ~40M HYPE/year purchased
- ~4% of total supply annually removed from circulation

**10-Year Scenario** (illustrative):

| Year | Annual Fees | Buyback $ | HYPE Price | HYPE Bought | Cumulative % |
|------|-------------|-----------|------------|-------------|--------------|
| 1 | $1B | $970M | $25 | 39M | 3.9% |
| 3 | $2B | $1.9B | $50 | 38M | 10% |
| 5 | $3B | $2.9B | $75 | 39M | 18% |
| 10 | $5B | $4.9B | $150 | 33M | 35% |

*Assumes price appreciation and declining marginal buyback impact*

---

## Valuation Model

### Primary Multiples

| Multiple | Formula | Interpretation |
|----------|---------|----------------|
| FDV/Revenue | FDV / Annualized Fees | Lower = cheaper |
| MC/Revenue | Market Cap / Annualized Fees | Current value |
| FCF Yield | Annualized Fees / FDV | Higher = better |

### Valuation Thresholds

| FDV/Revenue | Classification | Context |
|-------------|----------------|---------|
| < 30x | Deep value | Strong buy signal |
| 30-50x | Undervalued | Accumulate |
| 50-100x | Fair value | Hold |
| 100-200x | Fully valued | Take profits |
| > 200x | Overvalued | Caution |

### Bull Case: 1% Global Market Share

**Assumptions**:
- Global crypto derivatives: ~$200B daily → $73T annual
- 1% market share: $730B annual volume
- Take rate: 3.5 bps (0.035%)
- Annual fees: ~$2.5B

| Scenario | Market Share | Annual Volume | Annual Fees | FDV @ 50x |
|----------|--------------|---------------|-------------|-----------|
| Current | ~0.5% | ~$180B | ~$600M | $30B |
| Base | 1% | $730B | $2.5B | $125B |
| Bull | 2% | $1.5T | $5B | $250B |
| Mega Bull | 5% | $3.6T | $12.5B | $625B |

---

## Competition & Market Position

### DEX Competitors

| Protocol | Backing | Volume | Vol/OI | Notes |
|----------|---------|--------|--------|-------|
| **HYPE** | Organic | #1 | ~8-12x | Market leader |
| Aster | Binance/CZ | Growing | 30-50x+ | Points farming |
| Lighter | a16z | Moderate | 40-60x+ | VC backed |
| edgeX | - | Low | - | Speed focus |
| dYdX | VCs | #2-3 | 10-20x | V4 transition |
| GMX | Organic | #2-3 | 5-8x | Real yield |

### CEX Market Context

- Total crypto perp volume: ~$100-150B daily
- Binance: ~50% market share
- HYPE: ~1-3% of total (but ~60% of DEX)
- Growth opportunity: DEX share of total perps

### Competitive Moats

1. **Liquidity**: Best prices on DEX perps
2. **UX**: CEX-like experience
3. **Speed**: Sub-second finality
4. **Trust**: Post-TGE organic volume
5. **Ecosystem**: HIP-3 expansion
6. **Network Effects**: Liquidity attracts liquidity

---

## HIP-3 & New Products

### What is HIP-3?

HIP-3 (Hyperliquid Improvement Proposal 3) enables **permissionless perpetual market creation**:

- Anyone can deploy new perp markets on Hyperliquid
- Deployers stake HYPE (10,000 minimum)
- Revenue share between deployer and protocol
- Opens door to synthetic stocks, commodities, etc.

### Synthetic Stock Perps

HIP-3 enables trading of **stock perpetuals**:
- AAPL-PERP, TSLA-PERP, etc.
- 24/7 trading (unlike stock markets)
- No need to own underlying
- Settled in USDC

**Why This Matters**:
- Expands TAM beyond crypto traders
- Attracts equity traders to the platform
- New revenue stream

### Key Metrics

| Metric | Description |
|--------|-------------|
| HIP-3 Volume | Trading on HIP-3 markets |
| HIP-3 % of Total | Market share vs HL perps |
| Unique Deployers | Number of market creators |
| Top Assets | Highest volume HIP-3 markets |

---

## Staking & Validators

### Staking Mechanics

| Aspect | Details |
|--------|---------|
| Staking Token | HYPE |
| Reward Source | Inflation + portion of fees |
| Unbonding | 7-day period |
| Max Validators | 21 active |

### Centralization Trade-off

| Aspect | 21 Validators | 1000+ Validators |
|--------|---------------|------------------|
| Speed | Faster consensus | Slower consensus |
| Decentralization | Lower | Higher |
| Coordination | Easier | Harder |
| Attack Cost | Lower threshold | Higher threshold |

**Hyperliquid's Choice**: Prioritize speed for trading UX, accept centralization risk.

**Roadmap**: Plans to expand validator set over time as technology improves.

---

## Risk Factors

### Protocol Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Validator Centralization | Medium | Expansion roadmap |
| Smart Contract Risk | Medium | Audits, insurance fund |
| Oracle Manipulation | Medium | Multi-source oracles, circuit breakers |
| JELLY-type Incidents | Low | Improved risk parameters |

### Regulatory Risks

| Risk | Severity | Notes |
|------|----------|-------|
| No-KYC Model | High | Limits institutional adoption |
| Derivatives Classification | Medium | Offshore structure |
| US Access | High | Geo-blocking in place |

### Competitive Risks

| Risk | Severity | Trigger |
|------|----------|---------|
| Aster/Lighter Growth | Medium | If volume stays post-TGE |
| CEX Feature Parity | Low | Already competitive |
| Market Share Loss | Medium | < 50% DEX share |

### JELLY Incident (March 2024)

**What Happened**:
- Attacker attempted market manipulation on JELLY token
- Exploited HLP (liquidity provider) positions
- Forced protocol intervention

**Response**:
- Emergency measures to contain damage
- Improved oracle and risk controls
- Added circuit breakers for illiquid markets

**Lesson**: Even decentralized protocols need risk management for edge cases.

---

## Investment Vehicles (Public Markets)

### HYPD (Hyperion DeFi) - "The Operator"

| Metric | Details |
|--------|---------|
| Structure | Public company (OTC: HYPD) |
| Primary Asset | HYPE tokens |
| Strategy | Active yield generation |

**Revenue Streams**:
1. **Staking Rewards**: Staking HYPE holdings for yield
2. **Validator Operation**: Running Hyperliquid validator node
3. **HIP-3 Partnership (Felix)**: Deploying and earning from HIP-3 markets
4. **Market Making**: Potential LP activities

**Why Premium to NAV**: Active operations generate yield above passive holding.

### PURR (Hyperliquid Strategies) - "The Allocator"

| Metric | Details |
|--------|---------|
| Structure | Public company (OTC: PURR) |
| Primary Asset | HYPE tokens + Cash |
| Strategy | Treasury management |

**Balance Sheet**:
- Large HYPE holdings
- Significant cash position (dry powder)
- Passive holding strategy

**Why Discount to NAV**:
- No active yield generation
- Management overhead
- Illiquidity discount
- **Closing the Gap**: Share buybacks when trading at discount

### Comparison

| Metric | HYPD | PURR |
|--------|------|------|
| Strategy | Active operations | Passive treasury |
| Risk Profile | Higher (operational risk) | Lower (pure exposure) |
| Yield Generation | Yes (validator, HIP-3) | No (buyback only) |
| NAV Premium/Discount | Premium (1.1-1.2x) | Discount (0.7-0.8x) |
| Best For | Growth + yield seekers | Pure HYPE exposure |

---

## Key Thresholds

### Volume Signals

| Metric | Bullish | Neutral | Bearish |
|--------|---------|---------|---------|
| Volume Growth MoM | > 20% | 0-20% | Declining |
| Market Share (DEX) | > 60% | 50-60% | < 50% |
| Vol/OI Ratio | 5-15x | 15-25x | > 25x |

### Valuation Signals

| Metric | Bullish | Neutral | Bearish |
|--------|---------|---------|---------|
| FDV/Revenue | < 50x | 50-100x | > 100x |
| FCF Yield | > 2% | 1-2% | < 1% |
| MC/Revenue | < 30x | 30-50x | > 50x |

### Platform Health

| Metric | Healthy | Caution | Warning |
|--------|---------|---------|---------|
| Daily Users | Growing | Flat | Declining |
| Net Inflows | Positive | Neutral | Negative |
| AF Buyback Rate | Consistent | Slowing | Stopped |

---

## Required Frameworks

1. **PROTOCOL_ECONOMICS_FRAMEWORK** - Revenue, fees, buyback analysis
2. **DERIVATIVES_MICROSTRUCTURE_FRAMEWORK** - Trading dynamics, OI, funding
3. **SMART_MONEY_FRAMEWORK** - Whale behavior on Hyperliquid
4. **TOKEN_ECONOMICS_FRAMEWORK** - Supply, vesting, dilution analysis
5. **VALUATION_FRAMEWORK** - Multiples, scenario analysis, peer comparison

---

## Analysis Checklist

Before generating HYPE analysis, ensure you have:

### Platform Metrics
- [ ] Daily/monthly trading volume
- [ ] Open interest (total and by asset)
- [ ] Daily active users
- [ ] Net inflows/outflows
- [ ] Vol/OI ratio (organic score)

### Revenue & Buybacks
- [ ] Monthly fee revenue
- [ ] AF balance (USDC)
- [ ] Daily/cumulative buybacks
- [ ] Annualized revenue
- [ ] % of supply repurchased

### Valuation
- [ ] Current price, MC, FDV
- [ ] FDV/Revenue multiple
- [ ] MC/Revenue multiple
- [ ] FCF yield

### Competition
- [ ] DEX market share
- [ ] Competitor volumes
- [ ] Vol/OI comparisons (organic score)
- [ ] Points program status of competitors

### Supply
- [ ] Circulating supply
- [ ] Staking rate
- [ ] Upcoming unlocks
- [ ] AF HYPE holdings
