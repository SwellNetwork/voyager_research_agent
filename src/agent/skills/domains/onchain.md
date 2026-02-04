---
name: On-Chain Analysis Framework
version: 2.0
type: domain
domain: onchain
applicable_assets: [BTC, ETH]
last_updated: 2026-01-16
sources:
  - templates/report_prompts.py (ON_CHAIN_VALUATION_FRAMEWORK)
  - docs/gemini_analysis/P5-004_on_chain_valuation_deep_analysis.md
  - docs/research/P5-005-Gemini-Deep-Analysis-Holder-Exchange-Flow.md
---

# On-Chain Analysis Framework

## Overview

On-chain analysis uses blockchain data to understand holder behavior, network valuation, and supply dynamics. This framework applies primarily to BTC and ETH which have the richest on-chain datasets.

**Note**: This is a cross-asset framework. For asset-specific on-chain analysis, use the asset overlays (btc/onchain.md, eth/onchain.md).

## Core Valuation Metrics

### MVRV (Market Value to Realized Value)

MVRV compares market cap to the aggregate cost basis of all coins.

| MVRV Ratio | Classification | Historical Context | Frequency |
|------------|----------------|-------------------|-----------|
| > 3.2 | Extreme Overvaluation | Cycle top zone (2013, 2017, 2021) | ~6% of days |
| 2.4 - 3.2 | Overvalued | Distribution phase | ~14% of days |
| 1.5 - 2.4 | Fair to Elevated | Mid-bull run | ~20% of days |
| 1.0 - 1.5 | Fair Value | Healthy accumulation | ~40% of days |
| 0.8 - 1.0 | Undervalued | Strong accumulation zone | ~15% of days |
| < 0.8 | Deeply Undervalued | Cycle bottom zone (100% accuracy) | ~5% of days |

### MVRV Z-Score

Normalized version accounting for historical volatility:

| Z-Score | Signal |
|---------|--------|
| > 7 | Extreme bubble (rare) |
| 5 - 7 | Major cycle top |
| 2 - 5 | Elevated |
| 0 - 2 | Fair value range |
| -0.5 - 0 | Undervalued |
| < -0.5 | Generational opportunity |

## Profitability Metrics

### NUPL (Net Unrealized Profit/Loss)

| NUPL | Phase | Action |
|------|-------|--------|
| > 0.75 | Euphoria | Distribution imminent |
| 0.5 - 0.75 | Belief | Strong bull, hold |
| 0.25 - 0.5 | Optimism | Accumulate |
| 0 - 0.25 | Hope/Fear | Transition |
| < 0 | Capitulation | Strong accumulation |

### SOPR (Spent Output Profit Ratio)

| SOPR | Interpretation |
|------|----------------|
| > 1.05 | Profit-taking active |
| 1.0 - 1.05 | Neutral |
| 0.95 - 1.0 | Light capitulation |
| < 0.95 | Heavy capitulation |

### SOPR in Context
- Bull market: SOPR dips to 1.0 = Buy the dip
- Bear market: SOPR spikes above 1.0 = Relief rally (fade)

## Supply Distribution

### Holder Cohorts

| Cohort | Definition | Behavior |
|--------|------------|----------|
| LTH | Held > 155 days | Smart money, strategic |
| STH | Held < 155 days | More reactive, momentum |
| Whales | > 1000 coins | Market movers |
| Retail | < 1 coin | Sentiment indicator |

### LTH/STH Dynamics
- LTH accumulating = Bullish long-term
- LTH distributing = Late cycle warning
- STH capitulating = Bottom indicator
- STH accumulating = Momentum chase

## Exchange Flows

### Exchange Balance Analysis

| Trend | Duration | Signal |
|-------|----------|--------|
| Sustained outflow | > 30 days | Bullish accumulation |
| Sustained inflow | > 30 days | Bearish distribution |
| Large single inflow | Single event | Watch for selling |
| Large single outflow | Single event | OTC/cold storage |

### Exchange Flow Interpretation
- Declining reserves = Supply squeeze
- Rising reserves = Selling preparation
- Stablecoin inflows = Dry powder ready

