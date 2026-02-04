---
name: Crypto Research Framework
version: 1
type: domain
domain: research
applicable_assets: [BTC, ETH, SOL, HYPE, XRP, PUMP]
last_updated: 2025-01-13
description: Institutional-grade research report framework inspired by Goldman Sachs equity research
sources:
  - Claude Equity Research plugin (quant-sentiment-ai)
  - templates/report_prompts.py
---

# Institutional Crypto Research Framework

Generate an 8-section institutional research report following Goldman Sachs style standards. Each section must be data-driven with specific metrics, not vague generalizations.

## Report Structure

### 1. EXECUTIVE SUMMARY

**Format:**
```
DIRECTIONAL BIAS: [BULLISH/BEARISH/NEUTRAL] | Conviction: [High/Med/Low]

THESIS: [2-3 sentence investment thesis explaining the core view]

PRIMARY CATALYSTS (Next 30-90 days):
1. [Catalyst with date if known]
2. [Catalyst with date if known]
3. [Catalyst with date if known]

PRIMARY RISK: [Single biggest concern that could invalidate the thesis]
```

**Conviction Classification:**
| Signals Aligned | Bias | Conviction |
|-----------------|------|------------|
| 4+ bullish | BULLISH | High |
| 3 bullish | BULLISH | Med |
| 2 bullish | BULLISH | Low |
| Mixed signals | NEUTRAL | - |
| 2 bearish | BEARISH | Low |
| 3 bearish | BEARISH | Med |
| 4+ bearish | BEARISH | High |

---

### 2. ON-CHAIN VALUATION

Apply the asset-specific on-chain framework. Focus on:

**Valuation Metrics:**
- MVRV Z-Score: Current reading, regime classification, historical context
- NUPL: Market phase (Capitulation → Hope → Optimism → Belief → Euphoria)
- NVT Ratio: Network value efficiency

**Capital Flows:**
- Exchange Balance: Net flow direction, accumulation/distribution signal
- Realized Cap: Growth rate, capital inflow assessment
- Stablecoin Supply: Dry powder available

**Supply Analysis:**
- LTH/STH distribution changes
- Whale accumulation patterns
- Exchange reserve trends

**Output Format:**
```
ON-CHAIN HEALTH: [STRONG/NEUTRAL/WEAK]

Key Metrics:
- MVRV Z-Score: X.XX ([regime])
- NUPL: X.XX ([phase])
- Exchange Balance: [direction] [amount] over [period]

Assessment: [2-3 sentence interpretation]
```

---

### 3. DERIVATIVES POSITIONING

**Perpetual Futures Analysis:**
- Funding Rates: Annualized rate, crowding assessment
- Long/Short Ratio: Retail positioning, contrarian signal
- Open Interest: Saturation level, cascade risk

**Options Analysis (BTC/ETH only):**
- Max Pain: Current strike, gravitational pull
- Put/Call Ratio: Sentiment reading
- IV Term Structure: Contango/backwardation, volatility expectations
- Gamma Exposure: Dealer positioning, volatility impact

**Liquidation Risk:**
- Nearest liquidation clusters
- Imbalance direction (long vs short)
- Cascade probability assessment

**Output Format:**
```
POSITIONING: [CROWDED LONG/CROWDED SHORT/BALANCED]

Perpetuals:
- Funding: X.XX% annualized ([assessment])
- L/S Ratio: X.XX ([signal])
- OI: $XXB ([vs historical])

Options (if applicable):
- Max Pain: $XX,XXX
- Put/Call: X.XX ([sentiment])
- IV 1M: XX% ([term structure])

Liquidation Risk: [HIGH/MEDIUM/LOW]
- Nearest longs: $XX,XXX ($XXM at risk)
- Nearest shorts: $XX,XXX ($XXM at risk)
```

---

### 4. CATALYST ANALYSIS

**Near-Term (0-30 days):**
- Options expirations with size
- Protocol events (upgrades, governance)
- Macro data releases (FOMC, CPI, employment)

**Medium-Term (30-90 days):**
- Regulatory decisions with Polymarket odds
- ETF flow trends
- Major unlock schedules

**Court Cases / Regulatory:**
- Active cases affecting the asset
- Key hearing dates
- Probability-weighted outcomes

**Output Format:**
```
CATALYST CALENDAR:

Near-Term (0-30d):
- [Date]: [Event] | Impact: [High/Med/Low]
- [Date]: [Event] | Impact: [High/Med/Low]

Medium-Term (30-90d):
- [Date]: [Event] | Impact: [High/Med/Low] | Probability: XX%

Regulatory:
- [Case/Decision]: [Status] | Timeline: [Date] | Probability: XX%
```

---

### 5. VALUATION MODELS

Provide probability-weighted scenarios based on:
- Macro regime (Banana Zone status)
- On-chain health (MVRV regime)
- Derivatives positioning
- Sentiment extremes

