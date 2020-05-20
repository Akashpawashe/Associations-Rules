#install.packages("arules")
library(arules)
#install.packages("arulesViz")
library(arulesViz)

book <- read.csv("D:\\excelR\\Data science notes\\association rules\\asgmnt\\book.csv")

book_rules<- apriori(as.matrix(book),parameter=list(support=0.05,confidence=0.5,minlen=3))

inspect(head(sort(book_rules,by="lift")))
inspect(head(sort(book_rules,by="support")))
inspect(head(sort(book_rules,by="confidence")))
inspect(head(sort(book_rules, by = c("count","lift"))))

head(quality(book_rules))

set.seed(103);plot(book_rules,method = "graph")

colfunc <- colorRampPalette(c("black","red","yellow"))

plot(book_rules,method="scatterplot",jitter=0,col=colfunc(5))
plot(book_rules,method="matrix",engine = "3d")
plot(book_rules,method="grouped matrix",col=colfunc(5))
plot(book_rules,method="two-key plot",jitter=0)
plot(book_rules,method="paracoord")
plot(book_rules,method = "mosaic")


# using differnt support and confidence
book_rules2<- apriori(as.matrix(book),parameter=list(support=0.01,confidence=0.7,minlen=3))

inspect(head(sort(book_rules2,by="lift")))
inspect(head(sort(book_rules2,by="support")))
inspect(head(sort(book_rules2,by="confidence")))
inspect(head(sort(book_rules2, by = c("count","lift"))))

plot(book_rules2,method="scatterplot",jitter=0,col=colfunc(5))
plot(book_rules2,method="matrix",engine = "3d")
plot(book_rules2,method="grouped matrix",col=colfunc(5))
plot(book_rules2,method="two-key plot",jitter=0)
plot(book_rules2,method="paracoord")
plot(book_rules2,method = "mosaic")

