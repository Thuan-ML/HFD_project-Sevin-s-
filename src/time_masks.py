from __future__ import annotations
import pandas as pd

from config import GROUP1_RULES, GROUP2_RULES


def time_between(index: pd.DatetimeIndex, start: str, end: str):
    t = index.time
    start_t = pd.to_datetime(start).time()
    end_t = pd.to_datetime(end).time()
    return (t >= start_t) & (t <= end_t)


def group1_masks(df: pd.DataFrame):
    idx = df.index
    masks = {}

    masks["in_session"] = time_between(idx, GROUP1_RULES["session_start"], GROUP1_RULES["session_end"])
    masks["no_trade"] = time_between(idx, GROUP1_RULES["no_trade_start"], GROUP1_RULES["no_trade_end"])
    masks["force_exit"] = time_between(idx, GROUP1_RULES["force_exit"], GROUP1_RULES["session_end"])

    masks["drop_calc"] = (
        time_between(idx, GROUP1_RULES["drop_early_start"], GROUP1_RULES["drop_early_end"])
        | time_between(idx, GROUP1_RULES["drop_late_start"], GROUP1_RULES["drop_late_end"])
    )

    return masks


def group2_masks(df: pd.DataFrame):
    idx = df.index
    masks = {}

    masks["break_time"] = time_between(idx, GROUP2_RULES["break_start"], GROUP2_RULES["break_end"])
    masks["no_trade"] = time_between(idx, GROUP2_RULES["break_end"], GROUP2_RULES["no_trade_after_break_end"])
    masks["force_exit"] = time_between(idx, GROUP2_RULES["force_exit"], GROUP2_RULES["break_start"])

    return masks