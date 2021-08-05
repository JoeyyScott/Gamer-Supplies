## Testing

### Bugs
+ **Review Carousel**:
    + Upon adding this feature it worked when there was one review in the list. When adding another review, the two reviews were displaying simultaneously as Bootstrap uses the ```active``` class to determine what to show.
    + After researching around I found [this post](https://stackoverflow.com/questions/35836879/how-to-use-for-loop-with-bootstrap-carousel) which utilized a for loop inside the inner carousel to only render active for the first iteration in the loop.
        + The code stated was ```{% if forloop.counter == 1 %}active{% endif %}``` which I adapted to check for the first review.

+ **Carousel auto scrolling**:
    + When adding in the carousel it was auto scrolling which I wanted to remove according to the assessment handbook about aggressive autoplaying of content.
        + I consulted the Bootstrap docs and when reading about interval I noticed in the below article [here](https://getbootstrap.com/docs/5.0/components/carousel/#disable-touch-swiping) that you can set ```data-bs-interval="false"``` to prevent the carousel from autoplaying.