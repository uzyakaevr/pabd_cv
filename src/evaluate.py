import tensorflow as tf
import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.applications.xception import preprocess_input  

data_dir = 'data/raw/pinterest'
report_path = 'output/report.txt'
model_path = 'models/my_model'


def evaluate():
    test_data_gen = ImageDataGenerator(preprocessing_function=preprocess_input)
    test_df = test_data_gen.flow_from_directory(data_dir, target_size = (180, 180), 
                                               shuffle = False, 
                                               class_mode='categorical')
    model = tf.keras.models.load_model(model_path)
    metrics = [
        tf.metrics.BinaryAccuracy(),
        tf.metrics.Precision(),
        tf.metrics.Recall()
    ]
    model.compile(metrics=metrics)
    result = model.evaluate(test_df)
    _, acc, precision, recall = result

    result_lines = [
        f'Test data len: {len(test_df)}\n'
        f'Accuracy: {acc:.3f}, Precision: {precision:.3f}, Recall: {recall:.3f}'
    ]
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(result_lines)


if __name__ == '__main__':
    evaluate()