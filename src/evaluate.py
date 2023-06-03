import tensorflow as tf

data_dir = 'data\\raw\\kaggle'

test_df = tf.keras.utils.image_dataset_from_directory(data_dir, image_size=(180, 180))

model_path = 'models\\m1\\'

model = tf.saved_model.load(model_path)

metrics = [
    tf.metrics.BinaryAccuracy(),
    tf.metrics.Precision(),
    tf.metrics.Recall()
]

model.compile(metric=metrics)

result = model.evaluate(test_df)

loss, acc, precision, recall = result

result_lines =[
    f'Test data len: {len(test_df)}\n'
    f'Accuracy: {acc:3f}, Precision: {precision:3f}, Recall: {recall:3f}'
]
report_path = 'output/report.txt'
with open(report_path, 'w', encoding='utf-8') as f:
        f.write(result_lines)

