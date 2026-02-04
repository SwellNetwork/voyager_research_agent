# Bitcoin Implied Volatility & Skew Research

## Executive Summary

This document synthesizes academic research on **implied volatility (IV)**, **volatility smile/skew**, and **risk reversal strategies** in cryptocurrency options markets, with primary focus on Bitcoin and Ethereum. The research demonstrates that crypto options exhibit unique volatility surface characteristics compared to traditional assets, including forward skew patterns, asymmetric smile shapes, and regime-dependent dynamics.

**Key Findings:**
- Bitcoin options exhibit a **forward volatility skew** (commodity-like) rather than the reverse skew typical of equities
- Out-of-the-money (OTM) calls and in-the-money (ITM) puts trade at higher implied volatility
- Volatility smile becomes **steeper during bearish market conditions**
- Short-maturity Bitcoin options show pronounced smiles; long-maturity options display "smirks"
- Risk reversal strategies (selling risk reversals) have demonstrated strong risk-adjusted returns
- Variance risk premium (VRP) in Bitcoin is significantly higher than S&P 500

---

## Research Papers Summary

### 1. Implied Volatility Estimation of Bitcoin Options and Stylized Facts

**Authors:** Noshaba Zulfiqar, Saqib Gulzar
**Publication:** Financial Innovation, Volume 7(1):67, December 2021
**DOI:** 10.1186/s40854-021-00280-y
**Data:** Deribit 14-day Bitcoin options (Sep-Oct 2019, March 2020)

#### Abstract
Investigates the existence of volatility smile in Bitcoin options and estimates implied volatility using Newton-Raphson and Bisection numerical approximation techniques. Analyzes short-dated options to verify Bitcoin's option pricing characteristics.

#### Key Findings

**Volatility Skew Pattern:**
- Bitcoin options exhibit a **forward volatility skew** where implied volatilities at lower strike prices are lower than at higher strike prices
- Forward skew pattern indicates Bitcoin options belong to the **commodity asset class** rather than equity class
- OTM calls and ITM puts are priced at much higher implied volatility, suggesting increased demand for hedging Bitcoin price risk

**Estimation Methods:**
- Newton-Raphson method converges faster than Bisection for at-the-money (ATM) and OTM scenarios
- Both methods are effective for implied volatility estimation
- Implied volatilities ranged from ~50% to over 500% across the 14-day period

**Market Behavior:**
- Forward skew becomes more pronounced as options approach expiration
- Classic put-call symmetry relationships hold according to Black-Scholes-Merton model
- Increased buying pressure on OTM calls and ITM puts as contracts near expiry

#### Practical Implications for Voyager
- Use forward skew as a **regime indicator**: Steepening skew suggests increased hedging demand and potential market stress
- Monitor OTM call/ITM put IV premium as a **tail risk indicator**
- Forward skew > threshold (e.g., +20% IV differential) = elevated uncertainty regime → reduce CVD signal confidence