## Network Activity

### Active Addresses

| Trend | Interpretation |
|-------|----------------|
| Rising addresses + rising price | Healthy growth |
| Rising addresses + falling price | Accumulation phase |
| Falling addresses + rising price | Speculation (weak) |
| Falling addresses + falling price | Bear market |

### Transaction Volume
- Adjusted for internal transfers
- Compare to historical ranges
- Watch for divergences with price

## Whale Monitoring

### Whale Transaction Types

| Flow | Interpretation |
|------|----------------|
| Whale → Exchange | Selling pressure |
| Exchange → Whale | Accumulation |
| Whale → Whale | OTC, neutral |
| Unknown → Whale | Buying from market |

### Whale Accumulation Signals
- Large withdrawals from exchanges
- Dormant wallet reactivation (buying)
- Clustering of whale transactions

## Miner Metrics (BTC-Specific)

### Hash Ribbons
- 30-day MA vs 60-day MA
- Inversion = Miner capitulation
- Recovery = Strength returning

### Miner Flows
- Miner reserves depleting = Forced selling
- Miner reserves stable/rising = Holding

## On-Chain Confluence

### Bullish Confluence (Score 4+/6)
- [ ] MVRV < 1.5
- [ ] NUPL < 0.25
- [ ] SOPR reset to 1.0
- [ ] Exchange outflows sustained
- [ ] LTH accumulating
- [ ] Active addresses rising

### Bearish Confluence (Score 4+/6)
- [ ] MVRV > 2.5
- [ ] NUPL > 0.65
- [ ] SOPR elevated with price stalling
- [ ] Exchange inflows rising
- [ ] LTH distributing
- [ ] Active addresses declining

## Data Sources

### Primary On-Chain Providers
- Glassnode (comprehensive)
- CryptoQuant (exchange focus)
- IntoTheBlock (holder analysis)
- Santiment (social + on-chain)

### Metrics Reliability
- Exchange data: High reliability
- Holder cohorts: Medium (entity clustering imperfect)
- Active addresses: High
- MVRV/NUPL: Very high

## Integration Notes

### Combining with Other Frameworks
- On-chain provides medium-term view
- Derivatives provide short-term positioning
- Technical provides entry/exit timing
- Sentiment provides crowd psychology

### Lag Considerations
- On-chain signals often lead price by days/weeks
- Not suitable for intraday trading
- Best for position building/unwinding

---

## Academic References & Research Validation

This framework is grounded in peer-reviewed academic research and industry best practices. The following references provide traceability between research findings and the thresholds/signals used in this framework.

### MVRV (Market Value to Realized Value)

**Core Research:**
- **Huang & Chang (2022)** - "Using Crypto-Asset Pricing Methods to Build Technical Oscillators for Short-Term Bitcoin Trading" (*Information*, MDPI)
  - Google Scholar: https://scholar.google.com/scholar?q=Huang+Chang+2022+Bitcoin+MVRV+oscillators
  - **Key Finding:** MVRV > 3.7 marks overvaluation zones; MVRV < 1.0 marks undervaluation zones
  - **Validation:** Thresholds validated across multiple market cycles (2013-2022)
  - **Framework Impact:** Established our MVRV > 3.5 (extreme overvaluation) and MVRV < 0.75 (deeply undervalued) thresholds

- **Liu, Tsyvinski, Wu (2022)** - "Accounting for Cryptocurrency Value" (Yale Cowles Foundation Working Paper)
  - Google Scholar: https://scholar.google.com/scholar?q=Liu+Tsyvinski+Wu+2022+blockchain+cryptocurrency+value
  - **Key Finding:** Blockchain data provides "unprecedented transparency for valuation analysis"; price-to-network-value metrics show statistically significant return predictability
  - **Framework Impact:** Academic validation from Yale/Berkeley that cost-basis metrics (MVRV) have genuine predictive power

