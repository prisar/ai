from datasets import load_dataset

emotions = load_dataset("emotion")
print(emotions)

train_ds = emotions["train"]
print(train_ds.features)