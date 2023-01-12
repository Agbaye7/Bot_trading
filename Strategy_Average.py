strategy("TEST_1",overlay = true)

// Indicateurs
EMA1 = ta.ema (close, 50)
EMA2 = ta.ema (close, 100)

plot(EMA1, "EMA1", color=color.blue , linewidth=2)
plot(EMA2, "EMA2", color=color.red, linewidth=2)

// Signaux
Buysignal = ta.crossover(EMA1, EMA2) and close >= EMA2
plotchar(Buysignal, color=color.rgb(73, 81, 195), size = size.small, location=location.abovebar)

Sellsignal = ta.crossunder(EMA1,EMA2)
plotchar(Sellsignal, color=color.rgb(226, 69, 69), size = size.small, location=location.belowbar)

//stratégy
strategy.entry(id="Buy", direction=strategy.long, when=Buysignal)
strategy.close(id="Buy",when=Sellsignal)