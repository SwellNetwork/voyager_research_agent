---
name: HYPE Investment Analysis Domain
version: 2.0
type: domain
domain: hype_investment
last_updated: 2025-01-27
sources:
  - Hyperliquid documentation & whitepaper
  - Hyperliquid Stats Dashboard
  - ASXN Analytics
  - DefiLlama
---

# HYPE Investment Analysis Framework

This domain skill provides comprehensive guidance for answering investment analysis questions about Hyperliquid (HYPE). Use this when users ask about HYPE fundamentals, tokenomics, valuation, platform metrics, or investment thesis.

---

## I. CORE INFRASTRUCTURE (L1 & THROUGHPUT)

### Questions in this category:
- "What is the specific single-use purpose Hyperliquid was built for?"
- "What are the order throughput metrics (orders per second)?"
- "How does the Performant L1 architecture achieve CEX-like feel without lag?"
- "How does Hyperliquid differentiate its volume from competitors?"
- "What are Point Tourists versus organic volume?"

### L1 Differentiation: Purpose-Built vs General-Purpose

Unlike **general-purpose blockchains** (Ethereum, Solana, Arbitrum) that handle diverse workloads, Hyperliquid is a **single-purpose L1** built exclusively for **high-frequency orderbook trading**.

| Chain Type | Examples | Optimization | Trade-off |
|------------|----------|--------------|-----------|
| General-Purpose | Ethereum, Solana | Flexibility, diverse apps | Slower, bloated state |
| App-Specific | Hyperliquid, dYdX v4 | Max speed for one use case | Limited functionality |

**Why This Matters for Valuation**: Every CPU cycle, every state transition, every consensus round is optimized for one thing: processing orders. No smart contract bloat, no NFT mints, no memecoin launches competing for blockspace.

### Performance Specifications

| Metric | Hyperliquid | NASDAQ | Binance (CEX) | dYdX v4 |
|--------|-------------|--------|---------------|---------|
| Order Throughput | 200K orders/sec | 1M+ orders/sec | 1M+ orders/sec | ~10K orders/sec |
| Latency (order→confirm) | ~200ms | <1ms | ~10ms | 1-2s |
| Finality | Instant (1 block) | Centralized | Centralized | Instant |
| Custody | Self-custody | Broker-held | Exchange-held | Self-custody |

**Key Insight**: Hyperliquid is ~10-20x slower than Binance on raw latency, BUT:
1. Fast enough for 99% of traders (only HFT excluded)
2. Self-custody eliminates counterparty risk
3. Transparent execution (no front-running by exchange)
4. On-chain verifiability

### The Three-Layer Tech Stack

```
┌─────────────────────────────────────────────────┐
│                   HyperEVM                       │
│    (EVM-compatible smart contracts, DeFi)       │
│    - Vaults, structured products, integrations  │
│    - Runs PARALLEL to trading, not blocking it  │
├─────────────────────────────────────────────────┤
│                   HyperCore                      │
│    (Native orderbook, matching engine)          │
│    - Fully on-chain limit orderbook (not AMM)   │
│    - Price-time priority matching (like CEX)    │
│    - NO EVM gas overhead for trades             │
├─────────────────────────────────────────────────┤
│                   HyperBFT                       │
│    (Consensus layer, validator network)         │
│    - Modified Tendermint/HotStuff BFT           │
│    - ~200ms block time                          │
│    - 21 validators (speed vs decentralization)  │
└─────────────────────────────────────────────────┘
```

### Latency vs Decentralization Trade-off

| Design Choice | Benefit | Cost |
|---------------|---------|------|
| 21 validators | Fast BFT consensus | Centralization risk |
| 200ms blocks | Near-instant trading | Not as fast as CEX |
| Native orderbook | No EVM overhead | Less flexibility |
| No general compute | Trading optimized | Can't run arbitrary dApps |

**Hyperliquid's Bet**: Most traders will accept slightly worse latency for self-custody and transparency. The 200ms latency is imperceptible to humans and only excludes HFT strategies.

### "Point Tourists" vs Organic Volume

**The Problem**: Many DEX protocols bootstrap volume through **points programs**:
1. Trade volume → earn points
2. Points → expected airdrop allocation
3. Result: Artificial, unsustainable volume inflation

**"Point Tourists"** are users who:
- Farm volume purely for airdrop rewards
- Provide zero long-term value
- Leave immediately after Token Generation Event (TGE)
- Often use wash trading (self-trades to inflate volume)

### How to Detect Inflated vs Organic Volume

| Metric | Organic Volume | Points-Farmed Volume |
|--------|----------------|----------------------|
| Vol/OI Ratio | 5-15x daily | 25-100x+ daily |
| User Retention | Stable post-TGE | Cliff after airdrop |
| Trade Sizes | Varied, realistic | Round numbers, patterns |
| Time Distribution | 24/7 natural | Spikes around snapshots |

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

1. **Post-TGE Proof**: Volume remained high AFTER the airdrop (Nov 2024). Unlike competitors whose volume cratered post-TGE.

