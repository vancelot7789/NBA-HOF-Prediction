#import module
library('ggplot2')
library('ggthemes')
library('scales')
library('dplyr')
library('mice')
library('randomForest')
library('caret')
library('fastDummies')
library('ROCR')
library("DAAG")

#import dataset
full = read.csv('./final_player.csv')
full$Pos=factor(full$Pos)
#covert Pos into dummy variable
full=dummy_cols(full, select_columns = c("Pos"))

#The distribution of all player to Position
ggplot(full, aes(x=Pos))+ geom_bar()

#The distribution of retired player to Position&HoF
retired_player = filter(full,Active==0)
graph = ggplot(retired_player, aes(Pos,fill=factor(HoF))) + geom_bar()
graph + ylim(0,35)
graph + ylim(0,1050)

#data visualization
ggplot(full[!is.na(full$TRPG),], aes(Pos, TRPG)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$BPG),], aes(Pos, BPG)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$SPG),], aes(Pos, SPG)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$X3PG),], aes(Pos, X3PG)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$FG.),], aes(Pos, FG.)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$FT.),], aes(Pos, FT.)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$X3P.),], aes(Pos, X3P.)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$TRPG),], aes(Pos, EF.)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$EF.),], aes(Pos, DRTG)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$TRPG),], aes(Pos, ORTG)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$TRPG),], aes(Pos, VORP)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$TRPG),], aes(Pos, BPM)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$TRPG),], aes(Pos, EFF)) + 
  geom_boxplot(varwidth = TRUE)

ggplot(full[!is.na(full$TRPG),], aes(Pos, Win_Shares)) + 
  geom_boxplot(varwidth = TRUE)

#Fill the missing value
for(i in (1:5)){
  a=median(full[!is.na(full$TRPG)&full$Pos==i,]$TRPG)
  if(nrow(full[is.na(full$TRPG)&full$Pos==i,])!=0)
    full[is.na(full$TRPG)&full$Pos==i,]$TRPG=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$BPG)&full$Pos==i,]$BPG)
  if(nrow(full[is.na(full$BPG)&full$Pos==i,])!=0)
    full[is.na(full$BPG)&full$Pos==i,]$BPG=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$SPG)&full$Pos==i,]$SPG)
  if(nrow(full[is.na(full$SPG)&full$Pos==i,])!=0)
    full[is.na(full$SPG)&full$Pos==i,]$SPG=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$X3PG)&full$Pos==i,]$X3PG)
  if(nrow(full[is.na(full$X3PG)&full$Pos==i,])!=0)
    full[is.na(full$X3PG)&full$Pos==i,]$X3PG=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$FG.)&full$Pos==i,]$FG.)
  if(nrow(full[is.na(full$FG.)&full$Pos==i,])!=0)
    full[is.na(full$FG.)&full$Pos==i,]$FG.=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$FT.)&full$Pos==i,]$FT.)
  if(nrow(full[is.na(full$FT.)&full$Pos==i,])!=0)
    full[is.na(full$FT.)&full$Pos==i,]$FT.=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$X3P.)&full$Pos==i,]$X3P.)
  if(nrow(full[is.na(full$X3P.)&full$Pos==i,])!=0)
    full[is.na(full$X3P.)&full$Pos==i,]$X3P.=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$EF.)&full$Pos==i,]$EF.)
  if(nrow(full[is.na(full$EF.)&full$Pos==i,])!=0)
    full[is.na(full$EF.)&full$Pos==i,]$EF.=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$DRTG)&full$Pos==i,]$DRTG)
  if(nrow(full[is.na(full$DRTG)&full$Pos==i,])!=0)
    full[is.na(full$DRTG)&full$Pos==i,]$DRTG=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$ORTG)&full$Pos==i,]$ORTG)
  if(nrow(full[is.na(full$ORTG)&full$Pos==i,])!=0)
    full[is.na(full$ORTG)&full$Pos==i,]$ORTG=a
}


for(i in (1:5)){
  a=median(full[!is.na(full$VORP)&full$Pos==i,]$VORP)
  if(nrow(full[is.na(full$VORP)&full$Pos==i,])!=0)
    full[is.na(full$VORP)&full$Pos==i,]$VORP=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$BPM)&full$Pos==i,]$BPM)
  if(nrow(full[is.na(full$BPM)&full$Pos==i,])!=0)
    full[is.na(full$BPM)&full$Pos==i,]$BPM=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$EFF)&full$Pos==i,]$EFF)
  if(nrow(full[is.na(full$EFF)&full$Pos==i,])!=0)
    full[is.na(full$EFF)&full$Pos==i,]$EFF=a
}

for(i in (1:5)){
  a=median(full[!is.na(full$Win_Shares)&full$Pos==i,]$Win_Shares)
  if(nrow(full[is.na(full$Win_Shares)&full$Pos==i,])!=0)
    full[is.na(full$Win_Shares)&full$Pos==i,]$Win_Shares=a
}

full[is.na(full$TR),]$TR=full[is.na(full$TR),]$TRPG*full[is.na(full$TR),]$GP
full[is.na(full$TBLKS),]$TBLKS=full[is.na(full$TBLKS),]$BPG*full[is.na(full$TBLKS),]$GP
full[is.na(full$TSTLS),]$TSTLS=full[is.na(full$TSTLS),]$SPG*full[is.na(full$TSTLS),]$GP
full[is.na(full$T3PS),]$T3PS=full[is.na(full$T3PS),]$X3PG*full[is.na(full$T3PS),]$GP

