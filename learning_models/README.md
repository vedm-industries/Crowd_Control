Overview of DNNs: 

1. A typical DNN architecture for MNIST classification might involve:
   Input Layer: Receives the 28x28 grayscale image flattened into a 784-dimensional vector (28 * 28 pixels).
   Hidden Layers: Several hidden layers with a specific number of neurons (e.g., 128 neurons) are used to extract features from the image data. These layers apply activation functions to introduce non-linearity and allow the network to learn complex relationships.
   Output Layer: Contains 10 neurons, one for each digit (0-9). The activation function (e.g., softmax) converts the output layer's values into probabilities, indicating the likelihood of the input image belonging to each digit class.
2. Training and Evaluating the DNN
   The DNN learns by iteratively processing training images, comparing its predictions with the actual labels, and adjusting its internal weights and biases to minimize the error. Techniques like backpropagation are used to propagate the error back through the network, updating weights in each layer. Training performance is evaluated on a separate test set not used during training to assess the model's generalization ability to unseen data.
3. The CIFAR-10 Dataset
   CIFAR-10 is a more complex dataset compared to MNIST. It contains 60,000 color images of 10 object classes (e.g., airplanes, cars, dogs) sized 32x32 pixels. CIFAR-10 presents a greater challenge for DNNs due to the increased number of classes, color information, and potential for variations in image content.
4. Building a DNN for CIFAR-10 Classification
   A DNN architecture for CIFAR-10 might share similarities with the MNIST model but often requires:
   Convolutional Layers: These layers are designed to capture spatial features in images. They apply filters that convolve with the input image, extracting local features like edges, corners, and textures.
   Pooling Layers: These layers perform downsampling to reduce the dimensionality of the data and introduce a degree of invariance to small shifts or rotations in the images.
   More Complex Architectures: Due to the increased complexity of CIFAR-10, deeper networks with more hidden layers and neurons might be necessary for better performance.
5. Training and Evaluating the DNN: The training process for CIFAR-10 follows similar principles to MNIST, but training time may increase due to the larger dataset and more complex architecture. Regularization techniques like dropout can be helpful to prevent overfitting and improve generalization.


NOTE: These are all models I used to learn about and initially experiment with deep learning -- they will not have high accuracy scores and may not have every file in the directory to run. Please contact me if seriously interested in any of the models in this folder. 
