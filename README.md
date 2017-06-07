# Recommendation system for YouTube

This project focussed on recommending videos to multiple users to make them laugh. This system also analyzed the preblems of recommending popular videos with maximum view counts and likes. Main focus of this recommendation system is to implement a recommendation system which is personalized to the users based on his previous interests and other relative videos using **collaborative filtering technique**


### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Anaconda - Python version - 2.7 is used in this project. 

Get the **Developer API key** from Developer console for accessing YouTube API.

Click [here](http://help.dimsemenov.com/kb/wordpress-royalslider-tutorials/wp-how-to-get-youtube-api-key) to get the API key in a faster way 

### Installing

First, install the necessary packages for accessing YouTube API 

`pip install google-api-python-client`

Also, install nltk for checking the synonyms of the search keyword.

` pip install nltk`

And finally to implement recommendation system, install graphlab after registering with institutional email id.

`pip install graphlab`

### Running the tests

If you run the following code, it executes the evaluation metrics like **Precision** and **Recall**
This helps in testig the performance of the created recommendation system.

`model_performance = graphlab.compare(test_data, [popularity_model, item_sim_model])
graphlab.show_comparison(model_performance,[popularity_model, item_sim_model])`



### Authors

* Kathiravan Natarajan 