- **Mahmudov & Puell (2018)** - "Bitcoin Market-Value-to-Realized-Value (MVRV) Ratio" (Industry Foundational Research)
  - Google Scholar: https://scholar.google.com/scholar?q=Mahmudov+Puell+2018+MVRV+Bitcoin
  - **Key Finding:** Introduced MVRV concept; identified historical cycle extremes at MVRV 3.2-3.7 (tops) and 0.8-1.0 (bottoms)
  - **Framework Impact:** Foundational methodology for MVRV calculation and threshold identification

**Gemini Deep Analysis Synthesis:**
- **Document:** `docs/gemini_analysis/P5-004_on_chain_valuation_deep_analysis.md` (lines 22-147)
- **Updated Thresholds:** MVRV > 3.2 represents ~6% of trading days (extreme overvaluation); MVRV < 0.8 represents ~5% of days (extreme undervaluation)
- **Market Efficiency Note:** Post-2017 (after Bitcoin futures introduction), MVRV alone insufficient—requires multi-metric confirmation (CVD, NUPL, funding rates)

### NUPL (Net Unrealized Profit/Loss)

**Core Research:**
- **Omole & Enke (2024)** - "Deep learning for Bitcoin price direction prediction" (*Financial Innovation*, peer-reviewed)
  - Google Scholar: https://scholar.google.com/scholar?q=Omole+Enke+2024+Bitcoin+on-chain+features
  - **Key Finding:** 82.44% accuracy for next-day price direction using CNN-LSTM with on-chain features; "realized/unrealized value classifications demonstrated HIGHER predictive power" than technical indicators
  - **Framework Impact:** Validates NUPL's reliability for capitulation detection; confirms our NUPL < 0 (capitulation) and NUPL > 0.75 (euphoria) thresholds

- **Cohen & Aiche (2025)** - "Predicting the Bitcoin's price using AI" (*Frontiers in Artificial Intelligence*, peer-reviewed)
  - Google Scholar: https://scholar.google.com/scholar?q=Cohen+Aiche+2025+Bitcoin+AI+profitability+metrics
  - **Key Finding:** 1640% total return (2018-2024) using AI strategies with profitability metrics vs 223% buy-and-hold; 2022 bear market limited losses to -35% vs -65% for buy-and-hold
  - **Framework Impact:** Demonstrates NUPL-based regime detection enables superior risk management and downside protection

- **Adamant Capital (2018)** - "A Primer on Bitcoin Investor Sentiment and Changes in Saving Behavior"
  - Google Scholar: https://scholar.google.com/scholar?q=Adamant+Capital+2018+Bitcoin+NUPL+investor+sentiment
  - **Key Finding:** Established NUPL market cycle phases: Capitulation (< 0), Hope/Fear (0-0.25), Optimism (0.25-0.5), Belief (0.5-0.75), Euphoria (> 0.75)
  - **Framework Impact:** Direct source for our NUPL phase classification table

**Gemini Deep Analysis Synthesis:**
- **Document:** `docs/gemini_analysis/P5-004_on_chain_valuation_deep_analysis.md` (lines 150-315)
- **Reliability Score:** 8.9/10 overall; 100% accuracy for extreme capitulation (NUPL < 0); very low false positive rate in extreme zones
- **Best Use Case:** Strategic cycle phase identifier; combine with real-time SOPR and CVD for tactical timing

### SOPR (Spent Output Profit Ratio)

**Core Research:**
- **Omole & Enke (2024)** - "Deep learning for Bitcoin price direction prediction" (*Financial Innovation*)
  - Google Scholar: https://scholar.google.com/scholar?q=Omole+Enke+2024+Bitcoin+realized+value+features
  - **Key Finding:** "Realized value" features (SOPR is quintessential realized value metric) ranked as top-tier by Boruta feature selection; 82.44% predictive accuracy
  - **Framework Impact:** Academic validation that SOPR resets are leading indicators with genuine predictive power

