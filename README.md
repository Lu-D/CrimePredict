# Crime Predict

Commute safely.

## What it does

Crime Predict is a website that leverages historical Seattle crime logs to inform you on where historical crimes have occurred the most often as well as leveraging a custom neural network to predict where crime might occur next. Our network has been trained on date and time of day to predict future crime. 

## Our inspiration

Safety is a big concern for us (and something our parents constantly nag about). We wanted to be informed of which places have been historically dangerous and where future crimes are most likely to occur both on campus and during our commute.

## How we built it

We built this website using React and Python using:

- PyTorch
- A [Flask](https://flask.palletsprojects.com/en/1.1.x/) integration
- Nvidia GTX 2080ti
- Coffee ![](https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/google/208/hot-beverage_2615.gif)

## Challenges we faced

- Custom Neural Net Parameter Tuning
- Heatmap generation
- Front-end to back-end communication

## The dataset

Our dataset was provided for public use by Seattle [here](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5). It contains police reports for the past 12 years (nearly 90000 entries). We focused on location and start time and performed some minor data sanitation.

<p align="center">
    <img src="https://github.com/Lu-D/CrimePredict/raw/master/historicalshot.png", width="960">
    <br>
    <sup>Visualization of crimes from the Crime dataset since 2008.</sup>
</p>

## Custom Pytorch neural net

Our app uses a custom fully-connected neural network to predict the position of future crimes. Due to the short nature of this hackathon, we felt creating a demoable version with as simple a network would be the best (and might even help others learn). Despite its simplicity, tuning the network proved a significant challenge. We retrained it over 100(our visualization jupyter notebook says 164) times with different hyperparameters and structures. 

[](https://github.com/Lu-D/CrimePredict/raw/master/nn.svg)

<p align="center">
    <img src="https://github.com/Lu-D/CrimePredict/raw/master/nn.png", width="960">
    <br>
    <sup>Our network structure illustrated!</sup>
</p>

We trained with an Adam optimizer and learning rate of 0.00003 and batch size of 64 for 4 epochs. Training was extraordinarily sensitive as the networks would either underfit and still be a linear function or overfit and be centered on Seattle's downtown.

## Heatmap generation

<p align="center">
    <img src="https://github.com/Lu-D/CrimePredict/raw/master/1hourshot.png", width="960">
    <br>
    <sup>Predicted crime for December 21 at 01:00 in the morning.</sup>
</p>

We used google cloud's map widget at the core of our project. We created a jupyter notebooks visualization script as well as integration into the final website. The widget has the capability of generating heatmaps which look quite beautiful.

<p align="center">
    <img src="https://github.com/Lu-D/CrimePredict/raw/master/21hourshot.png", width="960">
    <br>
    <sup>Predicted crime for December 21 at 21:00 in the evening.</sup>
</p>


<p align="center">
    <img src="https://github.com/Lu-D/CrimePredict/raw/master/screenshot.png", width="960">
    <br>
    <sup>Our Website</sup>
</p>
## Accomplishments we're proud of

We like the results of our trained neural network. While it is not the most robust, it still surprised us with its performance. Two of us are also first time hackers and learning how to use Flask and integrating with a PyTorch application has been amazing.

## What's next for CrimePredict?
- more robust heatmap prediction with U-Net
- a more interactive frontend for users to explore our network's predictions
- avoid becoming Minority Report