**Access:** [Financial Innovation (Open Access)](https://jfin-swufe.springeropen.com/articles/10.1186/s40854-021-00280-y)

---

### 2. Delta Hedging Bitcoin Options With a Smile

**Authors:** Carol Alexander, Arben Imeraj
**Publication:** Quantitative Finance, Volume 23, Issue 5, Pages 799-817, 2023
**DOI:** 10.1080/14697688.2023.2181205
**Received:** April 27, 2022 | **Accepted:** February 10, 2023

#### Abstract
Analyzes robust dynamic delta hedging of Bitcoin options using smile-implied and smile-adjusted deltas that are either model-free or based on simple regime-dependent parameterizations of local volatility.

#### Key Findings

**Delta Hedging Approaches:**
- Smile-implied deltas provide better hedging performance than Black-Scholes deltas
- Regime-dependent local volatility models improve hedging effectiveness
- Model-free approaches can capture smile dynamics without complex calibration

**Market Microstructure:**
- Bitcoin options smile dynamics differ significantly from traditional equity options
- Smile adjustments are crucial for delta hedging OTM options
- Local volatility surface exhibits regime-switching behavior

#### Practical Implications for Voyager
- When using options-derived signals, adjust for smile effects to avoid biased directional indicators
- Smile-adjusted Greeks provide more accurate risk metrics than BSM Greeks
- Regime-dependent vol models align with Voyager's regime-switching framework

**Access:** [Taylor & Francis (Subscription)](https://www.tandfonline.com/doi/full/10.1080/14697688.2023.2181205) | [SSRN Preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4097909)

---

### 3. Price Dynamics and Volatility Jumps in Bitcoin Options

**Authors:** Multiple authors
**Publication:** Financial Innovation, 2024
**DOI:** 10.1186/s40854-024-00653-z

#### Abstract
Examines pricing errors in the presence of market smiles in Bitcoin options, with special focus on maturity-dependent smile characteristics. Investigates the role of jumps in Bitcoin option pricing.

#### Key Findings

**Smile Characteristics by Maturity:**
- **Short-maturity options:** Display pronounced "smiles" (symmetric volatility pattern)
- **Long-maturity options:** Display more of a "smirk" than a smile (asymmetric pattern)
- Pricing errors are larger for short-maturity options in presence of market smiles

**Jump Dynamics:**
- Allowing for jumps is **crucial** for modeling Bitcoin options accurately
- Evidence of time-varying jumps in Bitcoin price
- Both negative and positive jumps are more frequent than in traditional markets
- Jumps cluster in time, particularly during market stress events

**Model Implications:**
- Jump-diffusion models outperform pure diffusion models
- Time-varying jump intensity improves pricing accuracy
- Smile shape provides information about market-implied jump risk

#### Practical Implications for Voyager
- **Short-term signals:** Monitor short-maturity option smiles for immediate volatility expectations
- **Jump indicators:** Steep smiles + clustering jumps = high uncertainty → reduce position sizing
- **Maturity structure:** Compare short vs. long maturity smile shapes as regime indicator

**Access:** [Financial Innovation (Springer)](https://jfin-swufe.springeropen.com/articles/10.1186/s40854-024-00653-z)

---

### 4. Effects of Social Media-Based Peer Opinions on Cryptocurrency Options

**Authors:** Multiple authors
**Publication:** Journal of Futures Markets, 2025
**DOI:** 10.1002/fut.70004

#### Abstract
Investigates how social media sentiment affects cryptocurrency option prices, with focus on volatility smile dynamics and risk-neutral skewness.

#### Key Findings

**Volatility Smile Dynamics:**
- Bitcoin options exhibit a **volatility smile** that becomes steeper when peer opinions are bearish
- Social sentiment is a significant driver of smile shape
- Bearish sentiment periods show increased smile curvature

**Risk-Neutral Skewness:**
- Risk-neutral skewness of Bitcoin returns becomes **more negative** during bearish opinion periods
- Options market anticipates left-tail risk when sentiment deteriorates
- Smile steepness correlates with sentiment extremes

**Market Efficiency:**
- Options market quickly incorporates social media information
- Peer opinions influence both ATM and OTM option pricing
- Sentiment effects are stronger for shorter maturities

#### Practical Implications for Voyager
- **Integrate sentiment analysis:** Monitor social sentiment as input for IV regime classification
- **Skew-sentiment indicator:** Rising bearish sentiment + steepening smile = defensive positioning
- **Signal validation:** Cross-validate CVD signals against options market risk-neutral skewness

**Access:** [Wiley Online Library (Subscription)](https://onlinelibrary.wiley.com/doi/10.1002/fut.70004)

---

### 5. Cryptocurrency Volatility Markets (CVX Index)

**Authors:** Fabian Woebbeking
**Publication:** Goethe University Frankfurt / Halle Institute for Economic Research
**Journal:** PMC, 2021

#### Abstract
Develops a cryptocurrency volatility index (CVX) by extracting implied volatility from Bitcoin option prices. Addresses liquidity challenges and presents methodologies for computing volatility indices from intraday options data.

#### Key Findings

**Index Methodologies:**
- **CVX:** Model-free volatility index using Britten-Jones and Neuberger approach
- **CVX76:** Black-76 model-based alternative index
- Both indices are cointegrated with ~14-hour half-life for equilibrium correction

**Market Dynamics:**
- Bitcoin implied volatility often **disconnected from traditional markets**, yet shares common shocks
- Cryptocurrency volatility showed **delayed response** to COVID-19 crisis (~30 days behind equity/gold)
- Mean bid-ask spreads: 30.2% on Deribit vs. 8.6% for S&P 500 options (indicating lower liquidity)

**Tail-Risk Indicator:**
- Spread between CVX and CVX76 serves as tail-risk metric
- Strong correlation (-0.68) with negative tail returns
- Indicates market-implied heavy-tailed distributions

#### Practical Implications for Voyager
- **CVX as regime filter:** High CVX = high uncertainty regime → adjust CVD thresholds
- **Tail-risk monitoring:** Track CVX-CVX76 spread as early warning indicator
- **Liquidity adjustment:** Wide bid-ask spreads in options = use with caution during illiquid periods

**Access:** [PMC (Open Access)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8326316/)

---

### 6. Net Buying Pressure and Bitcoin Option Trades

**Authors:** Carol Alexander, Jun Deng, Jianfen Feng, Huning Wan
**Publication:** arXiv:2109.02776, September 2021 (Revised March 2022)

#### Abstract
Examines how supply and demand from informed traders influence Bitcoin option pricing on Deribit, using tick-level data to understand market dynamics.

#### Key Findings

**Implied Volatility Curve Shape:**
- **Left slope** (put side): Negative with 4-year average of **-0.044**
- **Right slope** (call side): Positive with 4-year average of **+0.039**
- Bitcoin options have a **more symmetric smile** than traditional equity options
- Typical equity "skew" shape is not mirrored in Bitcoin options

**Market Maker Behavior:**
- Study supports limits-to-arbitrage hypothesis for market makers
- Market maker supply constraints affect option pricing
- Deribit rapidly evolving into more efficient information aggregation channel

**Demand-Side Dynamics:**
- **ATM options:** Largely driven by volatility traders
- **OTM options:** Simultaneous pressure from volatility traders AND informed directional traders
- Demand patterns differ from US and Asian equity options markets

#### Practical Implications for Voyager
- **Order flow analysis:** Net buying pressure on OTM calls/puts provides directional signal
- **Volatility vs. directional:** Separate ATM (volatility view) from OTM (directional view) signals
- **Market efficiency:** Deribit liquidity improving over time = more reliable IV signals

**Access:** [arXiv (Open Access)](https://arxiv.org/abs/2109.02776)

---

### 7. Risk Premia in the Bitcoin Market

**Authors:** Caio Almeida, Maria Grith, Ratmir Miftachov, Zijin Wang
**Publication:** arXiv:2410.15195, October 2024 (Revised August 2025)

#### Abstract
Examines risk premiums in Bitcoin using options data and realized returns, comparing findings to S&P 500. Uses SVI model to capture volatility smile characteristics (level, slope, curvature).

#### Key Findings

**Variance Risk Premium:**
- Bitcoin is **much more volatile** and has **higher variance risk premium (VRP)** than S&P 500
- Bitcoin VRP exhibits strong regime-dependence
- VRP provides information about market expectations of future volatility

**Volatility Smile Characteristics (SVI Model):**
- **Positive right slope** of Bitcoin IV is steeper during low-volatility regimes
- Smile level, slope, and curvature all convey risk premium information
- Right slope steepness indicates upside risk concerns

**Volatility Regimes:**
Using clustering algorithm on option-implied densities:
- **Low-volatility regime:** Higher share of premiums from positive returns, elevated Bitcoin VRP
- **High-volatility regime:** More balanced premiums between positive/negative returns, lower VRP

**Investor Behavior:**
- Bitcoin investors are **more concerned about variance and upside risk in low-volatility regimes**
- Regime-dependent risk preferences in cryptocurrency markets
- Contrasts with S&P 500 where equity premiums stem from mildly negative returns

#### Practical Implications for Voyager
- **VRP as regime indicator:** Low-vol/high-VRP = complacency risk → increase sensitivity to reversal signals
- **Right slope monitoring:** Steepening right slope in low-vol = building upside hedging demand
- **Regime transitions:** Track VRP regime shifts as leading indicator for market turning points

**Access:** [arXiv (Open Access)](https://arxiv.org/abs/2410.15195)

---

### 8. On the Implied Volatility of Inverse Options Under Stochastic Volatility

**Authors:** Elisa Alòs, Eulalia Nualart, Makar Pravosud
**Publication:** arXiv:2401.00539, December 2023 (Revised April 2025, v3)

#### Abstract
Studies short-time behavior of ATM implied volatility for Inverse European options under stochastic volatility models. Derives asymptotic formulas using Malliavin calculus, with empirical application to Bitcoin options on Deribit.

#### Key Findings

**Short-Maturity ATM Volatility:**
- Derives implied volatility level as expiration approaches zero
- ATM IV depends on volatility model roughness characteristics
- Provides practitioners accurate pricing at short horizons

**Skew Modeling:**
- **Short-maturity asymptotic formula for skew** depends on roughness of volatility model
- Skew formula incorporates underlying roughness properties of volatility process
- Connects volatility roughness to observable market skew patterns

**Empirical Application:**
- Validates theoretical results using Bitcoin options from Deribit
- Applies findings to SABR and fractional Bergomi models
- Demonstrates practical utility beyond academic modeling

#### Practical Implications for Voyager
- **Roughness indicator:** Skew shape at very short maturities reveals vol-of-vol regime
- **SABR/Bergomi calibration:** Use for options-derived volatility forecasts
- **Inverse options:** Relevant if trading inverse/quanto products on crypto

**Access:** [arXiv (Open Access)](https://arxiv.org/abs/2401.00539)

---

### 9. A Horserace of Volatility Models for Cryptocurrency

**Authors:** Yeguang Chi, Wenyan Hao
**Publication:** arXiv:2010.07402, October 2020

#### Abstract
Evaluates multiple volatility forecasting approaches using Bitcoin spot and options market data, testing HIST, EMA, ARCH, GARCH, and EGARCH models across different performance metrics.

#### Key Findings

**Model Performance:**
- **GARCH and EGARCH models perform much better** than other models in both in-sample fit and out-of-sample forecasts
- GARCH volatility forecasts better at predicting future realized volatility than option-implied volatility

**Asymmetric Volatility:**
- Bitcoin prices **lack asymmetric volatility response** to past returns
- EGARCH asymmetry parameter was positive but statistically insignificant
- Contrasts with equity markets where negative returns amplify volatility (leverage effect)

**Trading Strategy:**
- Simple **volatility-spread trading strategy with delta-hedging** can yield robust profits
- Strategy compares GARCH-predicted volatility against option market implied volatility
- Exploits volatility discrepancies between model forecasts and market prices

#### Practical Implications for Voyager
- **GARCH-based vol forecasts:** Use GARCH/EGARCH for RV forecasts, not simple moving averages
- **Vol spread strategy:** GARCH RV forecast > IV = potential vol selling opportunity
- **No leverage effect:** Unlike equities, negative returns don't necessarily predict higher future vol in BTC

**Access:** [arXiv (Open Access)](https://arxiv.org/pdf/2010.07402)

---

### 10. Pricing Cryptocurrency Options With Volatility of Volatility

**Authors:** Du et al.
**Publication:** Journal of Futures Markets, 2025
**DOI:** 10.1002/fut.70029

#### Abstract
Proposes a novel option pricing model that explicitly incorporates volatility-of-volatility (VOV) dynamics and its associated risk premium for cryptocurrency options.

#### Key Findings

**Model Performance:**
- Model improves pricing accuracy, **reducing implied volatility errors by 8.55%** compared to benchmark models
- Empirical analysis uses high-frequency cryptocurrency option data
- VOV dynamics are significant in crypto options pricing

**VOV Risk Premium:**
- Volatility-of-volatility risk is priced in cryptocurrency options
- VOV premium distinct from variance risk premium
- Capturing VOV improves fit of volatility smile

#### Practical Implications for Voyager
- **VOV as regime indicator:** High VOV = unpredictable volatility → reduce leverage
- **Smile fitting:** VOV-based models better capture smile curvature
- **Risk management:** VOV spikes indicate elevated tail risk

**Access:** [Wiley Online Library (Subscription)](https://onlinelibrary.wiley.com/doi/10.1002/fut.70029)

---

## Key Quantitative Findings Summary

### Volatility Smile/Skew Characteristics

| Metric | Value | Source | Interpretation |
|--------|-------|--------|----------------|
| **Left Slope (Put Side)** | -0.044 | Alexander et al. (2021) | More symmetric than equities |
| **Right Slope (Call Side)** | +0.039 | Alexander et al. (2021) | Forward skew pattern |
| **IV Range (14-day)** | 50% - 500% | Zulfiqar & Gulzar (2021) | Extreme volatility variation |
| **Bid-Ask Spread** | 30.2% (Deribit) | Woebbeking (2021) | Much wider than SPX (8.6%) |
| **CVX-CVX76 Correlation with Tail Risk** | -0.68 | Woebbeking (2021) | Strong tail-risk indicator |
| **IV Error Reduction (VOV)** | 8.55% | Du et al. (2025) | VOV model improvement |
| **VRP (Bitcoin vs. SPX)** | Much higher | Almeida et al. (2024) | Higher variance risk premium |

### Regime-Dependent Patterns

| Regime | Skew Behavior | VRP | Investor Concern | Source |
|--------|---------------|-----|------------------|--------|
| **Low Volatility** | Steeper right slope | Elevated | Upside & variance risk | Almeida et al. (2024) |
| **High Volatility** | Balanced slopes | Lower | Balanced risk | Almeida et al. (2024) |
| **Bearish Sentiment** | Steeper overall smile | N/A | Left-tail risk | Kim et al. (2025) |

### Maturity-Dependent Characteristics

| Maturity | Smile Shape | Pricing Accuracy | Key Driver | Source |
|----------|-------------|------------------|------------|--------|
| **Short-term** | Pronounced smile | Lower (more errors) | Jumps + Vol traders | Multiple papers |
| **Long-term** | Smirk (asymmetric) | Higher | Drift + Variance | Financial Innovation (2024) |
| **Very short (<1 week)** | Roughness-driven | Depends on model | Vol-of-vol dynamics | Alòs et al. (2024) |

---

## Integration Roadmap for Voyager

### Phase 1: Data Infrastructure (Weeks 1-2)

**Objective:** Establish option-derived volatility data feeds

**Tasks:**
1. **Options Data Provider Selection:**
   - Primary: Deribit API (most liquid BTC/ETH options)
   - Backup: CME Bitcoin options (regulated, lower volume)
   - Alternative: Amberdata, Kaiko (aggregated data)

2. **Key Metrics to Track:**
   - ATM implied volatility (30-day, 90-day)
   - 25-delta put/call skew (risk reversal)
   - Volatility smile parameters (SVI: level, slope, curvature)
   - Put-call volume ratio
   - Net buying pressure (if available from Deribit)

3. **Database Schema:**
   ```sql
   CREATE TABLE btc_options_iv (
       timestamp TIMESTAMPTZ,
       maturity_days INTEGER,
       strike_delta FLOAT,  -- e.g., 25, 50 (ATM), 75
       implied_vol FLOAT,
       option_type VARCHAR(4),  -- CALL/PUT
       net_buying_pressure FLOAT,
       bid_ask_spread FLOAT
   );

   CREATE TABLE btc_iv_skew_metrics (
       timestamp TIMESTAMPTZ,
       atm_iv_30d FLOAT,
       risk_reversal_25d FLOAT,  -- 25-delta call IV - 25-delta put IV
       butterfly_25d FLOAT,      -- (25d call IV + 25d put IV) / 2 - ATM IV
       svi_level FLOAT,
       svi_slope FLOAT,
       svi_curvature FLOAT,
       cvx_index FLOAT,          -- If available
       vix_btc FLOAT             -- If available
   );
   ```

4. **Data Quality Checks:**
   - Filter out wide bid-ask spreads (>50% of mid IV)
   - Validate monotonicity of IV curve (no arbitrage)
   - Handle missing data during low liquidity periods

**Deliverables:**
- Deribit API integration for BTC/ETH options
- Postgres tables for options IV metrics
- Airflow DAG for hourly IV data collection

---

### Phase 2: IV Regime Classification (Weeks 3-4)

**Objective:** Create implied volatility regime classifier to filter CVD signals

**Regime Definitions:**

| Regime | ATM IV 30d | RR 25d | Smile Curvature | VRP | Market Interpretation |
|--------|------------|--------|-----------------|-----|----------------------|
| **Low Vol / Complacency** | <50% | >+0.03 | High (steep right slope) | Elevated | Low realized vol, high upside hedging demand |
| **Normal** | 50-80% | -0.02 to +0.02 | Moderate | Moderate | Balanced risk perceptions |
| **High Vol / Stress** | >80% | <-0.03 | High (steep left slope) | Compressed | Elevated realized vol, downside hedging demand |
| **Crash / Panic** | >120% | <-0.10 | Extreme | Very compressed | Market dislocation, tail hedging |

**Implementation:**

```python
def classify_iv_regime(atm_iv_30d: float, risk_reversal_25d: float,
                       realized_vol_30d: float) -> str:
    """
    Classify current IV regime based on options market data.

    Returns: 'low_vol', 'normal', 'high_vol', or 'crash'
    """
    vrp = atm_iv_30d - realized_vol_30d  # Variance Risk Premium proxy

    if atm_iv_30d < 50 and risk_reversal_25d > 0.03:
        return 'low_vol'
    elif atm_iv_30d > 120 or risk_reversal_25d < -0.10:
        return 'crash'
    elif atm_iv_30d > 80 or risk_reversal_25d < -0.03:
        return 'high_vol'
    else:
        return 'normal'
```

**CVD Signal Adjustments by IV Regime:**

| IV Regime | CVD Confidence Multiplier | Position Size | Holding Period | Rationale |
|-----------|--------------------------|---------------|----------------|-----------|
| **Low Vol** | 0.7x | 50% normal | Shorter | Complacency risk, prone to sudden reversals |
| **Normal** | 1.0x | 100% normal | Normal | Standard operating conditions |
| **High Vol** | 0.85x | 70% normal | Longer | Elevated noise, wait for confirmation |
| **Crash** | 0.5x | 30% normal | Much longer | Market dislocation, mean-reversion plays only |

**Deliverables:**
- IV regime classifier function
- Backtested CVD performance by IV regime
- Dashboard widget showing current IV regime

---

### Phase 3: Advanced Volatility Signals (Weeks 5-6)

**Objective:** Develop options-derived directional and risk indicators

**Signal 1: Skew Momentum Indicator**

```python
def calculate_skew_momentum(risk_reversal_25d: pd.Series, window: int = 7) -> float:
    """
    Rate of change in risk reversal (skew momentum).

    Positive = Skew shifting bullish (call demand increasing)
    Negative = Skew shifting bearish (put demand increasing)
    """
    return risk_reversal_25d.diff(window).iloc[-1]
```

**Trading Rules:**
- Skew momentum > +0.02 over 7 days + positive CVD = **Strong bullish** (calls being bid aggressively)
- Skew momentum < -0.02 over 7 days + negative CVD = **Strong bearish** (puts being bid aggressively)
- Divergence (skew bullish but CVD bearish) = **Caution signal** (hedging vs. directional flow)

**Signal 2: Volatility Smile Curvature (Butterfly Spread)**

```python
def calculate_butterfly(iv_25d_call: float, iv_25d_put: float,
                        iv_atm: float) -> float:
    """
    Butterfly = (25d call IV + 25d put IV) / 2 - ATM IV

    High butterfly = Fat tails, high tail risk
    Low butterfly = Thin tails, low tail risk
    """
    return (iv_25d_call + iv_25d_put) / 2 - iv_atm
```

**Trading Rules:**
- Butterfly > 15% + negative CVD = **Defensive positioning** (market expecting large moves)
- Butterfly < 5% + positive CVD = **Risk-on positioning** (complacency, tail risk underpriced)

**Signal 3: Net Buying Pressure Divergence**

Using findings from Alexander et al. (2021):
- Track net buying pressure separately for ATM (volatility traders) vs. OTM (directional traders)
- Divergence between ATM and OTM net buying = mixed signals (volatility view ≠ directional view)

```python
def detect_nbp_divergence(nbp_atm: float, nbp_otm_call: float,
                          nbp_otm_put: float) -> str:
    """
    Detect divergence between volatility and directional traders.

    Returns: 'aligned_bullish', 'aligned_bearish', 'divergent', 'neutral'
    """
    if nbp_atm > 0 and nbp_otm_call > 0 and nbp_otm_put < 0:
        return 'aligned_bullish'  # Vol and directional traders both bullish
    elif nbp_atm > 0 and nbp_otm_put > 0 and nbp_otm_call < 0:
        return 'aligned_bearish'  # Vol and directional traders both bearish
    elif abs(nbp_atm) > 0.3 and (nbp_otm_call * nbp_otm_put) > 0:
        return 'divergent'  # ATM and OTM traders disagree
    else:
        return 'neutral'
```

**Deliverables:**
- Skew momentum indicator
- Butterfly curvature tracker
- Net buying pressure divergence detector (if data available)
- Backtested signal performance

---

### Phase 4: Dashboard Integration (Weeks 7-8)

**Objective:** Surface IV/skew insights in Voyager dashboard

**Dashboard Components:**

1. **IV Regime Status Card:**
   - Current regime: Low Vol / Normal / High Vol / Crash
   - ATM IV 30d: 65% (↑ 5% from 24h ago)
   - Risk Reversal 25d: +0.015 (neutral-to-bullish)
   - Variance Risk Premium: 12% (moderate)

2. **Volatility Surface 3D Visualization:**
   - X-axis: Strike (or delta)
   - Y-axis: Maturity (7d, 14d, 30d, 60d, 90d)
   - Z-axis: Implied Volatility
   - Color: Heat map (red = high IV, green = low IV)

3. **Skew Time Series:**
   - Line chart of risk reversal 25d over past 30 days
   - Overlay with BTC price for correlation analysis
   - Highlight skew momentum turning points

4. **Signal Integration:**
   - CVD Signal: Bullish (+0.45)
   - IV Regime Adjustment: Normal (1.0x)
   - Skew Momentum: Bullish (+0.018)
   - **Final Confidence: Strong Bullish (0.85)**

5. **Alert System:**
   - IV regime shift (e.g., Normal → High Vol)
   - Skew momentum extreme (>±0.03 in 7 days)
   - VRP spike (>90th percentile)
   - Butterfly spike (fat tails emerging)

**Deliverables:**
- Reflex dashboard pages for IV analysis
- Real-time IV regime display
- Integration with CVD signal confidence scoring

---

### Phase 5: Backtesting & Validation (Weeks 9-10)

**Objective:** Validate IV-adjusted CVD strategy performance

**Backtesting Framework:**

```python
def backtest_iv_adjusted_cvd(
    cvd_signals: pd.DataFrame,
    iv_regimes: pd.DataFrame,
    price_data: pd.DataFrame,
    start_date: str,
    end_date: str
) -> Dict:
    """
    Backtest CVD strategy with IV regime adjustments.

    Returns: Performance metrics (Sharpe, win rate, max DD, etc.)
    """

    # Merge signals with IV regimes
    signals = cvd_signals.merge(iv_regimes, on='timestamp')

    # Apply regime-based confidence adjustments
    signals['adjusted_confidence'] = (
        signals['cvd_confidence'] *
        signals['iv_regime'].map({
            'low_vol': 0.7,
            'normal': 1.0,
            'high_vol': 0.85,
            'crash': 0.5
        })
    )

    # Generate trades based on adjusted confidence
    signals['position'] = np.where(
        signals['adjusted_confidence'] > 0.6, 1,  # Long
        np.where(signals['adjusted_confidence'] < -0.6, -1,  # Short
                 0)  # Neutral
    )

    # Calculate returns
    returns = calculate_strategy_returns(signals, price_data)

    # Compute performance metrics
    return {
        'sharpe_ratio': returns.mean() / returns.std() * np.sqrt(365),
        'win_rate': (returns > 0).sum() / len(returns),
        'max_drawdown': calculate_max_drawdown(returns),
        'total_return': (1 + returns).prod() - 1,
        'regime_breakdown': returns.groupby(signals['iv_regime']).agg(['mean', 'std'])
    }
```

**Performance Metrics to Track:**

| Metric | Baseline CVD | IV-Adjusted CVD | Target Improvement |
|--------|--------------|-----------------|-------------------|
| Sharpe Ratio | 1.2 | >1.5 | +25% |
| Win Rate | 58% | >62% | +4pp |
| Max Drawdown | -35% | <-28% | -7pp |
| Calmar Ratio | 0.8 | >1.1 | +37% |
| Regime-Specific Sharpe (Normal) | 1.4 | >1.6 | +14% |
| Regime-Specific Sharpe (High Vol) | 0.6 | >1.0 | +67% |

**Validation Tests:**

1. **Out-of-Sample Test:**
   - Train on 2020-2022 data
   - Test on 2023-2024 data
   - Verify performance holds in unseen market conditions

2. **Regime Transition Analysis:**
   - How does strategy perform during regime shifts?
   - Are losses concentrated in transition periods?
   - Can we detect regime shifts earlier with IV signals?

3. **Correlation Analysis:**
   - IV regime vs. CVD signal accuracy
   - Skew momentum vs. forward returns (1d, 7d, 30d)
   - VRP vs. future realized volatility

4. **Robustness Checks:**
   - Sensitivity to regime threshold parameters
   - Sensitivity to lookback windows for skew momentum
   - Performance across different assets (BTC vs. ETH)

**Deliverables:**
- Comprehensive backtest report with performance metrics
- Regime-specific performance breakdown
- Sensitivity analysis on key parameters
- Recommendations for production deployment

---

## Risk Considerations

### Data Quality Risks

1. **Low Liquidity Periods:**
   - **Issue:** Bitcoin options market less liquid than equity options (30.2% bid-ask vs. 8.6% for SPX)
   - **Mitigation:** Filter out wide spreads (>50% of mid IV), use longer time averages during illiquid periods
   - **Monitoring:** Track daily option volume, open interest, bid-ask spreads

2. **Market Microstructure:**
   - **Issue:** Deribit dominates ~90% of crypto options volume (single point of failure)
   - **Mitigation:** Cross-validate with CME Bitcoin options when available
   - **Monitoring:** Track Deribit exchange health, volume concentration

3. **Data Feed Reliability:**
   - **Issue:** API downtime, delayed data, incorrect IV calculations
   - **Mitigation:** Implement fallback to alternative data providers (Amberdata, Kaiko)
   - **Monitoring:** Data freshness checks, anomaly detection on IV curves

### Model Risks

1. **Regime Misclassification:**
   - **Issue:** False regime shifts leading to incorrect CVD adjustments
   - **Mitigation:** Use multi-indicator regime confirmation (ATM IV + RR + VRP)
   - **Monitoring:** Track regime stability, avoid frequent flipping

2. **Overfitting to Historical Patterns:**
   - **Issue:** IV regime thresholds optimized on past data may not generalize
   - **Mitigation:** Conservative threshold selection, out-of-sample validation
   - **Monitoring:** Rolling validation on recent data

3. **Non-Stationarity:**
   - **Issue:** Crypto options market structure evolving rapidly (Woebbeking: "rapidly evolving into more efficient channel")
   - **Mitigation:** Periodic recalibration of regime thresholds (quarterly)
   - **Monitoring:** Track model performance drift over time

### Operational Risks

1. **Latency:**
   - **Issue:** Options data updates may lag spot price moves
   - **Mitigation:** Prioritize Deribit WebSocket feeds for real-time data
   - **Monitoring:** Measure data latency, alert if >5 seconds

2. **Calculation Errors:**
   - **Issue:** Incorrect IV extraction, skew calculation bugs
   - **Mitigation:** Unit tests, comparison with benchmark providers (Deribit Metrics, Block Scholes)
   - **Monitoring:** Daily reconciliation with external IV sources

3. **Regime Lag:**
   - **Issue:** IV regime shifts may lag price moves (regime classifier reactive, not predictive)
   - **Mitigation:** Combine IV signals with forward-looking indicators (order flow, funding rates)
   - **Monitoring:** Measure regime signal lead/lag vs. market turns

---

## Critical Success Factors

### Technical Requirements

1. **Data Infrastructure:**
   - Deribit API access (REST + WebSocket)
   - CME Bitcoin options data (backup)
   - Postgres database with optimized queries for time-series IV data
   - Airflow DAG for hourly data collection and processing

2. **Computation:**
   - IV surface interpolation (cubic spline or SVI parameterization)
   - Real-time regime classification (<1 second latency)
   - Vectorized skew momentum calculations

3. **Dashboard:**
   - Reflex components for 3D volatility surface visualization
   - Real-time IV regime indicator
   - Integration with existing CVD signal display

### Validation Criteria

1. **Performance Improvement:**
   - IV-adjusted CVD strategy Sharpe ratio >1.5 (vs. baseline 1.2)
   - Max drawdown reduction >7 percentage points
   - Win rate improvement >4 percentage points

2. **Regime Effectiveness:**
   - High Vol regime: Strategy Sharpe improves from 0.6 → >1.0
   - Low Vol regime: Reduces whipsaw losses by >30%
   - Crash regime: Limits max single-trade loss to <3%

3. **Signal Quality:**
   - Skew momentum indicator: >55% directional accuracy (7-day forward returns)
   - VRP indicator: >60% accuracy in predicting realized vol regime shifts
   - Butterfly indicator: >65% accuracy in predicting tail events (>2σ moves)

### Ongoing Monitoring

1. **Daily Checks:**
   - IV data freshness and quality
   - Current regime classification
   - Active signal alerts

2. **Weekly Reviews:**
   - Strategy performance by regime
   - Signal accuracy metrics
   - Data quality issues

3. **Monthly Analysis:**
   - Regime transition analysis
   - Model parameter drift
   - Correlation stability
   - Competitive landscape (new data providers, liquidity shifts)

4. **Quarterly Recalibration:**
   - Regime threshold updates
   - Backtesting on recent data
   - Strategy parameter optimization
   - Research literature review (new academic findings)

---

## Implementation Priority

### HIGH PRIORITY (Weeks 1-4)
✅ **Phase 1:** Data infrastructure (Deribit API, database)
✅ **Phase 2:** IV regime classification & CVD adjustment framework

**Rationale:** Core functionality required to improve CVD signal quality during volatile markets. Addresses immediate need for risk management.

### MEDIUM PRIORITY (Weeks 5-8)
⚠️ **Phase 3:** Advanced volatility signals (skew momentum, butterfly, NBP)
⚠️ **Phase 4:** Dashboard integration

**Rationale:** Enhances signal quality but requires Phase 1-2 foundation. Provides user-facing value through dashboard visualization.

### LOWER PRIORITY (Weeks 9-10)
📊 **Phase 5:** Comprehensive backtesting & validation

**Rationale:** Validates system performance but can be done iteratively. Initial deployment can proceed with Phase 1-2 validated.

---

## Next Steps

1. **Immediate (This Week):**
   - Approve research findings and integration roadmap
   - Set up Deribit API access (free tier available for testing)
   - Define database schema for IV metrics

2. **Short-term (Weeks 1-2):**
   - Implement Deribit API integration in Airflow DAG
   - Create Postgres tables for options IV data
   - Build basic IV regime classifier

3. **Medium-term (Weeks 3-6):**
   - Backtest IV-adjusted CVD strategy on historical data
   - Develop advanced volatility signals (skew momentum, butterfly)
   - Design dashboard components for IV visualization

4. **Long-term (Weeks 7-10):**
   - Full dashboard integration
   - Comprehensive backtesting and validation
   - Production deployment with monitoring

---

## Academic Sources & Links

### Open Access Papers (PDFs Available)

1. [Implied volatility estimation of bitcoin options and the stylized facts of option pricing](https://jfin-swufe.springeropen.com/articles/10.1186/s40854-021-00280-y) - Zulfiqar & Gulzar (2021)
2. [Cryptocurrency volatility markets (CVX Index)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8326316/) - Woebbeking (2021)
3. [Net Buying Pressure and Bitcoin Option Trades](https://arxiv.org/abs/2109.02776) - Alexander et al. (2021)
4. [Risk Premia in the Bitcoin Market](https://arxiv.org/abs/2410.15195) - Almeida et al. (2024)
5. [On the Implied Volatility of Inverse Options](https://arxiv.org/abs/2401.00539) - Alòs et al. (2024)
6. [A Horserace of Volatility Models for Cryptocurrency](https://arxiv.org/pdf/2010.07402) - Chi & Hao (2020)

### Subscription/Paywalled Papers

7. [Delta Hedging Bitcoin Options With a Smile](https://www.tandfonline.com/doi/full/10.1080/14697688.2023.2181205) - Alexander & Imeraj (2023) | [SSRN Preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4097909)
8. [Effects of Social Media on Cryptocurrency Options](https://onlinelibrary.wiley.com/doi/10.1002/fut.70004) - Kim et al. (2025)
9. [Pricing Cryptocurrency Options With Volatility of Volatility](https://onlinelibrary.wiley.com/doi/10.1002/fut.70029) - Du et al. (2025)
10. [Price Dynamics and Volatility Jumps in Bitcoin Options](https://jfin-swufe.springeropen.com/articles/10.1186/s40854-024-00653-z) - Financial Innovation (2024)

### Additional Resources

- [Deribit Bitcoin Options Metrics](https://metrics.deribit.com/options/BTC)
- [Block Scholes Volatility Research](https://www.blockscholes.com/research)
- [CF Benchmarks Bitcoin Volatility Index](https://www.cfbenchmarks.com/indices/BVOL)
- [Glassnode Derivatives Analytics](https://studio.glassnode.com/charts?a=BTC&category=Derivatives)

---

## Glossary

**ATM (At-the-Money):** Option with strike price equal (or very close) to current spot price.

**Butterfly Spread:** (25d call IV + 25d put IV) / 2 - ATM IV. Measures curvature of volatility smile; high values indicate fat tails.

**CVX Index:** Cryptocurrency Volatility Index developed by Woebbeking (2021), similar to VIX for equities.

**Delta:** Option Greek measuring sensitivity to price changes. 25-delta = 25% probability of expiring in-the-money.

**Forward Skew:** Implied volatility increases with strike price (OTM calls > ATM > OTM puts). Typical of commodities.

**Implied Volatility (IV):** Market's expectation of future volatility, backed out from option prices using pricing models.

**OTM (Out-of-the-Money):** Call with strike > spot price; put with strike < spot price.

**Risk Reversal:** 25-delta call IV minus 25-delta put IV. Measures skew; positive = bullish skew (calls more expensive).

**Reverse Skew:** Implied volatility decreases with strike price (OTM puts > ATM > OTM calls). Typical of equities.

**SVI Model:** Stochastic Volatility Inspired parameterization of volatility smile (parameters: level, slope, curvature).

**Variance Risk Premium (VRP):** Implied variance minus realized variance. Measures compensation for selling volatility.

**Volatility Smile:** U-shaped pattern where OTM options have higher IV than ATM options.

**VOV (Volatility of Volatility):** Second-order volatility - how much volatility itself varies over time.

---

**Document Version:** 1.0
**Last Updated:** 2026-01-16
**Primary Researcher:** Claude (Sonnet 4.5)
**Status:** ✅ Research Complete | 📋 Pending Implementation
