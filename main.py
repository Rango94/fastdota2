import model
import readfile
import trainer

model=model.model(100)
file=readfile.readfile("D:/dota2data/dota2train.txt")
trainer=trainer.trainer(model,0.025,file)
trainer.train(300000)
trainer.prediction("D:/dota2data/dota2test.txt")