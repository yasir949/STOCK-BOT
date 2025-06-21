# US Stock Alert Bot for Telegram 🚀

This bot monitors US stocks and sends Telegram alerts if any stock rises by +3% intraday.

## Files:

- `stock_alert_bot.py` — Main bot script
- `split_symbols.py` — Split all_symbols.txt into smaller files
- `requirements.txt` — Python dependencies
- `symbols/` — Folder containing split symbols files

## How to Run:

1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Run the bot:

```bash
python stock_alert_bot.py
```

3. Customize:

- Edit `symbols.txt` to assign different stocks per worker (ex: symbols_1.txt, symbols_2.txt, ...)

Enjoy 🚀