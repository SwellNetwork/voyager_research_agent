---
name: BTC Base Agent
version: 1
asset: BTC
type: base
last_updated: 2025-01-13
sources:
  - templates/report_prompts.py (ASSET_FRAMEWORKS)
---

# BTC Analysis Framework

## Asset Narrative

Bitcoin: Store of value, network security, macro hedge, digital gold thesis.

BTC is the original cryptocurrency with the longest track record, highest liquidity, and most established institutional adoption. Analysis should focus on its role as:
- **Digital Gold**: Store of value and inflation hedge
- **Network Security**: Hash rate as a measure of network health
- **Macro Asset**: Correlation/decorrelation with traditional risk assets
- **Institutional Vehicle**: ETF flows as proxy for TradFi demand

## Primary Metrics

| Metric | Description | Why It Matters |
|--------|-------------|----------------|
| **MVRV Z-Score** | Market Value vs Realized Value | Cycle positioning indicator |
| **Exchange Balance** | BTC held on exchanges | Supply available for selling |
| **Hash Rate** | Network computational power | Security and miner confidence |
| **ETF Flows** | Daily inflows/outflows | Institutional demand proxy |
| **Halving Progress** | Days since/until halving | Supply schedule catalyst |

## Valuation Model

### MVRV Z-Score Regimes

Use MVRV Z-Score as the primary valuation framework for BTC:

| Z-Score Range | Classification | Implication | Historical Context |
|---------------|----------------|-------------|-------------------|
| > 4.0 | Extreme Overvaluation | Cycle top probability 80%+ | 2017, 2021 peaks |
| 3.0 - 4.0 | High Overvaluation | Distribution zone | Late bull market |
| 2.0 - 3.0 | Overvalued | Profit-taking advisable | Mid-to-late bull |
| 0.5 - 2.0 | Fair Value | Accumulation continues | Bull market base |
| 0.0 - 0.5 | Undervalued | Strong accumulation zone | Early cycle |
| -0.5 - 0.0 | Deep Undervalued | Generational opportunity | Bear market lows |
| < -0.5 | Extreme Undervaluation | Maximum opportunity | 2018, 2022 bottoms |

### NVT (Network Value to Transactions)

| NVT Ratio | Classification |
|-----------|----------------|
| > 100 | Overvalued relative to on-chain activity |
| 50 - 100 | Fair value |
| < 50 | Undervalued, high network utility |

### Realized Cap

Track Realized Cap growth as a measure of capital inflows:
- Rising Realized Cap + Rising Price = Healthy bull market
- Flat Realized Cap + Rising Price = Speculative premium (caution)
- Falling Realized Cap = Capital outflow, bearish

## Key Thresholds

### On-Chain Thresholds
- **MVRV Z Overheated**: 3.5
- **MVRV Z Undervalued**: -0.5
- **NUPL Euphoria**: > 0.75
- **NUPL Capitulation**: < 0.25
- **SOPR Reset**: < 1.0 (profit-taking exhausted)

### Exchange Flow Thresholds
- **Exchange Outflow Bullish**: < -10,000 BTC/day (sustained)
- **Exchange Inflow Bearish**: > +10,000 BTC/day (sustained)
- **Exchange Reserve Critical**: Watch for multi-year lows

### Derivatives Thresholds
- **Funding Crowded Long**: > 30% annualized
- **Funding Crowded Short**: < -20% annualized
- **Open Interest ATH**: Elevated leverage flush risk

### Institutional Thresholds
- **ETF Flow Strong**: > $500M/day inflow
- **ETF Flow Weak**: < -$300M/day outflow (sustained)

## Comparable Assets

| Asset | Comparison Basis | Notes |
|-------|------------------|-------|
| **Gold** | Store of value thesis | BTC as "digital gold", correlation during macro stress |
| **SPY** | Risk-on/risk-off proxy | BTC beta to equities, especially in 2022-2024 |
| **QQQ** | Tech correlation | Growth asset behavior, rate sensitivity |

## Unique Risk Factors

### Mining Risks
- **Mining Centralization**: Geographic concentration (China historically, now US/Kazakhstan)
- **Hash Rate Volatility**: Miner capitulation during bear markets
- **Energy Regulation**: ESG concerns, energy cost spikes

### Regulatory Risks
- **ETF Changes**: SEC actions on ETF structure or approval
- **Exchange Regulation**: OFAC sanctions, compliance requirements
- **Self-Custody**: Potential restrictions on non-custodial wallets

### Macro Risks
- **Rate Environment**: Higher rates reduce risk asset appetite
- **Dollar Strength**: DXY correlation (inverse)
- **Liquidity Conditions**: Fed balance sheet, M2 money supply

### Technical Risks
- **Quantum Computing**: Long-term cryptographic risk (10+ years)
- **Protocol Ossification**: Resistance to upgrades (feature, not bug for some)

## Required Frameworks

When analyzing BTC, you MUST apply these frameworks:

1. **ON_CHAIN_VALUATION_FRAMEWORK** - MVRV, NUPL, SOPR analysis
2. **HALVING_CYCLE_FRAMEWORK** - Supply schedule and historical patterns
3. **CAPITAL_FLOWS_FRAMEWORK** - Exchange flows, stablecoin movements
4. **ETF_FLOW_FRAMEWORK** - Institutional demand through ETF vehicles

## BTC-Specific Analysis Notes

### Halving Cycle Context
- Halvings occur every ~210,000 blocks (~4 years)
- Historical pattern: Rally begins 6-12 months post-halving
- Supply shock thesis: Reduced issuance + constant demand = price appreciation
- **CAUTION**: Past performance doesn't guarantee future results

### ETF Dynamics
- Spot Bitcoin ETFs approved January 2024
- Daily flows are a leading indicator of institutional sentiment
- Large inflows/outflows can move spot price
- Watch for rebalancing events and option expirations

### Exchange Balance Interpretation
- Declining exchange balance = Long-term holder accumulation
- Rising exchange balance = Preparation for selling
- Whale deposits to exchanges = Potential selling pressure
- **Lag Effect**: On-chain signals often lead price by days/weeks

### Miner Behavior
- Hash Ribbons: Miner capitulation signals
- Miner outflows: Watch for post-halving selling pressure
- Difficulty adjustments: Network health indicator
