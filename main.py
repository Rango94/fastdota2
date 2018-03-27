import model
import readfile
import trainer

model=model.model(1000)
file=readfile.readfile("D:/dota2data/dota2train.txt")
trainer=trainer.trainer(model,0.05,file)
trainer.train(50000000)
trainer.prediction("D:/dota2data/dota2train.txt")