2. **No Ongoing Points**: Hyperliquid discontinued points farming after TGE. Current volume is organic utility, not incentive farming.

3. **Product Superiority**: Users stay for:
   - Best liquidity (tightest spreads on DEX)
   - Fastest execution
   - Most trading pairs
   - Familiar CEX-like UX

4. **Network Effects**: Liquidity begets liquidity. Market makers concentrate where organic volume exists.

### Competitor Volume Quality Comparison

| Protocol | Backing | Vol/OI (approx) | Assessment |
|----------|---------|-----------------|------------|
| **Hyperliquid** | Organic | 8-12x | Highly organic |
| dYdX | VCs | 10-20x | Mixed quality |
| GMX | Organic | 5-8x | Very organic |
| Aster | Binance/CZ | 30-50x+ | Points-inflated |
| Lighter | a16z | 40-60x+ | Points-inflated |

**Investment Implication**: When Aster/Lighter TGEs occur, expect their volume to collapse as point tourists exit. This is a potential catalyst for Hyperliquid market share gains.

### Charts to Load:
- `hl_vol_oi_platform_chart` (organic score)
- `hl_competitor_volume_chart` (volume comparison)
- `hl_daily_volume_chart` (volume trends)

---

## II. MARKET STRUCTURE: WHY PERPS DOMINATE

### Questions in this category:
- "Why are Perps considered the winning product for crypto markets?"
- "How do perps affect capital efficiency compared to traditional monthly expiries?"
- "What is the difference between futures and perpetual futures?"

### Perpetual Futures vs Traditional Futures

| Feature | Perpetual Futures (Perps) | Traditional Futures |
|---------|---------------------------|---------------------|
| Expiry | **Never expires** | Monthly/quarterly |
| Settlement | Continuous (funding rate) | At expiry date |
| Roll Cost | **None** | Must roll positions |
| Capital Efficiency | **Higher** | Lower (roll management) |
| Price Tracking | Funding rate mechanism | Basis convergence |
| Mental Model | One price | Term structure |

### Why Perps Are the "Winning Product"

1. **No Expiry Management**: Traditional futures require rolling positions before expiry. Perps eliminate this operational burden entirely.

2. **Superior Capital Efficiency**:
   - No need to manage multiple expiry contracts
   - One position, one margin requirement
   - No calendar spread management

3. **Funding Rate Mechanism**: Instead of expiry settlement, perps use periodic funding payments:
   - When perp price > spot: Longs pay shorts (incentivizes selling)
   - When perp price < spot: Shorts pay longs (incentivizes buying)
   - This keeps perp price anchored to spot without expiry

4. **Simpler Mental Model**: Traders think in terms of one price, not a term structure of expiries.

### Crypto Market Structure

| Market | 24h Volume (approx) | Primary Product |
|--------|---------------------|-----------------|
| Crypto Derivatives | $100-200B | **~90% Perpetuals** |
| Traditional Futures | $5T+ | Dated expiries |

**Why Crypto Chose Perps**:
- 24/7 markets (no daily settlement complexity)
- Retail-dominated (simpler product wins)
- High leverage demand (perps allow 50-125x)
- No physical delivery complexity
- Funding rate = continuous price discovery

### Capital Efficiency Example

**Scenario**: Trader wants continuous long BTC exposure for 1 year

| Method | Capital Required | Management |
|--------|------------------|------------|
| Spot | 100% notional | Hold |
| Perp (10x leverage) | 10% notional | Monitor funding |
| Quarterly Futures | 10% notional | Roll 4x/year |

**Perp Advantage**: Same leverage as futures, but no roll management. Capital stays deployed efficiently.

---

## III. SELF-CUSTODY & THE FTX LESSON

### Questions in this category:
- "How does Hyperliquid's Self-Custody model mitigate FTX-type counterparty risks?"
- "How is this driving the shift from CEX to DEX?"
- "What are the remaining risks?"

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
3. **Hacks**: Hot wallet compromised
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
| Custody | Exchange holds funds | **You hold funds** |
| Withdrawal | Permission required | **Permissionless** |
| Counterparty Risk | Exchange solvency | Smart contract risk |
| Transparency | Trust their books | **On-chain verifiable** |
| Regulatory Risk | Can be frozen | Harder to freeze |

### Why This Drives CEX→DEX Migration

Post-FTX, sophisticated traders learned:
1. Don't trust centralized entities with large sums
2. Prefer verifiable, on-chain custody
3. Accept slightly worse execution for safety

**The Trade-off**:
- CEX: Faster (10ms), but counterparty risk
- DEX: Slower (200ms), but self-custody

As DEX UX improves (Hyperliquid leading), the trade-off becomes less painful, accelerating migration.

### Hyperliquid's Security Model

| Layer | Protection |
|-------|------------|
| Consensus | 21 validators (BFT majority required to attack) |
| Funds | User-controlled wallets on L1 |
| Margin | Smart contract escrow (audited) |
| Liquidations | Protocol-level, automated (no human intervention) |
| Insurance | HLP (Hyperliquidity Provider) vault |