**Output Format:**
```
SCENARIO ANALYSIS:

BULL CASE (XX% probability):
- Trigger: [What needs to happen]
- On-chain: MVRV reaches X.X, NUPL enters [phase]
- Target: $XX,XXX (+XX% from current)

BASE CASE (XX% probability):
- Assumptions: [Key assumptions]
- On-chain: MVRV stays X.X-X.X range
- Target: $XX,XXX (+/-XX% from current)

BEAR CASE (XX% probability):
- Trigger: [What could go wrong]
- On-chain: MVRV falls to X.X, NUPL enters [phase]
- Target: $XX,XXX (-XX% from current)

EXPECTED VALUE: $XX,XXX (probability-weighted)
```

---

### 6. RISK ASSESSMENT

**Systematic Risks:**
- Macro correlation (BTC beta to SPX/QQQ)
- Liquidity conditions (Fed, M2, TGA)
- Regulatory environment

**Idiosyncratic Risks:**
- Asset-specific vulnerabilities (apply asset framework)
- Concentration risk (whale holdings, exchange balances)
- Technical risk (support/resistance levels)

**Position Sizing Guidance:**
```
Risk Score: X/10

Recommended Allocation:
- Risk Score 1-3: Up to 5% portfolio
- Risk Score 4-6: Up to 3% portfolio
- Risk Score 7-10: Up to 1% portfolio

Key Invalidation Levels:
- Stop consideration: $XX,XXX (-XX%)
- Full exit: $XX,XXX (-XX%)
```

---

### 7. MACRO REGIME CONTEXT

**Banana Zone Assessment:**
- Score: X/100
- Signal: [ACTIVE/BUILDING/INACTIVE]
- Components: Sentiment, M2, FCI, Cycle

**Financial Conditions:**
- FCI Proxy: [LOOSENING/TIGHTENING/NEUTRAL]
- Components: VIX, HY OAS, Yield Curve

**Liquidity Cycle:**
- M2 YoY: +X.X%
- Fed Balance Sheet: [direction]
- Net Liquidity: [direction]

**Cross-Asset Signals:**
- Gold-BTC divergence: [signal]
- BTC/SPX correlation: X.XX
- Hurdle rate assessment: [beating/lagging] 8% debasement

**Output Format:**
```
MACRO REGIME: [RISK-ON/RISK-OFF/TRANSITIONAL]

Banana Zone: XX/100 ([signal])
FCI Direction: [LOOSENING/TIGHTENING]
Liquidity: [EXPANDING/CONTRACTING]

Cycle Position: [phase] of debt cycle (~XX% complete)
Lead Indicators: [What they're signaling]
```

---

### 8. TECHNICAL & SENTIMENT SYNTHESIS

**Technical Analysis:**
- Trend: RSI, MACD direction
- Key Levels: Major support/resistance
- Moving Averages: 50/200 SMA positioning

**Sentiment Analysis:**
- Fear & Greed Index: Score and regime
- Social Sentiment: Bullish/bearish ratio
- Contrarian Signals: Extreme readings

**Smart Money:**
- Top trader positioning
- Institutional flows (ETF, treasuries)
- Whale behavior

**Final Synthesis:**
```
TECHNICAL: [BULLISH/BEARISH/NEUTRAL]
SENTIMENT: [BULLISH/BEARISH/NEUTRAL] (contrarian: [signal])
SMART MONEY: [ACCUMULATING/DISTRIBUTING/NEUTRAL]

OVERALL SYNTHESIS:
[3-4 sentence summary combining all signals into cohesive view]

ACTIONABLE TAKEAWAY:
[1-2 sentences on what to do with this information]
```

---

## Signal Aggregation Framework

When determining directional bias, weight signals as follows:

| Signal Category | Weight | Bullish Trigger | Bearish Trigger |
|-----------------|--------|-----------------|-----------------|
| On-chain Health | 30% | MVRV < 2.0, NUPL < 0.5 | MVRV > 3.0, NUPL > 0.75 |
| Macro Regime | 25% | Banana Zone active, FCI loosening | Banana Zone inactive, FCI tightening |
| Derivatives | 20% | Negative funding, L/S < 1.0 | High funding, L/S > 2.0 |
| Sentiment | 15% | Extreme fear (contrarian) | Extreme greed (contrarian) |
| Technical | 10% | Above key MAs, RSI < 70 | Below key MAs, RSI > 70 |

**Scoring:**
- Calculate weighted score (0-1 scale)
- Score > 0.6 = BULLISH
- Score < 0.4 = BEARISH
- Score 0.4-0.6 = NEUTRAL

---

## Professional Standards

### Language Guidelines
- Use institutional terminology (basis points, delta exposure, realized value)
- Quantify everything - avoid vague terms like "high" or "significant"
- State confidence levels for probabilistic statements
- Cite specific metrics and thresholds

### Formatting Requirements
- Use tables for multi-dimensional data
- Include specific numbers, not ranges (unless uncertainty is high)
- Date all time-sensitive analysis
- Clearly separate facts from interpretation

### Disclaimer
Include at end of every report:
```
---
DISCLAIMER: This analysis is for informational purposes only and does not
constitute financial advice. Cryptocurrency investments carry significant
risk. Past performance does not guarantee future results. Always conduct
your own research before making investment decisions.
```
