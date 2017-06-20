dataMatrixdf <- read.table("Desktop/CG/DataSets/Modifications/Combo/DataMatrixCombo.txt",
                           header = FALSE)
d<-as.matrix(dataMatrixdf)
labeldf<-read.table("Desktop/CG/DataSets/Labels.txt",
                    header = FALSE)
y<-t(labeldf)
Lyf<-numeric(8)
Golf<-numeric(8)

for (row in 2:dim(d)[1])
  for (col in 1:dim(d)[2])
  {
    if((y[1,col]==1) && (d[row,col]==1))
    {
      Lyf[row]<-Lyf[row]+1
    }
    else if((y[1,col]==0) && (d[row,col]==1))
    {
      Golf[row]<-Golf[row]+1
    }
  }

#BAR PLOT
print(Lyf)
print(Golf)

LyfFrac<-Lyf/138
GolfFrac<-Golf/496
LyfGolf<-cbind(LyfFrac,GolfFrac)
LyfGolfMatrix<-as.matrix(LyfGolf)
colours=c("red", "blue")
barplot(t(LyfGolfMatrix), main="Protein localization as a function of PTM features", xlab= "Post Translational modifications", ylab = "Fraction of proteins", cex.lab = 1.5, cex.main = 1.4, beside=TRUE, col=colours)
legend("topright", c("Lysosome","Golgi"), cex=1.3, bty="n", fill=colours)

print(dim(d))

#Preparing the training data
dnew<-t(dataMatrixdf)


index <- 358:nrow(dnew)
dnew2<-cbind(dnew[index,])
labeldnew2<-labeldf[index,]
subindex<-1:nrow(dnew2)
testindex <- sample(subindex, trunc(length(subindex)*15/100))

testset <- dnew2[testindex,]
trainset <- dnew2[-testindex,]
testlabel<-labeldnew2[testindex]
trainlabel<-labeldnew2[-testindex]

print(testlabel)

print (trainlabel)
library(e1071)
#implementing the SVM
model<-svm(trainlabel~trainset, scale=FALSE, type="C-classification", kernel="linear", C=10, gamma=0.0001)
prediction<-predict(model, testset)
tab<-table(pred = prediction[1:length(trainlabel)], true = trainlabel)
print (tab)

w <- t(model$coefs) %*% model$SV
print(w)
tuned <- tune.svm(trainlabel~trainset, gamma = 10^(-6:-1), cost = 10^(1:2), scale=FALSE)
summary(tuned)