### Remaining Risks (Honest Assessment)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Smart contract bugs | Medium | Audits, bug bounties |
| Oracle manipulation | Medium | Multi-source oracles, circuit breakers (JELLY lesson) |
| Validator collusion | Medium | 21 validators = coordination required |
| Bridge risk | Medium | If funds bridged from other chains |
| Regulatory | High | Geo-blocking, offshore structure |

---

## 1. FUNDAMENTAL UNDERSTANDING

### Questions in this category:
- "What is Hyperliquid and how does it work?"
- "What are perpetual futures (perps) and why are they popular in crypto?"
- "How is Hyperliquid different from a centralized exchange like Binance?"
- "What is the Hyperliquid tech stack (HyperCore, HyperEVM, HyperBFT)?"
- "Who founded Hyperliquid and what is their background?"

### Key Facts:
- **Hyperliquid**: Decentralized perpetual futures exchange running on proprietary L1
- **Architecture**: HyperBFT consensus (modified Tendermint), HyperCore execution, HyperEVM for smart contracts
- **UX**: CEX-like orderbook experience with DEX self-custody
- **Founder**: Jeff Yan (ex-Citadel quantitative trader, Harvard Math)
- **Launch**: TGE November 2024
- **Throughput**: 200,000 orders/second target, ~200ms finality

### Data Needed:
- Protocol overview (no specific charts)
- Price chart for price history since TGE

### Charts to Load:
- `price_chart` (for TGE reference)
- `hl_daily_volume_chart` (platform activity)

---

## 2. TOKENOMICS & SUPPLY

### Questions in this category:
- "What is the total and circulating supply of HYPE?"
- "How are HYPE tokens distributed (genesis, core contributors, foundation, etc.)?"
- "What is the token vesting schedule for core contributors?"
- "How does HYPE staking work and what are the rewards?"
- "How many HYPE tokens have been burned or repurchased to date?"
- "What percentage of max supply has been bought back/burned YTD?"
- "How does the token unlock schedule affect circulating supply?"

### Key Facts:
| Metric | Value |
|--------|-------|
| Max Supply | 1,000,000,000 HYPE |
| Circulating (approx) | ~333M (33.3%) |
| Genesis Distribution | 31% to community |
| Core Contributors | 23.8% (vesting) |
| Foundation | 10.6% |
| Community Rewards | 38.888% |
| Buyback Source | Assistance Fund (AF) |

### Vesting Schedule:
- Core contributors: 1-year cliff, then linear over 2 years
- Unlocks begin November 2025

### Data Needed:
- Token distribution breakdown
- Circulating supply over time
- Buyback/burn history
- Staking APR

### Charts to Load:
- `hl_tokenomics_chart` (supply distribution pie chart)
- `hl_cumulative_buyback_chart` (buyback accumulation)
- `hl_daily_buyback_chart` (daily buyback rate)

### Tables to Query:
- Token supply data (derived from platform metrics)
- Buyback history

---

## 3. ASSISTANCE FUND (AF) - BUYBACK & BURN MECHANISM

### CRITICAL DISTINCTION: AF is NOT an Insurance Fund

**Common Hallucination to Avoid**: The AF does NOT backstop bad debt, cover liquidations, or act as insurance. Those functions are handled by the **HLP Vault** and **USDC Insurance Fund**.

| Fund | Purpose | What It Holds |
|------|---------|---------------|
| **Assistance Fund (AF)** | Buyback & Burn mechanism | HYPE (burned/sidelined) |
| **HLP Vault** | Market making + Liquidation backstop | USDC |
| **Insurance Fund** | Bad debt coverage | USDC |

**There is NO 10%/90% split.** The AF IS the buyback. ~99% of net fees flow to AF for buybacks.

### Questions in this category:
- "How does the Assistance Fund work?"
- "What percentage of protocol fees go to token buybacks?"
- "How much HYPE has the AF burned and what is its current balance?"
- "What is the daily/monthly average HYPE buyback rate?"
- "How does HYPE's buyback mechanism compare to traditional stock buybacks?"

### Key Facts:
| Metric | Description |
|--------|-------------|
| AF Fee Share | ~99% of net trading fees (excluding referral/builder fees) |
| AF Purpose | **Buyback & Burn ONLY** - NOT insurance |
| Buyback Frequency | Continuous, automatic, on-market purchases |
| Transparency | On-chain, fully auditable (address: 0xfefe...) |
| HYPE Destination | **Burned/Sidelined** (removed from circulation) |

### Buyback Mechanics (Correct):
1. Trading fees collected in USDC
2. ~99% of net fees flow to Assistance Fund (no split - AF IS the buyback)
3. AF automatically buys HYPE on the open market
4. **Purchased HYPE is burned/sidelined** (permanently removed from supply)
5. HYPE is NOT "held as reserves" - it's removed from circulation

