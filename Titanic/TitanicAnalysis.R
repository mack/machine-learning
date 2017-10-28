
train <- read.csv('train.csv', header = TRUE)
test <- read.csv('test.csv', header = TRUE)

test.survived <- data.frame(Survived = rep("None", nrow(test)), test[,])

data.combined <- rbind(train, test.survived)

str(data.combined)

data.combined$Survived <- as.factor(data.combined$Survived)

str(data.combined$Survived)

library(ggplot2)

train$Pclass <- as.factor(train$Pclass)

ggplot(train, aes(x = Pclass, fill = factor(Survived))) + 
  geom_bar(width = 0.5) + 
  xlab('P-Class') + 
  ylab('Total Count') +
  labs(fill = "Survived")
  