#split the dataset into two datasets
full$Pos = NULL
retired_player = filter(full,Active==0)
active_player = filter(full,Active==1)
retired_player$Active = NULL
active_player$Active = NULL

set.seed(12345)

train <-createDataPartition(y=retired_player$HoF,p=0.8,list=FALSE) 
train2 <- retired_player[train, ] # 80%的retired_player數據作為訓練數據
test2 <- retired_player[-train, ] # 20%的retired_player數據作為測試

#To see whether the datasets are uniform
print(colnames(train2))
print(colnames(test2))
print(colnames(active_player))

set.seed(999)

# Build the model (note: not all possible variables are used)
rf_model = randomForest(factor(HoF) ~ Pos_1 + Pos_2 + Pos_3 + Pos_4 + Pos_5 + All_Star + All_Nba + All_Def + 
                          Score_Champ + Assit_Champ + Trb_Champ + 
                          MVP + GP + PPG + TRPG + APG + BPG + SPG +
                          X3PG + TP + TR + TAST + TBLKS + TSTLS + T3PS +
                          FG. + FT. + X3P. + EF. + DRTG + ORTG + VORP +
                          BPM + EFF + Win_Shares,
                        data = train2 , mytry=2, ntree=50)

# Show model error
plot(rf_model, ylim=c(0,0.6))
legend('topright', colnames(rf_model$err.rate), col=1:3, fill=1:3)


# Get importance
importance    <- importance(rf_model)
varImportance <- data.frame(Variables = row.names(importance), 
                            Importance = round(importance[ ,'MeanDecreaseGini'],2))

# Create a rank variable based on importance
rankImportance <- varImportance %>%
  mutate(Rank = paste0('#',dense_rank(desc(Importance))))

# Use ggplot2 to visualize the relative importance of variables
ggplot(rankImportance, aes(x = reorder(Variables, Importance), 
                           y = Importance, fill = Importance)) +
  geom_bar(stat='identity') + 
  geom_text(aes(x = Variables, y = 0.5, label = Rank),
            hjust=0, vjust=0.55, size = 3, colour = 'red') +
  labs(x = 'Variables') +
  coord_flip() + 
  theme_few()


#The accuracy in train data
prediction_train = predict(rf_model, train2)

conf_matrix = table(prediction_train, train2$HoF)
print(conf_matrix)
accuracy = sum(diag(conf_matrix)) / sum(conf_matrix)
print(accuracy)


# The accuracy in test data
prediction_test = predict(rf_model, test2)

conf_matrix = table(prediction_test, test2$HoF)
print(conf_matrix)
accuracy = sum(diag(conf_matrix)) / sum(conf_matrix)
print(accuracy)

#The prediction of the active player
ActivePlayer=active_player
ActivePlayer$X=NULL
ActivePlayer$Name=NULL

prediction_active = predict(rf_model, ActivePlayer,type='prob')

# Write the solution to file
solution = data.frame(PlayerNAME=active_player$Name, prob = prediction_active)
write.csv(solution, file = 'rf_solution.csv', row.names = F)


#The initial state of logistic regression model
logit_full = glm(factor(HoF)~. - Name - X ,family = binomial(link = "logit"), 
                 data = train2, na.action = na.exclude)

logit_null = glm(factor(HoF)~1 - Name - X,family = binomial(link = "logit"), 
                 data = train2, na.action = na.exclude)

#algorithm
logit_forward = step(logit_null,scope=list(lower=logit_null,upper=logit_full),direction="forward")

logit_backward = step(logit_full,direction="backward")

logit_select = step(logit_full,direction="both")

#Train logistic regression model and show it summary
lr_model = glm(formula = factor(HoF) ~ All_Star + Score_Champ + GP + TRPG + APG + BPG + 
                 X3PG + TR + TBLKS + FG. + EF. + VORP + Win_Shares + Pos_4 + Pos_5 , family = binomial(link = "logit"), 
               data = train2, na.action = na.exclude)

summary(lr_model)

#The accuracy in train data
predict_train = predict(lr_model, train2)
table(train2$HoF, predict_train >= 0.5)

predict_train = ifelse(predict_train > 0.5,1,0)
misClasificError = mean(predict_train != train2$HoF)
print(paste('Accuracy',1-misClasificError))

#The accuracy in train data
predict_test = predict(lr_model, test2)
table(test2$HoF, predict_test >= 0.5)

predict_test = ifelse(predict_test > 0.5,1,0)
misClasificError = mean(predict_test != test2$HoF)
print(paste('Accuracy',1-misClasificError))

#The prediction of the HoF of the active player
ActivePlayer=active_player
ActivePlayer$X=NULL
ActivePlayer$Name=NULL

predict_active = predict(lr_model, newdata=ActivePlayer)
probs = exp(predict_active)/(1+exp(predict_active))

# Write the solution to file
solution = data.frame(PlayerNAME=active_player$Name, prob = probs)
write.csv(solution, file = 'lr_solution.csv', row.names = F)

#draw the ROC curve
library(ROCR)
predictions = predict(lr_model, newdata=test2)
ROCRpred = prediction(predictions, test2$HoF)
ROCRperf = performance(ROCRpred, measure = "tpr", x.measure = "fpr")

plot(ROCRperf, colorize = TRUE, text.adj = c(-0.2,1.7), print.cutoffs.at = seq(0,1,0.1))