### Comparison to Stock Buybacks:
| Aspect | HYPE AF | Traditional Buyback |
|--------|---------|---------------------|
| Frequency | Continuous, automatic | Quarterly/opportunistic |
| Transparency | Real-time on-chain | Disclosed quarterly |
| % of Revenue | ~99% | Typically 20-50% |
| Destination | **Burned/Sidelined** | Often cancelled shares |
| Insurance Function | **NONE** | N/A |

### Data Needed:
- AF HYPE balance over time (burned/sidelined tokens)
- Daily buyback amounts (HYPE and USD)
- Cumulative buybacks
- Total HYPE removed from circulation

### Charts to Load:
- `hl_af_balance_chart` (AF HYPE balance - burned tokens)
- `hl_daily_buyback_chart` (daily buybacks)
- `hl_cumulative_buyback_chart` (cumulative total)
- `hl_monthly_revenue_chart` (fee source)

### Tables to Query:
- AF balance snapshots
- Buyback transactions

---

## 4. TRADING VOLUME & MARKET METRICS

### Questions in this category:
- "What is HYPE's current monthly/yearly perp trading volume?"
- "How has perp volume grown over the past 12 months?"
- "What is HYPE's market share vs CEX perp volume?"
- "How does HYPE volume compare to competitors (Aster, Lighter, edgeX)?"
- "What is HYPE's spot trading volume?"
- "How does HYPE spot volume compare to other DEXs like Uniswap?"
- "What is the difference in take-rate between perps and spot?"
- "What is HYPE's current open interest?"
- "How does the volume-to-open-interest ratio compare to competitors?"
- "What does a high/low volume-to-OI ratio indicate about trading quality?"

### Key Metrics:
| Metric | What It Shows |
|--------|---------------|
| Daily Volume | Trading activity level |
| Monthly Volume | Revenue potential |
| OI | Outstanding positions / platform adoption |
| Vol/OI Ratio | Trading intensity, lower = more organic |
| Market Share | Competitive position |

### Volume/OI Interpretation:
| Vol/OI Ratio | Interpretation |
|--------------|----------------|
| < 5x | Very organic, position-focused trading |
| 5-10x | Healthy mix |
| 10-20x | Active trading, some wash |
| > 20x | Likely inflated by incentives |

### Data Needed:
- Daily/monthly perp volume
- Daily/monthly spot volume
- Platform open interest
- Competitor volumes (Aster, Lighter, dYdX, GMX)

### Charts to Load:
- `hl_daily_volume_chart` (daily volume)
- `hl_cumulative_volume_chart` (cumulative)
- `hl_competitor_volume_chart` (vs competitors)
- `hl_open_interest_chart` (OI by asset)
- `hl_vol_oi_platform_chart` (Vol/OI ratio)

### Tables to Query:
- Platform volume metrics
- Competitor volume data

---

## 5. FEES & REVENUE

### Questions in this category:
- "How much in fees has HYPE generated YTD/TTM?"
- "What is the average take-rate (in bps) for perps vs spot?"
- "How have monthly fees trended over the past year?"
- "What is the breakdown of fees by product (perps, spot, HLP)?"
- "How do HYPE's fees compare to CEX trading fees?"

### Fee Structure:
| Market Type | Maker Fee | Taker Fee |
|-------------|-----------|-----------|
| Perps | 0.01% | 0.035% |
| Spot | 0.01% | 0.025% |

### Revenue Model:
- ~97-99% of fees -> Assistance Fund -> Buybacks
- ~1-3% -> Operating expenses
- Take-rate varies by product and volume tier

### CEX Comparison:
| Exchange | Taker Fee (Perps) |
|----------|-------------------|
| Hyperliquid | 0.035% |
| Binance | 0.05% |
| Bybit | 0.055% |
| OKX | 0.05% |

### Data Needed:
- Monthly fee revenue
- Fee breakdown by product
- Historical fee trends
- Annualized revenue

### Charts to Load:
- `hl_monthly_revenue_chart` (monthly revenue breakdown)
- `hl_cumulative_revenue_chart` (cumulative fees)
- `hl_daily_volume_chart` (volume for fee calculation)

### Tables to Query:
- Revenue metrics
- Fee history

---

## 6. VALUATION

### Questions in this category:
- "What is HYPE's current market cap (circulating vs fully diluted)?"
- "What is HYPE trading at on a P/E or P/CF basis?"
- "How should investors think about valuing HYPE given ~99% of fees go to buybacks?"
- "What are the bull/bear case valuations for HYPE?"
- "What would HYPE be worth if it achieves $5bn in annual fees?"

### Key Valuation Metrics:
| Metric | Formula | Interpretation |
|--------|---------|----------------|
| FDV/Revenue | FDV / Annualized Fees | Lower = cheaper |
| MC/Revenue | Market Cap / Annualized Fees | Current holder value |
| FCF Yield | Annualized Fees / FDV | Higher = better |

