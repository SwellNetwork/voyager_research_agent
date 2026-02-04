from pathlib import Path

from agents import function_tool


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def _read_text_from_candidates(label: str, candidates: list[str]) -> str:
    for relative_path in candidates:
        file_path = PROJECT_ROOT / relative_path
        if file_path.exists():
            return file_path.read_text(encoding="utf-8")
    tried_paths = ", ".join(str(PROJECT_ROOT / p) for p in candidates)
    raise FileNotFoundError(f"Could not find {label}. Tried: {tried_paths}")


def get_prompt_data():
    return _read_text_from_candidates(
        "prompt data file",
        [
            "resource/prompt_data.txt",
            "resource/report_data.txt",
            "data/prompt_data.txt",
        ],
    )


def get_charts_data():
    return _read_text_from_candidates(
        "charts data file",
        [
            "resource/charts_data.txt",
            "data/charts_data.txt",
        ],
    )


@function_tool
def get_report_data():
    """Load report context and chart datasets used by the agent.

    Returns:
    - prompt_data (str): narrative market context for report writing. Includes
      sections such as current snapshot, technical indicators, derivatives
      (funding/open interest/long-short), liquidation stats, sentiment
      (Fear & Greed), macro context, benchmark performance, prediction markets,
      risk calendar, and smart money positioning.
    - charts_data (str): chart-ready CSV datasets for plotting. Includes
      price timeseries, funding timeseries (by exchange and aggregate),
      open-interest timeseries (by exchange and aggregate), fear & greed
      timeseries, liquidation long/short levels, and benchmark performance.
    """
    prompt_data = get_prompt_data()
    charts_data = get_charts_data()
    return {
        "prompt_data": prompt_data,
        "charts_data": charts_data,
    }
