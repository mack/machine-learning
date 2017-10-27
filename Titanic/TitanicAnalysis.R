
train <- read.csv('train.csv', header = TRUE)
test <- read.csv('test.csv', header = TRUE)

test.survived <- data.frame(survived = rep("None", nrow(test)), test[,])

data.combined <- rbind(train, test.survived)