### Valuation Framework:
| FDV/Revenue | Classification |
|-------------|----------------|
| < 30x | Deep value |
| 30-50x | Undervalued |
| 50-100x | Fair value |
| 100-200x | Fully valued |
| > 200x | Overvalued |

### Scenario Analysis Template:
| Scenario | Annual Fees | FDV/Rev | Implied FDV |
|----------|-------------|---------|-------------|
| Bear | $500M | 50x | $25B |
| Base | $1B | 75x | $75B |
| Bull | $2B | 100x | $200B |

### Data Needed:
- Current price, market cap, FDV
- Annualized fee revenue
- Revenue multiples over time

### Charts to Load:
- `hl_fdv_vs_revenue_chart` (FDV and revenue trends)
- `hl_fdv_multiple_chart` (FDV/Revenue ratio)
- `hl_mc_multiple_chart` (MC/Revenue ratio)
- `hl_fcf_yield_chart` (FCF yield %)

### Tables to Query:
- Valuation metrics
- Price data

---

## 7. COMPETITION & MARKET POSITION

### Questions in this category:
- "Who are HYPE's main competitors in the perp DEX space?"
- "How does Aster compare to HYPE (backed by Binance/CZ)?"
- "How does Lighter compare to HYPE (backed by a16z)?"
- "Why is competitor volume potentially inflated (points/airdrop farming)?"
- "What is HYPE's share vs major CEXs like Binance, ByBit, Bitget?"
- "How has HYPE's market share vs CEXs trended over time?"
- "What advantages does HYPE have over CEXs?"

### DEX Competitor Landscape:
| Protocol | Backing | Strength | Weakness |
|----------|---------|----------|----------|
| Aster | Binance/CZ | Capital, ecosystem | Centralization concerns |
| Lighter | a16z | VC capital | Newer, less volume |
| edgeX | - | Speed | Less liquid |
| dYdX | Various VCs | First mover | Token economics |
| GMX | Organic | Real yield | Slower growth |

### Volume Quality Assessment:
- **Organic indicators**: Consistent vol/OI, diverse user base
- **Incentivized indicators**: High vol/OI spikes, points farming
- HYPE advantage: Organic volume post-TGE (no ongoing incentives)

### CEX Market Share Context:
- Total crypto perp volume: ~$100-150B daily
- Binance: ~50% share
- HYPE: ~1-3% share (growing)

### Data Needed:
- Competitor volume data
- Market share trends
- Vol/OI comparisons

### Charts to Load:
- `hl_competitor_volume_chart` (volume comparison)
- `hl_vol_oi_platform_chart` (organic score)

---

## 8. HIP-3 & NEW PRODUCTS

### Questions in this category:
- "What is HIP-3 and how does it work?"
- "What new markets have been launched on HIP-3 (xyz, flx, vntl)?"
- "How do synthetic stock perps work on Hyperliquid?"
- "What is the staking requirement to launch a HIP-3 market?"
- "What is HIP-3 Growth Mode and why does it matter?"
- "How much volume are HIP-3 markets generating?"

### HIP-3 Overview:
- Permissionless market deployment on Hyperliquid
- Third parties can launch perpetual markets
- Revenue share with market deployers
- HYPE staking required for deployment

### HIP-3 Requirements:
| Aspect | Requirement |
|--------|-------------|
| HYPE Stake | 10,000 HYPE minimum |
| Market Type | Any asset with price feed |
| Fee Share | Deployer gets portion of fees |
| Liquidity | Deployer may provide initial liquidity |

### Growth Mode:
- Reduced fees to bootstrap new markets
- Volume incentives for early traders
- Transition to normal fees once liquid

### Data Needed:
- HIP-3 deployer volume breakdown
- HIP-3 vs HL perp volume comparison
- New market launches

### Charts to Load:
- `hip3_volume_chart` (volume by DEX)
- `hip3_vs_hl_volume_chart` (HIP-3 share)
- `hip3_market_share_chart` (market share)
- `hip3_oi_chart` (open interest)
- `hip3_traders_chart` (unique traders)

### Tables to Query:
- HIP-3 volume data
- Deployer metrics

---

## 9. STAKING & VALIDATORS

### Questions in this category:
- "How does HYPE staking work?"
- "What is the current staking APR?"
- "How many validators does HYPE have and what is the max?"
- "Who are the largest validators on Hyperliquid?"
- "What are the centralization concerns around validator count?"

### Staking Mechanics:
| Aspect | Details |
|--------|---------|
| Staking Token | HYPE |
| Reward Source | Inflation + fees |
| Lock Period | 7-day unbonding |
| Min Stake | Varies by validator |
| Max Validators | 21 active |

### Validator Distribution:
- Current active: 21 validators
- Top validators by stake (approximate):
  - Hyperliquid Foundation
  - Kinetiq
  - Community operators

### Centralization Concerns:
- Only 21 active validators (similar to dPoS chains)
- Foundation controls significant stake
- Trade-off: Speed vs decentralization
- Roadmap: Increasing validator set over time

