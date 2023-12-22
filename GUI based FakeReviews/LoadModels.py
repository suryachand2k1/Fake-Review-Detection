from Model import Model
import pickle


class LoadModels:
    
    def loadModel(self,model):
        with open('tfidf.txt', 'rb') as file:
            model.setTFIDF(pickle.load(file))
        file.close()

        with open('emsvm.txt', 'rb') as file:
            model.setEMSVM(pickle.load(file))
        file.close()

        with open('emnb.txt', 'rb') as file:
            model.setEMNaiveBayes(pickle.load(file))
        file.close()

        with open('svm.txt', 'rb') as file:
            model.setSVM(pickle.load(file))
        file.close()

        with open('nb.txt', 'rb') as file:
            model.setNaiveBayes(pickle.load(file))
        file.close()
    
