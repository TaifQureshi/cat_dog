import pickle
import cv2
from tqdm import tqdm

LABELS = {CATS: 0, DOGS: 1}
category = ["Dog", "Cat"]
training_data = []

for label in LABELS:
    print(label)
    for f in tqdm(os.listdir(label)):
        if "jpg" in f:
            try:
                path = os.path.join(label, f)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                training_data.append([np.array(img), np.eye(2)[LABELS[label]]])  # do something like print(np.eye(2)[1]), just makes one_hot 
                #print(np.eye(2)[self.LABELS[label]])

                if label == CATS:
                    catcount += 1
                elif label == DOGS:
                    dogcount += 1

            except Exception as e:
                pass
                #print(label, f, str(e))

np.random.shuffle(training_data)
np.save("training_data.npy", training_data)
print('Cats:',catcount)
print('Dogs:',dogcount)