- **Shirakashi (2019)** - "Introducing SOPR: spent outputs to predict bitcoin lows and tops" (Industry Research, Medium/Unconfiscatable)
  - Google Scholar: https://scholar.google.com/scholar?q=Shirakashi+2019+SOPR+Bitcoin+spent+outputs
  - **Key Finding:** SOPR resets to 1.0 mark reversals; bull market: SOPR dips to 1.0 = buy signal; bear market: SOPR rises to 1.0 = sell signal
  - **Framework Impact:** Original SOPR methodology; established SOPR > 1 (profit-taking) and SOPR < 1 (loss realization) framework

**Gemini Deep Analysis Synthesis:**
- **Document:** `docs/gemini_analysis/P5-004_on_chain_valuation_deep_analysis.md` (lines 317-572)
- **Predictive Accuracy:** Bull market resets 75-80%, bear market resets 80-85%, regime changes 90-95%
- **Key Variants:** aSOPR (80-85% accuracy), LTH-SOPR (85-90% accuracy, slower but more reliable), STH-SOPR (70-75% accuracy, faster but noisier)
- **Best Practice:** Use SOPR as primary short-term timing tool; validate with NUPL cycle phase; confirm with CVD for highest-conviction trades

### Holder Cohort Analysis (LTH/STH Dynamics)

**Core Research:**
- **Liu, Zhang, Zhao (2022)** - "Deciphering Bitcoin Blockchain Data by Cohort Analysis" (*Nature Scientific Data*, peer-reviewed)
  - Google Scholar: https://scholar.google.com/scholar?q=Liu+Zhang+Zhao+2022+Bitcoin+cohort+analysis+Nature
  - **Key Finding:** Cohort-based analysis reduces computational burden from 1.3 TB full blockchain to manageable datasets; enables tracking of holder behavior over time
  - **Framework Impact:** Methodological foundation for LTH (>155 days) vs STH (<155 days) classification

- **Chen (2024)** - "Correlation Between Bitcoin Price and Total Supply of Long-term Holders" (*Highlights in Business, Economics and Management*)
  - Google Scholar: https://scholar.google.com/scholar?q=Chen+2024+Bitcoin+long-term+holders+supply+correlation
  - **Key Finding:** Vector Autoregression (VAR) analysis across 14 years (2010-2024) shows negative correlation: ↑ Price = ↓ LTH Supply (distribution phase); 1% price shock creates negative LTH supply effect for t>2 periods
  - **Framework Impact:** Validates our "LTH distributing = late cycle warning" and "LTH accumulating = bullish long-term" signals; provides 2-4 week lead time

- **ScienceDirect (2025)** - "Market Expectations and the Holding Behaviors of Bitcoin Whales, Dolphins, and Minnows" (*Research in International Business and Finance*)
  - Google Scholar: https://scholar.google.com/scholar?q=Bitcoin+whales+dolphins+minnows+contrarian+2025
  - **Key Finding:** Whales (>1,000 BTC) exhibit contrarian behavior (buy dips, sell rallies); dolphins/minnows exhibit momentum behavior; whale proportion increase from 1% to 6% raises daily volatility 104%
  - **Framework Impact:** Distinguishes whale accumulation (contrarian, during fear) from retail accumulation (momentum, during FOMO); explains our whale monitoring signals

**Gemini Deep Analysis Synthesis:**
- **Document:** `docs/research/P5-005-Gemini-Deep-Analysis-Holder-Exchange-Flow.md` (lines 13-273)
- **Most Reliable Predictor:** LTH supply changes (2-4 week lead, 70-80% accuracy)
- **Whale Behavior:** Contrarian (buy at Fear Index 0-25, sell at Greed 75-100); exchange outflows = accumulation, inflows = distribution

### Exchange Flow Dynamics

**Core Research:**
- **Hoang & Baur (2022)** - "Loaded for Bear: Bitcoin Private Wallets, Exchange Reserves and Prices" (*Journal of Banking and Finance*)
  - Google Scholar: https://scholar.google.com/scholar?q=Hoang+Baur+2022+Bitcoin+exchange+reserves+prices
  - **Key Finding:** Exchange reserve increases negatively related to contemporaneous AND future Bitcoin returns; 1-7 day lead time
  - **Framework Impact:** Validates our "rising reserves = selling pressure" (bearish) interpretation in bear markets