### Data Needed:
- Staking APR history
- Validator stake distribution
- Total staked HYPE

### Charts to Load:
- Validator distribution (if available)
- Staking APR trends (if available)

---

## 10. RISKS & CONCERNS

### Questions in this category:
- "What are the regulatory risks for HYPE given its no-KYC approach?"
- "How does lack of KYC limit institutional adoption?"
- "What jurisdictions is Hyperliquid restricted from?"
- "What happened in the JELLY incident and what does it mean?"
- "What are the centralization risks with only 21 validators?"
- "How did the protocol respond to the market manipulation attack?"
- "Is competitor volume growth (Aster, Lighter) a threat to HYPE?"
- "Will point/airdrop farming volume return to HYPE after competitor TGEs?"

### Risk Categories:

#### Regulatory Risks:
| Risk | Impact | Mitigation |
|------|--------|------------|
| No-KYC Model | Institutional barriers | May add optional KYC tier |
| Derivatives Classification | Potential restrictions | Offshore structure |
| US Access | Regulatory scrutiny | Geo-blocking |

#### Technical/Security Risks:
| Risk | Impact | Mitigation |
|------|--------|------------|
| Validator Centralization | Censorship risk | Validator expansion roadmap |
| Smart Contract Risk | Fund loss | Audits, insurance fund |
| JELLY-type Incidents | Reputation | Improved risk parameters |

#### JELLY Incident Summary:
- March 2024: Market manipulation attempt on JELLY token
- Attacker tried to exploit HLP positions
- Protocol responded with emergency intervention
- Resulted in improved oracle and risk controls

#### Competitive Risks:
| Risk | Impact | Likelihood |
|------|--------|------------|
| Aster/Lighter Growth | Volume loss | Medium |
| CEX Feature Parity | User migration | Low |
| Regulatory Crackdown | Market access | Medium |

### Data Needed:
- Historical incident timeline
- Validator distribution
- Competitor growth metrics

---

## 11. INVESTMENT VEHICLES (HYPD & PURR)

### Questions in this category:
- "How much HYPE does HYPD own and at what cost basis?"
- "What is HYPD's current mNAV and how is it calculated?"
- "What income streams does HYPD have (staking, validator, HIP-3 fees)?"
- "Who leads HYPD and what is their background?"
- "What is HYPD's Felix partnership and how does it work?"
- "How much HYPE does PURR own?"
- "What is PURR's mNAV and discount to NAV?"
- "How much cash does PURR have on its balance sheet?"
- "Who leads PURR and what is their background?"
- "How do HYPD and PURR compare as ways to gain HYPE exposure?"
- "Which offers better value - HYPD at 1.14x mNAV or PURR at 0.77x?"

---

### HYPD (Hyperion DeFi) - "The Operator"

**Overview**: HYPD is an actively managed public company focused on generating yield from HYPE holdings through operational activities on the Hyperliquid ecosystem.

| Metric | Details |
|--------|---------|
| Structure | Public company (OTC: HYPD) |
| Primary Asset | HYPE tokens |
| Strategy | Active yield generation |
| Management Style | Operational participation in ecosystem |

#### HYPD Revenue Streams

1. **Staking Rewards**
   - Stakes HYPE holdings for protocol staking rewards
   - Earns inflation rewards + portion of fees
   - Yield varies with staking participation rate

2. **Validator Operation**
   - Runs a Hyperliquid validator node
   - Earns validator commissions on staked HYPE
   - Contributes to network security
   - **Why This Matters**: Active operational role, not just passive holding

3. **HIP-3 Partnership (Felix)**
   - Partnership with Felix to deploy HIP-3 markets
   - Felix is a HIP-3 market deployer
   - HYPD earns share of trading fees from deployed markets
   - **Synthetic Stock Perps**: Felix deploys markets like AAPL-PERP, TSLA-PERP
   - Revenue share structure between HYPD, Felix, and Hyperliquid protocol

4. **Potential Market Making**
   - May provide liquidity on Hyperliquid
   - Additional yield from bid-ask spread capture

#### What Are HIP-3 Markets?

HIP-3 (Hyperliquid Improvement Proposal 3) enables **permissionless perpetual market creation**:

- Anyone can deploy new perp markets (with 10,000 HYPE stake)
- Deployers earn portion of trading fees from their markets
- Enables **synthetic stock perps**: AAPL, TSLA, NVDA, etc.
- 24/7 trading of stock exposure (unlike stock markets)
- No need to own underlying asset

**HYPD's Angle**: Through Felix partnership, HYPD earns fees from synthetic stock trading without deploying capital as inventory.

#### Why HYPD Trades at Premium to NAV

| Factor | Impact |
|--------|--------|
| Active yield generation | Higher returns than passive holding |
| Validator income | Recurring revenue stream |
| HIP-3 fee share | Growth optionality |
| Operational expertise | Management value-add |
| Scarcity | Limited public market HYPE exposure |

