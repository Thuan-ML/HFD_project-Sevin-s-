from __future__ import annotations
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path)

    if not isinstance(df.index, pd.DatetimeIndex):
        datetime_col = None
        for col in df.columns:
            c = col.lower()
            if "datetime" in c or "time" in c or "date" in c:
                datetime_col = col
                break

        if datetime_col is not None:
            df[datetime_col] = pd.to_datetime(df[datetime_col])
            df = df.set_index(datetime_col)

    return df.sort_index()