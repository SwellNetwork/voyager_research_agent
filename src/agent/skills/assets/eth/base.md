---
name: ETH Base Agent
version: 1
asset: ETH
type: base
last_updated: 2025-01-13
sources:
  - templates/report_prompts.py (ASSET_FRAMEWORKS)
---

# ETH Analysis Framework

## Asset Narrative

Ethereum: Smart contract platform, fee revenue generator, staking yield asset.

ETH is fundamentally different from BTC in that it has:
- **Protocol Revenue**: Fee generation from network usage
- **Staking Yield**: Native yield from consensus participation
- **Ecosystem Value**: L2s, DeFi, NFTs built on top
- **Deflationary Mechanics**: EIP-1559 burn mechanism

## Primary Metrics

| Metric | Description | Why It Matters |
|--------|-------------|----------------|
| **Gas Usage** | Network fee consumption | Protocol utility and demand |
| **Blob Fees** | L2 data availability costs | L2 adoption and revenue |
| **Staking Rate** | % of ETH staked | Supply removed from circulation |
| **L2 TVL** | Value locked on Layer 2s | Ecosystem health |
| **ETF Flows** | Spot ETH ETF flows | Institutional demand |

## Valuation Model

### FDV/Fee Revenue Approach

For ETH, protocol economics matter more than pure MVRV:

| FDV/Annual Fees | Classification |
|-----------------|----------------|
| > 100x | Overvalued relative to usage |
| 50-100x | Fair value zone |
| 30-50x | Undervalued |
| < 30x | Significantly undervalued |

### Staking Yield Comparison

Compare ETH staking yield to risk-free rate:

| ETH Yield vs 10Y Treasury | Implication |
|---------------------------|-------------|
| ETH Yield > Treasury + 2% | Attractive risk premium |
| ETH Yield ≈ Treasury | Neutral |
| ETH Yield < Treasury | Headwind, opportunity cost |

### MVRV for ETH

MVRV still applies to ETH but with adjusted thresholds:

| MVRV Ratio | Classification |
|------------|----------------|
| > 3.0 | Overvalued |
| 2.0 - 3.0 | Elevated |
| 1.0 - 2.0 | Fair value |
| < 1.0 | Undervalued |

## Key Thresholds

### Protocol Metrics
- **Staking Rate Healthy**: > 25%
- **Staking Rate Excessive**: > 40% (centralization concerns)
- **L2 TVL Growth Bullish**: > 15% MoM
- **Blob Fee Growth Bullish**: > 10% MoM

### Deflationary Mechanics
- **Net Issuance Negative**: Deflationary (bullish)
- **Burn Rate High**: Strong fee demand
- **Ultrasound Money**: Sustained deflation

### Derivatives Thresholds
- **Funding Crowded**: > 25% annualized
- **ETH/BTC Ratio Support**: 0.04
- **ETH/BTC Ratio Resistance**: 0.08

## Comparable Assets

| Asset | Comparison Basis | Notes |
|-------|------------------|-------|
| **SOL** | L1 competitor | Higher TPS, different tradeoffs |
| **AVAX** | L1 competitor | Subnets vs L2 approach |
| **BNB** | Exchange chain | Centralized alternative |

## Unique Risk Factors

### Technical Risks
- **L2 Value Extraction**: L2s may capture value from L1
- **Staking Centralization**: Lido dominance concerns
- **Smart Contract Risk**: Systemic risk from DeFi exploits

### Regulatory Risks
- **Securities Classification**: SEC posture on ETH
- **Staking Regulation**: Potential restrictions on staking services
- **DeFi Regulation**: Impact on ecosystem usage

### Economic Risks
- **Fee Volatility**: Revenue highly variable
- **Competition**: L1 alternatives gaining share
- **L2 Fragmentation**: Liquidity split across rollups

## Required Frameworks

When analyzing ETH, apply these frameworks:

1. **ON_CHAIN_VALUATION_FRAMEWORK** - MVRV, NUPL with ETH-specific adjustments
2. **ETF_FLOW_FRAMEWORK** - Spot ETH ETF dynamics
3. **PROTOCOL_ECONOMICS_FRAMEWORK** - Fee revenue, staking yield analysis

## ETH-Specific Analysis Notes

### The Merge Impact
- Transition from PoW to PoS (September 2022)
- ~90% reduction in issuance
- Enabled staking yield

### EIP-1559 Dynamics
- Base fee burned, tips to validators
- Deflationary when usage > issuance
- Watch burn rate relative to issuance

### L2 Ecosystem
- Rollups (Arbitrum, Optimism, Base, zkSync)
- L2 activity growing vs L1
- Blob fees (EIP-4844) = L2 revenue to L1

### ETH/BTC Ratio
- Key relative performance metric
- Below 0.04 = ETH underperformance (potential opportunity)
- Above 0.08 = ETH outperformance (caution on ratio)
- Ratio often leads absolute price moves

### Staking Dynamics
- Validator queue: Long queue = high demand
- Withdrawals enabled: Exit risk normalized
- Liquid staking: stETH, rETH as proxies
