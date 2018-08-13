rm(list=ls())
library(readxl)
X <- read_excel("stock_predictions/own_prediction/russell3000/ru3000_membershiplist_20180625.xlsx")
View(X)

symbols = c(as.matrix(X[,3])[,1],as.matrix(X[,7])[,1])
symbols = symbols[-which(symbols=="Ticker")]
symbols = symbols[!is.na(symbols)]
symbols = sort(symbols)

write(symbols,file = "stock_predictions/own_prediction/russell3000/ru3000_membershiplist_20180625.txt")