- **Chi & Hao (2025)** - "Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets"
  - Google Scholar: https://scholar.google.com/scholar?q=Chi+Hao+2025+cryptocurrency+on-chain+flows+forecasting
  - **Key Finding:** Exchange inflows predict higher short-term returns for BTC and ETH (1-3 day lead time); contradicts Hoang & Baur in bull market contexts
  - **Framework Impact:** Regime-dependent interpretation: bear market (inflows = bearish), bull market (inflows = trading activity/liquidity)

- **Muminov et al. (2024)** - "Enhanced Bitcoin Price Direction Forecasting with DQN" (*IEEE Access*)
  - Google Scholar: https://scholar.google.com/scholar?q=Muminov+2024+Bitcoin+DQN+exchange+flows+miner
  - **Key Finding:** Deep Q-Network combining exchange flows + miner outflows + stablecoin inflows + options OI achieves 82%+ accuracy (1-3 day lead)
  - **Framework Impact:** Multi-source integration (exchange flows + other metrics) dramatically improves accuracy; validates our confluence approach

**Gemini Deep Analysis Synthesis:**
- **Document:** `docs/research/P5-005-Gemini-Deep-Analysis-Holder-Exchange-Flow.md` (lines 75-275)
- **Lead Times:** Exchange netflows (1-7 days, 60-70% accuracy), LTH to exchange flows (2-4 weeks, 75-80% accuracy), combined signals (4-8 weeks, 75-85% accuracy)
- **Critical Limitation:** Exchange attribution errors, internal transfers create noise; regime-dependent interpretation required

### Multi-Metric Confluence Strategy

**Core Research:**
- **Huang & Chang (2022)** - Market efficiency research
  - **Key Finding:** "Trading performance significantly worsened after 2017... suggests market maturation"; single-factor strategies no longer sufficient
  - **Framework Impact:** Justifies our multi-metric approach (MVRV + NUPL + SOPR + CVD) for post-2017 markets

- **Omole & Enke (2024)** - Feature importance study
  - **Key Finding:** "Combined on-chain + technical indicators outperformed either alone"; 82.44% accuracy achieved by combining multiple feature types
  - **Framework Impact:** Validates confluence scoring system; no single metric sufficient in efficient markets

**Gemini Deep Analysis Synthesis:**
- **Document:** `docs/gemini_analysis/P5-004_on_chain_valuation_deep_analysis.md` (lines 575-1085)
- **Optimal Strategy:** Multi-timeframe hierarchy (MVRV/NUPL = strategic, SOPR = tactical, CVD = execution)
- **Expected Performance:** 70-85% win rate with confluence scoring, 2.5-3.5 Sharpe ratio, vs single-metric approaches

### Implementation Notes

**Threshold Updates Based on Research:**
- **MVRV Extremes:** Updated from generic >3.5/<0.75 to research-validated >3.2 (tops, 6% of days) and <0.8 (bottoms, 5% of days)
- **NUPL Reliability:** 100% accuracy for capitulation (< 0), 82.44% predictive accuracy validated by peer-review
- **SOPR Context-Dependency:** Bull market resets 75-80% accurate, regime changes 90-95% accurate
- **LTH Supply Lead Time:** 2-4 weeks advance warning validated by 14-year VAR analysis

**Critical Limitations Identified:**
- Entity clustering uncertainty (one entity can control many addresses)
- Lost coins vs patient holders (unknown percentage of LTH supply permanently lost)
- Post-2017 market efficiency requires multi-metric confirmation
- Regime-dependent interpretation (bear vs bull markets)

**Data Sources:**
- Primary: Glassnode (LTH/STH cohorts, NUPL, aSOPR)
- Secondary: CryptoQuant (exchange flows, miner flows)
- Validation: Coin Metrics (cross-verification)

**Research-to-Practice Traceability:**
All thresholds and signals in this framework trace to specific academic papers or peer-reviewed industry research. Gemini deep analysis documents (`P5-004`, `P5-005`) provide comprehensive synthesis with implementation roadmaps.
