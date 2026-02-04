# Academic References Template for Skills Files

This document provides a standardized format for adding academic references to skills files, ensuring consistency and traceability across the Voyager data pipeline research framework.

---

## Template Structure

### Standard Citation Format

```markdown
### [Sequential Number]. [Paper Title]

**Authors:** [Last Name, First Initial. (comma-separated list)]
**Publication:** [Journal/Conference Name, Volume X, Issue Y, pages Z1-Z2]
**Year:** [YYYY]
**DOI:** [10.xxxx/xxxxx] (if available)

#### Key Finding Relevant to [Framework Section Name]:

[1-2 sentence summary from Gemini analysis highlighting the core insight that relates to the specific framework component]

#### Methodology:
- Dataset: [Data source description]
- Period: [Time period covered]
- Key techniques: [Brief list of methods used]

#### Relevance to [Specific Framework Section]:
[2-3 sentences explaining how this research validates or informs the framework thresholds, signals, or trading logic in this section]

**URLs:**
- Google Scholar: [Link to Google Scholar page]
- Publisher/Source: [Direct link to paper]
- arXiv: [Link if available]

**PDF Availability:** ✅ [Freely available at URL] | 🔒 [Access restricted - requires institutional subscription]
```

---

## Complete Example

### 1. Order Flow Analysis of Cryptocurrency Markets

**Authors:** Silantyev, E.
**Publication:** Digital Finance, Volume 1, Issue 1, pages 191-218
**Year:** 2019
**DOI:** 10.1007/s42521-019-00007-w

#### Key Finding Relevant to CVD Signal Framework:

Trade flow imbalance is consistently superior at explaining contemporaneous price changes compared to aggregate order flow imbalance, exhibiting a strong linear relationship with price movements over sufficiently large time intervals.

#### Methodology:
- Dataset: BitMEX XBTUSD perpetual contract
- Period: 2018 trading data
- Key techniques: Trade and quote data analysis, order book event impact analysis, comparison of trade flow vs aggregate flow imbalance

#### Relevance to CVD Signal Thresholds:

This foundational research directly validates the CVD framework's core premise - that measuring the difference between aggressive buys and sells (trade flow imbalance) is highly predictive of price changes. The finding that this relationship strengthens over larger time intervals informs our use of 4-hour CVD windows for swing trading signals rather than minute-level noise.

**URLs:**
- Google Scholar: https://scholar.google.com/scholar?q=Order+flow+analysis+of+cryptocurrency+markets+Silantyev
- Publisher: https://link.springer.com/article/10.1007/s42521-019-00007-w
- ResearchGate: https://www.researchgate.net/publication/332089928_Order_flow_analysis_of_cryptocurrency_markets

**PDF Availability:** 🔒 Access restricted - requires Springer institutional subscription or purchase

---

## Usage Guidelines

### When to Add References

Add academic references to skills files when:

1. **Framework Validation:** Research validates specific thresholds or signal logic
2. **Methodology Justification:** Papers explain why certain approaches work
3. **Performance Metrics:** Studies provide expected accuracy or performance benchmarks
4. **Risk Assessment:** Research identifies failure modes or edge cases

### Placement in Skills Files

Insert the `## Academic References` section at the **end of the skills file**, before any final notes or appendices.

```markdown
---

## Academic References

[Insert references using the standard template above]

---

## Data Quality Notes
[Existing data quality content...]
```

### Framework Section Mapping

Map references to specific framework sections:

| Framework Section | Reference Focus |
|------------------|----------------|
| **Regime Detection** | Volatility modeling, regime identification papers |
| **Signal Thresholds (ELR, Funding, L/S)** | Leverage metrics, funding rate analysis, positioning studies |
| **Options Signals (GEX, Skew, IV)** | Options market microstructure, gamma exposure, volatility |
| **On-Chain Integration** | Exchange flows, holder behavior, MVRV/SOPR metrics |
| **Liquidation Dynamics** | Cascade risk, liquidation clustering, leverage unwinding |
| **Scenario Templates** | Backtesting studies, historical pattern validation |

### Multiple References for Same Section

When multiple papers support a single framework section:

```markdown
#### Relevance to ELR Thresholds:

This research supports the 2.5-4% HIGH leverage classification for ETH by demonstrating that elevated OI/MCap ratios above 3% precede cascade events with 72% accuracy (also validated by [Author2 Year] who found similar thresholds at 2.8% using different methodology).
```

---

## Integration with Gemini Analysis

### Workflow for Adding References

1. **Gemini Deep Analysis:** Use Gemini to analyze 15-25 papers per domain
2. **Extract Key Findings:** Identify 1-2 sentence summaries per paper
3. **Map to Framework:** Connect findings to specific skills file sections
4. **Add References:** Use this template to format and insert references

