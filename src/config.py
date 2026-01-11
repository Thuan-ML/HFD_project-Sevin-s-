CONTRACTS = {
    "SP":  {"cost": 12, "point_value": 50},
    "NQ":  {"cost": 12, "point_value": 20},
    "CAD": {"cost": 10, "point_value": 100000},
    "AUD": {"cost": 10, "point_value": 100000},
    "XAU": {"cost": 15, "point_value": 100},
    "XAG": {"cost": 10, "point_value": 5000},
}

GROUP1_ASSETS = ["SP", "NQ"]
GROUP2_ASSETS = ["CAD", "AUD", "XAU", "XAG"]

GROUP1_RULES = {
    "session_start": "09:30",
    "session_end": "16:00",
    "no_trade_start": "09:31",
    "no_trade_end": "09:55",
    "force_exit": "15:40",
    "drop_early_start": "09:31",
    "drop_early_end": "09:40",
    "drop_late_start": "15:51",
    "drop_late_end": "16:00",
}

GROUP2_RULES = {
    "break_start": "17:00",
    "break_end": "18:00",
    "force_exit": "16:50",
    "no_trade_after_break_end": "18:10",
}

ANNUALIZATION_DAYS = 252