# 🏈 NFL Betting Predictor

A command-line application written in Python that helps users make informed bets on NFL games. It evaluates matchups using a points-based system that considers team performance, betting odds, spreads, and over/under lines. It supports predicting regular games, playoff matchups, point totals, and converting odds into winning probabilities.

---

## 🎯 Features

- Predict the winner of an NFL game.
- Recommend Over/Under picks based on team scoring averages.
- Calculate betting probabilities from odds.
- Covers:
  - Team recent form and past records.
  - Moneyline and spread percentages.
  - Home/away records and ATS (Against the Spread) stats.
  - Odds for straight win and handicap win.
- Supports different prediction scenarios:
  1. Regular game predictions (winner + Over/Under + handicap).
  2. Playoff predictions.
  3. Over/Under only.
  4. Odds-to-probability conversion.

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### Run the App

Save the file as `main.py` and run:

```bash
python main.py
```

---

## 🧠 How It Works

1. The app presents a menu with different betting options.
2. Based on your selection, you will be prompted to enter data such as:
   - Team names
   - Betting odds
   - Recent records
   - Points scored
   - Over/Under line
3. It calculates scores for both teams based on several factors.
4. The team with the higher score is predicted to win.
5. If odds are provided, the app shows:
   - Estimated payout
   - Winning probability for each bet
6. Over/Under prediction is calculated from the average total points per game.

---

## 📘 Example Usage

When run, the program will ask:

```
Types of bets:
1. Match winner & Over/Under & Handicap
2. Predict a playoff series
3. Just predict Over/Under
4. Convert odds to probability
Which one do you want to do?
```

Depending on your choice, it will guide you through a series of inputs and show a prediction like:

```
Bet on the HOME TEAM
With odds: 2.10
Winning probability: 47.62%
Handicap: +3.5
Handicap odds: 1.90
Over/Under Line: 45.5
Recommended: OVER
Potential winnings: $110
```

---

## 📂 Project Structure

```
main.py
README.md
```

---

## 📄 License

This project is open-source under the MIT License. You're free to use, adapt, and improve it!