**Typical Premium**: 1.1-1.2x mNAV (market NAV)

---

### PURR (Hyperliquid Strategies) - "The Allocator"

**Overview**: PURR is a passively managed treasury company holding HYPE tokens and cash, focused on capital preservation and opportunistic deployment.

| Metric | Details |
|--------|---------|
| Structure | Public company (OTC: PURR) |
| Primary Assets | HYPE tokens + Cash |
| Strategy | Treasury management |
| Management Style | Passive holding, opportunistic |

#### PURR Balance Sheet Composition

| Asset | Purpose |
|-------|---------|
| HYPE Holdings | Core exposure to Hyperliquid |
| Cash (USDC/USD) | Dry powder for opportunities |
| Other | Minimal other assets |

**Cash Position Significance**:
- Provides downside protection
- Enables opportunistic HYPE purchases on dips
- Reduces volatility vs pure HYPE exposure
- But also dilutes upside participation

#### Why PURR Trades at Discount to NAV

| Factor | Impact |
|--------|--------|
| No active yield | Lower returns than staking |
| Management overhead | Expenses without operational income |
| Cash drag | Dilutes HYPE upside |
| Illiquidity discount | OTC trading, limited buyers |
| Passive strategy | No management alpha |

**Typical Discount**: 0.7-0.8x mNAV

#### NAV Gap Closing Mechanism

Management may use **share buybacks** when trading at significant discount:
- Buy back PURR shares below NAV
- Effectively arbitrage the discount
- Increases NAV per remaining share
- Signals management confidence

---

### HYPD vs PURR Comparison

| Factor | HYPD | PURR |
|--------|------|------|
| **Strategy** | Active operations | Passive treasury |
| **Revenue** | Staking + Validator + HIP-3 | Buyback yield only |
| **Risk Profile** | Higher (operational risk) | Lower (pure exposure) |
| **NAV Status** | Premium (1.1-1.2x) | Discount (0.7-0.8x) |
| **Upside Participation** | 100% HYPE + yield | Diluted by cash |
| **Downside Protection** | Less (fully deployed) | More (cash buffer) |
| **Best For** | Growth + yield seekers | Pure exposure, value buyers |

### Investment Decision Framework

**Choose HYPD if**:
- You want yield ON TOP of HYPE exposure
- You believe HIP-3/Felix will generate material fees
- You're comfortable paying premium for operational value
- You want validator/staking income

**Choose PURR if**:
- You want pure HYPE exposure at a discount
- You believe discount will narrow (buyback catalyst)
- You prefer simpler, passive strategy
- You value the cash buffer for downside protection

**Choose Direct HYPE if**:
- You want maximum upside participation
- You can self-custody and stake
- You don't need public market wrapper
- You want immediate liquidity (DEX trading)

### mNAV Calculation Framework

```
mNAV = (HYPE Holdings × HYPE Price) + Cash + Other Assets
                        ─────────────────────────────────
                             Shares Outstanding

Price/mNAV = Stock Price / mNAV per Share
```

| Metric | HYPD | PURR |
|--------|------|------|
| HYPE Holdings | Check SEC filings | Check SEC filings |
| Cash Position | Minimal | Significant |
| Other Assets | Minimal | Minimal |
| Shares Outstanding | SEC filings | SEC filings |
| **Price/mNAV** | ~1.14x (premium) | ~0.77x (discount) |

### Data Needed (SEC Filings):
- Form 8-K: Material events, HYPE acquisitions
- Form 10-Q: Quarterly financials, holdings
- Proxy statements: Management compensation, strategy
- Stock price: OTC quotes

**Note**: Detailed financial data requires SEC EDGAR integration (not currently in database).

---

## 12. GROWTH PROJECTIONS & SCENARIOS

### Questions in this category:
- "What is HYPE's path to $5bn in annual fees?"
- "What market share assumptions drive the bull case?"
- "How would token supply change under various fee/buyback scenarios?"
- "What is the 10-year scenario analysis for HYPE?"
- "How sensitive is HYPE valuation to market share assumptions?"

### Path to $5B Annual Fees:
| Assumption | Current | Required |
|------------|---------|----------|
| Daily Volume | ~$3-5B | ~$15-20B |
| Take Rate | 3.5bps | 3.5bps |
| Spot Volume | ~$100M | ~$2B |
| Market Share (DEX) | ~60% | ~70% |
| Market Share (Total) | ~2% | ~10% |

### 10-Year Scenario Framework:
| Year | Volume Growth | Fee Growth | Supply Change |
|------|---------------|------------|---------------|
| Y1 | 50% | 50% | -3% (buybacks) |
| Y2 | 30% | 30% | -4% |
| Y3-5 | 20% CAGR | 20% CAGR | -5% CAGR |
| Y6-10 | 10% CAGR | 10% CAGR | -3% CAGR |

### Sensitivity Analysis:
| Market Share | Annual Fees | FDV @ 50x |
|--------------|-------------|-----------|
| 5% | $2.5B | $125B |
| 10% | $5B | $250B |
| 15% | $7.5B | $375B |
| 20% | $10B | $500B |