### Citation Style

- **Academic format:** Author (Year), Title, Journal
- **Consistency:** Use consistent formatting across all skills files
- **DOI preference:** Always include DOI when available for permanent linking
- **Multiple sources:** Google Scholar + Publisher + arXiv (when available)

---

## Quality Standards

### Minimum Reference Requirements

- **Citation completeness:** All author names, year, publication, DOI (if available)
- **Key finding:** 1-2 sentence summary directly from Gemini analysis
- **Relevance explanation:** 2-3 sentences connecting to framework section
- **URL verification:** All links tested and working
- **PDF status:** Clearly marked as freely available or restricted

### Peer Review Standards

Only include references that meet:

- ✅ Published in peer-reviewed journals or reputable conferences
- ✅ Available on arXiv preprints from recognized institutions
- ✅ Working papers from academic researchers with institutional affiliation

Do NOT include:

- ❌ Blog posts or Medium articles
- ❌ Trading course materials
- ❌ Unverified social media claims
- ❌ Commercial research without methodology disclosure

---

## Template Variations

### For arXiv Preprints

```markdown
### 3. Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books

**Authors:** Wang, H. K.
**Publication:** arXiv preprint
**Year:** 2025
**arXiv ID:** 2506.05764v2

[Rest of template follows same structure]

**URLs:**
- arXiv Abstract: https://arxiv.org/abs/2506.05764
- arXiv HTML: https://arxiv.org/html/2506.05764v2
- Google Scholar: https://scholar.google.com/[search URL]

**PDF Availability:** ✅ Freely available at https://arxiv.org/pdf/2506.05764
```

### For Conference Papers

```markdown
### 5. High-Frequency Trading Dynamics in Cryptocurrency Markets

**Authors:** Smith, J., Johnson, A., & Williams, R.
**Publication:** Proceedings of the 2024 International Conference on Computational Finance (ICCF '24)
**Year:** 2024
**DOI:** 10.1145/3588869.3588870

[Rest of template follows same structure]
```

### For Multi-Author Papers (>3 Authors)

```markdown
**Authors:** Chen, X., Liu, Y., Zhang, W., et al. (12 authors)
**Full Author List:** https://doi.org/10.xxxx/xxxxx
```

---

## Example Section in Skills File

Here's how the Academic References section would appear in a complete skills file:

```markdown
---

## Academic References

### 1. Order Flow Analysis of Cryptocurrency Markets

**Authors:** Silantyev, E.
**Publication:** Digital Finance, Volume 1, Issue 1, pages 191-218
**Year:** 2019
**DOI:** 10.1007/s42521-019-00007-w

#### Key Finding Relevant to CVD Signal Framework:

Trade flow imbalance is consistently superior at explaining contemporaneous price changes compared to aggregate order flow imbalance, with strong linear relationship over larger time intervals.

#### Methodology:
- Dataset: BitMEX XBTUSD perpetual contract
- Period: 2018 trading data
- Key techniques: Trade/quote analysis, order book event impact, flow comparison

#### Relevance to CVD Signal Thresholds:

Validates CVD framework's core premise that aggressive buy/sell difference predicts price changes. The strengthening relationship over larger intervals informs our 4-hour CVD windows for swing trading rather than minute-level analysis.

**URLs:**
- Google Scholar: https://scholar.google.com/scholar?q=Order+flow+analysis+of+cryptocurrency+markets+Silantyev
- Publisher: https://link.springer.com/article/10.1007/s42521-019-00007-w

**PDF Availability:** 🔒 Access restricted

---

### 2. [Next reference follows same format]

---

## Data Quality Notes
[Existing content...]
```

---

## Maintenance and Updates

### Annual Review Process

1. **Q4 Review:** Check all DOI links and URLs annually
2. **New Research:** Add newly published papers as they become available
3. **Deprecated Research:** Mark papers with contradicted findings
4. **Version Control:** Track reference additions in git commit messages

### Commit Message Format

```
feat(skills): add academic reference to BTC perpetuals

- Added Silantyev (2019) CVD validation paper
- Reference validates CVD signal framework
- Maps to CVD Signal Thresholds section

Related: P1-001 CVD Academic Research
```

---

## Contact and Questions

For questions about this template or academic reference standards:

- **Research Lead:** Check docs/research/ for detailed analysis
- **Framework Questions:** Review templates/report_prompts.py
- **Data Quality Issues:** Tag in PR with `research` label

---

**Template Version:** 1.0
**Last Updated:** 2026-01-16
**Maintained By:** Voyager Research Team
