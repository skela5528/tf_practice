import tensorflow as tf
tf.get_logger().setLevel('INFO')


def _set_tf_logging(log_level: str = 'INFO'):
    tf.get_logger().setLevel(log_level)


if __name__ == '__main__':
    print(tf.__version__)