### Data Needed:
- Historical growth rates
- Market size projections
- Fee projections

---

## 13. COMPARATIVE ANALYSIS

### Questions in this category:
- "How does HYPE compare to Coinbase (COIN) as an exchange investment?"
- "How does HYPE's fee generation compare to traditional exchanges?"
- "How does the ~99% fee-to-buyback model compare to dividend yields?"

### HYPE vs COIN Comparison:
| Metric | HYPE | Coinbase |
|--------|------|----------|
| Revenue Model | Trading fees | Trading + custody + subscription |
| Fee Destination | ~99% buybacks | Dividends + reinvestment |
| Regulation | Offshore DEX | US regulated |
| Vol/Revenue | Higher | Lower |
| Growth Rate | Higher | Lower |

### Buyback vs Dividend Comparison:
| Aspect | HYPE Buyback | Traditional Dividend |
|--------|--------------|----------------------|
| Tax Efficiency | Capital gains | Income tax |
| Flexibility | Continuous | Quarterly |
| Signal | Bullish | Neutral |
| Reinvestment | Automatic | Manual |

### Exchange Revenue Multiples:
| Exchange | Revenue ($B) | Valuation | Multiple |
|----------|--------------|-----------|----------|
| Coinbase | ~3B | ~50B | ~17x |
| Binance | ~10B+ | Private | - |
| HYPE | ~1B | ~30B | ~30x |

---

## 14. TECHNICAL ANALYSIS & PRICE

### Questions in this category:
- "What is HYPE's current price and how has it performed since TGE?"
- "What are key support/resistance levels for HYPE?"
- "What drove the price spike in late 2024/early 2025?"

### Price History Context:
- TGE: November 2024
- TGE Price: ~$3-4
- ATH: ~$35+ (January 2025)
- Key Levels: $20, $25, $30 (round numbers)

### Technical Factors:
- Low float (high volatility)
- Limited CEX listings initially
- Airdrop recipient selling pressure
- Platform metrics correlation

### Data Needed:
- OHLCV price data
- Technical indicators (RSI, MACD)
- Volume analysis

### Charts to Load:
- `price_chart` (OHLCV with indicators)
- `rsi_chart` (momentum)
- `volume_chart` (volume analysis)

---

## 15. ECOSYSTEM & PARTNERSHIPS

### Questions in this category:
- "What major projects are building on Hyperliquid?"
- "What is the USDH stablecoin and how does it fit in?"
- "Who are the major validators and infrastructure partners?"
- "What is Kinetiq's role in the ecosystem?"

### Key Ecosystem Components:

#### Native Products:
| Product | Description |
|---------|-------------|
| HyperCore | Perp trading engine |
| HyperEVM | Smart contract platform |
| HLP | Liquidity provider vault |
| USDH | Native stablecoin (planned) |

#### Key Partners:
| Partner | Role |
|---------|------|
| Kinetiq | Validator, infrastructure |
| Various | HIP-3 deployers |
| Market Makers | Liquidity provision |

### USDH Stablecoin:
- Native stablecoin for Hyperliquid ecosystem
- Designed to capture settlement/margin use case
- Potential fee generation source

---

## DATA SOURCE SUMMARY

### Primary Data Sources:
1. **On-chain data**: Hyperliquid L1 (volume, OI, AF balance, staking)
2. **Trading data**: DeFiLlama, The Block, ASXN (volume, fees)
3. **Price data**: CoinGecko, CoinMarketCap
4. **Company filings**: SEC filings for HYPD/PURR
5. **Protocol docs**: Hyperliquid whitepaper, HIP proposals

### Chart Categories by Question Type:

| Question Category | Charts |
|-------------------|--------|
| Fundamentals | price_chart |
| Tokenomics | hl_tokenomics_chart, hl_cumulative_buyback_chart |
| Assistance Fund | hl_af_balance_chart, hl_daily_buyback_chart |
| Volume | hl_daily_volume_chart, hl_competitor_volume_chart |
| Fees | hl_monthly_revenue_chart, hl_cumulative_revenue_chart |
| Valuation | hl_fdv_vs_revenue_chart, hl_fdv_multiple_chart |
| Competition | hl_competitor_volume_chart, hl_vol_oi_platform_chart |
| HIP-3 | hip3_volume_chart, hip3_vs_hl_volume_chart |
| Staking | (validator charts if available) |
| Price | price_chart, rsi_chart |

---

## RESPONSE GUIDELINES

When answering HYPE investment questions:

1. **Cite specific metrics** (e.g., "$874M YTD fees" not "high fees")
2. **Reference timeframes** for all data points
3. **Provide context** with comparisons to competitors/peers
4. **Flag data staleness** if data may need refresh
5. **Include caveats** about risks and uncertainties
6. **Use available charts** to visualize key metrics
7. **Cross-reference** multiple data sources for accuracy
