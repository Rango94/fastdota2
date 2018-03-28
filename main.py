import model
import readfile
import trainer

model=model.model(1000)
file=readfile.readfile("D:/dota2data/dota2train.txt")
trainer=trainer.trainer(model,0.5,file)
trainer.train(100000000)
trainer.model.save("D:/dota2data/model.model",trainer.weghtlayer)
trainer.prediction("D:/dota2data/dota2train.txt")